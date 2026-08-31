import os

code_step6 = """'use client';

import React from 'react';
import { ImprovedSubmissionGround } from '@/types';
import { FileEdit, CheckCircle, ShieldCheck, ArrowRight, AlertTriangle } from 'lucide-react';

interface Step6Props {
  grounds: ImprovedSubmissionGround[];
}

export const Step6SubmissionOptimizerView: React.FC<Step6Props> = ({ grounds }) => {
  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <FileEdit className="w-4 h-4 text-amber-400" />
          STEP 6: Submission Improvement Engine (Fact → Evidence → Statute → Precedent → Rebuttal)
        </h3>
        <p className="text-xs text-slate-400">
          Reconstruction of appellate grounds using unbreakable deductive legal syllogisms and pre-empting Revenue counterarguments.
        </p>
      </div>

      <div className="space-y-4">
        {grounds.map((g, idx) => (
          <div key={idx} className="legal-glass rounded-xl p-5 border border-legal-800 shadow-xl">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-3 border-b border-legal-800">
              <div className="flex items-center gap-2">
                <span className="font-mono font-bold text-xs px-2.5 py-1 rounded bg-amber-500 text-black">
                  {g.groundNumber}
                </span>
                <h4 className="font-serif font-bold text-sm text-white">{g.title}</h4>
              </div>
              <div className="flex items-center gap-2 font-mono text-xs">
                <span className="text-slate-400">Ground Strength:</span>
                <span className="text-emerald-400 font-bold px-2 py-0.5 rounded bg-emerald-950/80 border border-emerald-800">
                  {g.groundStrength}/100
                </span>
              </div>
            </div>

            {/* Core Proposition */}
            <div className="mt-3 bg-legal-950/70 p-3.5 rounded-lg border border-legal-800/80">
              <div className="text-[11px] font-mono text-amber-400 uppercase font-bold mb-1">
                Core Legal Proposition:
              </div>
              <p className="text-xs text-slate-200 leading-relaxed font-serif">
                "{g.proposition}"
              </p>
            </div>

            {/* Structured 6-Part Flow */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 text-xs">
              <div className="bg-legal-900/60 p-3 rounded-lg border border-legal-800/60">
                <strong className="text-slate-300 font-mono text-[10px] uppercase text-blue-400">1. Supporting Facts:</strong>
                <ul className="list-disc list-inside text-slate-300 mt-1 space-y-1">
                  {g.supportingFacts.map((sf, i) => (
                    <li key={i}>{sf}</li>
                  ))}
                </ul>
              </div>
              <div className="bg-legal-900/60 p-3 rounded-lg border border-legal-800/60">
                <strong className="text-slate-300 font-mono text-[10px] uppercase text-emerald-400">2. Evidentiary Linkage:</strong>
                <ul className="list-disc list-inside text-emerald-200/90 mt-1 space-y-1 font-mono text-[11px]">
                  {g.evidence.map((ev, i) => (
                    <li key={i}>{ev}</li>
                  ))}
                </ul>
              </div>
            </div>

            {/* Precedent & Statutory Integration */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 text-xs">
              <div className="bg-legal-900/60 p-3 rounded-lg border border-legal-800/60 font-mono text-[11px]">
                <strong className="text-purple-400 text-[10px] uppercase">3. Statutory Foundation:</strong>
                <p className="text-purple-200 mt-1">{g.statutoryBasis}</p>
              </div>
              <div className="bg-legal-900/60 p-3 rounded-lg border border-legal-800/60 font-mono text-[11px]">
                <strong className="text-amber-400 text-[10px] uppercase">4. Controlling Precedent:</strong>
                <p className="text-amber-200 mt-1">{g.precedent}</p>
              </div>
            </div>

            {/* Counterargument & Rebuttal */}
            <div className="mt-3 bg-gradient-to-r from-rose-950/40 via-legal-950 to-emerald-950/40 p-3.5 rounded-lg border border-legal-800 text-xs">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <strong className="text-rose-400 font-mono text-[10px] uppercase">Anticipated Revenue Attack:</strong>
                  <p className="text-rose-200/90 mt-1 leading-relaxed">{g.likelyRevenueCounterargument}</p>
                </div>
                <div>
                  <strong className="text-emerald-400 font-mono text-[10px] uppercase">Pre-Emptive Rebuttal:</strong>
                  <p className="text-emerald-200/90 mt-1 leading-relaxed">{g.response}</p>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

code_step7 = """'use client';

import React from 'react';
import { AdversarialRedTeamItem } from '@/types';
import { Swords, ShieldAlert, CheckCircle2, XCircle, AlertTriangle } from 'lucide-react';

interface Step7Props {
  redTeamItems: AdversarialRedTeamItem[];
}

export const Step7RedTeamBattleView: React.FC<Step7Props> = ({ redTeamItems }) => {
  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <Swords className="w-4 h-4 text-rose-400" />
          STEP 7: Adversarial Red-Team Stress Test (Revenue Opposing Counsel Simulation)
        </h3>
        <p className="text-xs text-slate-400">
          Independent aggressive critique acting as senior departmental counsel to probe weaknesses in facts, evidence, and statutory interpretations.
        </p>
      </div>

      <div className="grid grid-cols-1 gap-4">
        {redTeamItems.map((item) => (
          <div key={item.id} className="legal-glass rounded-xl p-5 border border-legal-800 shadow-xl">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-3 border-b border-legal-800">
              <div className="flex items-center gap-2">
                <span className="font-mono text-xs px-2.5 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800">
                  {item.category}
                </span>
                <span className="text-xs font-mono text-slate-400">
                  Attack Strength: <strong className="text-rose-400">{item.strengthOfOpposingArgument}/100</strong>
                </span>
              </div>
              <div className="flex items-center gap-2 font-mono text-xs">
                <span className="text-slate-400">Defense Survival:</span>
                <span className={`px-2 py-0.5 rounded font-bold border ${item.survivesAttack ? 'bg-emerald-950/80 text-emerald-300 border-emerald-500/50' : 'bg-rose-950/80 text-rose-300 border-rose-500/50'}`}>
                  {item.survivesAttack ? 'SURVIVES ATTACK' : 'VULNERABLE'}
                </span>
                <span className="text-[11px] px-2 py-0.5 rounded bg-legal-900 border border-legal-700 text-slate-300">
                  Risk: {item.residualRisk}
                </span>
              </div>
            </div>

            {/* Attack & Defense Split */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-3 text-xs">
              {/* Opposing Counsel Attack */}
              <div className="bg-rose-950/30 p-3.5 rounded-lg border border-rose-900/50">
                <div className="flex items-center gap-2 text-rose-400 font-mono text-[11px] font-bold uppercase mb-1">
                  <ShieldAlert className="w-4 h-4 text-rose-400" />
                  <span>Revenue Standing Counsel Attack:</span>
                </div>
                <p className="text-rose-100/90 leading-relaxed font-serif italic mt-1.5">
                  "{item.opposingArgument}"
                </p>
              </div>

              {/* Taxpayer Defense */}
              <div className="bg-emerald-950/30 p-3.5 rounded-lg border border-emerald-900/50">
                <div className="flex items-center gap-2 text-emerald-400 font-mono text-[11px] font-bold uppercase mb-1">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                  <span>Taxpayer Shield & Rebuttal:</span>
                </div>
                <p className="text-emerald-100/90 leading-relaxed font-serif mt-1.5">
                  {item.taxpayerResponse}
                </p>
                <div className="mt-2.5 pt-2 border-t border-emerald-900/40 text-[11px] font-mono text-emerald-300">
                  <strong>Supporting Evidence: </strong>{item.evidenceSupportingResponse}
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

code_step8 = """'use client';

import React from 'react';
import { EvidenceGapItem } from '@/types';
import { Search, AlertCircle, FilePlus2, CheckCircle2 } from 'lucide-react';

interface Step8Props {
  evidenceGaps: EvidenceGapItem[];
}

export const Step8EvidenceGapView: React.FC<Step8Props> = ({ evidenceGaps }) => {
  const getPriorityPill = (p: string) => {
    switch (p) {
      case 'CRITICAL':
        return 'bg-rose-950 text-rose-300 border-rose-500/60 font-bold';
      case 'HIGH':
        return 'bg-orange-950 text-orange-300 border-orange-500/60 font-semibold';
      case 'MEDIUM':
        return 'bg-amber-950 text-amber-300 border-amber-500/60';
      default:
        return 'bg-slate-900 text-slate-300 border-slate-700';
    }
  };

  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <Search className="w-4 h-4 text-amber-400" />
          STEP 8: Evidence Gap Analysis & Remediation Roadmap
        </h3>
        <p className="text-xs text-slate-400">
          Prioritization of missing or un-relied documents required to convert uncertain parameters into litigation-proof evidence.
        </p>
      </div>

      <div className="space-y-3">
        {evidenceGaps.map((gap) => (
          <div key={gap.id} className="legal-glass rounded-xl p-4 border border-legal-800 shadow-lg">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-2.5 border-b border-legal-800">
              <div className="flex items-center gap-2">
                <FilePlus2 className="w-4 h-4 text-amber-400 flex-shrink-0" />
                <h4 className="font-serif font-bold text-sm text-white">{gap.missingEvidence}</h4>
              </div>
              <div className="flex items-center gap-2 font-mono text-xs">
                <span className={`px-2.5 py-0.5 rounded border ${getPriorityPill(gap.priority)}`}>
                  {gap.priority} PRIORITY
                </span>
                <span className="text-[11px] px-2 py-0.5 rounded bg-legal-900 border border-legal-700 text-slate-300">
                  {gap.category}
                </span>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 text-xs">
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800/80">
                <strong className="text-slate-400 font-mono text-[10px] uppercase">Legal Relevance & Rationale:</strong>
                <p className="text-slate-300 mt-1 leading-relaxed">{gap.legalRelevance}</p>
                <p className="text-slate-400 mt-1 italic">{gap.whyItMatters}</p>
              </div>
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800/80">
                <strong className="text-emerald-400 font-mono text-[10px] uppercase">Remediation Action & Source:</strong>
                <p className="text-emerald-200 mt-1"><strong>Source:</strong> {gap.possibleSource}</p>
                <p className="text-slate-300 mt-1"><strong>Impact If Obtained:</strong> {gap.impactIfObtained}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

with open("src/components/steps/Step6SubmissionOptimizerView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step6)
with open("src/components/steps/Step7RedTeamBattleView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step7)
with open("src/components/steps/Step8EvidenceGapView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step8)

print("Wrote Step Views 6 to 8 successfully!")