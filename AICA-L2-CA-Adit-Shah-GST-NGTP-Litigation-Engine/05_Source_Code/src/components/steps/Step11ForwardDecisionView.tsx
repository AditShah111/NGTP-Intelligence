'use client';

import React from 'react';
import { ForwardLitigationDecision } from '../../types';
import { Compass, TrendingUp, CheckCircle2 } from 'lucide-react';

interface Props {
  decision: ForwardLitigationDecision;
}

export const Step11ForwardDecisionView: React.FC<Props> = ({ decision }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 11: Forward Litigation Decision & Score Potential</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Quantifying score improvements achievable through specific evidentiary and drafting actions.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-6">
          <div className="bg-beige-50 border border-beige-200 rounded-xl p-5 text-center">
            <div className="text-xs font-mono uppercase text-slate-500">Current Score</div>
            <div className="text-3xl font-mono font-bold text-slate-900 mt-1">{decision.currentReadinessScore}/100</div>
          </div>
          <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-5 text-center">
            <div className="text-xs font-mono uppercase text-emerald-800 font-semibold">Potential Score After Remediation</div>
            <div className="text-3xl font-mono font-bold text-emerald-700 mt-1">{decision.potentialScoreAfterRemediation}/100</div>
          </div>
        </div>

        <div className="mt-6 space-y-3">
          <h4 className="font-serif font-bold text-sm text-slate-900">Mandatory Remediation Actions:</h4>
          <div className="space-y-2">
            {decision.actionRequiredToAchievePotential.map((action, idx) => (
              <div key={idx} className="flex items-center gap-2.5 p-3 rounded-lg bg-beige-50/80 border border-beige-200 text-xs text-slate-800">
                <CheckCircle2 className="w-4 h-4 text-amber-700 flex-shrink-0" />
                <span>{action}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
