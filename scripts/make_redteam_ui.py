import os

code_redteam_ui = """'use client';

import React, { useState } from 'react';
import { AdversarialRedTeamItem } from '@/types';
import { Swords, ShieldAlert, CheckCircle2, XCircle, AlertTriangle, Play, Shield, Flame, RotateCcw } from 'lucide-react';

interface Step7Props {
  redTeamItems: AdversarialRedTeamItem[];
}

export const Step7RedTeamBattleView: React.FC<Step7Props> = ({ redTeamItems }) => {
  const [selectedAttackId, setSelectedAttackId] = useState<string>(redTeamItems[0]?.id || '');
  const [activeSimulationFilter, setActiveSimulationFilter] = useState<'ALL' | 'VULNERABLE' | 'SURVIVES'>('ALL');

  const filteredItems = redTeamItems.filter(item => {
    if (activeSimulationFilter === 'VULNERABLE') return !item.survivesAttack;
    if (activeSimulationFilter === 'SURVIVES') return item.survivesAttack;
    return true;
  });

  const selectedItem = redTeamItems.find(i => i.id === selectedAttackId) || redTeamItems[0];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-2">
        <div>
          <h3 className="text-lg font-serif font-bold text-white flex items-center gap-2">
            <Swords className="w-5 h-5 text-rose-400" />
            STEP 7: Adversarial Red-Team War Room (Opposing Standing Counsel Attack Simulation)
          </h3>
          <p className="text-xs text-slate-400">
            Independent aggressive stress-testing simulating Senior Revenue Departmental Representatives to pressure-test factual assertions, statutory interpretations, and burden of proof.
          </p>
        </div>

        {/* Filter Pills */}
        <div className="flex items-center gap-1.5 bg-legal-950 p-1 rounded-lg border border-legal-800 text-xs font-mono">
          {(['ALL', 'SURVIVES', 'VULNERABLE'] as const).map(filter => (
            <button
              key={filter}
              onClick={() => setActiveSimulationFilter(filter)}
              className={`px-2.5 py-1 rounded-md transition-all ${
                activeSimulationFilter === filter 
                  ? 'bg-amber-500 text-black font-bold' 
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              {filter}
            </button>
          ))}
        </div>
      </div>

      {/* Featured Arena Card for Active Attack */}
      {selectedItem && (
        <div className="legal-glass rounded-2xl p-6 border-2 border-rose-500/40 shadow-2xl relative overflow-hidden bg-gradient-to-b from-rose-950/20 via-legal-950/80 to-emerald-950/20">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-4 border-b border-legal-800">
            <div className="flex items-center gap-2.5">
              <span className="p-2 rounded-lg bg-rose-500/20 border border-rose-500/40 text-rose-400">
                <Flame className="w-5 h-5" />
              </span>
              <div>
                <span className="text-[10px] font-mono uppercase text-rose-400 tracking-wider font-bold">ACTIVE SIMULATION FOCUS</span>
                <h4 className="text-base font-serif font-bold text-white">{selectedItem.category}</h4>
              </div>
            </div>
            <div className="flex items-center gap-3 font-mono text-xs">
              <div className="bg-rose-950/80 px-3 py-1 rounded-lg border border-rose-800 text-rose-300">
                Attack Force: <strong>{selectedItem.strengthOfOpposingArgument}/100</strong>
              </div>
              <div className={`px-3 py-1 rounded-lg border font-bold ${selectedItem.survivesAttack ? 'bg-emerald-950/90 text-emerald-300 border-emerald-600' : 'bg-rose-950/90 text-rose-300 border-rose-600'}`}>
                {selectedItem.survivesAttack ? 'DEFENSE HOLDS (PASSED)' : 'RISK OF COLLAPSE'}
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-4">
            {/* Left: Revenue Attack */}
            <div className="bg-rose-950/40 p-5 rounded-xl border border-rose-900/60 flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-2 text-rose-400 font-mono text-xs font-bold uppercase mb-2">
                  <ShieldAlert className="w-4 h-4 text-rose-400" />
                  <span>Revenue Standing Counsel Attack Vector</span>
                </div>
                <p className="text-sm text-rose-100 font-serif leading-relaxed italic">
                  "{selectedItem.opposingArgument}"
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-rose-900/50 text-xs text-slate-400">
                <strong className="text-rose-400">Tactical Revenue Aim:</strong> Shift burden to taxpayer & trigger non-obstante Section 16(2) denial.
              </div>
            </div>

            {/* Right: Taxpayer Shield */}
            <div className="bg-emerald-950/40 p-5 rounded-xl border border-emerald-900/60 flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-2 text-emerald-400 font-mono text-xs font-bold uppercase mb-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                  <span>Taxpayer Appellate Counter-Shield</span>
                </div>
                <p className="text-xs text-emerald-100 font-serif leading-relaxed">
                  {selectedItem.taxpayerResponse}
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-emerald-900/50 text-xs font-mono text-emerald-300 bg-emerald-950/60 p-2.5 rounded">
                <strong>Evidentiary Backing: </strong>{selectedItem.evidenceSupportingResponse}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Grid of All Red-Team Attack Vectors */}
      <div className="space-y-3">
        <div className="text-xs font-mono uppercase text-slate-400 font-bold">All Opposing Attack Vectors ({filteredItems.length}):</div>
        <div className="grid grid-cols-1 gap-3">
          {filteredItems.map((item) => (
            <div 
              key={item.id}
              onClick={() => setSelectedAttackId(item.id)}
              className={`legal-glass rounded-xl p-4 border transition-all cursor-pointer ${
                selectedAttackId === item.id 
                  ? 'border-amber-500 bg-legal-900/90 shadow-xl shadow-amber-500/5' 
                  : 'border-legal-800 hover:border-legal-700'
              }`}
            >
              <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-2 border-b border-legal-800">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs font-bold text-amber-400">{item.category}</span>
                </div>
                <div className="flex items-center gap-2 font-mono text-xs">
                  <span className="text-rose-400 font-semibold">Attack: {item.strengthOfOpposingArgument}/100</span>
                  <span className={`px-2 py-0.5 rounded text-[11px] font-bold border ${item.survivesAttack ? 'bg-emerald-950 text-emerald-300 border-emerald-700' : 'bg-rose-950 text-rose-300 border-rose-700'}`}>
                    {item.survivesAttack ? 'SURVIVES' : 'FAIL'}
                  </span>
                  <span className="text-slate-400 text-[10px]">Residual Risk: {item.residualRisk}</span>
                </div>
              </div>
              <p className="text-xs text-slate-300 mt-2 line-clamp-2 italic font-serif">
                "{item.opposingArgument}"
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
"""

with open("src/components/steps/Step7RedTeamBattleView.tsx", "w", encoding="utf-8") as f:
    f.write(code_redteam_ui)

print("Updated Step7RedTeamBattleView with live war-room interactivity!")