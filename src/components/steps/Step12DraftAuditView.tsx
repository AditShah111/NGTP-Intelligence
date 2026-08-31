'use client';

import React from 'react';
import { DraftAuditDefect } from '../../types';
import { CheckSquare, AlertTriangle, CheckCircle, ShieldAlert } from 'lucide-react';

interface Step12Props {
  defects: DraftAuditDefect[];
}

export const Step12DraftAuditView: React.FC<Step12Props> = ({ defects }) => {
  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <CheckSquare className="w-4 h-4 text-amber-400" />
          STEP 12: Draft Audit (Pleadings, Jurisdiction, Citations, Prayer Validity)
        </h3>
        <p className="text-xs text-slate-400">
          Automated audit of Show Cause Notice reply or First Appeal memo for fatal drafting defects and missing prayers.
        </p>
      </div>

      <div className="space-y-3">
        {defects.map((d) => (
          <div key={d.id} className="legal-glass rounded-xl p-4 border border-legal-800 shadow-lg">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-2 border-b border-legal-800">
              <span className="font-serif font-bold text-sm text-white">{d.parameter}</span>
              <span className={`text-[11px] font-mono px-2 py-0.5 rounded border ${d.severity === 'Critical' ? 'bg-rose-950 text-rose-300 border-rose-600 font-bold' : (d.severity === 'High' ? 'bg-orange-950 text-orange-300 border-orange-600' : 'bg-amber-950 text-amber-300 border-amber-600')}`}>
                {d.severity} Severity
              </span>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 text-xs">
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800">
                <strong className="text-rose-400 font-mono text-[10px] uppercase">Issue / Defect Detected:</strong>
                <p className="text-slate-300 mt-1 leading-relaxed">{d.issueDetected}</p>
              </div>
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800">
                <strong className="text-emerald-400 font-mono text-[10px] uppercase">Recommended Pleading Correction:</strong>
                <p className="text-emerald-200 mt-1 leading-relaxed">{d.recommendedCorrection}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
