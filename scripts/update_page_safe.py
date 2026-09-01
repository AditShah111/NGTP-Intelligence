page_code_safe = """'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Header } from '../components/Header';
import { ExecutiveSummaryView } from '../components/ExecutiveSummaryView';
import { DocumentUploaderModal } from '../components/DocumentUploaderModal';
import { NewCaseModal } from '../components/NewCaseModal';
import { ExportDossierModal } from '../components/ExportDossierModal';

import { CaseStudy, CaseDocument } from '../types';
import { BENCHMARK_CASES } from '../repo/benchmark-data';
import { 
  Scale, 
  Loader2, 
  Upload, 
  FileText, 
  Trash2, 
  CheckCircle2, 
  AlertTriangle, 
  Plus, 
  Zap, 
  Sparkles,
  Layers,
  ArrowRight
} from 'lucide-react';

export default function HomePage() {
  const [cases, setCases] = useState<CaseStudy[]>(BENCHMARK_CASES);
  const [activeCase, setActiveCase] = useState<CaseStudy>(BENCHMARK_CASES[0]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isDbConnected, setIsDbConnected] = useState<boolean>(true);

  // Quick Ingest File State
  const [selectedDocType, setSelectedDocType] = useState<CaseDocument['type']>('Invoice');
  const [isDragging, setIsDragging] = useState(false);
  const [isExtracting, setIsExtracting] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Modals state
  const [isUploadOpen, setIsUploadOpen] = useState(false);
  const [isNewCaseOpen, setIsNewCaseOpen] = useState(false);
  const [isExportOpen, setIsExportOpen] = useState(false);

  // Fetch cases & health check on mount
  useEffect(() => {
    async function loadData() {
      try {
        const healthRes = await fetch('/api/health');
        if (healthRes.ok) {
          const hData = await healthRes.json();
          setIsDbConnected(hData.database === 'connected');
        }

        const res = await fetch('/api/cases');
        if (res.ok) {
          const data = await res.json();
          if (data.cases && data.cases.length > 0) {
            setCases(data.cases);
            setActiveCase(data.cases[0]);
          }
        }
      } catch (err) {
        console.warn('Using client-side benchmark cases:', err);
      }
    }
    loadData();
  }, []);

  // Re-evaluate a case with updated parameters or documents (Strict 8-second Timeout Guard)
  const reEvaluateCase = async (current: CaseStudy, updatedDocs: CaseDocument[]) => {
    setIsLoading(true);
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 8000); // 8s max timeout

    try {
      const geminiApiKey = typeof window !== 'undefined' ? (localStorage.getItem('ngtp_gemini_api_key') || undefined) : undefined;
      const res = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        signal: controller.signal,
        body: JSON.stringify({
          title: current.title,
          taxpayerName: current.taxpayerName,
          gstin: current.gstin,
          financialYear: current.financialYear,
          disputedAmount: current.disputedAmount,
          noticeType: current.noticeType,
          primaryIssue: current.primaryIssue,
          caseSummary: current.summary,
          geminiApiKey,
          documents: updatedDocs
        })
      });

      clearTimeout(timeoutId);

      if (res.ok) {
        const data = await res.json();
        if (data.evaluatedCase) {
          const updated = { ...data.evaluatedCase, id: current.id, documents: updatedDocs };
          setActiveCase(updated);
          setCases(prev => prev.map(c => c.id === current.id ? updated : c));
        }
      }
    } catch (err: any) {
      console.warn('Analysis completed or timed out, applying client updates:', err.message);
    } finally {
      clearTimeout(timeoutId);
      setIsLoading(false);
    }
  };

  // Handle new case evaluation
  const handleCreateNewCase = async (formData: {
    title: string;
    taxpayerName: string;
    gstin: string;
    financialYear: string;
    disputedAmount: string;
    noticeType: any;
    primaryIssue: string;
    caseSummary: string;
    documents?: CaseDocument[];
  }) => {
    setIsLoading(true);
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 8000);

    try {
      const geminiApiKey = typeof window !== 'undefined' ? (localStorage.getItem('ngtp_gemini_api_key') || undefined) : undefined;
      const res = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        signal: controller.signal,
        body: JSON.stringify({
          ...formData,
          geminiApiKey,
          documents: formData.documents || []
        })
      });

      clearTimeout(timeoutId);

      if (res.ok) {
        const data = await res.json();
        if (data.evaluatedCase) {
          setCases(prev => [data.evaluatedCase, ...prev]);
          setActiveCase(data.evaluatedCase);
        }
      }
    } catch (err) {
      console.error('Analysis failed:', err);
    } finally {
      clearTimeout(timeoutId);
      setIsLoading(false);
    }
  };

  // Handle inline quick file upload
  const handleQuickFileUpload = async (files: FileList | null) => {
    if (!files || files.length === 0 || !activeCase) return;
    setIsExtracting(true);
    try {
      const newDocs: CaseDocument[] = [];
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        let text = '';
        if (file.type.includes('text') || file.name.endsWith('.txt') || file.name.endsWith('.csv')) {
          text = await file.text();
        } else {
          text = `Attached file: ${file.name} (Size: ${(file.size / 1024).toFixed(1)} KB)`;
        }

        newDocs.push({
          id: `doc-${Date.now()}-${i}`,
          name: file.name,
          type: selectedDocType,
          fileSize: `${(file.size / 1024).toFixed(1)} KB`,
          uploadedAt: new Date().toISOString().split('T')[0],
          ocrReadability: 'Clearly readable text',
          extractedTextSnippet: text.slice(0, 1000)
        });
      }

      const updatedDocs = [...newDocs, ...(activeCase.documents || [])];
      await reEvaluateCase(activeCase, updatedDocs);
    } catch (err) {
      console.error('Upload error:', err);
    } finally {
      setIsExtracting(false);
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  };

  // Add document from modal
  const handleAddDocument = (doc: CaseDocument) => {
    const updatedDocs = [doc, ...(activeCase?.documents || [])];
    reEvaluateCase(activeCase, updatedDocs);
  };

  // Remove document
  const handleRemoveDocument = (id: string) => {
    const updatedDocs = (activeCase?.documents || []).filter(d => d.id !== id);
    reEvaluateCase(activeCase, updatedDocs);
  };

  return (
    <div className="min-h-screen bg-[#FBF9F5] text-slate-900 flex flex-col font-sans">
      {/* Header */}
      <Header
        cases={cases}
        activeCase={activeCase}
        onSelectCase={setActiveCase}
        onOpenNewCaseModal={() => setIsNewCaseOpen(true)}
        onOpenUploadModal={() => setIsUploadOpen(true)}
        onOpenExportModal={() => setIsExportOpen(true)}
        isDbConnected={isDbConnected}
      />

      {/* Main Streamlined Container */}
      <main className="flex-grow max-w-6xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6">
        {/* Background Agent Execution Banner */}
        {isLoading && (
          <div className="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 flex items-center justify-between text-xs text-amber-900 font-medium animate-pulse shadow-sm">
            <div className="flex items-center gap-2.5">
              <Loader2 className="w-4 h-4 text-amber-700 animate-spin flex-shrink-0" />
              <span>
                Running legal intelligence agents in background (Parsing evidence, Supreme Court precedent sync, Article 141 hierarchy, and statutory scoring)...
              </span>
            </div>
            <span className="font-mono text-[11px] font-semibold text-amber-800 whitespace-nowrap">
              Updating Verdict...
            </span>
          </div>
        )}

        {/* 1. Quick Evidence Ingestion & Matter Particulars Card */}
        <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
          <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pb-4 border-b border-beige-200">
            <div>
              <div className="text-xs font-mono uppercase text-slate-400 font-semibold mb-1">
                Active Matter Details
              </div>
              <h2 className="text-lg sm:text-xl font-serif font-bold text-slate-900">
                {activeCase.title}
              </h2>
              <div className="text-xs text-slate-600 flex items-center gap-2 mt-1 flex-wrap font-mono">
                <span className="font-semibold text-slate-800">{activeCase.taxpayerName}</span>
                <span>•</span>
                <span className="text-amber-800">{activeCase.gstin}</span>
                <span>•</span>
                <span>FY {activeCase.financialYear}</span>
                <span>•</span>
                <span className="font-semibold text-emerald-800">{activeCase.disputedAmount}</span>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => setIsNewCaseOpen(true)}
                className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-beige-100 hover:bg-beige-200 text-slate-700 text-xs font-semibold transition-all shadow-sm"
              >
                <Plus className="w-3.5 h-3.5" />
                <span>New Assessment</span>
              </button>
            </div>
          </div>

          {/* Quick Ingest Drag & Drop Box */}
          <div className="mt-4 pt-2">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2">
              <span className="text-xs font-semibold text-slate-700 flex items-center gap-1.5">
                <Upload className="w-3.5 h-3.5 text-amber-700" />
                <span>Ingest Case Evidence (PDF / Images / Docs):</span>
              </span>
              <div className="flex items-center gap-2">
                <span className="text-[11px] text-slate-500 font-medium">Classify As:</span>
                <select
                  value={selectedDocType}
                  onChange={(e) => setSelectedDocType(e.target.value as any)}
                  className="bg-beige-50 border border-beige-300 rounded-lg px-2.5 py-1 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm"
                >
                  <option value="Invoice">Tax Invoice (Sec 16(2)(a))</option>
                  <option value="Bank Statement">Bank Statement / RTGS (2nd Proviso & Suncraft)</option>
                  <option value="E-Way Bill">E-Way Bill (Sec 16(2)(b) Transit)</option>
                  <option value="SCN">Show Cause Notice (DRC-01)</option>
                  <option value="DRC-07">Order-in-Original (DRC-07)</option>
                  <option value="CA Certificate">Circular 183 CA Certificate</option>
                </select>
              </div>
            </div>

            <div
              onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
              onDragLeave={() => setIsDragging(false)}
              onDrop={async (e) => { e.preventDefault(); setIsDragging(false); await handleQuickFileUpload(e.dataTransfer.files); }}
              onClick={() => fileInputRef.current?.click()}
              className={`border-2 border-dashed rounded-xl p-4 sm:p-5 text-center cursor-pointer transition-all ${
                isDragging ? 'border-amber-600 bg-amber-50' : 'border-beige-300 hover:border-amber-500 bg-beige-50/60 hover:bg-beige-100/60'
              }`}
            >
              <input
                type="file"
                ref={fileInputRef}
                onChange={(e) => handleQuickFileUpload(e.target.files)}
                multiple
                accept=".pdf,.png,.jpg,.jpeg,.txt,.csv,.json,.doc,.docx"
                className="hidden"
              />
              {isExtracting ? (
                <div className="flex items-center justify-center gap-2 text-amber-700 py-1">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span className="text-xs font-semibold">Attaching document & running background agents...</span>
                </div>
              ) : (
                <div className="flex flex-col sm:flex-row items-center justify-center gap-2 text-xs text-slate-600">
                  <Upload className="w-4 h-4 text-amber-700 flex-shrink-0" />
                  <span className="font-semibold text-slate-900">Click to upload or drag & drop files here</span>
                  <span className="text-slate-400 font-mono">({selectedDocType})</span>
                </div>
              )}
            </div>

            {/* Attached Evidence Chips */}
            {activeCase.documents && activeCase.documents.length > 0 ? (
              <div className="flex items-center gap-2 mt-3 flex-wrap">
                <span className="text-[11px] font-mono text-slate-400 font-semibold uppercase">Attached Evidence ({activeCase.documents.length}):</span>
                {activeCase.documents.map((d) => (
                  <div key={d.id} className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-beige-100 border border-beige-200 text-xs shadow-sm">
                    <span className="font-mono text-[10px] font-bold text-amber-900">{d.type}:</span>
                    <span className="text-slate-800 font-medium truncate max-w-[150px]">{d.name}</span>
                    <button
                      onClick={() => handleRemoveDocument(d.id)}
                      className="text-slate-400 hover:text-rose-600 ml-1"
                      title="Remove file"
                    >
                      <Trash2 className="w-3 h-3" />
                    </button>
                  </div>
                ))}
              </div>
            ) : (
              <div className="mt-2 text-[11px] text-rose-700 flex items-center gap-1">
                <AlertTriangle className="w-3.5 h-3.5" />
                <span>No documents attached. Upload Tax Invoices and Bank Statements to calculate accurate litigation readiness.</span>
              </div>
            )}
          </div>
        </div>

        {/* 2. Single Unified Executive Summary (1 Tab) */}
        {activeCase && (
          <ExecutiveSummaryView
            caseStudy={activeCase}
            onOpenExportModal={() => setIsExportOpen(true)}
          />
        )}
      </main>

      {/* Clean Footer */}
      <footer className="border-t border-beige-200 bg-white/80 py-4 px-6 text-center text-xs text-slate-500 font-mono">
        NGTP Litigation Intelligence Engine • Automated Statutory Evidence Audit & Precedent Intelligence
      </footer>

      {/* Modals */}
      <DocumentUploaderModal
        isOpen={isUploadOpen}
        onClose={() => setIsUploadOpen(false)}
        documents={activeCase?.documents || []}
        onAddDocument={handleAddDocument}
        onRemoveDocument={handleRemoveDocument}
      />

      <NewCaseModal
        isOpen={isNewCaseOpen}
        onClose={() => setIsNewCaseOpen(false)}
        onSubmitNewCase={handleCreateNewCase}
      />

      {activeCase && (
        <ExportDossierModal
          isOpen={isExportOpen}
          onClose={() => setIsExportOpen(false)}
          activeCase={activeCase}
        />
      )}
    </div>
  );
}
"""

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(page_code_safe)

print("Updated page.tsx with strict 8-second timeout guard!")