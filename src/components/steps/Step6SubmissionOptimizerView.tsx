'use client';

import React from 'react';
import { ImprovedSubmissionGround } from '../../types';
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
