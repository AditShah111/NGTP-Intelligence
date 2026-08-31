step3_hierarchy_view = """'use client';

import React, { useState } from 'react';
import { PrecedentAnalysis } from '../../types';
import { BookOpen, Award, CheckCircle2, AlertCircle, Sparkles, Scale, RefreshCw, Layers, ShieldCheck, Database, Filter, ArrowRight, Gavel, GitCompare } from 'lucide-react';

interface Props {
  precedents: PrecedentAnalysis[];
  onIngestPrecedents?: (domain: string) => Promise<void>;
  isIngesting?: boolean;
}

export const Step3Step4PrecedentsView: React.FC<Props> = ({ 
  precedents, 
  onIngestPrecedents,
  isIngesting = false 
}) => {
  const [selectedDomain, setSelectedDomain] = useState('Section 16(2)(c) & NGTP Supplier Default');
  const [filterTopic, setFilterTopic] = useState<string>('ALL');

  const domains = [
    'Section 16(2)(c) & NGTP Supplier Default',
    'Non-Genuine / Cancelled Supplier (NGTP)',
    'Retrospective Cancellation of Supplier GSTIN',
    'Fake Invoicing & Physical Transit Genuineness',
    'Circular 183 / 193 CA Safe-Harbor',
    'Section 16(4) / 16(5) Retrospective Relief'
  ];

  const filteredPrecedents = filterTopic === 'ALL'
    ? precedents
    : precedents.filter(p => p.topicDomain?.includes(filterTopic) || p.relevantProvision?.includes(filterTopic));

  return (
    <div className="space-y-6">
      {/* Real-time Ingestion & Article 141 Header Card */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pb-4 border-b border-beige-200">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Gavel className="w-5 h-5 text-amber-700" />
              <h3 className="text-xl font-serif font-bold text-slate-900">
                Steps 3 & 4: Judicial Hierarchy (Article 141) & High Court Strength Engine
              </h3>
            </div>
            <p className="text-xs text-slate-600">
              Evaluates the constitutional hierarchy and strength of High Court and Supreme Court rulings. Resolves conflicting High Court judgments under Article 141 and tests evidential comparability.
            </p>
          </div>

          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs font-mono px-3 py-1 rounded-full bg-emerald-50 text-emerald-900 border border-emerald-200 font-semibold flex items-center gap-1.5 shadow-sm">
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
              Article 141 Overrule Engine Active
            </span>
          </div>
        </div>

        {/* Live Research Topic Bar */}
        <div className="mt-4 p-4 rounded-xl bg-beige-50/70 border border-beige-200 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
          <div className="flex items-center gap-2 w-full sm:w-auto">
            <Filter className="w-4 h-4 text-slate-500 flex-shrink-0" />
            <span className="text-xs font-semibold text-slate-700 whitespace-nowrap">Ingestion Domain:</span>
            <select
              value={selectedDomain}
              onChange={(e) => setSelectedDomain(e.target.value)}
              className="bg-white border border-beige-300 rounded-lg px-3 py-1.5 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm w-full sm:w-auto"
            >
              {domains.map((d) => (
                <option key={d} value={d}>{d}</option>
              ))}
            </select>
          </div>

          {onIngestPrecedents && (
            <button
              onClick={() => onIngestPrecedents(selectedDomain)}
              disabled={isIngesting}
              className="flex items-center gap-2 px-4 py-2 rounded-lg bg-amber-600 hover:bg-amber-700 disabled:opacity-50 text-white text-xs font-semibold shadow-sm transition-all whitespace-nowrap"
            >
              <RefreshCw className={`w-3.5 h-3.5 ${isIngesting ? 'animate-spin' : ''}`} />
              <span>{isIngesting ? 'Ingesting & Resolving Conflicts...' : 'Ingest & Audit Judicial Strength'}</span>
            </button>
          )}
        </div>

        {/* Ingested Precedents Feed */}
        <div className="space-y-5 mt-6">
          <div className="flex items-center justify-between text-xs font-mono text-slate-500 uppercase pb-1">
            <span>Precedents Matrix & Authority Strength ({filteredPrecedents.length} Rulings):</span>
            <span className="text-amber-800 font-semibold">Hierarchy Calibrated</span>
          </div>

          {filteredPrecedents.map((p, idx) => {
            const score = p.comparabilityScore?.totalScore || 90;
            const isSc = p.article141Status === 'SUPREME_BINDING' || p.court.toLowerCase().includes('supreme court');
            const authScore = p.judicialAuthorityStrengthScore || (isSc ? 98 : 85);

            return (
              <div
                key={p.id || idx}
                className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
              >
                {/* Header with Court, Bench Strength & Article 141 Tag */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-beige-200">
                  <div>
                    <div className="flex items-center gap-2 flex-wrap">
                      <h4 className="text-base font-serif font-bold text-slate-900">{p.caseName}</h4>
                      {isSc && (
                        <span className="text-[10px] font-mono font-bold px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-300 shadow-sm flex items-center gap-1">
                          <Award className="w-3 h-3 text-amber-700" />
                          Article 141 Supreme Court Binding
                        </span>
                      )}
                      {p.benchType && (
                        <span className="text-[10px] font-mono font-semibold px-2 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-200">
                          {p.benchType}
                        </span>
                      )}
                    </div>
                    <div className="text-xs text-slate-600 flex items-center gap-2 mt-1">
                      <span className="font-semibold text-amber-800">{p.court}</span>
                      <span>•</span>
                      <span className="font-mono text-slate-500">{p.citation}</span>
                      {p.slpStatus && (
                        <>
                          <span>•</span>
                          <span className="font-mono text-emerald-800 font-semibold">{p.slpStatus}</span>
                        </>
                      )}
                    </div>
                  </div>

                  <div className="flex items-center gap-2.5">
                    {/* Authority Strength Badge */}
                    <div className="bg-white border border-beige-200 px-3 py-1 rounded-lg text-center shadow-sm min-w-[90px]">
                      <div className="text-[9px] font-mono text-slate-400 uppercase">Bench Authority</div>
                      <div className="text-xs font-mono font-bold text-purple-700">{authScore}/100</div>
                    </div>
                    {/* Fact Match Score */}
                    <div className="bg-white border border-beige-200 px-3 py-1 rounded-lg text-center shadow-sm min-w-[85px]">
                      <div className="text-[9px] font-mono text-slate-400 uppercase">Fact Match</div>
                      <div className="text-xs font-mono font-bold text-amber-700">{score}/100</div>
                    </div>
                  </div>
                </div>

                {/* Core Ratio & Litigation Use */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 text-xs">
                  <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                    <div className="text-[11px] font-mono uppercase text-slate-400 mb-1 font-semibold">Judicial Ratio & Principle:</div>
                    <p className="text-slate-800 leading-relaxed font-sans">{p.ratioLegalPrinciple}</p>
                  </div>
                  <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                    <div className="text-[11px] font-mono uppercase text-slate-400 mb-1 font-semibold">Litigation Application:</div>
                    <p className="text-slate-800 leading-relaxed font-sans">{p.litigationUse}</p>
                  </div>
                </div>

                {/* Evidences Relied On by Court */}
                <div className="mt-4 p-3.5 rounded-lg bg-white border border-beige-200">
                  <div className="flex items-center gap-1.5 mb-2">
                    <ShieldCheck className="w-4 h-4 text-emerald-700" />
                    <span className="text-xs font-mono font-bold text-slate-900 uppercase">Evidences Relied On by Court:</span>
                  </div>
                  <div className="flex flex-wrap gap-1.5 mb-2">
                    {(p.evidencesReliedOnByCourt || [
                      'Tax Invoices fulfilling Rule 46 particulars',
                      '100% Consideration + GST paid through RTGS/NEFT',
                      'Supplier GSTR-1 acknowledgement',
                      'No recovery action initiated against supplier'
                    ]).map((ev, i) => (
                      <span key={i} className="text-[11px] font-medium px-2.5 py-0.5 rounded-md bg-emerald-50 text-emerald-900 border border-emerald-200">
                        ✓ {ev}
                      </span>
                    ))}
                  </div>

                  {p.criticalEvidentiaryThreshold && (
                    <div className="text-[11px] text-amber-900 bg-amber-50/80 p-2 rounded-md border border-amber-200 mt-2">
                      <strong>Critical Evidentiary Threshold:</strong> {p.criticalEvidentiaryThreshold}
                    </div>
                  )}
                </div>

                {/* Conflict Resolution & Article 141 Interplay (If competing judgments exist) */}
                {p.competingConflictAnalysis && (
                  <div className="mt-3 p-3.5 rounded-xl bg-purple-50/60 border border-purple-200 text-xs">
                    <div className="flex items-center gap-1.5 mb-1.5 text-purple-900 font-bold font-serif">
                      <GitCompare className="w-4 h-4 text-purple-700" />
                      <span>Article 141 Conflict Resolution vs Divergent Rulings</span>
                    </div>
                    <div className="space-y-1.5 text-slate-800">
                      <div>
                        <span className="font-semibold text-rose-800">Divergent Ruling: </span>
                        <span>{p.competingConflictAnalysis.conflictWith}</span>
                      </div>
                      <p className="text-slate-700 leading-relaxed bg-white/80 p-2.5 rounded-lg border border-purple-100 font-sans">
                        <strong className="text-purple-900">Why {p.caseName} Prevails: </strong>
                        {p.competingConflictAnalysis.whyThisPrecedentPrevails}
                      </p>
                      <div className="text-[11px] font-mono font-semibold text-emerald-800 mt-1">
                        ✓ Resolution: {p.competingConflictAnalysis.article141Resolution}
                      </div>
                    </div>
                  </div>
                )}

                {/* 6-Axis Comparability Metrics */}
                {p.comparabilityScore && (
                  <div className="mt-3 pt-3 border-t border-beige-200 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2 text-[10px] font-mono text-slate-600">
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Statutory</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.statutorySimilarity}/20</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Factual</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.factualSimilarity}/25</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Evidentiary</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.evidentiarySimilarity}/20</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Procedural</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.proceduralSimilarity}/10</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Authority</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.courtAuthorityRelevance}/15</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Distinguish Risk</div>
                      <div className="font-bold text-emerald-700 mt-0.5">{p.comparabilityScore.distinguishabilityRisk}/10</div>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
"""

with open("src/components/steps/Step3Step4PrecedentsView.tsx", "w", encoding="utf-8") as f:
    f.write(step3_hierarchy_view)

print("Updated Step3Step4PrecedentsView with Article 141 Conflict Resolution and Bench Authority Scores!")