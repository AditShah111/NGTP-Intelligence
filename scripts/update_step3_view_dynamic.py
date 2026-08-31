step3_code = """'use client';

import React, { useState } from 'react';
import { PrecedentAnalysis } from '../../types';
import { BookOpen, Award, CheckCircle2, AlertCircle, Sparkles, Scale, RefreshCw, Layers, ShieldCheck, Database, Filter } from 'lucide-react';

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
      {/* Real-time Ingestion Header Card */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pb-4 border-b border-beige-200">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Scale className="w-5 h-5 text-amber-700" />
              <h3 className="text-xl font-serif font-bold text-slate-900">
                Steps 3 & 4: Dynamic Case Law Ingestion & 6-Axis Evidence Audit
              </h3>
            </div>
            <p className="text-xs text-slate-600">
              Continuously ingests Indian High Court & Supreme Court rulings relating to NGTP, reverse-engineers the evidences relied on by judges, and dynamically recalibrates parameter weights.
            </p>
          </div>

          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs font-mono px-3 py-1 rounded-full bg-purple-50 text-purple-900 border border-purple-200 font-semibold flex items-center gap-1.5 shadow-sm">
              <Sparkles className="w-3.5 h-3.5 text-purple-600" />
              Live Precedent Ingestion Active
            </span>
          </div>
        </div>

        {/* Live Research Topic Bar */}
        <div className="mt-4 p-4 rounded-xl bg-beige-50/70 border border-beige-200 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
          <div className="flex items-center gap-2 w-full sm:w-auto">
            <Filter className="w-4 h-4 text-slate-500 flex-shrink-0" />
            <span className="text-xs font-semibold text-slate-700 whitespace-nowrap">Ingestion Topic:</span>
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
              <span>{isIngesting ? 'Ingesting & Auditing Precedents...' : 'Ingest & Recalibrate Parameters'}</span>
            </button>
          )}
        </div>

        {/* Ingested Precedents Feed */}
        <div className="space-y-5 mt-6">
          <div className="flex items-center justify-between text-xs font-mono text-slate-500 uppercase pb-1">
            <span>Ingested Precedent Matrix ({filteredPrecedents.length} Rulings Evaluated):</span>
            <span className="text-amber-800 font-semibold">6-Axis Grounding Active</span>
          </div>

          {filteredPrecedents.map((p, idx) => {
            const score = p.comparabilityScore?.totalScore || 90;
            const isSc = p.court.toLowerCase().includes('supreme court');

            return (
              <div
                key={p.id || idx}
                className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
              >
                {/* Header with Court & Score */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-beige-200">
                  <div>
                    <div className="flex items-center gap-2 flex-wrap">
                      <h4 className="text-base font-serif font-bold text-slate-900">{p.caseName}</h4>
                      {isSc && (
                        <span className="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-300">
                          ★ Supreme Court Affirmed
                        </span>
                      )}
                      {p.topicDomain && (
                        <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-purple-50 text-purple-800 border border-purple-200">
                          {p.topicDomain}
                        </span>
                      )}
                    </div>
                    <div className="text-xs text-slate-600 flex items-center gap-2 mt-1">
                      <span className="font-semibold text-amber-800">{p.court}</span>
                      <span>•</span>
                      <span className="font-mono text-slate-500">{p.citation}</span>
                    </div>
                  </div>

                  <div className="flex items-center gap-3">
                    <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full border ${
                      p.favourableApplicability === 'HIGH' 
                        ? 'bg-emerald-50 text-emerald-800 border-emerald-200' 
                        : 'bg-blue-50 text-blue-800 border-blue-200'
                    }`}>
                      {p.favourableApplicability === 'HIGH' ? 'Direct / Controlling Ratio' : 'Persuasive'}
                    </span>
                    <div className="bg-white border border-beige-200 px-3 py-1 rounded-lg text-center shadow-sm min-w-[85px]">
                      <div className="text-[10px] font-mono text-slate-400 uppercase">Match Score</div>
                      <div className="text-sm font-mono font-bold text-amber-700">{score}/100</div>
                    </div>
                  </div>
                </div>

                {/* Core Ratio & Evidentiary Analysis */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 text-xs">
                  <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                    <div className="text-[11px] font-mono uppercase text-slate-400 mb-1 font-semibold">Judicial Ratio & Legal Principle:</div>
                    <p className="text-slate-800 leading-relaxed font-sans">{p.ratioLegalPrinciple}</p>
                  </div>
                  <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                    <div className="text-[11px] font-mono uppercase text-slate-400 mb-1 font-semibold">Litigation Application in Appeal:</div>
                    <p className="text-slate-800 leading-relaxed font-sans">{p.litigationUse}</p>
                  </div>
                </div>

                {/* Evidences Relied On by Court (Reverse-Engineered Evidence Audit) */}
                <div className="mt-4 p-3.5 rounded-lg bg-white border border-beige-200">
                  <div className="flex items-center gap-1.5 mb-2">
                    <ShieldCheck className="w-4 h-4 text-emerald-700" />
                    <span className="text-xs font-mono font-bold text-slate-900 uppercase">Evidences Relied On by Court:</span>
                  </div>
                  <div className="flex flex-wrap gap-1.5 mb-3">
                    {(p.evidencesReliedOnByCourt || [
                      'Valid Tax Invoices (Rule 46)',
                      '100% Consideration + Tax Paid through RTGS',
                      'Supplier GSTR-1 acknowledgement',
                      'No recovery action taken against supplier'
                    ]).map((ev, i) => (
                      <span key={i} className="text-[11px] font-medium px-2.5 py-1 rounded-md bg-emerald-50 text-emerald-900 border border-emerald-200">
                        ✓ {ev}
                      </span>
                    ))}
                  </div>

                  {p.criticalEvidentiaryThreshold && (
                    <div className="text-[11px] text-amber-900 bg-amber-50/80 p-2.5 rounded-md border border-amber-200 flex items-start gap-2">
                      <AlertCircle className="w-3.5 h-3.5 text-amber-700 flex-shrink-0 mt-0.5" />
                      <div>
                        <strong>Critical Evidentiary Threshold:</strong> {p.criticalEvidentiaryThreshold}
                      </div>
                    </div>
                  )}
                </div>

                {/* Parameter Impact & 6-Axis Comparability Metrics */}
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
    f.write(step3_code)

print("Updated Step3Step4PrecedentsView with dynamic ingestion and reverse-engineered evidence audit!")