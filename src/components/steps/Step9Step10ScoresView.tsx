'use client';

import React from 'react';
import { ReadinessScoreBreakdown, ViabilityScoreBreakdown } from '../../types';
import { Gauge, Award, TrendingUp, ShieldCheck, CheckCircle2, AlertCircle, ArrowUpRight, Scale, BarChart3 } from 'lucide-react';

interface Step9Props {
  readiness: ReadinessScoreBreakdown;
  viability: ViabilityScoreBreakdown;
}

export const Step9Step10ScoresView: React.FC<Step9Props> = ({ readiness, viability }) => {
  const readinessColor = readiness.totalScore >= 85 ? '#10b981' : (readiness.totalScore >= 70 ? '#f59e0b' : '#ef4444');
  const viabilityColor = viability.totalScore >= 85 ? '#3b82f6' : (viability.totalScore >= 70 ? '#f59e0b' : '#ef4444');

  // SVG Circular Gauge calculations
  const radius = 54;
  const circumference = 2 * Math.PI * radius;
  const readinessOffset = circumference - (readiness.totalScore / 100) * circumference;
  const viabilityOffset = circumference - (viability.totalScore / 100) * circumference;

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-2">
        <div>
          <h3 className="text-lg font-serif font-bold text-white flex items-center gap-2">
            <Gauge className="w-5 h-5 text-amber-400" />
            STEPS 9 & 10: Dual Scoring Engine (Readiness vs Viability)
          </h3>
          <p className="text-xs text-slate-400">
            Independent mathematical modeling separating procedural & evidentiary readiness from substantive legal merits on appeal.
          </p>
        </div>
      </div>

      {/* Dual Radial Gauge Showcase */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Step 9: Litigation Readiness Gauge */}
        <div className="legal-glass rounded-2xl p-6 border border-emerald-500/30 shadow-2xl relative overflow-hidden group hover:border-emerald-500/60 transition-all">
          <div className="absolute -right-8 -top-8 w-32 h-32 bg-emerald-500/10 rounded-full blur-2xl pointer-events-none"></div>
          
          <div className="flex items-center justify-between pb-4 border-b border-legal-800/80">
            <div>
              <span className="text-[11px] font-mono uppercase tracking-widest text-emerald-400 font-bold flex items-center gap-1.5">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                STEP 9 AUDIT
              </span>
              <h4 className="text-xl font-serif font-bold text-white mt-1">Litigation Readiness Score</h4>
              <p className="text-xs text-slate-400">Pleading, evidence & procedural fitness</p>
            </div>
            
            {/* Circular Gauge */}
            <div className="relative flex items-center justify-center">
              <svg className="w-32 h-32 transform -rotate-90">
                <circle
                  cx="64"
                  cy="64"
                  r={radius}
                  stroke="#172440"
                  strokeWidth="10"
                  fill="transparent"
                />
                <circle
                  cx="64"
                  cy="64"
                  r={radius}
                  stroke={readinessColor}
                  strokeWidth="10"
                  strokeDasharray={circumference}
                  strokeDashoffset={readinessOffset}
                  strokeLinecap="round"
                  fill="transparent"
                  className="transition-all duration-1000 ease-out"
                />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center font-mono">
                <span className="text-3xl font-extrabold text-white">{readiness.totalScore}</span>
                <span className="text-[10px] text-slate-400">/ 100</span>
              </div>
            </div>
          </div>

          <div className="mt-4 mb-3">
            <span className="text-xs font-mono font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-800/60 inline-flex items-center gap-1.5">
              <CheckCircle2 className="w-3.5 h-3.5" />
              Interpretation: {readiness.interpretation}
            </span>
          </div>

          {/* 7 Weighted Dimension Bars */}
          <div className="space-y-2.5 pt-2 text-xs font-mono">
            {[
              { label: 'A. Statutory Position', val: readiness.statutoryPosition, max: 20, pct: (readiness.statutoryPosition / 20) * 100 },
              { label: 'B. Evidence Quality & Traceability', val: readiness.evidence, max: 20, pct: (readiness.evidence / 20) * 100 },
              { label: 'C. Precedent Strength', val: readiness.precedent, max: 15, pct: (readiness.precedent / 15) * 100 },
              { label: 'D. Lower Authority Error Identification', val: readiness.lowerAuthorityError, max: 15, pct: (readiness.lowerAuthorityError / 15) * 100 },
              { label: 'E. Drafting Quality & Syllogism', val: readiness.draftingQuality, max: 10, pct: (readiness.draftingQuality / 10) * 100 },
              { label: 'F. Counterargument Resilience', val: readiness.counterargumentResilience, max: 10, pct: (readiness.counterargumentResilience / 10) * 100 },
              { label: 'G. Procedural Position & Limitation', val: readiness.proceduralPosition, max: 10, pct: (readiness.proceduralPosition / 10) * 100 },
            ].map((d, i) => (
              <div key={i} className="bg-legal-950/70 p-2.5 rounded-lg border border-legal-800/60">
                <div className="flex justify-between items-center mb-1">
                  <span className="text-slate-300">{d.label}</span>
                  <span className="text-emerald-400 font-bold">{d.val} / {d.max}</span>
                </div>
                <div className="w-full bg-legal-900 rounded-full h-1.5 overflow-hidden">
                  <div 
                    className="bg-gradient-to-r from-emerald-600 to-emerald-400 h-1.5 rounded-full transition-all duration-700" 
                    style={{ width: `${d.pct}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Step 10: Litigation Viability Gauge */}
        <div className="legal-glass rounded-2xl p-6 border border-blue-500/30 shadow-2xl relative overflow-hidden group hover:border-blue-500/60 transition-all">
          <div className="absolute -right-8 -top-8 w-32 h-32 bg-blue-500/10 rounded-full blur-2xl pointer-events-none"></div>

          <div className="flex items-center justify-between pb-4 border-b border-legal-800/80">
            <div>
              <span className="text-[11px] font-mono uppercase tracking-widest text-blue-400 font-bold flex items-center gap-1.5">
                <span className="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>
                STEP 10 MERITS
              </span>
              <h4 className="text-xl font-serif font-bold text-white mt-1">Litigation Viability Score</h4>
              <p className="text-xs text-slate-400">Substantive likelihood of favourable decree</p>
            </div>

            {/* Circular Gauge */}
            <div className="relative flex items-center justify-center">
              <svg className="w-32 h-32 transform -rotate-90">
                <circle
                  cx="64"
                  cy="64"
                  r={radius}
                  stroke="#172440"
                  strokeWidth="10"
                  fill="transparent"
                />
                <circle
                  cx="64"
                  cy="64"
                  r={radius}
                  stroke={viabilityColor}
                  strokeWidth="10"
                  strokeDasharray={circumference}
                  strokeDashoffset={viabilityOffset}
                  strokeLinecap="round"
                  fill="transparent"
                  className="transition-all duration-1000 ease-out"
                />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center font-mono">
                <span className="text-3xl font-extrabold text-white">{viability.totalScore}</span>
                <span className="text-[10px] text-slate-400">/ 100</span>
              </div>
            </div>
          </div>

          <div className="mt-4 mb-3">
            <span className="text-xs font-mono font-semibold px-3 py-1 rounded-full bg-blue-950/80 text-blue-300 border border-blue-800/60 inline-flex items-center gap-1.5">
              <TrendingUp className="w-3.5 h-3.5" />
              Outcome Probability: {viability.probabilityOfFavourableOutcome}
            </span>
          </div>

          {/* Viability Breakdown */}
          <div className="space-y-2.5 pt-2 text-xs font-mono">
            {[
              { label: 'Substantive Legal Merits', val: viability.merits, max: 20, pct: (viability.merits / 20) * 100 },
              { label: 'Documentary Substratum', val: viability.evidenceQuality, max: 20, pct: (viability.evidenceQuality / 20) * 100 },
              { label: 'Binding Precedent Support', val: viability.precedentSupport, max: 15, pct: (viability.precedentSupport / 15) * 100 },
              { label: 'Opposing Case Resilience', val: viability.opposingCaseDifficulty, max: 15, pct: (viability.opposingCaseDifficulty / 15) * 100 },
              { label: 'Procedural Soundness', val: viability.proceduralSoundness, max: 10, pct: (viability.proceduralSoundness / 10) * 100 },
              { label: 'Curability of Evidence Gaps', val: viability.curabilityOfGaps, max: 10, pct: (viability.curabilityOfGaps / 10) * 100 },
              { label: 'Appellate Forum Jurisprudence Trend', val: viability.appellateForumTrend, max: 10, pct: (viability.appellateForumTrend / 10) * 100 },
            ].map((d, i) => (
              <div key={i} className="bg-legal-950/70 p-2.5 rounded-lg border border-legal-800/60">
                <div className="flex justify-between items-center mb-1">
                  <span className="text-slate-300">{d.label}</span>
                  <span className="text-blue-400 font-bold">{d.val} / {d.max}</span>
                </div>
                <div className="w-full bg-legal-900 rounded-full h-1.5 overflow-hidden">
                  <div 
                    className="bg-gradient-to-r from-blue-600 to-blue-400 h-1.5 rounded-full transition-all duration-700" 
                    style={{ width: `${d.pct}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>

          <div className="mt-4 p-3.5 rounded-xl bg-blue-950/40 border border-blue-900/60 text-xs text-blue-200 leading-relaxed font-sans">
            <strong className="font-mono text-blue-300">Analytical Evaluation: </strong>
            {viability.probabilityNote}
          </div>
        </div>
      </div>
    </div>
  );
};
