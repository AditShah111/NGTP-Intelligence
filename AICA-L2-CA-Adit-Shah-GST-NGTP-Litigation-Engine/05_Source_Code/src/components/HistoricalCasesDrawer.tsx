'use client';

import React, { useState } from 'react';
import { CaseStudy } from '../types';
import { 
  X, 
  FolderOpen, 
  Trash2, 
  Scale, 
  Calendar, 
  ArrowRight, 
  AlertTriangle,
  FileText,
  ShieldAlert,
  Loader2
} from 'lucide-react';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  cases: CaseStudy[];
  activeCaseId?: string;
  onSelectCase: (c: CaseStudy) => void;
  onClearHistory: () => void;
  onDeleteSingleCase?: (id: string) => void;
}

export const HistoricalCasesDrawer: React.FC<Props> = ({
  isOpen,
  onClose,
  cases,
  activeCaseId,
  onSelectCase,
  onClearHistory,
  onDeleteSingleCase
}) => {
  const [showClearConfirm, setShowClearConfirm] = useState(false);
  const [caseToDelete, setCaseToDelete] = useState<CaseStudy | null>(null);
  const [isDeleting, setIsDeleting] = useState(false);

  if (!isOpen) return null;

  const handleConfirmClearAll = async () => {
    setIsDeleting(true);
    try {
      await fetch('/api/cases', { method: 'DELETE' });
      localStorage.setItem('ngtp_history_cleared', 'true');
      onClearHistory();
      setShowClearConfirm(false);
    } catch (err) {
      console.error('Failed to clear cases:', err);
    } finally {
      setIsDeleting(false);
    }
  };

  const handleConfirmDeleteSingle = async () => {
    if (!caseToDelete) return;
    setIsDeleting(true);
    try {
      await fetch(`/api/cases?id=${caseToDelete.id}`, { method: 'DELETE' });
      if (onDeleteSingleCase) {
        onDeleteSingleCase(caseToDelete.id);
      }
      setCaseToDelete(null);
    } catch (err) {
      console.error('Failed to delete case:', err);
    } finally {
      setIsDeleting(false);
    }
  };

  return (
    <>
      <div className="fixed inset-0 z-50 overflow-hidden bg-black/40 backdrop-blur-sm transition-opacity">
        <div className="absolute inset-y-0 right-0 max-w-full flex pl-10">
          <div className="w-screen max-w-md bg-white border-l border-beige-200 shadow-2xl flex flex-col">
            {/* Header */}
            <div className="px-6 py-4 border-b border-beige-200 flex items-center justify-between bg-beige-50/50">
              <div className="flex items-center gap-2">
                <FolderOpen className="w-5 h-5 text-amber-700" />
                <h3 className="font-serif font-bold text-slate-900 text-base">
                  Historical Matters
                </h3>
                <span className="font-mono text-[11px] px-2 py-0.5 rounded-full bg-beige-200 text-slate-700 font-semibold">
                  {cases.length}
                </span>
              </div>
              <button
                onClick={onClose}
                className="text-slate-400 hover:text-slate-700 p-1 rounded-lg hover:bg-beige-100 transition-all"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Subheader / Info banner */}
            <div className="px-6 py-3 bg-amber-50/40 border-b border-amber-100/80 text-[11px] text-amber-900 leading-relaxed font-sans">
              All stored matters and benchmark evaluations are kept in your private database. Click any matter below to load it into the workspace.
            </div>

            {/* Body: Cases List */}
            <div className="flex-1 overflow-y-auto p-4 space-y-2.5">
              {cases.length === 0 ? (
                <div className="text-center py-16 px-4">
                  <Scale className="w-10 h-10 text-slate-300 mx-auto mb-2" />
                  <p className="text-sm font-semibold text-slate-700">No Historical Matters</p>
                  <p className="text-xs text-slate-500 mt-1">
                    Database and cache are clean. Start a new assessment from the main screen.
                  </p>
                </div>
              ) : (
                cases.map((c) => {
                  const isActive = c.id === activeCaseId;
                  const isProceed = c.finalOutput?.executiveVerdict?.recommendation === 'PROCEED';
                  const isRectify = c.finalOutput?.executiveVerdict?.recommendation === 'PROCEED AFTER RECTIFICATION';

                  return (
                    <div
                      key={c.id}
                      className={`group p-3.5 rounded-xl border text-left transition-all relative ${
                        isActive
                          ? 'border-amber-600 bg-amber-50/50 shadow-sm'
                          : 'border-beige-200 bg-white hover:border-amber-300 hover:bg-beige-50/40'
                      }`}
                    >
                      <div 
                        onClick={() => { onSelectCase(c); onClose(); }}
                        className="cursor-pointer"
                      >
                        <div className="flex items-start justify-between gap-2 mb-1.5">
                          <h4 className="font-serif font-bold text-xs text-slate-900 line-clamp-1 pr-6">
                            {c.title}
                          </h4>
                        </div>

                        <div className="text-[11px] text-slate-600 space-y-0.5">
                          <div>Entity: <strong className="text-slate-800">{c.taxpayerName}</strong></div>
                          <div className="font-mono text-[10px] text-slate-500 flex items-center gap-2">
                            <span>GSTIN: {c.gstin}</span>
                            <span>•</span>
                            <span>FY: {c.financialYear}</span>
                          </div>
                        </div>

                        <div className="flex items-center justify-between mt-2.5 pt-2 border-t border-beige-100 text-[10px] font-mono">
                          <span className={`px-2 py-0.5 rounded font-bold border ${
                            isProceed ? 'bg-emerald-50 text-emerald-800 border-emerald-200' :
                            isRectify ? 'bg-amber-50 text-amber-800 border-amber-200' :
                            'bg-rose-50 text-rose-800 border-rose-200'
                          }`}>
                            {c.finalOutput?.executiveVerdict?.recommendation || 'EVALUATED'}
                          </span>
                          <span className="text-slate-500">
                            Score: <strong className="text-slate-900">{c.readinessScore?.totalScore || 0}/100</strong>
                          </span>
                        </div>
                      </div>

                      {/* Individual Delete Button */}
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          setCaseToDelete(c);
                        }}
                        className="absolute top-3 right-3 text-slate-300 hover:text-rose-600 p-1 transition-all rounded hover:bg-rose-50"
                        title="Permanently delete this case"
                      >
                        <Trash2 className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  );
                })
              )}
            </div>

            {/* Footer / Clear History Button */}
            {cases.length > 0 && (
              <div className="p-4 border-t border-beige-200 bg-beige-50/50">
                <button
                  onClick={() => setShowClearConfirm(true)}
                  className="w-full flex items-center justify-center gap-2 py-2 px-3 rounded-xl border border-rose-200 text-rose-700 bg-rose-50/60 hover:bg-rose-100 hover:border-rose-300 text-xs font-semibold transition-all shadow-sm"
                >
                  <Trash2 className="w-3.5 h-3.5" />
                  <span>Clear All Historical Matters & Cache</span>
                </button>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* CONFIRMATION MODAL: CLEAR ALL HISTORY */}
      {showClearConfirm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 animate-fade-in">
          <div className="bg-white border border-beige-300 rounded-2xl w-full max-w-md shadow-2xl p-6 relative">
            <div className="flex items-center gap-3 text-rose-700 mb-3">
              <div className="w-10 h-10 rounded-xl bg-rose-100 flex items-center justify-center flex-shrink-0">
                <ShieldAlert className="w-5 h-5 text-rose-700" />
              </div>
              <h3 className="font-serif font-bold text-lg text-slate-900">
                Permanently Delete All Matters?
              </h3>
            </div>

            <p className="text-xs text-slate-600 mb-5 leading-relaxed font-sans">
              Are you sure you want to permanently clear all <strong className="text-slate-900">{cases.length} historical matters</strong> and database cache?
              <br /><br />
              <strong className="text-rose-800">This action is permanent and cannot be undone.</strong> On page refresh, the database will remain clean and will not reload any cached cases.
            </p>

            <div className="flex items-center justify-end gap-2.5 pt-2 border-t border-beige-200">
              <button
                type="button"
                disabled={isDeleting}
                onClick={() => setShowClearConfirm(false)}
                className="px-4 py-2 text-xs font-semibold rounded-xl border border-beige-300 text-slate-700 hover:bg-beige-50 transition-all"
              >
                Cancel
              </button>
              <button
                type="button"
                disabled={isDeleting}
                onClick={handleConfirmClearAll}
                className="px-5 py-2 text-xs font-bold rounded-xl bg-rose-600 hover:bg-rose-700 text-white shadow-md transition-all flex items-center gap-1.5"
              >
                {isDeleting ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Trash2 className="w-3.5 h-3.5" />}
                <span>{isDeleting ? 'Deleting Permanently...' : 'Yes, Permanently Delete All'}</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* CONFIRMATION MODAL: DELETE SINGLE CASE */}
      {caseToDelete && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 animate-fade-in">
          <div className="bg-white border border-beige-300 rounded-2xl w-full max-w-md shadow-2xl p-6 relative">
            <div className="flex items-center gap-3 text-rose-700 mb-3">
              <div className="w-9 h-9 rounded-xl bg-rose-100 flex items-center justify-center flex-shrink-0">
                <AlertTriangle className="w-5 h-5 text-rose-700" />
              </div>
              <h3 className="font-serif font-bold text-base text-slate-900">
                Delete Single Matter?
              </h3>
            </div>

            <p className="text-xs text-slate-600 mb-5 leading-relaxed font-sans">
              Are you sure you want to permanently delete:
              <br />
              <strong className="text-slate-900 font-serif block mt-1">{caseToDelete.title}</strong>
              <span className="text-slate-500 font-mono text-[11px]">Entity: {caseToDelete.taxpayerName} (GSTIN: {caseToDelete.gstin})</span>
            </p>

            <div className="flex items-center justify-end gap-2.5 pt-2 border-t border-beige-200">
              <button
                type="button"
                disabled={isDeleting}
                onClick={() => setCaseToDelete(null)}
                className="px-4 py-2 text-xs font-semibold rounded-xl border border-beige-300 text-slate-700 hover:bg-beige-50 transition-all"
              >
                Cancel
              </button>
              <button
                type="button"
                disabled={isDeleting}
                onClick={handleConfirmDeleteSingle}
                className="px-5 py-2 text-xs font-bold rounded-xl bg-rose-600 hover:bg-rose-700 text-white shadow-md transition-all flex items-center gap-1.5"
              >
                {isDeleting ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Trash2 className="w-3.5 h-3.5" />}
                <span>{isDeleting ? 'Deleting...' : 'Delete Matter'}</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};
