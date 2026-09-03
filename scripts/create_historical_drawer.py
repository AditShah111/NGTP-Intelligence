historical_drawer_code = """'use client';

import React from 'react';
import { CaseStudy } from '../types';
import { FolderOpen, X, Trash2, Calendar, FileText, ArrowRight, ShieldCheck, Scale } from 'lucide-react';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  cases: CaseStudy[];
  activeCaseId?: string;
  onSelectCase: (c: CaseStudy) => void;
  onClearHistory?: () => void;
}

export const HistoricalCasesDrawer: React.FC<Props> = ({
  isOpen,
  onClose,
  cases,
  activeCaseId,
  onSelectCase,
  onClearHistory
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/40 backdrop-blur-sm animate-fade-in">
      {/* Backdrop click */}
      <div className="absolute inset-0" onClick={onClose} />

      {/* Slide-over Drawer Panel */}
      <div className="relative w-full max-w-md bg-white h-full shadow-2xl flex flex-col border-l border-beige-300 z-10 animate-slide-in-right">
        {/* Header */}
        <div className="p-5 border-b border-beige-200 flex items-center justify-between bg-beige-50/80">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-amber-100 flex items-center justify-center">
              <FolderOpen className="w-4 h-4 text-amber-800" />
            </div>
            <div>
              <h3 className="font-serif font-bold text-base text-slate-900">Historical & Saved Matters</h3>
              <p className="text-xs text-slate-500 font-mono">{cases.length} records available</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 hover:bg-beige-100 transition-all"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Case List */}
        <div className="flex-grow overflow-y-auto p-4 space-y-3">
          {cases.length === 0 ? (
            <div className="text-center py-16 text-slate-400 text-xs">
              No historical matters stored. All data is clean.
            </div>
          ) : (
            cases.map((c) => {
              const isActive = c.id === activeCaseId;
              const readiness = c.readinessScore?.totalScore || 0;
              const recommendation = c.finalOutput?.executiveVerdict?.recommendation || 'NOT EVALUATED';

              return (
                <div
                  key={c.id}
                  onClick={() => {
                    onSelectCase(c);
                    onClose();
                  }}
                  className={`p-4 rounded-xl border transition-all cursor-pointer shadow-sm ${
                    isActive 
                      ? 'bg-amber-50/70 border-amber-400 ring-1 ring-amber-400' 
                      : 'bg-white border-beige-200 hover:border-amber-300 hover:bg-beige-50/50'
                  }`}
                >
                  <div className="flex items-start justify-between gap-2">
                    <div>
                      <h4 className="font-serif font-bold text-sm text-slate-900 leading-snug">
                        {c.taxpayerName}
                      </h4>
                      <div className="text-xs text-slate-500 font-mono mt-0.5">
                        {c.gstin} • FY {c.financialYear}
                      </div>
                    </div>
                    <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-700">
                      {c.disputedAmount}
                    </span>
                  </div>

                  <div className="mt-3 pt-2.5 border-t border-beige-100 flex items-center justify-between text-xs">
                    <span className={`font-mono text-[10px] font-bold px-2 py-0.5 rounded-full ${
                      recommendation === 'PROCEED' ? 'bg-emerald-50 text-emerald-800' :
                      recommendation === 'PROCEED AFTER RECTIFICATION' ? 'bg-amber-50 text-amber-800' :
                      'bg-rose-50 text-rose-800'
                    }`}>
                      {recommendation}
                    </span>

                    <span className="text-amber-700 font-semibold font-mono text-[11px] flex items-center gap-1">
                      Score: {readiness}/100 <ArrowRight className="w-3 h-3" />
                    </span>
                  </div>
                </div>
              );
            })
          )}
        </div>

        {/* Footer with Clear Cache option */}
        <div className="p-4 border-t border-beige-200 bg-beige-50/50 flex items-center justify-between">
          {onClearHistory && cases.length > 0 && (
            <button
              onClick={() => {
                if (confirm('Clear all historical matters and reset to clean state?')) {
                  onClearHistory();
                  onClose();
                }
              }}
              className="flex items-center gap-1.5 text-xs text-rose-700 hover:text-rose-900 font-medium transition-all"
            >
              <Trash2 className="w-3.5 h-3.5" />
              <span>Clear History & Cache</span>
            </button>
          )}

          <button
            onClick={onClose}
            className="ml-auto px-4 py-1.5 rounded-lg bg-slate-900 text-white text-xs font-semibold hover:bg-slate-800 transition-all"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};
"""

with open("src/components/HistoricalCasesDrawer.tsx", "w", encoding="utf-8") as f:
    f.write(historical_drawer_code)

print("Created src/components/HistoricalCasesDrawer.tsx!")