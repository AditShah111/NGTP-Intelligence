'use client';

import React from 'react';
import { Building2, Calendar, FileSpreadsheet, ShieldAlert, Award, TrendingUp, AlertTriangle } from 'lucide-react';
import { CaseStudy } from '@/types';

interface CaseOverviewCardProps {
  activeCase: CaseStudy;
}

export const CaseOverviewCard: React.FC<CaseOverviewCardProps> = ({ activeCase }) => {
  const readiness = activeCase.readinessScore.totalScore;
  const viability = activeCase.viabilityScore.totalScore;

  const getBadgeColor = (rec: string) => {
    if (rec.includes('PROCEED') && !rec.includes('NOT')) return 'bg-emerald-950/80 text-emerald-300 border-emerald-500/40';
    if (rec.includes('HOLD') || rec.includes('RECTIFICATION')) return 'bg-amber-950/80 text-amber-300 border-amber-500/40';
    return 'bg-rose-950/80 text-rose-300 border-rose-500/40';
  };

  return (
    <div className="legal-glass rounded-xl p-5 border border-legal-700/60 shadow-xl mb-6">
      <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-4 pb-4 border-b border-legal-800/80">
        <div>
          <div className="flex flex-wrap items-center gap-2.5 mb-1.5">
            <span className="px-2.5 py-0.5 rounded text-xs font-mono font-medium bg-blue-950/80 text-blue-300 border border-blue-800/50">
              {activeCase.noticeType}
            </span>
            <span className="px-2.5 py-0.5 rounded text-xs font-mono font-medium bg-purple-950/80 text-purple-300 border border-purple-800/50">
              FY {activeCase.financialYear}
            </span>
            <span className={`px-2.5 py-0.5 rounded text-xs font-bold font-mono border ${getBadgeColor(activeCase.finalOutput.executiveVerdict.recommendation)}`}>
              VERDICT: {activeCase.finalOutput.executiveVerdict.recommendation}
            </span>
          </div>
          <h2 className="text-xl font-serif font-bold text-white tracking-wide">
            {activeCase.title}
          </h2>
          <p className="text-xs text-slate-400 mt-1 max-w-3xl">
            <strong className="text-slate-300">Taxpayer:</strong> {activeCase.taxpayerName} | <strong className="text-slate-300">GSTIN:</strong> {activeCase.gstin} | <strong className="text-slate-300">Disputed Tax:</strong> <span className="text-amber-400 font-mono font-semibold">{activeCase.disputedAmount}</span>
          </p>
        </div>

        {/* Dual Score Highlights */}
        <div className="flex items-center gap-3">
          <div className="bg-legal-900/90 border border-emerald-500/30 rounded-lg p-3 text-center min-w-[120px]">
            <div className="text-[10px] font-mono uppercase tracking-wider text-slate-400">Readiness</div>
            <div className="text-2xl font-mono font-extrabold text-emerald-400">{readiness}<span className="text-xs text-slate-500">/100</span></div>
            <div className="text-[10px] text-emerald-500/90 font-medium">{readiness >= 85 ? 'Litigation Ready' : 'Rectify First'}</div>
          </div>
          <div className="bg-legal-900/90 border border-blue-500/30 rounded-lg p-3 text-center min-w-[120px]">
            <div className="text-[10px] font-mono uppercase tracking-wider text-slate-400">Viability</div>
            <div className="text-2xl font-mono font-extrabold text-blue-400">{viability}<span className="text-xs text-slate-500">/100</span></div>
            <div className="text-[10px] text-blue-400/90 font-medium">Outcome: {activeCase.viabilityScore.probabilityOfFavourableOutcome}</div>
          </div>
        </div>
      </div>

      {/* Summary Box */}
      <div className="mt-3 text-xs text-slate-300 leading-relaxed bg-legal-950/60 p-3 rounded-lg border border-legal-800/50 flex items-start gap-2.5">
        <ShieldAlert className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
        <div>
          <strong className="text-amber-300">Case Gist:</strong> {activeCase.summary}
        </div>
      </div>
    </div>
  );
};
