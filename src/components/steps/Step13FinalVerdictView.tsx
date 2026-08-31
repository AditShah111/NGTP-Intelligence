'use client';

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
