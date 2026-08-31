'use client';

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
