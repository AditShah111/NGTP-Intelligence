summary_view_code = """'use client';

import React from 'react';
import { CaseStudy } from '../types';
import { 
  ShieldCheck, 
  AlertTriangle, 
  XCircle, 
  CheckCircle2, 
  Gavel, 
  Scale, 
  Award, 
  Swords, 
  FileText, 
  ListChecks, 
  Download,
  AlertCircle
} from 'lucide-react';

interface Props {
  caseStudy: CaseStudy;
  onOpenExportModal: () => void;
}

export const ExecutiveSummaryView: React.FC<Props> = ({ caseStudy, onOpenExportModal }) => {
  const { 
    finalOutput, 
    statutoryParameters, 
    redTeamItems, 
    readinessScore, 
    viabilityScore,
    precedents,
    documents 
  } = caseStudy;

  const isProceed = finalOutput.executiveVerdict.recommendation === 'PROCEED';
  const isRectify = finalOutput.executiveVerdict.recommendation === 'PROCEED AFTER RECTIFICATION';

  return (
    <div className="space-y-6 animate-fade-in">
      {/* 1. Core Verdict & Decision Banner */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 pb-6 border-b border-beige-200">
          <div>
            <div className="text-xs font-mono uppercase text-slate-400 font-semibold tracking-wider mb-1">
              Executive Litigation Verdict
            </div>
            <div className="flex items-center gap-3">
              <span className={`text-xl sm:text-2xl font-serif font-bold px-4 py-1.5 rounded-xl border shadow-sm ${
                isProceed ? 'bg-emerald-50 text-emerald-900 border-emerald-300' :
                isRectify ? 'bg-amber-50 text-amber-900 border-amber-300' :
                'bg-rose-50 text-rose-900 border-rose-300'
              }`}>
                {finalOutput.executiveVerdict.recommendation}
              </span>
              <span className="text-xs font-mono font-semibold px-3 py-1 rounded-lg bg-beige-100 text-slate-700 border border-beige-300">
                Probability: {viabilityScore.probabilityOfFavourableOutcome}
              </span>
            </div>
          </div>

          <div className="flex items-center gap-4">
            <div className="text-center p-3 sm:p-4 rounded-xl bg-beige-50 border border-beige-200 min-w-[120px]">
              <div className="text-[11px] font-mono text-slate-500 uppercase">Readiness Score</div>
              <div className="text-2xl sm:text-3xl font-mono font-bold text-slate-900 mt-0.5">
                {readinessScore.totalScore}<span className="text-sm text-slate-400">/100</span>
              </div>
            </div>
            <div className="text-center p-3 sm:p-4 rounded-xl bg-beige-50 border border-beige-200 min-w-[120px]">
              <div className="text-[11px] font-mono text-slate-500 uppercase">Viability Score</div>
              <div className="text-2xl sm:text-3xl font-mono font-bold text-amber-700 mt-0.5">
                {viabilityScore.totalScore}<span className="text-sm text-slate-400">/100</span>
              </div>
            </div>
          </div>
        </div>

        {/* Core Decision Reasons */}
        <div className="mt-6">
          <div className="text-xs font-mono uppercase text-slate-400 font-semibold mb-3">
            Core Decision Drivers & Legal Rationale:
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {finalOutput.executiveVerdict.top5Reasons.map((reason, idx) => (
              <div key={idx} className="flex items-start gap-2.5 p-3 rounded-xl bg-beige-50/70 border border-beige-200 text-xs text-slate-800">
                <CheckCircle2 className="w-4 h-4 text-emerald-700 flex-shrink-0 mt-0.5" />
                <span className="leading-relaxed">{reason}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Advantage & Risk Highlights */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4 pt-4 border-t border-beige-200 text-xs">
          <div className="p-3.5 rounded-xl bg-emerald-50/60 border border-emerald-200">
            <div className="font-mono text-[11px] uppercase font-bold text-emerald-900 mb-1 flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-700" />
              Single Strongest Advantage:
            </div>
            <p className="text-slate-800 font-medium leading-relaxed">
              {finalOutput.finalLitigationAssessment.singleStrongestAdvantage}
            </p>
          </div>
          <div className="p-3.5 rounded-xl bg-rose-50/60 border border-rose-200">
            <div className="font-mono text-[11px] uppercase font-bold text-rose-900 mb-1 flex items-center gap-1.5">
              <AlertTriangle className="w-4 h-4 text-rose-700" />
              Single Biggest Risk:
            </div>
            <p className="text-slate-800 font-medium leading-relaxed">
              {finalOutput.finalLitigationAssessment.singleBiggestRisk}
            </p>
          </div>
        </div>
      </div>

      {/* 2. Summary of Statutory & Evidentiary Parameters Checked (P1 to P8) */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200 mb-4">
          <div className="flex items-center gap-2">
            <Scale className="w-5 h-5 text-amber-700" />
            <h3 className="text-lg font-serif font-bold text-slate-900">
              Statutory & Evidentiary Parameters Checked (P1–P8)
            </h3>
          </div>
          <span className="text-xs font-mono text-slate-500">
            {statutoryParameters.filter(p => p.assessment === 'SATISFIED').length} of {statutoryParameters.length} Satisfied
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
          {statutoryParameters.map((p) => {
            const isSatisfied = p.assessment === 'SATISFIED';
            const isCritical = p.risk === 'CRITICAL' || p.risk === 'HIGH';

            return (
              <div
                key={p.id}
                className="bg-beige-50/60 border border-beige-200 rounded-xl p-4 flex flex-col justify-between hover:border-amber-300 transition-all shadow-sm"
              >
                <div>
                  <div className="flex items-center justify-between gap-2 mb-2">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-200">
                        {p.parameterCode}
                      </span>
                      <span className="font-serif font-bold text-xs text-slate-900">{p.title}</span>
                    </div>
                    <span className={`text-[10px] font-semibold px-2 py-0.5 rounded-full border ${
                      isSatisfied ? 'bg-emerald-50 text-emerald-800 border-emerald-200' :
                      p.assessment === 'PARTIALLY SATISFIED' ? 'bg-amber-50 text-amber-800 border-amber-200' :
                      'bg-rose-50 text-rose-800 border-rose-200'
                    }`}>
                      {p.assessment}
                    </span>
                  </div>

                  <p className="text-[11px] text-slate-600 leading-relaxed mb-2 font-sans">
                    {p.reason}
                  </p>
                </div>

                <div className="pt-2 border-t border-beige-200/80 flex items-center justify-between text-[10px] font-mono">
                  <span className="text-slate-500 truncate max-w-[200px]" title={p.courtEvidentiaryPrecedent}>
                    Anchor: <strong className="text-slate-800">{p.courtEvidentiaryPrecedent || 'Statutory Act'}</strong>
                  </span>
                  <span className={isCritical ? 'text-rose-700 font-bold' : 'text-emerald-700 font-semibold'}>
                    Risk: {p.risk}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* 3. Department Counter-Party Response (Adversarial Standing Counsel Arguments) */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200 mb-4">
          <div className="flex items-center gap-2">
            <Swords className="w-5 h-5 text-rose-700" />
            <h3 className="text-lg font-serif font-bold text-slate-900">
              Department Standing Counsel Response & Counter-Defense
            </h3>
          </div>
          <span className="text-xs font-mono text-purple-800 bg-purple-50 px-2.5 py-1 rounded-full border border-purple-200">
            Adversarial War-Room Audit
          </span>
        </div>

        <div className="space-y-3.5">
          {redTeamItems.map((item) => (
            <div key={item.id} className="p-4 rounded-xl bg-beige-50/60 border border-beige-200 space-y-2.5">
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono uppercase font-bold text-rose-800 flex items-center gap-1.5">
                  <AlertCircle className="w-3.5 h-3.5 text-rose-600" />
                  {item.category} (Attack Strength: {item.strengthOfOpposingArgument}%)
                </span>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200 font-bold">
                  {item.survivesAttack ? '✓ Defense Survives' : '⚠️ Defense Vulnerable'}
                </span>
              </div>

              <div className="text-xs text-slate-800 bg-white p-3 rounded-lg border border-beige-200 leading-relaxed font-sans">
                <strong className="text-rose-900 font-semibold block mb-1">Department Revenue Argument:</strong>
                {item.opposingArgument}
              </div>

              <div className="text-xs text-slate-800 bg-emerald-50/40 p-3 rounded-lg border border-emerald-200 leading-relaxed font-sans">
                <strong className="text-emerald-900 font-semibold block mb-1">Our Prepared Taxpayer Response:</strong>
                {item.taxpayerResponse}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 4. Action Plan & Export Brief */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="text-base font-serif font-bold text-slate-900">
            Comprehensive Litigation Dossier Ready
          </div>
          <p className="text-xs text-slate-600 mt-0.5">
            Export the complete structured legal brief with Article 141 citations, IRAC grounds, and evidentiary matrices.
          </p>
        </div>
        <button
          onClick={onOpenExportModal}
          className="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-semibold text-xs shadow-md transition-all whitespace-nowrap"
        >
          <Download className="w-4 h-4" />
          <span>Export Appeal Brief / Dossier</span>
        </button>
      </div>
    </div>
  );
};
"""

with open("src/components/ExecutiveSummaryView.tsx", "w", encoding="utf-8") as f:
    f.write(summary_view_code)

print("Created src/components/ExecutiveSummaryView.tsx!")