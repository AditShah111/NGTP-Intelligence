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
      <header className="sticky top-0 z-40 bg-white/95 border-b border-beige-200/90 backdrop-blur-md px-6 py-3.5 shadow-sm">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          {/* Brand & Logo */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-amber-50 border border-amber-200/80 flex items-center justify-center shadow-sm">
              <Scale className="w-5 h-5 text-amber-700" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-lg font-serif font-bold text-slate-900 tracking-tight">
                  NGTP <span className="text-amber-800 font-sans font-semibold text-xs px-2 py-0.5 rounded-full bg-amber-100/80 border border-amber-200">LITIGATION ENGINE</span>
                </h1>
                <span className="flex items-center gap-1.5 text-[11px] font-mono text-emerald-800 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200 font-medium">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-600 animate-pulse"></span>
                  v1.0 Live
                </span>
              </div>
              <p className="text-xs text-slate-500 font-sans">GST Appellate Strategy, Section 16(2)(c) & Supreme Court Precedent Red-Team</p>
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
                className="bg-beige-50 text-slate-800 text-xs rounded-lg border border-beige-300 px-3 py-2 pr-8 focus:outline-none focus:border-amber-600 font-medium max-w-[220px] truncate shadow-sm"
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
              className={`flex items-center gap-1.5 text-xs px-3 py-2 rounded-lg border transition-all font-medium shadow-sm ${
                hasApiKey 
                  ? 'bg-purple-50 border-purple-200 text-purple-900 hover:bg-purple-100' 
                  : 'bg-white border-beige-300 text-slate-700 hover:bg-beige-50'
              }`}
              title="Configure Gemini 3.5 / 2.5 LLM API Key"
            >
              <Sparkles className={`w-3.5 h-3.5 ${hasApiKey ? 'text-purple-600' : 'text-slate-500'}`} />
              <span>{hasApiKey ? 'Gemini 3.5 Active' : 'Set Gemini 3.5 Key'}</span>
            </button>

            {/* New Assessment Button */}
            <button
              onClick={onOpenNewCaseModal}
              className="flex items-center gap-1.5 text-xs bg-amber-600 hover:bg-amber-700 text-white font-semibold px-3.5 py-2 rounded-lg transition-all shadow-sm"
            >
              <PlusCircle className="w-4 h-4" />
              <span>New Assessment</span>
            </button>

            {/* Case Files */}
            <button
              onClick={onOpenUploadModal}
              className="flex items-center gap-1.5 text-xs bg-white hover:bg-beige-50 text-slate-800 border border-beige-300 px-3 py-2 rounded-lg transition-all font-medium shadow-sm"
            >
              <FileText className="w-4 h-4 text-blue-600" />
              <span>Case Files</span>
            </button>

            {/* Export Dossier */}
            <button
              onClick={onOpenExportModal}
              className="flex items-center gap-1.5 text-xs bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-300 px-3 py-2 rounded-lg transition-all font-medium shadow-sm"
            >
              <Download className="w-4 h-4 text-amber-700" />
              <span>Export Dossier</span>
            </button>

            {/* Database Health Pill */}
            <div className="flex items-center gap-1.5 text-[11px] font-mono px-2.5 py-1.5 rounded-lg bg-beige-100 border border-beige-200 text-slate-700">
              <Database className={`w-3.5 h-3.5 ${isDbConnected ? 'text-emerald-600' : 'text-amber-600'}`} />
              <span>{isDbConnected ? 'Supabase' : 'Cache Store'}</span>
            </div>
          </div>
        </div>
      </header>

      {/* Gemini Key Config Modal */}
      {isKeyModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4">
          <div className="bg-white border border-beige-300 rounded-2xl w-full max-w-md shadow-2xl p-6 relative">
            <button
              onClick={() => setIsKeyModalOpen(false)}
              className="absolute top-5 right-5 text-slate-400 hover:text-slate-700"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="flex items-center gap-2 mb-4 pb-3 border-b border-beige-200">
              <div className="p-2 rounded-lg bg-purple-50 text-purple-700">
                <Sparkles className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-base font-serif font-bold text-slate-900">Google Gemini 3.5 API Key</h3>
                <p className="text-xs text-slate-500">Enables dynamic generative legal reasoning and Red-Team opposing attacks.</p>
              </div>
            </div>

            <form onSubmit={handleSaveKey} className="space-y-4 text-xs">
              <div>
                <label className="block text-slate-700 mb-1 font-semibold">Gemini API Key (Google AI Studio)</label>
                <input
                  type="password"
                  value={apiKeyInput}
                  onChange={(e) => setApiKeyInput(e.target.value)}
                  placeholder="AIzaSy..."
                  className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600 font-mono shadow-inner"
                />
                <p className="text-[11px] text-slate-500 mt-1">
                  Saved securely in your browser local session for direct Gemini API evaluation.
                </p>
              </div>

              <div className="flex justify-end gap-2 pt-2 border-t border-beige-200">
                <button
                  type="button"
                  onClick={() => {
                    localStorage.removeItem('ngtp_gemini_api_key');
                    setApiKeyInput('');
                    setHasApiKey(false);
                    setIsKeyModalOpen(false);
                  }}
                  className="px-3 py-1.5 rounded-lg bg-rose-50 text-rose-700 hover:bg-rose-100 font-medium transition-colors"
                >
                  Clear Key
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 rounded-lg bg-amber-600 hover:bg-amber-700 text-white font-semibold transition-colors shadow-sm"
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
