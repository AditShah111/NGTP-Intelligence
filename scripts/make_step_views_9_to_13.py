import os

code_step9 = """'use client';

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
"""

code_step11 = """'use client';

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
"""

code_step12 = """'use client';

import React from 'react';
import { DraftAuditDefect } from '@/types';
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
"""

code_step13 = """'use client';

import React from 'react';
import { FinalEvaluatorOutput } from '@/types';
import { Gavel, Award, ShieldAlert, CheckCircle2, ArrowRight, FileText, AlertTriangle } from 'lucide-react';

interface Step13Props {
  output: FinalEvaluatorOutput;
}

export const Step13FinalVerdictView: React.FC<Step13Props> = ({ output }) => {
  const v = output.executiveVerdict;
  const a = output.finalLitigationAssessment;

  const getVerdictStyle = (rec: string) => {
    if (rec.includes('PROCEED') && !rec.includes('NOT')) return 'bg-emerald-950/90 text-emerald-300 border-emerald-500/60 shadow-emerald-500/10';
    if (rec.includes('HOLD') || rec.includes('RECTIFICATION')) return 'bg-amber-950/90 text-amber-300 border-amber-500/60 shadow-amber-500/10';
    return 'bg-rose-950/90 text-rose-300 border-rose-500/60 shadow-rose-500/10';
  };

  return (
    <div className="space-y-6">
      {/* 1. Executive Verdict Banner */}
      <div className={`rounded-xl p-6 border ${getVerdictStyle(v.recommendation)} shadow-2xl`}>
        <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-4 pb-4 border-b border-legal-800/80">
          <div>
            <span className="text-[11px] font-mono uppercase tracking-widest text-slate-400 font-bold">EXECUTIVE VERDICT</span>
            <h3 className="text-2xl font-serif font-extrabold text-white mt-1">
              RECOMMENDATION: {v.recommendation}
            </h3>
            <p className="text-xs text-slate-300 mt-1">
              Rigorous evaluative synthesis for senior tax counsel review.
            </p>
          </div>
          <div className="flex items-center gap-4 font-mono">
            <div className="text-center bg-black/40 p-3 rounded-lg border border-legal-700 min-w-[120px]">
              <div className="text-[10px] text-slate-400">Readiness Score</div>
              <div className="text-2xl font-bold text-emerald-400">{v.litigationReadiness}/100</div>
            </div>
            <div className="text-center bg-black/40 p-3 rounded-lg border border-legal-700 min-w-[120px]">
              <div className="text-[10px] text-slate-400">Viability Score</div>
              <div className="text-2xl font-bold text-blue-400">{v.litigationViability}/100</div>
            </div>
          </div>
        </div>

        {/* Top 5 Reasons */}
        <div className="mt-4">
          <div className="text-[11px] font-mono uppercase text-amber-400 font-bold mb-2">Top 5 Evaluative Pillars:</div>
          <ul className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs text-slate-200">
            {v.top5Reasons.map((reason, idx) => (
              <li key={idx} className="flex items-start gap-2 bg-black/30 p-2.5 rounded border border-legal-800/60">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                <span className="leading-relaxed">{reason}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* 2 & 3. Strongest vs Weakest Parameters */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div className="legal-glass rounded-xl p-4 border border-legal-800">
          <strong className="text-emerald-400 font-mono text-[11px] uppercase">2. Strongest Legal Parameters:</strong>
          <ul className="list-disc list-inside text-slate-300 mt-2 space-y-1.5">
            {output.strongestLegalParameters.map((p, i) => (
              <li key={i}>{p}</li>
            ))}
          </ul>
        </div>
        <div className="legal-glass rounded-xl p-4 border border-legal-800">
          <strong className="text-rose-400 font-mono text-[11px] uppercase">3. Weakest Parameters (Litigation Risk):</strong>
          <ul className="list-disc list-inside text-slate-300 mt-2 space-y-1.5">
            {output.weakestParameters.map((p, i) => (
              <li key={i}>{p}</li>
            ))}
          </ul>
        </div>
      </div>

      {/* 4 & 5. Grounds & Opposing Arguments */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div className="legal-glass rounded-xl p-4 border border-legal-800">
          <strong className="text-blue-400 font-mono text-[11px] uppercase">4. Strongest Ranked Grounds of Challenge:</strong>
          <div className="mt-2 space-y-1.5">
            {output.strongestGroundsOfChallenge.map((g, i) => (
              <div key={i} className="flex justify-between items-center p-2 rounded bg-legal-950 border border-legal-800">
                <span>Rank #{g.rank}: {g.ground}</span>
                <span className="font-mono text-emerald-400 font-bold">{g.strength}/100</span>
              </div>
            ))}
          </div>
        </div>
        <div className="legal-glass rounded-xl p-4 border border-legal-800">
          <strong className="text-rose-400 font-mono text-[11px] uppercase">5. Strongest Opposing Arguments:</strong>
          <ul className="list-disc list-inside text-rose-200/90 mt-2 space-y-1.5">
            {output.strongestOpposingArguments.map((oa, i) => (
              <li key={i}>{oa}</li>
            ))}
          </ul>
        </div>
      </div>

      {/* 10. Litigation Improvement Plan (P0 / P1 / P2) */}
      <div className="legal-glass rounded-xl p-5 border border-amber-500/40 shadow-xl">
        <div className="text-sm font-serif font-bold text-amber-300 mb-3 flex items-center gap-2">
          <Award className="w-4 h-4 text-amber-400" />
          10. Action Priority Matrix (P0 / P1 / P2)
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
          <div className="bg-rose-950/40 p-3.5 rounded-lg border border-rose-800/60">
            <strong className="text-rose-300 font-mono text-[11px] uppercase">P0 — Must Fix Before Filing:</strong>
            <ul className="list-disc list-inside text-slate-200 mt-2 space-y-1">
              {output.litigationImprovementPlan.p0MustFixBeforeFiling.map((item, i) => (
                <li key={i}>{item}</li>
              ))}
            </ul>
          </div>
          <div className="bg-amber-950/40 p-3.5 rounded-lg border border-amber-800/60">
            <strong className="text-amber-300 font-mono text-[11px] uppercase">P1 — Strongly Recommended:</strong>
            <ul className="list-disc list-inside text-slate-200 mt-2 space-y-1">
              {output.litigationImprovementPlan.p1StronglyRecommended.map((item, i) => (
                <li key={i}>{item}</li>
              ))}
            </ul>
          </div>
          <div className="bg-blue-950/40 p-3.5 rounded-lg border border-blue-800/60">
            <strong className="text-blue-300 font-mono text-[11px] uppercase">P2 — Additional Strengthening:</strong>
            <ul className="list-disc list-inside text-slate-200 mt-2 space-y-1">
              {output.litigationImprovementPlan.p2AdditionalStrengthening.map((item, i) => (
                <li key={i}>{item}</li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      {/* 11. Final Litigation Assessment Answers */}
      <div className="legal-glass rounded-xl p-5 border border-legal-800 bg-[#0a0f1d] shadow-xl text-xs space-y-3">
        <div className="text-sm font-serif font-bold text-white mb-2">11. Final Strategic Counsel Answers:</div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          <div className="bg-legal-950 p-3 rounded border border-legal-800">
            <span className="text-slate-400 font-mono text-[10px] uppercase">Should the matter proceed to litigation?</span>
            <p className="text-emerald-300 font-bold mt-1">{a.shouldProceed ? 'YES' : 'NO'} - {a.proceedExplanation}</p>
          </div>
          <div className="bg-legal-950 p-3 rounded border border-legal-800">
            <span className="text-slate-400 font-mono text-[10px] uppercase">Single Biggest Litigation Risk:</span>
            <p className="text-rose-300 mt-1">{a.singleBiggestRisk}</p>
          </div>
          <div className="bg-legal-950 p-3 rounded border border-legal-800">
            <span className="text-slate-400 font-mono text-[10px] uppercase">Single Strongest Advantage:</span>
            <p className="text-amber-300 mt-1">{a.singleStrongestAdvantage}</p>
          </div>
          <div className="bg-legal-950 p-3 rounded border border-legal-800">
            <span className="text-slate-400 font-mono text-[10px] uppercase">Evidence Most Needed:</span>
            <p className="text-blue-300 mt-1">{a.evidenceMostNeeded}</p>
          </div>
        </div>
        <div className="bg-legal-950 p-3 rounded border border-legal-800">
          <span className="text-slate-400 font-mono text-[10px] uppercase">Legal Proposition Requiring Most Careful Drafting:</span>
          <p className="text-purple-300 mt-1">{a.propositionRequiringCarefulDrafting}</p>
        </div>
      </div>
    </div>
  );
};
"""

with open("src/components/steps/Step9Step10ScoresView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step9)
with open("src/components/steps/Step11ForwardDecisionView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step11)
with open("src/components/steps/Step12DraftAuditView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step12)
with open("src/components/steps/Step13FinalVerdictView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step13)

print("Wrote Step Views 9 to 13 successfully!")