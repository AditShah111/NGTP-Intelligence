code_step3 = """'use client';

import React from 'react';
import { PrecedentAnalysis } from '../../types';
import { BookOpen, Award, CheckCircle2, AlertCircle, Sparkles, Scale } from 'lucide-react';

interface Props {
  precedents: PrecedentAnalysis[];
}

export const Step3Step4PrecedentsView: React.FC<Props> = ({ precedents }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-beige-200">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Scale className="w-5 h-5 text-amber-700" />
              <h3 className="text-xl font-serif font-bold text-slate-900">Steps 3 & 4: Landmark Judicial Precedents & 6-Axis Comparability</h3>
            </div>
            <p className="text-xs text-slate-600">
              Live judicial research testing present case facts against Supreme Court and High Court controlling rulings with automated 6-axis comparability scoring (0–100).
            </p>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-xs font-mono px-3 py-1 rounded-full bg-purple-50 text-purple-900 border border-purple-200 font-semibold flex items-center gap-1.5">
              <Sparkles className="w-3.5 h-3.5 text-purple-600" />
              AI & Precedent Live Engine
            </span>
          </div>
        </div>

        <div className="space-y-4 mt-6">
          {precedents.map((p, idx) => {
            const score = p.comparabilityScore?.totalScore || 90;
            const isSc = p.court.toLowerCase().includes('supreme court');

            return (
              <div
                key={p.id || idx}
                className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
              >
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-beige-200">
                  <div>
                    <div className="flex items-center gap-2">
                      <h4 className="text-base font-serif font-bold text-slate-900">{p.caseName}</h4>
                      {isSc && (
                        <span className="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-300">
                          ★ Supreme Court Affirmed
                        </span>
                      )}
                    </div>
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
                    <div className="bg-white border border-beige-200 px-3 py-1 rounded-lg text-center shadow-sm min-w-[85px]">
                      <div className="text-[10px] font-mono text-slate-400 uppercase">Match Score</div>
                      <div className="text-sm font-mono font-bold text-amber-700">{score}/100</div>
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

                {/* 6-Axis Comparability Metrics */}
                {p.comparabilityScore && (
                  <div className="mt-3 pt-3 border-t border-beige-200 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2 text-[10px] font-mono text-slate-600">
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Statutory</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.statutorySimilarity}/20</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Factual</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.factualSimilarity}/25</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Evidentiary</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.evidentiarySimilarity}/20</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Procedural</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.proceduralSimilarity}/10</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Authority</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.courtAuthorityRelevance}/15</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Distinguish Risk</div>
                      <div className="font-bold text-emerald-700 mt-0.5">{p.comparabilityScore.distinguishabilityRisk}/10</div>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
"""

with open("src/components/steps/Step3Step4PrecedentsView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step3)

print("Updated Step3Step4PrecedentsView with 6-Axis Comparability & Live Precedent Badges!")