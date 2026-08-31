'use client';

import React, { useState, useEffect } from 'react';
import { Scale, ShieldAlert, FileText, PlusCircle, RefreshCw, Download, Database, Key, Sparkles, Check, X } from 'lucide-react';
import { CaseStudy } from '../types';

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
      <header className="sticky top-0 z-40 bg-[#0c1322]/95 border-b border-legal-800/80 backdrop-blur-md px-6 py-3.5">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          {/* Brand & Logo */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-amber-500/20 via-blue-600/30 to-purple-600/20 border border-amber-500/40 flex items-center justify-center shadow-lg shadow-amber-500/5">
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
              <p className="text-xs text-slate-400">GST Appellate Strategy, Section 16(2)(c) & Precedent Red-Team</p>
            </div>
          </div>

          {/* Controls */}
          <div className="flex flex-wrap items-center gap-2.5">
            {/* Case Selector */}
            <div className="relative">
              <select
                value={activeCase?.id || ''}
                onChange={(e) => {
                  const found = cases.find(c => c.id === e.target.value);
                  if (found) onSelectCase(found);
                }}
                className="bg-legal-900 text-slate-200 text-xs rounded-lg border border-legal-700 px-3 py-2 pr-8 focus:outline-none focus:border-amber-400 font-medium max-w-[220px] truncate"
              >
                {cases.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.taxpayerName} ({c.financialYear})
                  </option>
                ))}
              </select>
            </div>

            {/* Gemini API Key Toggle */}
            <button
              onClick={() => setIsKeyModalOpen(true)}
              className={`flex items-center gap-1.5 text-xs px-3 py-2 rounded-lg border transition-all ${
                hasApiKey 
                  ? 'bg-purple-950/70 border-purple-500/50 text-purple-300' 
                  : 'bg-legal-900 border-legal-700 text-slate-400 hover:text-slate-200'
              }`}
              title="Configure Gemini 3.5 / 2.5 LLM API Key"
            >
              <Sparkles className={`w-3.5 h-3.5 ${hasApiKey ? 'text-purple-400' : 'text-slate-400'}`} />
              <span>{hasApiKey ? 'Gemini 3.5 Active' : 'Set Gemini 3.5 Key'}</span>
            </button>

            {/* New Assessment Button */}
            <button
              onClick={onOpenNewCaseModal}
              className="flex items-center gap-1.5 text-xs bg-amber-500 hover:bg-amber-400 text-black font-semibold px-3 py-2 rounded-lg transition-all shadow-md shadow-amber-500/10"
            >
              <PlusCircle className="w-4 h-4" />
              <span>New Assessment</span>
            </button>

            {/* Case Files */}
            <button
              onClick={onOpenUploadModal}
              className="flex items-center gap-1.5 text-xs bg-legal-800 hover:bg-legal-700 text-slate-200 border border-legal-600 px-3 py-2 rounded-lg transition-all"
            >
              <FileText className="w-4 h-4 text-blue-400" />
              <span>Case Files</span>
            </button>

            {/* Export Dossier */}
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

      {/* Gemini Key Config Modal */}
      {isKeyModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4">
          <div className="bg-[#0c1322] border border-purple-500/50 rounded-2xl w-full max-w-md shadow-2xl p-6 relative">
            <button
              onClick={() => setIsKeyModalOpen(false)}
              className="absolute top-5 right-5 text-slate-400 hover:text-white"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="flex items-center gap-2 mb-4 pb-3 border-b border-legal-800">
              <Sparkles className="w-5 h-5 text-purple-400" />
              <div>
                <h3 className="text-base font-serif font-bold text-white">Google Gemini API Key</h3>
                <p className="text-xs text-slate-400">Enables dynamic generative reasoning, Red-Team opposing attacks, and deep pleading audits.</p>
              </div>
            </div>

            <form onSubmit={handleSaveKey} className="space-y-4 text-xs">
              <div>
                <label className="block text-slate-300 mb-1 font-medium">Gemini API Key (AI Studio)</label>
                <input
                  type="password"
                  value={apiKeyInput}
                  onChange={(e) => setApiKeyInput(e.target.value)}
                  placeholder="AIzaSy..."
                  className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-purple-400 font-mono"
                />
                <p className="text-[11px] text-slate-500 mt-1">
                  Stored securely in your browser session for direct API calls to Gemini 1.5 Pro / Flash.
                </p>
              </div>

              <div className="flex justify-end gap-2 pt-2 border-t border-legal-800">
                <button
                  type="button"
                  onClick={() => {
                    localStorage.removeItem('ngtp_gemini_api_key');
                    setApiKeyInput('');
                    setHasApiKey(false);
                    setIsKeyModalOpen(false);
                  }}
                  className="px-3 py-1.5 rounded-lg bg-legal-900 text-rose-400 hover:bg-rose-950 transition-colors"
                >
                  Clear Key
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 rounded-lg bg-purple-600 hover:bg-purple-500 text-white font-semibold transition-colors"
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
