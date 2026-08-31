'use client';

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
