'use client';

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
