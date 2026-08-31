'use client';

import React from 'react';
import { LowerAuthorityError } from '../../types';
import { AlertOctagon, Scale, ShieldAlert } from 'lucide-react';

interface Props {
  errors: LowerAuthorityError[];
}

export const Step5LowerAuthorityErrorsView: React.FC<Props> = ({ errors }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 5: Lower Authority Error Audit</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Auditing the impugned SCN / DRC-07 order for jurisdictional, evidentiary, and statutory defects.
            </p>
          </div>
        </div>

        <div className="space-y-4 mt-6">
          {errors.map((e) => (
            <div
              key={e.id}
              className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
            >
              <div className="flex items-center justify-between gap-2 pb-3 border-b border-beige-200">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-rose-100 text-rose-900 border border-rose-200">
                    {e.strength} Error
                  </span>
                  <h4 className="font-serif font-bold text-sm text-slate-900">{e.finding}</h4>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-3 text-xs">
                <div>
                  <div className="text-[11px] font-mono uppercase text-slate-400 mb-1">Officer Reasoning:</div>
                  <p className="text-slate-700 leading-relaxed bg-white p-3 rounded-lg border border-beige-200">
                    {e.lowerAuthorityReasoning}
                  </p>
                </div>
                <div>
                  <div className="text-[11px] font-mono uppercase text-slate-400 mb-1">Fatal Legal Defect:</div>
                  <p className="text-rose-900 leading-relaxed bg-rose-50 p-3 rounded-lg border border-rose-200">
                    {e.legalError}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
