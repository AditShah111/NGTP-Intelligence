'use client';

import React from 'react';
import { ReadinessScoreBreakdown, ViabilityScoreBreakdown } from '../../types';
import { Gauge, CheckCircle2, AlertTriangle, TrendingUp } from 'lucide-react';

interface Props {
  readiness: ReadinessScoreBreakdown;
  viability: ViabilityScoreBreakdown;
}

export const Step9Step10ScoresView: React.FC<Props> = ({ readiness, viability }) => {
  const readinessRadius = 55;
  const readinessCircumference = 2 * Math.PI * readinessRadius;
  const readinessOffset = readinessCircumference - (readiness.totalScore / 100) * readinessCircumference;

  const viabilityRadius = 55;
  const viabilityCircumference = 2 * Math.PI * viabilityRadius;
  const viabilityOffset = viabilityCircumference - (viability.totalScore / 100) * viabilityCircumference;

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Readiness Card */}
        <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
          <div className="text-center pb-4 border-b border-beige-200">
            <h3 className="text-lg font-serif font-bold text-slate-900">Step 9: Litigation Readiness Score</h3>
            <p className="text-xs text-slate-500 mt-0.5">Is the case legally and evidentially complete for filing?</p>
          </div>

          <div className="flex flex-col items-center justify-center my-6">
            <div className="relative w-36 h-36 flex items-center justify-center">
              <svg className="w-full h-full -rotate-90" viewBox="0 0 140 140">
                <circle cx="70" cy="70" r={readinessRadius} className="text-beige-200 stroke-current" strokeWidth="12" fill="transparent" />
                <circle
                  cx="70"
                  cy="70"
                  r={readinessRadius}
                  className="text-amber-600 stroke-current transition-all duration-1000 ease-out"
                  strokeWidth="12"
                  strokeDasharray={readinessCircumference}
                  strokeDashoffset={readinessOffset}
                  strokeLinecap="round"
                  fill="transparent"
                />
              </svg>
              <div className="absolute text-center">
                <span className="text-3xl font-mono font-bold text-slate-900">{readiness.totalScore}</span>
                <span className="text-xs text-slate-400 block">/ 100</span>
              </div>
            </div>
            <p className="text-xs font-semibold text-slate-700 text-center mt-2 px-4 py-1.5 rounded-full bg-beige-100">
              {readiness.interpretation}
            </p>
          </div>

          <div className="space-y-2 pt-2 border-t border-beige-200 text-xs">
            <div className="flex justify-between py-1 border-b border-beige-100 text-slate-600">
              <span>Statutory Position:</span>
              <strong className="text-slate-900 font-mono">{readiness.statutoryPosition}/20</strong>
            </div>
            <div className="flex justify-between py-1 border-b border-beige-100 text-slate-600">
              <span>Evidence Quality:</span>
              <strong className="text-slate-900 font-mono">{readiness.evidence}/20</strong>
            </div>
            <div className="flex justify-between py-1 border-b border-beige-100 text-slate-600">
              <span>Precedent Support:</span>
              <strong className="text-slate-900 font-mono">{readiness.precedent}/15</strong>
            </div>
            <div className="flex justify-between py-1 text-slate-600">
              <span>Lower Authority Error Audit:</span>
              <strong className="text-slate-900 font-mono">{readiness.lowerAuthorityError}/15</strong>
            </div>
          </div>
        </div>

        {/* Viability Card */}
        <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
          <div className="text-center pb-4 border-b border-beige-200">
            <h3 className="text-lg font-serif font-bold text-slate-900">Step 10: Litigation Viability Score</h3>
            <p className="text-xs text-slate-500 mt-0.5">What is the probability of a favourable outcome?</p>
          </div>

          <div className="flex flex-col items-center justify-center my-6">
            <div className="relative w-36 h-36 flex items-center justify-center">
              <svg className="w-full h-full -rotate-90" viewBox="0 0 140 140">
                <circle cx="70" cy="70" r={viabilityRadius} className="text-beige-200 stroke-current" strokeWidth="12" fill="transparent" />
                <circle
                  cx="70"
                  cy="70"
                  r={viabilityRadius}
                  className="text-emerald-600 stroke-current transition-all duration-1000 ease-out"
                  strokeWidth="12"
                  strokeDasharray={viabilityCircumference}
                  strokeDashoffset={viabilityOffset}
                  strokeLinecap="round"
                  fill="transparent"
                />
              </svg>
              <div className="absolute text-center">
                <span className="text-3xl font-mono font-bold text-slate-900">{viability.totalScore}</span>
                <span className="text-xs text-slate-400 block">/ 100</span>
              </div>
            </div>
            <p className="text-xs font-semibold text-emerald-800 text-center mt-2 px-4 py-1.5 rounded-full bg-emerald-50 border border-emerald-200">
              Outcome Probability: {viability.probabilityOfFavourableOutcome}
            </p>
          </div>

          <div className="bg-beige-50 p-3.5 rounded-xl border border-beige-200 text-xs text-slate-700 leading-relaxed">
            <p className="italic">{viability.probabilityNote}</p>
          </div>
        </div>
      </div>
    </div>
  );
};
