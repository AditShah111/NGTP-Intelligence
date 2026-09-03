header_clean_code = """'use client';

import React, { useState, useEffect } from 'react';
import { Scale, FileText, PlusCircle, RefreshCw, Download, Database, Key, Sparkles, FolderOpen, Plus } from 'lucide-react';
import { CaseStudy } from '../types';

interface HeaderProps {
  cases: CaseStudy[];
  activeCase: CaseStudy | null;
  onSelectCase: (c: CaseStudy) => void;
  onResetToCleanWorkspace: () => void;
  onOpenNewCaseModal: () => void;
  onOpenHistoricalDrawer: () => void;
  onOpenExportModal: () => void;
  isDbConnected: boolean;
}

export const Header: React.FC<HeaderProps> = ({
  cases,
  activeCase,
  onSelectCase,
  onResetToCleanWorkspace,
  onOpenNewCaseModal,
  onOpenHistoricalDrawer,
  onOpenExportModal,
  isDbConnected
}) => {
  const [isKeyModalOpen, setIsKeyModalOpen] = useState(false);
  const [apiKeyInput, setApiKeyInput] = useState('');
  const [hasApiKey, setHasApiKey] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem('ngtp_gemini_api_key');
    if (saved) {
      setHasApiKey(true);
      setApiKeyInput(saved);
    }
  }, []);

  const handleSaveKey = (e: React.FormEvent) => {
    e.preventDefault();
    if (apiKeyInput.trim()) {
      localStorage.setItem('ngtp_gemini_api_key', apiKeyInput.trim());
      setHasApiKey(true);
    } else {
      localStorage.removeItem('ngtp_gemini_api_key');
      setHasApiKey(false);
    }
    setIsKeyModalOpen(false);
  };

  return (
    <>
      <header className="sticky top-0 z-40 bg-white/95 border-b border-beige-200/90 backdrop-blur-md px-4 sm:px-6 py-3 shadow-sm">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
          {/* Brand & Logo */}
          <div className="flex items-center gap-3 w-full md:w-auto justify-between md:justify-start">
            <div 
              onClick={onResetToCleanWorkspace}
              className="flex items-center gap-2.5 cursor-pointer hover:opacity-90 transition-all"
              title="Return to clean assessment screen"
            >
              <div className="w-9 h-9 rounded-xl bg-amber-50 border border-amber-200/80 flex items-center justify-center shadow-sm">
                <Scale className="w-5 h-5 text-amber-700" />
              </div>
              <div>
                <h1 className="text-base font-serif font-bold text-slate-900 tracking-tight leading-tight">
                  NGTP <span className="text-amber-800 font-sans font-semibold text-[11px] px-2 py-0.5 rounded-full bg-amber-100/80 border border-amber-200">LITIGATION ENGINE</span>
                </h1>
                <p className="text-[11px] text-slate-500 font-sans">Automated Evidence Audit & Section 16(2)(c) Judicial Intelligence</p>
              </div>
            </div>

            {/* Mobile-only Historical Button */}
            <button
              onClick={onOpenHistoricalDrawer}
              className="md:hidden flex items-center gap-1.5 text-xs px-2.5 py-1.5 rounded-lg bg-beige-100 text-slate-700 border border-beige-300 font-medium"
            >
              <FolderOpen className="w-3.5 h-3.5" />
              <span>History ({cases.length})</span>
            </button>
          </div>

          {/* Controls */}
          <div className="flex flex-wrap items-center gap-2 w-full md:w-auto justify-end">
            {/* PROMINENT: NEW ASSESSMENT BUTTON */}
            <button
              onClick={onOpenNewCaseModal}
              className="flex items-center gap-1.5 text-xs px-3.5 py-2 rounded-xl bg-amber-600 hover:bg-amber-700 text-white font-bold transition-all shadow-sm"
              title="Start a new matter assessment"
            >
              <Plus className="w-4 h-4" />
              <span>+ New Assessment</span>
            </button>

            {/* Historical Matters Drawer Trigger */}
            <button
              onClick={onOpenHistoricalDrawer}
              className="flex items-center gap-1.5 text-xs bg-white hover:bg-beige-50 text-slate-700 border border-beige-300 px-3 py-2 rounded-xl transition-all font-medium shadow-sm"
              title="View past assessments and cached cases"
            >
              <FolderOpen className="w-3.5 h-3.5 text-amber-700" />
              <span>Past Cases ({cases.length})</span>
            </button>

            {/* Gemini API Key Toggle */}
            <button
              onClick={() => setIsKeyModalOpen(true)}
              className={`flex items-center gap-1.5 text-xs px-3 py-2 rounded-xl border transition-all font-medium shadow-sm ${
                hasApiKey 
                  ? 'bg-purple-50 border-purple-200 text-purple-900 hover:bg-purple-100' 
                  : 'bg-white border-beige-300 text-slate-700 hover:bg-beige-50'
              }`}
              title="Configure Gemini LLM API Key"
            >
              <Sparkles className={`w-3.5 h-3.5 ${hasApiKey ? 'text-purple-600' : 'text-slate-500'}`} />
              <span>{hasApiKey ? 'Gemini Active' : 'Set Gemini Key'}</span>
            </button>

            {/* Export Dossier (Visible when a case is active) */}
            {activeCase && (
              <button
                onClick={onOpenExportModal}
                className="flex items-center gap-1.5 text-xs bg-slate-900 hover:bg-slate-800 text-white font-semibold px-3 py-2 rounded-xl transition-all shadow-sm"
              >
                <Download className="w-3.5 h-3.5" />
                <span>Export Dossier</span>
              </button>
            )}

            {/* Database Health Status */}
            <div className="flex items-center gap-1 text-[11px] font-mono px-2.5 py-2 rounded-xl bg-beige-100/80 border border-beige-200 text-slate-600">
              <Database className={`w-3 h-3 ${isDbConnected ? 'text-emerald-600' : 'text-amber-600'}`} />
              <span>{isDbConnected ? 'Cloud DB' : 'Local'}</span>
            </div>
          </div>
        </div>
      </header>

      {/* Gemini Key Config Modal */}
      {isKeyModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4">
          <div className="bg-white border border-beige-300 rounded-2xl w-full max-w-md shadow-2xl p-6 relative">
            <h3 className="font-serif font-bold text-lg text-slate-900 mb-1">
              Google Gemini API Key
            </h3>
            <p className="text-xs text-slate-600 mb-4 font-sans">
              Enter your Gemini API Key to enable continuous real-time High Court precedent ingestion and adversarial Red-Team generation.
            </p>

            <form onSubmit={handleSaveKey} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1 font-mono">
                  Gemini API Key:
                </label>
                <input
                  type="password"
                  value={apiKeyInput}
                  onChange={(e) => setApiKeyInput(e.target.value)}
                  placeholder="AIzaSy..."
                  className="w-full bg-beige-50 border border-beige-300 rounded-lg p-2.5 text-xs font-mono text-slate-900 focus:outline-none focus:border-amber-600"
                />
              </div>

              <div className="flex items-center justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setIsKeyModalOpen(false)}
                  className="px-3.5 py-1.5 text-xs rounded-lg border border-beige-300 text-slate-600 hover:bg-beige-50"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-1.5 text-xs font-semibold rounded-lg bg-amber-600 text-white hover:bg-amber-700 shadow-sm"
                >
                  Save API Key
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  );
};
"""

with open("src/components/Header.tsx", "w", encoding="utf-8") as f:
    f.write(header_clean_code)

print("Updated Header.tsx with prominent '+ New Assessment' button!")