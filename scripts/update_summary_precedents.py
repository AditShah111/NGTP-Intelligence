with open("src/components/ExecutiveSummaryView.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add state isPrecedentsOpen
content = content.replace(
    "const [isGroundsOpen, setIsGroundsOpen] = useState(false);",
    "const [isGroundsOpen, setIsGroundsOpen] = useState(false);\n  const [isPrecedentsOpen, setIsPrecedentsOpen] = useState(false);"
)

# Add Precedents Matrix Card
precedent_card = """
      {/* 2.5 Dynamic Judicial Precedent Matrix (Article 141 & Dynamic Parameter Calibration) */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
        <div 
          onClick={() => setIsPrecedentsOpen(!isPrecedentsOpen)}
          className="flex items-center justify-between pb-3 border-b border-beige-200 cursor-pointer"
        >
          <div className="flex items-center gap-2">
            <Scale className="w-5 h-5 text-amber-700" />
            <div>
              <h3 className="text-lg font-serif font-bold text-slate-900">
                Article 141 Judicial Precedents & Dynamic Calibration Matrix
              </h3>
              <p className="text-xs text-slate-500 font-sans mt-0.5">
                {precedents.length} High Court & Supreme Court authorities dynamically ingested & recalibrating parameters
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-xs font-mono text-amber-900 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200 font-bold">
              {precedents.length} Precedents Synced
            </span>
            <button className="text-slate-400 hover:text-slate-700">
              {isPrecedentsOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
            </button>
          </div>
        </div>

        {isPrecedentsOpen ? (
          <div className="space-y-3 animate-fade-in pt-2">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {precedents.map((prec) => {
                const isSupreme = prec.court.includes('Supreme Court') || prec.article141Status === 'SUPREME_BINDING';
                return (
                  <div key={prec.id} className="p-4 rounded-xl bg-beige-50/70 border border-beige-200 space-y-2 text-xs">
                    <div className="flex items-start justify-between gap-2">
                      <div>
                        <span className="font-serif font-bold text-slate-900 text-xs block">
                          {prec.caseName}
                        </span>
                        <span className="text-[11px] font-mono text-amber-900 font-semibold">
                          {prec.court} &bull; {prec.year}
                        </span>
                      </div>
                      <span className={`font-mono text-[10px] px-2 py-0.5 rounded font-bold whitespace-nowrap ${
                        isSupreme 
                          ? 'bg-purple-100 text-purple-900 border border-purple-200' 
                          : 'bg-blue-50 text-blue-900 border border-blue-200'
                      }`}>
                        Auth: {prec.judicialAuthorityStrengthScore || 85}/100
                      </span>
                    </div>

                    <p className="text-[11px] text-slate-700 leading-relaxed font-sans">
                      <strong className="text-slate-900">Ratio:</strong> {prec.ratioLegalPrinciple}
                    </p>

                    <div className="p-2 rounded bg-white border border-beige-200/80 space-y-1 text-[10px] font-mono text-slate-600">
                      <div>
                        <strong>Court Required Evidences:</strong>{' '}
                        <span className="text-emerald-800 font-semibold">
                          {(prec.evidencesReliedOnByCourt || []).join(', ') || 'Tax Invoices, Bank Payment Proof'}
                        </span>
                      </div>
                      <div>
                        <strong>Distinguishing Risk:</strong>{' '}
                        <span className="text-amber-800">
                          {prec.distinguishingFactors || 'None detected for bona fide buyer'}
                        </span>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        ) : (
          <div className="flex items-center justify-between text-xs text-slate-600 bg-beige-50/50 p-3 rounded-xl border border-beige-200/60">
            <span className="font-mono text-[11px]">
              Ingested authorities: <strong>{precedents.map(p => p.caseName.split(' ')[0]).join(', ')}</strong>
            </span>
            <button 
              onClick={() => setIsPrecedentsOpen(true)}
              className="text-amber-800 font-bold hover:underline font-mono text-[11px]"
            >
              View Full Precedents Table &rarr;
            </button>
          </div>
        )}
      </div>
"""

content = content.replace(
    "{/* 3. Statement of Facts & Grounds of Appeal Review */}",
    precedent_card + "\n      {/* 3. Statement of Facts & Grounds of Appeal Review */}"
)

with open("src/components/ExecutiveSummaryView.tsx", "w", encoding="utf-8") as f:
    f.write(content)

print("Added Article 141 Judicial Precedents Matrix card to ExecutiveSummaryView.tsx!")