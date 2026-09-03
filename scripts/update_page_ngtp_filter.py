import re

with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add import of validateNGTPScope
if "import { validateNGTPScope } from '../service/ngtp-gatekeeper';" not in content:
    content = content.replace(
        "import { BENCHMARK_CASES } from '../repo/benchmark-data';",
        "import { BENCHMARK_CASES } from '../repo/benchmark-data';\nimport { validateNGTPScope, NGTPGatekeeperResult } from '../service/ngtp-gatekeeper';"
    )

# Add scopeRejection state
if "const [scopeRejection, setScopeRejection] = useState" not in content:
    content = content.replace(
        "const [activeCase, setActiveCase] = useState<CaseStudy | null>(null);",
        "const [activeCase, setActiveCase] = useState<CaseStudy | null>(null);\n  const [scopeRejection, setScopeRejection] = useState<NGTPGatekeeperResult | null>(null);"
    )

# Update handleResetWorkspace to clear scopeRejection
content = content.replace(
    "setActiveCase(null);\n    setTitle('');",
    "setActiveCase(null);\n    setScopeRejection(null);\n    setTitle('');"
)

# Update handleRunEvaluation to check gatekeeper
run_eval_old = """  // Run Legal Evaluation Engine
  const handleRunEvaluation = async () => {
    setIsLoading(true);
    const controller = new AbortController();"""

run_eval_new = """  // Run Legal Evaluation Engine
  const handleRunEvaluation = async () => {
    setScopeRejection(null);

    const matterTitle = title.trim() || `${taxpayerName || 'Matter'} - FY ${financialYear}`;
    const taxpayer = taxpayerName.trim() || 'Taxpayer Entity';
    const gstinNum = gstin.trim() || 'Unspecified GSTIN';
    const amount = disputedAmount.trim() || 'Amount under dispute';
    const summary = writtenSubmission.trim() || `${primaryIssue}. Ingested documents: ${uploadedDocuments.length}.`;

    // Package written submission as an explicit document if provided
    let allDocs = [...uploadedDocuments];
    if (writtenSubmission.trim()) {
      const isGrounds = submissionCategory.includes('Grounds');
      const submissionDoc: CaseDocument = {
        id: `doc-sub-${Date.now()}`,
        name: `${submissionCategory.replace(/[^a-zA-Z0-9]/g, '_')}.txt`,
        type: isGrounds ? 'Grounds of Appeal' : 'Reply',
        fileSize: `${(new Blob([writtenSubmission]).size / 1024).toFixed(1)} KB`,
        uploadedAt: new Date().toISOString().split('T')[0],
        ocrReadability: 'Clearly readable text',
        extractedTextSnippet: writtenSubmission.slice(0, 3000)
      };
      allDocs = [submissionDoc, ...allDocs.filter(d => !d.id.startsWith('doc-sub-'))];
    }

    // Client-side Pre-Flight NGTP Scope Check
    const preflightScope = validateNGTPScope(matterTitle, primaryIssue, summary, noticeType, allDocs);
    if (!preflightScope.isNGTP) {
      setActiveCase(null);
      setScopeRejection(preflightScope);
      setIsLoading(false);
      return;
    }

    setIsLoading(true);
    const controller = new AbortController();"""

if "preflightScope = validateNGTPScope" not in content:
    content = content.replace(run_eval_old, run_eval_new)

# Handle API 422 notApplicable response
api_res_check_old = """      if (res.ok) {
        const data = await res.json();
        if (data.evaluatedCase) {
          setActiveCase(data.evaluatedCase);
          setCases(prev => [data.evaluatedCase, ...prev.filter(c => c.id !== data.evaluatedCase.id)]);
        }
      }"""

api_res_check_new = """      const data = await res.json();
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
      }"""

content = content.replace(api_res_check_old, api_res_check_new)

# Insert the NOT APPLICABLE banner right above 2. EXECUTIVE VERDICT
banner_code = """
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
        )}
"""

if "{/* NON-NGTP SCOPE REJECTION BANNER */}" not in content:
    content = content.replace(
        "{/* 2. EXECUTIVE VERDICT & SUMMARY (Appears when activeCase is evaluated) */}",
        banner_code + "\n        {/* 2. EXECUTIVE VERDICT & SUMMARY (Appears when activeCase is evaluated) */}"
    )

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated page.tsx with NGTP gatekeeper pre-flight check and high-visibility rejection banner!")