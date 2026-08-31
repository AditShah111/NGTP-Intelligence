'use client';

import React from 'react';
import { EvidenceGapItem } from '../../types';
import { Search, AlertCircle, FilePlus2, CheckCircle2 } from 'lucide-react';

interface Step8Props {
  evidenceGaps: EvidenceGapItem[];
}

export const Step8EvidenceGapView: React.FC<Step8Props> = ({ evidenceGaps }) => {
  const getPriorityPill = (p: string) => {
    switch (p) {
      case 'CRITICAL':
        return 'bg-rose-950 text-rose-300 border-rose-500/60 font-bold';
      case 'HIGH':
        return 'bg-orange-950 text-orange-300 border-orange-500/60 font-semibold';
      case 'MEDIUM':
        return 'bg-amber-950 text-amber-300 border-amber-500/60';
      default:
        return 'bg-slate-900 text-slate-300 border-slate-700';
    }
  };

  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <Search className="w-4 h-4 text-amber-400" />
          STEP 8: Evidence Gap Analysis & Remediation Roadmap
        </h3>
        <p className="text-xs text-slate-400">
          Prioritization of missing or un-relied documents required to convert uncertain parameters into litigation-proof evidence.
        </p>
      </div>

      <div className="space-y-3">
        {evidenceGaps.map((gap) => (
          <div key={gap.id} className="legal-glass rounded-xl p-4 border border-legal-800 shadow-lg">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-2.5 border-b border-legal-800">
              <div className="flex items-center gap-2">
                <FilePlus2 className="w-4 h-4 text-amber-400 flex-shrink-0" />
                <h4 className="font-serif font-bold text-sm text-white">{gap.missingEvidence}</h4>
              </div>
              <div className="flex items-center gap-2 font-mono text-xs">
                <span className={`px-2.5 py-0.5 rounded border ${getPriorityPill(gap.priority)}`}>
                  {gap.priority} PRIORITY
                </span>
                <span className="text-[11px] px-2 py-0.5 rounded bg-legal-900 border border-legal-700 text-slate-300">
                  {gap.category}
                </span>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 text-xs">
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800/80">
                <strong className="text-slate-400 font-mono text-[10px] uppercase">Legal Relevance & Rationale:</strong>
                <p className="text-slate-300 mt-1 leading-relaxed">{gap.legalRelevance}</p>
                <p className="text-slate-400 mt-1 italic">{gap.whyItMatters}</p>
              </div>
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800/80">
                <strong className="text-emerald-400 font-mono text-[10px] uppercase">Remediation Action & Source:</strong>
                <p className="text-emerald-200 mt-1"><strong>Source:</strong> {gap.possibleSource}</p>
                <p className="text-slate-300 mt-1"><strong>Impact If Obtained:</strong> {gap.impactIfObtained}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
