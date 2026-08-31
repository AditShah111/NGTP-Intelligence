'use client';

import React from 'react';
import { ReadinessScoreBreakdown, ViabilityScoreBreakdown } from '@/types';
import { Gauge, Award, TrendingUp, ShieldCheck, CheckCircle2 } from 'lucide-react';

interface Step9Props {
  readiness: ReadinessScoreBreakdown;
  viability: ViabilityScoreBreakdown;
}

export const Step9Step10ScoresView: React.FC<Step9Props> = ({ readiness, viability }) => {
  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <Gauge className="w-4 h-4 text-amber-400" />
          STEPS 9 & 10: Dual Scoring Engine (Litigation Readiness vs Substantive Viability)
        </h3>
        <p className="text-xs text-slate-400">
          Mathematical scoring separating procedural & drafting readiness from substantive legal viability on merits.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Step 9: Litigation Readiness Score Card */}
        <div className="legal-glass rounded-xl p-5 border border-emerald-500/40 shadow-xl">
          <div className="flex justify-between items-center pb-3 border-b border-legal-800">
            <div>
              <div className="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold">STEP 9 SCORE</div>
              <h4 className="font-serif font-bold text-lg text-white">Litigation Readiness</h4>
            </div>
            <div className="text-right">
              <div className="text-3xl font-mono font-extrabold text-emerald-400">
                {readiness.totalScore}<span className="text-xs text-slate-500">/100</span>
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800">
                {readiness.interpretation}
              </span>
            </div>
          </div>

          <div className="mt-4 space-y-2.5 text-xs font-mono">
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">A. Statutory Position</span>
              <span className="text-emerald-400 font-bold">{readiness.statutoryPosition}/20</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">B. Evidence Quality & Traceability</span>
              <span className="text-emerald-400 font-bold">{readiness.evidence}/20</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">C. Precedent Strength</span>
              <span className="text-emerald-400 font-bold">{readiness.precedent}/15</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">D. Lower Authority Error Identification</span>
              <span className="text-emerald-400 font-bold">{readiness.lowerAuthorityError}/15</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">E. Drafting Quality & Structure</span>
              <span className="text-emerald-400 font-bold">{readiness.draftingQuality}/10</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">F. Counterargument Resilience</span>
              <span className="text-emerald-400 font-bold">{readiness.counterargumentResilience}/10</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">G. Procedural Position & Limitation</span>
              <span className="text-emerald-400 font-bold">{readiness.proceduralPosition}/10</span>
            </div>
          </div>
        </div>

        {/* Step 10: Litigation Viability Score Card */}
        <div className="legal-glass rounded-xl p-5 border border-blue-500/40 shadow-xl">
          <div className="flex justify-between items-center pb-3 border-b border-legal-800">
            <div>
              <div className="text-[11px] font-mono uppercase tracking-wider text-blue-400 font-bold">STEP 10 SCORE</div>
              <h4 className="font-serif font-bold text-lg text-white">Substantive Viability</h4>
            </div>
            <div className="text-right">
              <div className="text-3xl font-mono font-extrabold text-blue-400">
                {viability.totalScore}<span className="text-xs text-slate-500">/100</span>
              </div>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-blue-300 border border-blue-800">
                Outcome: {viability.probabilityOfFavourableOutcome}
              </span>
            </div>
          </div>

          <div className="mt-4 space-y-2.5 text-xs font-mono">
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">Merits on Law</span>
              <span className="text-blue-400 font-bold">{viability.merits}/20</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">Documentary Substratum</span>
              <span className="text-blue-400 font-bold">{viability.evidenceQuality}/20</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">Binding Precedent Support</span>
              <span className="text-blue-400 font-bold">{viability.precedentSupport}/15</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">Procedural Soundness</span>
              <span className="text-blue-400 font-bold">{viability.proceduralSoundness}/10</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">Opposing Case Resilience</span>
              <span className="text-blue-400 font-bold">{viability.opposingCaseDifficulty}/15</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">Curability of Evidence Gaps</span>
              <span className="text-blue-400 font-bold">{viability.curabilityOfGaps}/10</span>
            </div>
            <div className="flex justify-between items-center p-2 rounded bg-legal-950/80 border border-legal-800">
              <span className="text-slate-300">Appellate Forum Trend</span>
              <span className="text-blue-400 font-bold">{viability.appellateForumTrend}/10</span>
            </div>
          </div>
          <div className="mt-3 p-2.5 rounded bg-blue-950/40 border border-blue-900/50 text-[11px] text-blue-200">
            <strong className="font-mono">Assessment Note:</strong> {viability.probabilityNote}
          </div>
        </div>
      </div>
    </div>
  );
};
