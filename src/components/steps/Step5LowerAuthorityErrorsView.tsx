'use client';

import React from 'react';
import { LowerAuthorityError } from '@/types';
import { AlertOctagon, ShieldAlert, Gavel } from 'lucide-react';

interface Step5Props {
  errors: LowerAuthorityError[];
}

export const Step5LowerAuthorityErrorsView: React.FC<Step5Props> = ({ errors }) => {
  const getSeverityBadge = (strength: string) => {
    switch (strength) {
      case 'Fundamental':
        return 'bg-rose-950/80 text-rose-300 border-rose-500/50';
      case 'Serious':
        return 'bg-orange-950/80 text-orange-300 border-orange-500/50';
      case 'Material':
        return 'bg-amber-950/80 text-amber-300 border-amber-500/50';
      default:
        return 'bg-blue-950/80 text-blue-300 border-blue-500/50';
    }
  };

  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <AlertOctagon className="w-4 h-4 text-rose-400" />
          STEP 5: Lower Authority Error Analysis & Defect Matrix
        </h3>
        <p className="text-xs text-slate-400">
          Identification of jurisdictional flaws, ignored documentary evidence, statutory misconstructions, and natural justice violations.
        </p>
      </div>

      <div className="space-y-3">
        {errors.map((e) => (
          <div key={e.id} className="legal-glass rounded-xl p-4 border border-legal-800 hover:border-rose-500/40 transition-all">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-2.5 border-b border-legal-800">
              <div className="font-serif font-bold text-sm text-white flex items-center gap-2">
                <Gavel className="w-4 h-4 text-rose-400 flex-shrink-0" />
                <span>{e.finding}</span>
              </div>
              <span className={`px-2.5 py-0.5 rounded text-[11px] font-mono font-bold border ${getSeverityBadge(e.strength)}`}>
                {e.strength} Error
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 text-xs">
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800/80">
                <strong className="text-slate-400 font-mono text-[10px] uppercase">Lower Authority Reasoning:</strong>
                <p className="text-slate-300 mt-1 leading-relaxed">{e.lowerAuthorityReasoning}</p>
              </div>
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800/80">
                <strong className="text-amber-400 font-mono text-[10px] uppercase">Evidence Ignored / Misread:</strong>
                <p className="text-amber-200/90 mt-1 leading-relaxed">{e.evidenceIgnoredMisread}</p>
              </div>
            </div>

            <div className="mt-3 pt-2.5 border-t border-legal-800/60 flex flex-col sm:flex-row justify-between gap-2 text-xs">
              <div className="text-rose-300">
                <strong className="text-slate-400">Legal Error: </strong>
                {e.legalError}
              </div>
              <div className="font-mono text-blue-300 text-[11px] flex-shrink-0">
                <strong className="text-slate-400">Counter Authority: </strong>
                {e.relevantAuthority}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
