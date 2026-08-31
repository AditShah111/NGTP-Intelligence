'use client';

import React from 'react';
import { ImprovedSubmissionGround } from '../../types';
import { FileEdit, ShieldCheck, ArrowRight } from 'lucide-react';

interface Props {
  grounds: ImprovedSubmissionGround[];
}

export const Step6SubmissionOptimizerView: React.FC<Props> = ({ grounds }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 6: Syllogistic Grounds of Appeal & Submission Optimizer</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Structured grounds of challenge formulated according to IRAC (Issue, Rule, Application, Conclusion) standards.
            </p>
          </div>
        </div>

        <div className="space-y-4 mt-6">
          {grounds.map((g) => (
            <div
              key={g.groundNumber}
              className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
            >
              <div className="flex items-center justify-between gap-2 pb-3 border-b border-beige-200">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs font-bold px-2.5 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-200">
                    {g.groundNumber}
                  </span>
                  <h4 className="font-serif font-bold text-sm text-slate-900">{g.title}</h4>
                </div>
                <span className="text-xs font-mono font-bold text-amber-700 bg-white px-2.5 py-1 rounded border border-beige-200">
                  Strength: {g.groundStrength}/100
                </span>
              </div>

              <div className="mt-3 text-xs space-y-3">
                <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                  <strong className="text-slate-900 font-serif">Legal Proposition:</strong>
                  <p className="text-slate-700 mt-1 leading-relaxed">{g.proposition}</p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  <div className="bg-white p-3 rounded-lg border border-beige-200">
                    <span className="text-[11px] font-mono uppercase text-slate-400">Statutory Basis:</span>
                    <p className="text-slate-800 font-semibold mt-0.5">{g.statutoryBasis}</p>
                  </div>
                  <div className="bg-white p-3 rounded-lg border border-beige-200">
                    <span className="text-[11px] font-mono uppercase text-slate-400">Controlling Precedent:</span>
                    <p className="text-amber-800 font-semibold mt-0.5">{g.precedent}</p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
