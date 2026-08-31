'use client';

import React from 'react';
import { ForwardLitigationDecision } from '@/types';
import { Navigation, TrendingUp, ShieldAlert, CheckCircle2, ArrowUpRight } from 'lucide-react';

interface Step11Props {
  decision: ForwardLitigationDecision;
}

export const Step11ForwardDecisionView: React.FC<Step11Props> = ({ decision }) => {
  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <Navigation className="w-4 h-4 text-amber-400" />
          STEP 11: Base Score → Forward Litigation Decision
        </h3>
        <p className="text-xs text-slate-400">
          Remediation roadmap bridging current readiness to maximum litigation potential.
        </p>
      </div>

      <div className="legal-glass rounded-xl p-5 border border-legal-800 shadow-xl">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 pb-4 border-b border-legal-800">
          <div>
            <div className="text-xs font-mono text-slate-400 uppercase">Score Progression</div>
            <div className="text-lg font-serif font-bold text-white mt-0.5">Potential Score Lift via Targeted Remediation</div>
          </div>
          <div className="flex items-center gap-4 font-mono">
            <div className="text-center p-2.5 rounded bg-legal-950 border border-legal-800 min-w-[100px]">
              <div className="text-[10px] text-slate-400">Current Score</div>
              <div className="text-xl font-bold text-amber-400">{decision.currentReadinessScore}/100</div>
            </div>
            <ArrowUpRight className="w-5 h-5 text-emerald-400" />
            <div className="text-center p-2.5 rounded bg-emerald-950/80 border border-emerald-700 min-w-[100px]">
              <div className="text-[10px] text-emerald-300">Potential Score</div>
              <div className="text-xl font-bold text-emerald-400">{decision.potentialScoreAfterRemediation}/100</div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 text-xs">
          <div className="bg-emerald-950/30 p-3.5 rounded-lg border border-emerald-900/50">
            <strong className="text-emerald-400 font-mono text-[11px] uppercase">Score Enhancers:</strong>
            <ul className="list-disc list-inside text-emerald-200/90 mt-1.5 space-y-1">
              {decision.scoreEnhancers.map((e, idx) => (
                <li key={idx}>{e}</li>
              ))}
            </ul>
          </div>
          <div className="bg-rose-950/30 p-3.5 rounded-lg border border-rose-900/50">
            <strong className="text-rose-400 font-mono text-[11px] uppercase">Score Reducers:</strong>
            <ul className="list-disc list-inside text-rose-200/90 mt-1.5 space-y-1">
              {decision.scoreReducers.map((r, idx) => (
                <li key={idx}>{r}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className="mt-4 bg-legal-950 p-4 rounded-lg border border-legal-800 text-xs">
          <strong className="text-amber-400 font-mono text-[11px] uppercase">Mandatory Action Items to Achieve 100/100 Potential:</strong>
          <ul className="list-decimal list-inside text-slate-200 mt-2 space-y-1.5">
            {decision.actionRequiredToAchievePotential.map((act, idx) => (
              <li key={idx} className="leading-relaxed">{act}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};
