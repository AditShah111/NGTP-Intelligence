'use client';

import React from 'react';
import { PrecedentAnalysis } from '@/types';
import { BookOpen, Award, CheckCircle2, ShieldCheck, Scale } from 'lucide-react';

interface Step3Props {
  precedents: PrecedentAnalysis[];
}

export const Step3Step4PrecedentsView: React.FC<Step3Props> = ({ precedents }) => {
  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <BookOpen className="w-4 h-4 text-amber-400" />
          STEPS 3 & 4: Precedent Parameter Engine & Comparability Scoring (0–100)
        </h3>
        <p className="text-xs text-slate-400">
          Rigorous analysis of controlling judgments (Suncraft, D.Y. Beathel, Arise India, LGW Industries) with objective comparability scoring.
        </p>
      </div>

      <div className="space-y-4">
        {precedents.map((p) => {
          const comp = p.comparabilityScore;
          return (
            <div key={p.id} className="legal-glass rounded-xl p-5 border border-legal-800 shadow-xl">
              <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-3 pb-3 border-b border-legal-800">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="font-serif font-bold text-base text-amber-300">{p.caseName}</span>
                  </div>
                  <div className="text-xs font-mono text-slate-400 flex flex-wrap items-center gap-3">
                    <span className="text-blue-400 font-semibold">{p.court}</span>
                    <span>•</span>
                    <span className="text-slate-300">{p.citation}</span>
                    <span>•</span>
                    <span className="text-purple-400">{p.relevantProvision}</span>
                  </div>
                </div>

                {/* Comparability Score Card */}
                <div className="bg-legal-900/90 border border-amber-500/40 rounded-xl p-3 text-center min-w-[140px] shadow-lg">
                  <div className="text-[10px] font-mono uppercase tracking-wider text-amber-400/90 font-bold">Comparability</div>
                  <div className="text-2xl font-mono font-extrabold text-amber-300">
                    {comp.totalScore}<span className="text-xs text-slate-500">/100</span>
                  </div>
                  <div className="text-[10px] font-mono text-emerald-400 font-semibold mt-0.5">
                    {p.favourableApplicability === 'HIGH' ? 'Directly Controlling' : 'Persuasive'}
                  </div>
                </div>
              </div>

              {/* Ratio Decidendi & Legal Principle */}
              <div className="mt-3 bg-legal-950/70 p-3.5 rounded-lg border border-legal-800">
                <div className="text-[11px] font-mono text-amber-400 uppercase tracking-wider font-bold mb-1">
                  Ratio Decidendi / Legal Principle:
                </div>
                <p className="text-xs text-slate-200 leading-relaxed font-serif italic">
                  "{p.ratioLegalPrinciple}"
                </p>
              </div>

              {/* Conditions & Operational Deployment */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-3 text-xs">
                <div className="bg-legal-900/50 p-3 rounded-lg border border-legal-800/60">
                  <strong className="text-slate-300 font-mono text-[11px]">Necessary Conditions for Application:</strong>
                  <ul className="list-disc list-inside text-slate-300 mt-1.5 space-y-1">
                    {p.necessaryConditions.map((nc, idx) => (
                      <li key={idx} className="leading-tight">{nc}</li>
                    ))}
                  </ul>
                </div>
                <div className="bg-legal-900/50 p-3 rounded-lg border border-legal-800/60">
                  <strong className="text-slate-300 font-mono text-[11px]">Tactical Appellate Deployment:</strong>
                  <p className="text-slate-300 mt-1.5 leading-relaxed">{p.litigationUse}</p>
                </div>
              </div>

              {/* Comparability Dimension Breakdown */}
              <div className="mt-3 pt-3 border-t border-legal-800/80">
                <div className="text-[10px] font-mono text-slate-400 uppercase mb-2">Comparability Score Breakdown:</div>
                <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2 text-center text-xs font-mono">
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Statutory</div>
                    <div className="text-amber-400 font-bold">{comp.statutorySimilarity}/20</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Factual</div>
                    <div className="text-amber-400 font-bold">{comp.factualSimilarity}/25</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Evidentiary</div>
                    <div className="text-amber-400 font-bold">{comp.evidentiarySimilarity}/20</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Procedural</div>
                    <div className="text-amber-400 font-bold">{comp.proceduralSimilarity}/10</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Forum Binding</div>
                    <div className="text-amber-400 font-bold">{comp.courtAuthorityRelevance}/15</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Distinction Risk</div>
                    <div className="text-emerald-400 font-bold">{comp.distinguishabilityRisk}/10</div>
                  </div>
                </div>
                <p className="text-[11px] text-slate-400 mt-2 italic">
                  <strong className="text-slate-300">Scoring Note:</strong> {comp.explanation}
                </p>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
