import os

code_header = """'use client';

import React from 'react';
import { Scale, ShieldAlert, FileText, PlusCircle, RefreshCw, Download, Database, CheckCircle2 } from 'lucide-react';
import { CaseStudy } from '@/types';

interface HeaderProps {
  cases: CaseStudy[];
  activeCase: CaseStudy | null;
  onSelectCase: (c: CaseStudy) => void;
  onOpenNewCaseModal: () => void;
  onOpenUploadModal: () => void;
  onOpenExportModal: () => void;
  isDbConnected: boolean;
}

export const Header: React.FC<HeaderProps> = ({
  cases,
  activeCase,
  onSelectCase,
  onOpenNewCaseModal,
  onOpenUploadModal,
  onOpenExportModal,
  isDbConnected
}) => {
  return (
    <header className="sticky top-0 z-40 bg-[#0c1322]/95 border-b border-legal-800/80 backdrop-blur-md px-6 py-3.5">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
        {/* Brand & Logo */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-amber-500/20 via-legal-600/30 to-blue-600/20 border border-amber-500/40 flex items-center justify-center shadow-lg shadow-amber-500/5">
            <Scale className="w-5 h-5 text-amber-400" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-lg font-serif font-bold text-white tracking-wide">
                NGTP <span className="text-amber-400 font-sans font-medium text-xs px-2 py-0.5 rounded bg-amber-500/10 border border-amber-500/30">LITIGATION ENGINE</span>
              </h1>
              <span className="flex items-center gap-1 text-[11px] font-mono text-emerald-400 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                v1.0 Ready
              </span>
            </div>
            <p className="text-xs text-slate-400">GST Appellate Strategy, Section 16(2)(c) & Judicial Precedent Engine</p>
          </div>
        </div>

        {/* Case Switcher & Action Controls */}
        <div className="flex flex-wrap items-center gap-2.5">
          {/* Active Case Selector */}
          <div className="relative">
            <select
              value={activeCase?.id || ''}
              onChange={(e) => {
                const found = cases.find(c => c.id === e.target.value);
                if (found) onSelectCase(found);
              }}
              className="bg-legal-900 text-slate-200 text-xs rounded-lg border border-legal-700 px-3 py-2 pr-8 focus:outline-none focus:border-amber-400 font-medium max-w-[240px] truncate"
            >
              {cases.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.taxpayerName} ({c.financialYear})
                </option>
              ))}
            </select>
          </div>

          {/* New Case Button */}
          <button
            onClick={onOpenNewCaseModal}
            className="flex items-center gap-1.5 text-xs bg-amber-500 hover:bg-amber-400 text-black font-semibold px-3 py-2 rounded-lg transition-all shadow-md shadow-amber-500/10"
          >
            <PlusCircle className="w-4 h-4" />
            <span>New Assessment</span>
          </button>

          {/* Upload Documents Button */}
          <button
            onClick={onOpenUploadModal}
            className="flex items-center gap-1.5 text-xs bg-legal-800 hover:bg-legal-700 text-slate-200 border border-legal-600 px-3 py-2 rounded-lg transition-all"
          >
            <FileText className="w-4 h-4 text-blue-400" />
            <span>Case Files</span>
          </button>

          {/* Export Legal Dossier */}
          <button
            onClick={onOpenExportModal}
            className="flex items-center gap-1.5 text-xs bg-gradient-to-r from-legal-800 to-legal-700 hover:from-legal-700 hover:to-legal-600 text-amber-300 border border-amber-500/40 px-3 py-2 rounded-lg transition-all"
          >
            <Download className="w-4 h-4 text-amber-400" />
            <span>Export Dossier</span>
          </button>

          {/* Database Health Pill */}
          <div className="flex items-center gap-1.5 text-[11px] font-mono px-2.5 py-1.5 rounded-lg bg-legal-950 border border-legal-800 text-slate-400">
            <Database className={`w-3.5 h-3.5 ${isDbConnected ? 'text-emerald-400' : 'text-amber-400'}`} />
            <span>{isDbConnected ? 'Supabase' : 'Isolated Cache'}</span>
          </div>
        </div>
      </div>
    </header>
  );
};
"""

code_overview = """'use client';

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
"""

code_nav = """'use client';

import React from 'react';
import { 
  Table, 
  Scale, 
  BookOpen, 
  AlertOctagon, 
  FileEdit, 
  Swords, 
  Search, 
  Gauge, 
  Navigation, 
  CheckSquare, 
  Gavel
} from 'lucide-react';

interface StepProgressNavProps {
  activeStep: number;
  onSelectStep: (step: number) => void;
}

export const StepProgressNav: React.FC<StepProgressNavProps> = ({
  activeStep,
  onSelectStep
}) => {
  const steps = [
    { num: 1, label: 'Fact Matrix', icon: Table },
    { num: 2, label: 'Statutory Engine', icon: Scale },
    { num: 3, label: 'Precedents & Score', icon: BookOpen },
    { num: 5, label: 'Lower Authority Errors', icon: AlertOctagon },
    { num: 6, label: 'Submission Optimizer', icon: FileEdit },
    { num: 7, label: 'Red-Team Adversary', icon: Swords },
    { num: 8, label: 'Evidence Gaps', icon: Search },
    { num: 9, label: 'Readiness & Viability', icon: Gauge },
    { num: 11, label: 'Forward Decision', icon: Navigation },
    { num: 12, label: 'Draft Audit', icon: CheckSquare },
    { num: 13, label: 'Final Evaluator Verdict', icon: Gavel },
  ];

  return (
    <div className="flex items-center gap-1.5 overflow-x-auto pb-3 mb-5 border-b border-legal-800/60 scrollbar-thin">
      {steps.map((s) => {
        const Icon = s.icon;
        const isActive = activeStep === s.num;
        return (
          <button
            key={s.num}
            onClick={() => onSelectStep(s.num)}
            className={`flex items-center gap-2 px-3 py-2 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
              isActive
                ? 'bg-amber-500 text-black font-semibold shadow-md shadow-amber-500/20'
                : 'bg-legal-900/80 hover:bg-legal-800 text-slate-300 border border-legal-800/80 hover:border-legal-700'
            }`}
          >
            <Icon className={`w-3.5 h-3.5 ${isActive ? 'text-black' : 'text-amber-400'}`} />
            <span>Step {s.num}: {s.label}</span>
          </button>
        );
      })}
    </div>
  );
};
"""

with open("src/components/Header.tsx", "w", encoding="utf-8") as f:
    f.write(code_header)
with open("src/components/CaseOverviewCard.tsx", "w", encoding="utf-8") as f:
    f.write(code_overview)
with open("src/components/StepProgressNav.tsx", "w", encoding="utf-8") as f:
    f.write(code_nav)

print("Wrote Header, OverviewCard, and StepProgressNav")