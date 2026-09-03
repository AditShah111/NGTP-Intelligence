'use client';

import React from 'react';
import { Building2, FileCode, IndianRupee, AlertCircle, Calendar, ShieldCheck, FileSpreadsheet, Paperclip } from 'lucide-react';
import { CaseStudy } from '../types';

interface CaseOverviewCardProps {
  activeCase: CaseStudy;
}

export const CaseOverviewCard: React.FC<CaseOverviewCardProps> = ({ activeCase }) => {
  return (
    <div className="bg-white border border-beige-200/90 rounded-2xl p-6 mb-6 shadow-sm">
      <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 pb-6 border-b border-beige-200">
        <div>
          <div className="flex items-center gap-2 mb-1.5">
            <span className="font-mono text-[11px] font-semibold uppercase px-2.5 py-0.5 rounded-full bg-amber-50 text-amber-900 border border-amber-200">
              {activeCase.noticeType}
            </span>
            <span className="text-xs text-slate-500 font-mono">FY {activeCase.financialYear}</span>
            <span className="text-xs text-slate-400">•</span>
            <span className="text-xs text-slate-600 font-mono font-medium flex items-center gap-1">
              <Paperclip className="w-3 h-3 text-slate-400" />
              {activeCase.documents?.length || 0} Files Attached
            </span>
          </div>
          <h2 className="text-2xl font-serif font-bold text-slate-900 tracking-tight">{activeCase.title}</h2>
          <p className="text-xs text-slate-600 mt-1 max-w-3xl leading-relaxed">{activeCase.summary}</p>
        </div>

        {/* Dual Quick Score Pills */}
        <div className="flex items-center gap-3">
          <div className="bg-beige-50 border border-beige-300 rounded-xl p-3.5 text-center min-w-[130px] shadow-sm">
            <div className="text-[11px] font-mono uppercase text-slate-500 font-semibold tracking-wide">Readiness</div>
            <div className={`text-2xl font-bold font-mono mt-0.5 ${
              activeCase.readinessScore.totalScore >= 80 ? 'text-emerald-700' :
              activeCase.readinessScore.totalScore >= 50 ? 'text-amber-700' : 'text-rose-700'
            }`}>
              {activeCase.readinessScore.totalScore}<span className="text-xs text-slate-400">/100</span>
            </div>
          </div>

          <div className="bg-beige-50 border border-beige-300 rounded-xl p-3.5 text-center min-w-[130px] shadow-sm">
            <div className="text-[11px] font-mono uppercase text-slate-500 font-semibold tracking-wide">Viability</div>
            <div className={`text-2xl font-bold font-mono mt-0.5 ${
              activeCase.viabilityScore.totalScore >= 80 ? 'text-emerald-700' :
              activeCase.viabilityScore.totalScore >= 50 ? 'text-amber-700' : 'text-rose-700'
            }`}>
              {activeCase.viabilityScore.totalScore}<span className="text-xs text-slate-400">/100</span>
            </div>
          </div>
        </div>
      </div>

      {/* Metadata Row */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 pt-4 text-xs">
        <div className="flex items-center gap-2.5">
          <div className="p-2 rounded-lg bg-beige-100 text-slate-700">
            <Building2 className="w-4 h-4 text-amber-700" />
          </div>
          <div>
            <div className="text-[11px] text-slate-400 uppercase font-mono">Taxpayer</div>
            <div className="font-semibold text-slate-800 truncate max-w-[180px]">{activeCase.taxpayerName}</div>
          </div>
        </div>

        <div className="flex items-center gap-2.5">
          <div className="p-2 rounded-lg bg-beige-100 text-slate-700">
            <FileCode className="w-4 h-4 text-blue-700" />
          </div>
          <div>
            <div className="text-[11px] text-slate-400 uppercase font-mono">GSTIN</div>
            <div className="font-mono font-semibold text-slate-800">{activeCase.gstin}</div>
          </div>
        </div>

        <div className="flex items-center gap-2.5">
          <div className="p-2 rounded-lg bg-beige-100 text-slate-700">
            <IndianRupee className="w-4 h-4 text-emerald-700" />
          </div>
          <div>
            <div className="text-[11px] text-slate-400 uppercase font-mono">Disputed ITC / Tax</div>
            <div className="font-semibold text-slate-800">{activeCase.disputedAmount}</div>
          </div>
        </div>

        <div className="flex items-center gap-2.5">
          <div className="p-2 rounded-lg bg-beige-100 text-slate-700">
            <AlertCircle className="w-4 h-4 text-amber-700" />
          </div>
          <div>
            <div className="text-[11px] text-slate-400 uppercase font-mono">Primary Issue</div>
            <div className="font-semibold text-slate-800 truncate max-w-[200px]" title={activeCase.primaryIssue}>
              {activeCase.primaryIssue}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
