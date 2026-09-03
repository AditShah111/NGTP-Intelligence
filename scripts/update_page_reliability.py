with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add evalError state
content = content.replace(
    "const [scopeRejection, setScopeRejection] = useState<NGTPGatekeeperResult | null>(null);",
    "const [scopeRejection, setScopeRejection] = useState<NGTPGatekeeperResult | null>(null);\n  const [evalError, setEvalError] = useState<string | null>(null);"
)

# Update handleSelectHistoricalCase to close drawer and clear error
content = content.replace(
    "setUploadedDocuments(c.documents || []);\n  };",
    "setUploadedDocuments(c.documents || []);\n    setIsHistoryDrawerOpen(false);\n    setEvalError(null);\n    setScopeRejection(null);\n    window.scrollTo({ top: 0, behavior: 'smooth' });\n  };"
)

# Update handleRunEvaluation: timeout to 60s, explicit error setting
old_run_eval = """    setIsLoading(true);
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 8000);

    try {
      const geminiApiKey = typeof window !== 'undefined' ? (localStorage.getItem('ngtp_gemini_api_key') || undefined) : undefined;
      const res = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        signal: controller.signal,
        body: JSON.stringify({
          title: matterTitle,
          taxpayerName: taxpayer,
          gstin: gstinNum,
          financialYear,
          disputedAmount: amount,
          noticeType,
          primaryIssue,
          caseSummary: summary,
          geminiApiKey,
          documents: allDocs
        })
      });

      clearTimeout(timeoutId);

      const data = await res.json();
      if (res.status === 422 || data.notApplicable) {
        setActiveCase(null);
        setScopeRejection({
          isNGTP: false,
          detectedDomain: data.detectedDomain || 'Non-NGTP Domain',
          confidenceScore: 95,
          rejectionReason: data.rejectionReason || 'Project is not within NGTP statutory scope.',
          matchedKeywords: [],
          allowedTopics: data.allowedTopics || []
        });
        return;
      }

      if (res.ok && data.evaluatedCase) {
        setScopeRejection(null);
        setActiveCase(data.evaluatedCase);
        setCases(prev => [data.evaluatedCase, ...prev.filter(c => c.id !== data.evaluatedCase.id)]);
      }
    } catch (err: any) {
      console.warn('Evaluation response:', err.message);
    } finally {
      clearTimeout(timeoutId);
      setIsLoading(false);
    }"""

new_run_eval = """    setIsLoading(true);
    setEvalError(null);
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 60000);

    try {
      const geminiApiKey = typeof window !== 'undefined' ? (localStorage.getItem('ngtp_gemini_api_key') || undefined) : undefined;
      const res = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        signal: controller.signal,
        body: JSON.stringify({
          title: matterTitle,
          taxpayerName: taxpayer,
          gstin: gstinNum,
          financialYear,
          disputedAmount: amount,
          noticeType,
          primaryIssue,
          caseSummary: summary,
          geminiApiKey,
          documents: allDocs
        })
      });

      clearTimeout(timeoutId);

      const data = await res.json().catch(() => ({}));
      if (res.status === 422 || data.notApplicable) {
        setActiveCase(null);
        setScopeRejection({
          isNGTP: false,
          detectedDomain: data.detectedDomain || 'Non-NGTP Domain',
          confidenceScore: 95,
          rejectionReason: data.rejectionReason || 'Project is not within NGTP statutory scope.',
          matchedKeywords: [],
          allowedTopics: data.allowedTopics || []
        });
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }

      if (res.ok && data.evaluatedCase) {
        setScopeRejection(null);
        setEvalError(null);
        setActiveCase(data.evaluatedCase);
        setCases(prev => [data.evaluatedCase, ...prev.filter(c => c.id !== data.evaluatedCase.id)]);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } else {
        setEvalError(data.error || `Evaluation returned error status ${res.status}`);
      }
    } catch (err: any) {
      console.error('Evaluation failed:', err);
      const isAbort = err.name === 'AbortError' || err.message?.includes('aborted');
      setEvalError(isAbort 
        ? 'Evaluation timed out after 60 seconds. Please check historical cases or re-run.' 
        : `Evaluation failed: ${err.message || 'Network request error'}`);
    } finally {
      clearTimeout(timeoutId);
      setIsLoading(false);
    }"""

content = content.replace(old_run_eval, new_run_eval)

# Move scopeRejection and add evalError banner to top of main
eval_error_banner = """        {/* EVALUATION ERROR BANNER */}
        {evalError && (
          <div className="bg-rose-50 border-2 border-rose-300 rounded-2xl p-5 shadow-sm animate-fade-in flex items-start justify-between gap-3 text-xs">
            <div className="flex items-center gap-3">
              <span className="text-xl">⚠️</span>
              <div>
                <strong className="text-rose-900 font-bold block">Evaluation Alert:</strong>
                <span className="text-rose-800">{evalError}</span>
              </div>
            </div>
            <button onClick={() => setEvalError(null)} className="text-slate-400 hover:text-slate-700">
              <X className="w-4 h-4" />
            </button>
          </div>
        )}"""

# Remove old scopeRejection banner from bottom
old_scope_block_re = r"""        \{\/\* NON-NGTP SCOPE REJECTION BANNER \*\/\}[\s\S]*?\{\/\* 2\. MATTER PARTICULARS"""
import re
# We can place scopeRejection and evalError right under the loading banner
top_alerts = eval_error_banner + """

        {/* NON-NGTP SCOPE REJECTION BANNER */}
        {scopeRejection && (
          <div className="bg-rose-50 border-2 border-rose-300 rounded-2xl p-6 sm:p-7 shadow-md animate-fade-in space-y-4">
            <div className="flex items-start justify-between gap-3">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-rose-100 border border-rose-200 flex items-center justify-center flex-shrink-0 text-rose-700 font-bold text-lg">
                  ⛔
                </div>
                <div>
                  <span className="text-[11px] font-mono uppercase font-bold text-rose-800 tracking-wider">
                    Execution Halted &bull; Statutory Scope Filter
                  </span>
                  <h3 className="text-lg font-serif font-bold text-slate-900">
                    NOT APPLICABLE: Non-NGTP Matter Detected
                  </h3>
                </div>
              </div>
              <button
                onClick={() => setScopeRejection(null)}
                className="text-slate-400 hover:text-slate-700 p-1"
                title="Dismiss"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="p-4 rounded-xl bg-white border border-rose-200 space-y-2">
              <div className="text-xs text-slate-800 font-sans leading-relaxed">
                <strong className="text-rose-900">Detected Subject Domain:</strong>{' '}
                <span className="font-mono font-semibold px-2 py-0.5 rounded bg-rose-100 text-rose-900">
                  {scopeRejection.detectedDomain}
                </span>
              </div>
              <p className="text-xs text-slate-600 font-sans leading-relaxed">
                {scopeRejection.rejectionReason}
              </p>
            </div>

            <div className="pt-1">
              <span className="text-[11px] font-mono font-bold text-slate-700 uppercase block mb-2">
                Permitted NGTP Disputes for this Engine:
              </span>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                {scopeRejection.allowedTopics?.map((topic, i) => (
                  <div key={i} className="flex items-center gap-2 p-2 rounded-lg bg-white/80 border border-rose-100 text-slate-700">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0" />
                    <span>{topic}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="pt-2 flex justify-end">
              <button
                onClick={() => {
                  setScopeRejection(null);
                  handleResetWorkspace();
                }}
                className="px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold shadow-sm transition-all"
              >
                Reset to Clean NGTP Assessment
              </button>
            </div>
          </div>
        )}"""

content = content.replace(
    "{/* Background Agent Execution Banner */}\n        {isLoading && (",
    top_alerts + "\n\n        {/* Background Agent Execution Banner */}\n        {isLoading && ("
)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated page.tsx with 60s timeout, evalError banner, and top-of-page alert placements!")