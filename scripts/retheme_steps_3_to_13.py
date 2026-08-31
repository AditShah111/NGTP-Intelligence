import os

# Step 3 & 4: Precedents
s3 = """'use client';

import React from 'react';
import { PrecedentAnalysis } from '../../types';
import { BookOpen, Award, CheckCircle2, AlertCircle } from 'lucide-react';

interface Props {
  precedents: PrecedentAnalysis[];
}

export const Step3Step4PrecedentsView: React.FC<Props> = ({ precedents }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Steps 3 & 4: Landmark Judicial Precedents & 6-Axis Comparability</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Quantified factual, statutory, and evidentiary similarity scores (0–100) against leading Supreme Court and High Court precedents.
            </p>
          </div>
        </div>

        <div className="space-y-4 mt-6">
          {precedents.map((p) => (
            <div
              key={p.id}
              className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-beige-200">
                <div>
                  <h4 className="text-base font-serif font-bold text-slate-900">{p.caseName}</h4>
                  <div className="text-xs text-slate-600 flex items-center gap-2 mt-0.5">
                    <span className="font-semibold text-amber-800">{p.court}</span>
                    <span>•</span>
                    <span className="font-mono text-slate-500">{p.citation}</span>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full border ${
                    p.favourableApplicability === 'HIGH' 
                      ? 'bg-emerald-50 text-emerald-800 border-emerald-200' 
                      : 'bg-blue-50 text-blue-800 border-blue-200'
                  }`}>
                    {p.favourableApplicability === 'HIGH' ? 'Direct / Controlling Ratio' : 'Persuasive'}
                  </span>
                  <div className="bg-white border border-beige-200 px-3 py-1 rounded-lg text-center shadow-sm">
                    <div className="text-[10px] font-mono text-slate-400 uppercase">Match Score</div>
                    <div className="text-sm font-mono font-bold text-amber-700">{p.comparabilityScore.totalScore}/100</div>
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 text-xs">
                <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                  <div className="text-[11px] font-mono uppercase text-slate-400 mb-1 font-semibold">Core Ratio & Legal Principle:</div>
                  <p className="text-slate-800 leading-relaxed font-sans">{p.ratioLegalPrinciple}</p>
                </div>
                <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                  <div className="text-[11px] font-mono uppercase text-slate-400 mb-1 font-semibold">Litigation Application:</div>
                  <p className="text-slate-800 leading-relaxed font-sans">{p.litigationUse}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
"""
with open("src/components/steps/Step3Step4PrecedentsView.tsx", "w", encoding="utf-8") as f:
    f.write(s3)

# Step 5: Lower Authority Errors
s5 = """'use client';

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
"""
with open("src/components/steps/Step5LowerAuthorityErrorsView.tsx", "w", encoding="utf-8") as f:
    f.write(s5)

# Step 6: Submission Optimizer
s6 = """'use client';

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
"""
with open("src/components/steps/Step6SubmissionOptimizerView.tsx", "w", encoding="utf-8") as f:
    f.write(s6)

# Step 7: Red-Team War Room
s7 = """'use client';

import React from 'react';
import { AdversarialRedTeamItem } from '../../types';
import { Swords, ShieldAlert, CheckCircle2, AlertTriangle } from 'lucide-react';

interface Props {
  redTeamItems: AdversarialRedTeamItem[];
}

export const Step7RedTeamBattleView: React.FC<Props> = ({ redTeamItems }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 7: Adversarial Red-Team War Room (Opposing Counsel Simulation)</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Simulating aggressive Revenue Standing Counsel attacks against Section 16(2)(c), Section 155, and supplier legitimacy.
            </p>
          </div>
          <span className="text-xs font-mono px-3 py-1 rounded-full bg-rose-50 text-rose-800 border border-rose-200 font-semibold">
            {redTeamItems.length} Attack Vectors Tested
          </span>
        </div>

        <div className="space-y-4 mt-6">
          {redTeamItems.map((item) => (
            <div
              key={item.id}
              className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
            >
              <div className="flex items-center justify-between gap-2 pb-3 border-b border-beige-200">
                <span className="font-mono text-xs font-bold text-slate-700 uppercase tracking-wide">
                  {item.category}
                </span>
                <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full border ${
                  item.survivesAttack 
                    ? 'bg-emerald-50 text-emerald-800 border-emerald-200' 
                    : 'bg-rose-50 text-rose-800 border-rose-200'
                }`}>
                  {item.survivesAttack ? '✓ Defense Survives Attack' : '⚠️ Residual Vulnerability'}
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-3 text-xs">
                <div className="bg-rose-50/80 p-3.5 rounded-lg border border-rose-200">
                  <div className="text-[11px] font-mono uppercase text-rose-800 font-bold mb-1 flex items-center gap-1.5">
                    <Swords className="w-3.5 h-3.5 text-rose-600" />
                    Revenue Attack (Standing Counsel):
                  </div>
                  <p className="text-rose-950 leading-relaxed font-sans">{item.opposingArgument}</p>
                </div>

                <div className="bg-emerald-50/80 p-3.5 rounded-lg border border-emerald-200">
                  <div className="text-[11px] font-mono uppercase text-emerald-800 font-bold mb-1 flex items-center gap-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                    Taxpayer Defensive Counter:
                  </div>
                  <p className="text-emerald-950 leading-relaxed font-sans">{item.taxpayerResponse}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
"""
with open("src/components/steps/Step7RedTeamBattleView.tsx", "w", encoding="utf-8") as f:
    f.write(s7)

# Step 8: Evidence Gaps
s8 = """'use client';

import React from 'react';
import { EvidenceGapItem } from '../../types';
import { SearchX, AlertTriangle, ArrowUpRight } from 'lucide-react';

interface Props {
  evidenceGaps: EvidenceGapItem[];
}

export const Step8EvidenceGapView: React.FC<Props> = ({ evidenceGaps }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 8: Evidence Gap Prioritization & Remediation</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Prioritized list of missing documents required to convert potential legal arguments into unassailable evidence.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          {evidenceGaps.map((g, idx) => (
            <div
              key={idx}
              className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
            >
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-200">
                  {g.priority} Priority
                </span>
                <span className="text-[11px] font-mono text-slate-500">{g.category}</span>
              </div>

              <h4 className="font-serif font-bold text-sm text-slate-900 mb-2">{g.missingEvidence}</h4>
              <p className="text-xs text-slate-700 leading-relaxed bg-white p-3 rounded-lg border border-beige-200 mb-3">
                {g.whyItMatters}
              </p>

              <div className="text-[11px] text-slate-600 pt-2 border-t border-beige-200 flex items-center justify-between font-mono">
                <span>Source: <strong className="text-slate-800">{g.possibleSource}</strong></span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
"""
with open("src/components/steps/Step8EvidenceGapView.tsx", "w", encoding="utf-8") as f:
    f.write(s8)

# Step 9 & 10: Scores (Dual SVG Radial Gauges)
s9 = """'use client';

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
"""
with open("src/components/steps/Step9Step10ScoresView.tsx", "w", encoding="utf-8") as f:
    f.write(s9)

# Step 11: Forward Decision
s11 = """'use client';

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
"""
with open("src/components/steps/Step11ForwardDecisionView.tsx", "w", encoding="utf-8") as f:
    f.write(s11)

# Step 12: Draft Audit
s12 = """'use client';

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
"""
with open("src/components/steps/Step12DraftAuditView.tsx", "w", encoding="utf-8") as f:
    f.write(s12)

# Step 13: Final Executive Verdict
s13 = """'use client';

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
"""
with open("src/components/steps/Step13FinalVerdictView.tsx", "w", encoding="utf-8") as f:
    f.write(s13)

print("Rethemed Step 3 through Step 13!")