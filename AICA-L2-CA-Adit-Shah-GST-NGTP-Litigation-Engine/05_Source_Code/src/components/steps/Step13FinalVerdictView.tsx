'use client';

import React from 'react';
import { FinalEvaluatorOutput } from '../../types';
import { Trophy, CheckCircle2, AlertTriangle, ShieldCheck, Download } from 'lucide-react';

interface Props {
  output: FinalEvaluatorOutput;
}

export const Step13FinalVerdictView: React.FC<Props> = ({ output }) => {
  const { executiveVerdict, finalLitigationAssessment } = output;
  const isProceed = executiveVerdict.recommendation === 'PROCEED' || executiveVerdict.recommendation === 'PROCEED AFTER RECTIFICATION';

  return (
    <div className="space-y-6">
      {/* Executive Decision Banner */}
      <div className={`border rounded-2xl p-8 shadow-sm ${
        isProceed ? 'bg-emerald-50/60 border-emerald-300' : 'bg-rose-50/60 border-rose-300'
      }`}>
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pb-6 border-b border-beige-300/60">
          <div>
            <div className="flex items-center gap-2 mb-1.5">
              <Trophy className={`w-5 h-5 ${isProceed ? 'text-emerald-700' : 'text-rose-700'}`} />
              <span className="font-mono text-xs uppercase font-bold text-slate-600">Executive Evaluator Verdict</span>
            </div>
            <h2 className="text-2xl font-serif font-bold text-slate-900">{executiveVerdict.recommendation}</h2>
            <p className="text-xs text-slate-600 mt-1 max-w-2xl leading-relaxed font-sans">
              {finalLitigationAssessment.proceedExplanation}
            </p>
          </div>

          <div className="flex items-center gap-3">
            <div className="bg-white border border-beige-300 rounded-xl p-4 text-center min-w-[130px] shadow-sm">
              <div className="text-[11px] font-mono uppercase text-slate-500 font-semibold">Readiness</div>
              <div className="text-2xl font-bold font-mono text-amber-700 mt-0.5">{executiveVerdict.litigationReadiness}/100</div>
            </div>
            <div className="bg-white border border-beige-300 rounded-xl p-4 text-center min-w-[130px] shadow-sm">
              <div className="text-[11px] font-mono uppercase text-slate-500 font-semibold">Viability</div>
              <div className="text-2xl font-bold font-mono text-emerald-700 mt-0.5">{executiveVerdict.litigationViability}/100</div>
            </div>
          </div>
        </div>

        {/* Top 5 Reasons */}
        <div className="pt-6">
          <h4 className="font-serif font-bold text-sm text-slate-900 mb-3">Top 5 Evidentiary & Strategic Rationale:</h4>
          <div className="space-y-2">
            {executiveVerdict.top5Reasons.map((reason, idx) => (
              <div key={idx} className="flex items-start gap-2.5 p-3 rounded-xl bg-white border border-beige-200 text-xs text-slate-800 shadow-sm">
                <span className="font-mono font-bold text-amber-700">{idx + 1}.</span>
                <span className="leading-relaxed font-sans">{reason}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
