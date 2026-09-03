'use client';

import React from 'react';
import { DraftAuditDefect } from '../../types';
import { CheckCircle2, AlertTriangle } from 'lucide-react';

interface Props {
  defects: DraftAuditDefect[];
}

export const Step12DraftAuditView: React.FC<Props> = ({ defects }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 12: Pleading Defect Audit</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Auditing the appeal memo / SCN reply for statutory omissions, adverse concessions, and jurisdictional defects.
            </p>
          </div>
        </div>

        <div className="space-y-4 mt-6">
          {defects.map((d) => (
            <div key={d.id} className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 shadow-sm">
              <div className="flex items-center justify-between gap-2 pb-2 border-b border-beige-200">
                <span className="font-mono text-xs font-bold text-slate-800">{d.parameter}</span>
                <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200">
                  {d.severity} Severity
                </span>
              </div>
              <div className="mt-3 text-xs space-y-2">
                <p className="text-slate-800 leading-relaxed font-sans">{d.issueDetected}</p>
                <div className="bg-emerald-50 p-3 rounded-lg border border-emerald-200 text-emerald-950 font-medium">
                  <strong className="text-emerald-900">Recommended Correction:</strong> {d.recommendedCorrection}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
