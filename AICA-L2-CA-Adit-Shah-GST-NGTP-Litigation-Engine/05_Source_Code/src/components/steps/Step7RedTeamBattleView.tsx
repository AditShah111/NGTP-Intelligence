'use client';

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
