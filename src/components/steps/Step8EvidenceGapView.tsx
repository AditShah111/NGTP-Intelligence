'use client';

import React from 'react';
import { EvidenceGapItem } from '../../types';
import { SearchX, AlertTriangle, ArrowUpRight } from 'lucide-react';

interface Props {
  evidenceGaps: EvidenceGapItem[];
}

export const Step8EvidenceGapView: React.FC<Props> = ({ evidenceGaps }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 8: Evidence Gap Prioritization & Remediation</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Prioritized list of missing documents required to convert potential legal arguments into unassailable evidence.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          {evidenceGaps.map((g, idx) => (
            <div
              key={idx}
              className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
            >
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-200">
                  {g.priority} Priority
                </span>
                <span className="text-[11px] font-mono text-slate-500">{g.category}</span>
              </div>

              <h4 className="font-serif font-bold text-sm text-slate-900 mb-2">{g.missingEvidence}</h4>
              <p className="text-xs text-slate-700 leading-relaxed bg-white p-3 rounded-lg border border-beige-200 mb-3">
                {g.whyItMatters}
              </p>

              <div className="text-[11px] text-slate-600 pt-2 border-t border-beige-200 flex items-center justify-between font-mono">
                <span>Source: <strong className="text-slate-800">{g.possibleSource}</strong></span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
