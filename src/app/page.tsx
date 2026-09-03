'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Header } from '../components/Header';
import { ExecutiveSummaryView } from '../components/ExecutiveSummaryView';
import { HistoricalCasesDrawer } from '../components/HistoricalCasesDrawer';
import { NewCaseModal } from '../components/NewCaseModal';
import { ExportDossierModal } from '../components/ExportDossierModal';

import { CaseStudy, CaseDocument } from '../types';
import { BENCHMARK_CASES } from '../repo/benchmark-data';
import { validateNGTPScope, NGTPGatekeeperResult } from '../service/ngtp-gatekeeper';
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
  ArrowRight,
  FolderOpen,
  X,
  PlusCircle,
  FileEdit,
  FolderArchive,
  BookOpen
} from 'lucide-react';

export default function HomePage() {
  const [cases, setCases] = useState<CaseStudy[]>([]);
  const [activeCase, setActiveCase] = useState<CaseStudy | null>(null);
  const [scopeRejection, setScopeRejection] = useState<NGTPGatekeeperResult | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isDbConnected, setIsDbConnected] = useState<boolean>(true);

  // Ingestion Mode: 'submission' (Written Text) vs 'evidence' (Document Files)
  const [ingestTab, setIngestTab] = useState<'submission' | 'evidence'>('submission');

  // Clean Workspace Form State
  const [title, setTitle] = useState('');
  const [taxpayerName, setTaxpayerName] = useState('');
  const [gstin, setGstin] = useState('');
  const [financialYear, setFinancialYear] = useState('2018-19');
  const [disputedAmount, setDisputedAmount] = useState('');
  const [noticeType, setNoticeType] = useState<'SCN / DRC-01' | 'Order-in-Original / DRC-07' | 'First Appeal / APL-01' | 'High Court Writ Petition'>('Order-in-Original / DRC-07');
  const [primaryIssue, setPrimaryIssue] = useState('Section 16(2)(c) recovery from buyer without pursuing defaulting supplier');

  // Dedicated Written Submission State
  const [writtenSubmission, setWrittenSubmission] = useState('');
  const [submissionCategory, setSubmissionCategory] = useState<'Reply to SCN / DRC-01' | 'Statement of Facts & Grounds of Appeal' | 'Personal Hearing Written Submissions' | 'High Court Writ Petition Submissions' | 'General Written Legal Arguments'>('Reply to SCN / DRC-01');

  // Uploaded Documentary Evidence
  const [uploadedDocuments, setUploadedDocuments] = useState<CaseDocument[]>([]);
  const [selectedDocType, setSelectedDocType] = useState<CaseDocument['type']>('Invoice');
  const [isDragging, setIsDragging] = useState(false);
  const [isExtracting, setIsExtracting] = useState(false);
  const [isParsingDoc, setIsParsingDoc] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const submissionFileInputRef = useRef<HTMLInputElement>(null);

  // Drawers & Modals
  const [isNewCaseOpen, setIsNewCaseOpen] = useState(false);
  const [isHistoryDrawerOpen, setIsHistoryDrawerOpen] = useState(false);
  const [isExportOpen, setIsExportOpen] = useState(false);
  // Auto-scroll to top when activeCase verdict is evaluated
  useEffect(() => {
    if (activeCase) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }, [activeCase]);

  // Fetch past cases & health check on mount
  useEffect(() => {
    async function loadData() {
      try {
        const healthRes = await fetch('/api/health');
        if (healthRes.ok) {
          const hData = await healthRes.json();
          setIsDbConnected(hData.database === 'connected');
        }

        const isCleared = typeof window !== 'undefined' && localStorage.getItem('ngtp_history_cleared') === 'true';

        const res = await fetch('/api/cases');
        if (res.ok) {
          const data = await res.json();
          if (data.cases && data.cases.length > 0) {
            setCases(data.cases);
          } else {
            setCases([]);
          }
        } else {
          setCases([]);
        }
      } catch (err) {
        console.warn('Cases load:', err);
        setCases([]);
      }
    }
    loadData();
  }, []);

  // Reset to 100% clean pristine workspace
  const handleResetWorkspace = () => {
    setActiveCase(null);
    setScopeRejection(null);
    setTitle('');
    setTaxpayerName('');
    setGstin('');
    setFinancialYear('2018-19');
    setDisputedAmount('');
    setNoticeType('Order-in-Original / DRC-07');
    setPrimaryIssue('Section 16(2)(c) recovery from buyer without pursuing defaulting supplier');
    setWrittenSubmission('');
    setUploadedDocuments([]);
  };

  // Clear all historical cases / cache permanently
  const handleClearHistory = () => {
    localStorage.setItem('ngtp_history_cleared', 'true');
    setCases([]);
    handleResetWorkspace();
  };

  // Run Legal Evaluation Engine
  const handleRunEvaluation = async () => {
    setScopeRejection(null);

    const matterTitle = title.trim() || `${taxpayerName || 'Matter'} - FY ${financialYear}`;
    const taxpayer = taxpayerName.trim() || 'Taxpayer Entity';
    const gstinNum = gstin.trim() || 'Unspecified GSTIN';
    const amount = disputedAmount.trim() || 'Amount under dispute';
    const summary = writtenSubmission.trim() || `${primaryIssue}. Ingested documents: ${uploadedDocuments.length}.`;

    // Package written submission as an explicit document if provided
    let allDocs = [...uploadedDocuments];
    if (writtenSubmission.trim()) {
      const isGrounds = submissionCategory.includes('Grounds');
      const submissionDoc: CaseDocument = {
        id: `doc-sub-${Date.now()}`,
        name: `${submissionCategory.replace(/[^a-zA-Z0-9]/g, '_')}.txt`,
        type: isGrounds ? 'Grounds of Appeal' : 'Reply',
        fileSize: `${(new Blob([writtenSubmission]).size / 1024).toFixed(1)} KB`,
        uploadedAt: new Date().toISOString().split('T')[0],
        ocrReadability: 'Clearly readable text',
        extractedTextSnippet: writtenSubmission.slice(0, 3000)
      };
      allDocs = [submissionDoc, ...allDocs.filter(d => !d.id.startsWith('doc-sub-'))];
    }

    // Client-side Pre-Flight NGTP Scope Check
    const preflightScope = validateNGTPScope(matterTitle, primaryIssue, summary, noticeType, allDocs);
    if (!preflightScope.isNGTP) {
      setActiveCase(null);
      setScopeRejection(preflightScope);
      setIsLoading(false);
      return;
    }

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
          title: matterTitle,
          taxpayerName: taxpayer,
          gstin: gstinNum,
          financialYear,
          disputedAmount: amount,
          noticeType,
          primaryIssue,
          caseSummary: summary,
          geminiApiKey,
          documents: allDocs
        })
      });

      clearTimeout(timeoutId);

      const data = await res.json();
      if (res.status === 422 || data.notApplicable) {
        setActiveCase(null);
        setScopeRejection({
          isNGTP: false,
          detectedDomain: data.detectedDomain || 'Non-NGTP Domain',
          confidenceScore: 95,
          rejectionReason: data.rejectionReason || 'Project is not within NGTP statutory scope.',
          matchedKeywords: [],
          allowedTopics: data.allowedTopics || []
        });
        return;
      }

      if (res.ok && data.evaluatedCase) {
        setScopeRejection(null);
        setActiveCase(data.evaluatedCase);
        setCases(prev => [data.evaluatedCase, ...prev.filter(c => c.id !== data.evaluatedCase.id)]);
      }
    } catch (err: any) {
      console.warn('Evaluation response:', err.message);
    } finally {
      clearTimeout(timeoutId);
      setIsLoading(false);
    }
  };

  // Create new case from modal (Master Data Only - Intelligence runs only once from the main UI)
  const handleCreateNewCaseFromModal = (formData: {
    title: string;
    taxpayerName: string;
    gstin: string;
    financialYear: string;
    disputedAmount: string;
    noticeType: any;
    primaryIssue: string;
    caseSummary: string;
  }) => {
    setActiveCase(null);
    setScopeRejection(null);
    setTitle(formData.title);
    setTaxpayerName(formData.taxpayerName);
    setGstin(formData.gstin);
    setFinancialYear(formData.financialYear);
    setDisputedAmount(formData.disputedAmount);
    setNoticeType(formData.noticeType);
    setPrimaryIssue(formData.primaryIssue);
    setWrittenSubmission(formData.caseSummary || '');
    setUploadedDocuments([]);
    setIsNewCaseOpen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Quick Ingest File Drag-and-Drop (Evidence Tab)
  const handleFileUpload = async (files: FileList | null) => {
    if (!files || files.length === 0) return;
    setIsExtracting(true);
    try {
      const newDocs: CaseDocument[] = [];
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        let text = '';
        if (file.type.includes('text') || file.name.endsWith('.txt') || file.name.endsWith('.csv')) {
          text = await file.text();
        } else {
          text = `Evidence file: ${file.name} (Size: ${(file.size / 1024).toFixed(1)} KB)`;
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

      const updatedDocs = [...newDocs, ...uploadedDocuments];
      setUploadedDocuments(updatedDocs);

      // If a case is already active on screen, auto re-evaluate it
      if (activeCase) {
        const updatedCaseDocs = [...newDocs, ...(activeCase.documents || [])];
        const geminiApiKey = typeof window !== 'undefined' ? (localStorage.getItem('ngtp_gemini_api_key') || undefined) : undefined;
        fetch('/api/analyze', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            title: activeCase.title,
            taxpayerName: activeCase.taxpayerName,
            gstin: activeCase.gstin,
            financialYear: activeCase.financialYear,
            disputedAmount: activeCase.disputedAmount,
            noticeType: activeCase.noticeType,
            primaryIssue: activeCase.primaryIssue,
            caseSummary: activeCase.summary,
            geminiApiKey,
            documents: updatedCaseDocs
          })
        }).then(r => r.json()).then(data => {
          if (data.evaluatedCase) {
            setActiveCase(data.evaluatedCase);
            setCases(prev => [data.evaluatedCase, ...prev.filter(c => c.id !== data.evaluatedCase.id)]);
          }
        }).catch(e => console.warn(e));
      }
    } catch (err) {
      console.error('File upload error:', err);
    } finally {
      setIsExtracting(false);
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  };

  // Import text file into Written Submission textarea (clean parsing for .docx, .doc, .pdf, .txt)
  const handleSubmissionFileImport = async (files: FileList | null) => {
    if (!files || files.length === 0) return;
    const file = files[0];
    const filename = file.name.toLowerCase();

    // Plain text formats (.txt, .md, .csv) can be read directly
    if (filename.endsWith('.txt') || filename.endsWith('.md') || filename.endsWith('.csv')) {
      try {
        const text = await file.text();
        setWrittenSubmission(text);
      } catch (e) {
        console.warn('Could not read text directly:', e);
      }
      return;
    }

    // For .docx, .doc, .pdf, send to server extractor to cleanly parse text without binary zip tags
    setIsParsingDoc(true);
    try {
      const formData = new FormData();
      formData.append('file', file);

      const res = await fetch('/api/extract-text', {
        method: 'POST',
        body: formData
      });

      if (res.ok) {
        const data = await res.json();
        if (data.text) {
          setWrittenSubmission(data.text);
        }
      } else {
        const errData = await res.json().catch(() => ({}));
        alert(`Could not extract text: ${errData.error || 'Server parsing error'}`);
      }
    } catch (e: any) {
      console.error('Document extraction error:', e);
      alert('Error parsing document. Please ensure it is a valid .docx, .pdf, or .txt file.');
    } finally {
      setIsParsingDoc(false);
      if (submissionFileInputRef.current) submissionFileInputRef.current.value = '';
    }
  };

  // Remove document
  const handleRemoveDoc = (id: string) => {
    setUploadedDocuments(prev => prev.filter(d => d.id !== id));
    if (activeCase) {
      const updatedCaseDocs = (activeCase.documents || []).filter(d => d.id !== id);
      setActiveCase({ ...activeCase, documents: updatedCaseDocs });
    }
  };

  // Load a historical case
  const handleSelectHistoricalCase = (c: CaseStudy) => {
    setActiveCase(c);
    setTitle(c.title);
    setTaxpayerName(c.taxpayerName);
    setGstin(c.gstin);
    setFinancialYear(c.financialYear);
    setDisputedAmount(c.disputedAmount);
    setNoticeType(c.noticeType as any);
    setPrimaryIssue(c.primaryIssue);
    setWrittenSubmission(c.summary);
    setUploadedDocuments(c.documents || []);
  };

  return (
    <div className="min-h-screen bg-[#FBF9F5] text-slate-900 flex flex-col font-sans">
      {/* Clean Header with New Assessment & Historical Triggers */}
      <Header
        cases={cases}
        activeCase={activeCase}
        onSelectCase={handleSelectHistoricalCase}
        onResetToCleanWorkspace={handleResetWorkspace}
        onOpenNewCaseModal={() => setIsNewCaseOpen(true)}
        onOpenHistoricalDrawer={() => setIsHistoryDrawerOpen(true)}
        onOpenExportModal={() => setIsExportOpen(true)}
        isDbConnected={isDbConnected}
      />

      {/* Main Container */}
      <main className="flex-grow max-w-5xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6">
        {/* Background Agent Execution Banner */}
        {isLoading && (
          <div className="p-4 rounded-2xl bg-amber-50 border border-amber-200 flex items-center justify-between text-xs text-amber-900 font-medium animate-pulse shadow-sm">
            <div className="flex items-center gap-2.5">
              <Loader2 className="w-4 h-4 text-amber-700 animate-spin flex-shrink-0" />
              <span>
                Running legal intelligence agents in background (Auditing written submissions, SCN grounds, precedent hierarchy, and documentary evidence)...
              </span>
            </div>
            <span className="font-mono text-[11px] font-semibold text-amber-800 whitespace-nowrap">
              Updating Verdict...
            </span>
          </div>
        )}

                {/* 1. EXECUTIVE VERDICT & LITIGATION READINESS OUTPUT (Rendered at top when evaluated) */}
        {activeCase && (
          <div className="space-y-4 animate-fade-in">
            <ExecutiveSummaryView
              caseStudy={activeCase}
              onOpenExportModal={() => setIsExportOpen(true)}
            />
          </div>
        )}

        {/* 2. MATTER PARTICULARS & EVIDENCE INGESTION WORKSPACE */}
        <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-7 shadow-sm">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-beige-200">
            <div>
              <div className="text-[11px] font-mono uppercase text-slate-400 font-bold tracking-wider mb-0.5">
                {activeCase ? 'Active Matter Assessment' : 'Matter Particulars & Ingestion'}
              </div>
              <h2 className="text-lg sm:text-xl font-serif font-bold text-slate-900">
                {activeCase ? 'Modify Matter Particulars & Evidence' : 'Matter Assessment Workspace'}
              </h2>
            </div>

            <div className="flex items-center gap-2 flex-wrap">
              {activeCase && (
                <button
                  onClick={handleResetWorkspace}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-beige-100 hover:bg-beige-200 text-slate-700 text-xs font-semibold transition-all shadow-sm"
                  title="Clear on-screen data back to blank form"
                >
                  <X className="w-3.5 h-3.5" />
                  <span>Clear Screen</span>
                </button>
              )}
            </div>
          </div>

          {/* Form Inputs Grid (Matter Details) */}
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3.5 mt-5">
            <div>
              <label className="block text-[11px] font-mono text-slate-500 font-semibold mb-1">
                Taxpayer Entity:
              </label>
              <input
                type="text"
                value={taxpayerName}
                onChange={(e) => setTaxpayerName(e.target.value)}
                placeholder="e.g. Kaveri Steel Processing"
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm"
              />
            </div>

            <div>
              <label className="block text-[11px] font-mono text-slate-500 font-semibold mb-1">
                GSTIN Number:
              </label>
              <input
                type="text"
                value={gstin}
                onChange={(e) => setGstin(e.target.value)}
                placeholder="e.g. 27AABCK1234E1ZX"
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-xs font-mono text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm"
              />
            </div>

            <div>
              <label className="block text-[11px] font-mono text-slate-500 font-semibold mb-1">
                Financial Year:
              </label>
              <select
                value={financialYear}
                onChange={(e) => setFinancialYear(e.target.value)}
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm"
              >
                <option value="2017-18">FY 2017-18</option>
                <option value="2018-19">FY 2018-19</option>
                <option value="2019-20">FY 2019-20</option>
                <option value="2020-21">FY 2020-21</option>
                <option value="2021-22">FY 2021-22</option>
                <option value="2022-23">FY 2022-23</option>
                <option value="2023-24">FY 2023-24</option>
              </select>
            </div>

            <div>
              <label className="block text-[11px] font-mono text-slate-500 font-semibold mb-1">
                Disputed Tax Amount:
              </label>
              <input
                type="text"
                value={disputedAmount}
                onChange={(e) => setDisputedAmount(e.target.value)}
                placeholder="e.g. INR 25,00,000"
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm"
              />
            </div>
          </div>

          {/* CLEAN TABS: WRITTEN SUBMISSION vs DOCUMENTARY EVIDENCE */}
          <div className="mt-6 pt-4 border-t border-beige-200">
            <div className="flex items-center gap-2 border-b border-beige-200 pb-3">
              <button
                onClick={() => setIngestTab('submission')}
                className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-sm ${
                  ingestTab === 'submission'
                    ? 'bg-amber-600 text-white shadow-amber-200'
                    : 'bg-beige-100 text-slate-700 hover:bg-beige-200'
                }`}
              >
                <FileEdit className="w-4 h-4" />
                <span>Written Submission</span>
                {writtenSubmission.trim() && (
                  <span className="w-2 h-2 rounded-full bg-emerald-400" title="Written submission present"></span>
                )}
              </button>

              <button
                onClick={() => setIngestTab('evidence')}
                className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-sm ${
                  ingestTab === 'evidence'
                    ? 'bg-amber-600 text-white shadow-amber-200'
                    : 'bg-beige-100 text-slate-700 hover:bg-beige-200'
                }`}
              >
                <FolderArchive className="w-4 h-4" />
                <span>Documentary Evidence</span>
                {uploadedDocuments.length > 0 && (
                  <span className={`font-mono text-[10px] px-1.5 py-0.5 rounded font-bold ${
                    ingestTab === 'evidence' ? 'bg-white/25 text-white' : 'bg-beige-200 text-slate-800'
                  }`}>
                    {uploadedDocuments.length}
                  </span>
                )}
              </button>
            </div>

            {/* TAB 1 CONTENT: WRITTEN SUBMISSION */}
            {ingestTab === 'submission' && (
              <div className="mt-4 space-y-3 animate-fade-in">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-semibold text-slate-700">Submission Category:</span>
                    <select
                      value={submissionCategory}
                      onChange={(e) => setSubmissionCategory(e.target.value as any)}
                      className="bg-beige-50 border border-beige-300 rounded-lg px-2.5 py-1 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm"
                    >
                      <option value="Reply to SCN / DRC-01">Reply to SCN / DRC-01</option>
                      <option value="Statement of Facts & Grounds of Appeal">Statement of Facts & Grounds of Appeal (APL-01 / Tribunal)</option>
                      <option value="Personal Hearing Written Submissions">Personal Hearing Written Submissions</option>
                      <option value="High Court Writ Petition Submissions">High Court Writ Petition Submissions</option>
                      <option value="General Written Legal Arguments">General Written Legal Arguments</option>
                    </select>
                  </div>

                  <div className="flex items-center gap-2">
                    <input
                      type="file"
                      ref={submissionFileInputRef}
                      onChange={(e) => handleSubmissionFileImport(e.target.files)}
                      accept=".txt,.doc,.docx,.pdf"
                      className="hidden"
                    />
                    <button
                      type="button"
                      disabled={isParsingDoc}
                      onClick={() => submissionFileInputRef.current?.click()}
                      className="text-[11px] font-mono font-semibold px-2.5 py-1 rounded bg-white border border-beige-300 text-slate-700 hover:bg-beige-50 transition-all shadow-sm flex items-center gap-1 disabled:opacity-60"
                    >
                      {isParsingDoc ? (
                        <>
                          <Loader2 className="w-3 h-3 animate-spin text-amber-700" />
                          <span>Extracting Text...</span>
                        </>
                      ) : (
                        <>
                          <Upload className="w-3 h-3 text-amber-700" />
                          <span>Load Text from File (.docx, .pdf, .txt)</span>
                        </>
                      )}
                    </button>

                    <span className="text-[11px] font-mono text-slate-400">
                      {writtenSubmission.length} characters
                    </span>
                  </div>
                </div>

                <textarea
                  rows={8}
                  value={writtenSubmission}
                  onChange={(e) => setWrittenSubmission(e.target.value)}
                  placeholder={`Paste or type your complete written submission here:
- Factual background & timeline of transaction
- Primary grounds of challenge against Section 16(2)(c) / Section 74
- Contentions regarding bona fide purchaser status, payment through banking channels, Rule 46 compliance
- Rebuttal to Departmental allegations of non-genuine supplier (NGTP)...`}
                  className="w-full bg-beige-50/70 border border-beige-300 rounded-xl p-3.5 text-xs text-slate-900 leading-relaxed focus:outline-none focus:border-amber-600 font-sans shadow-inner"
                />

                <p className="text-[11px] text-slate-500 font-mono">
                  ✓ The agent will audit this written submission for factual contradictions, missing constitutional impossibility arguments, and drafting defects.
                </p>
              </div>
            )}

            {/* TAB 2 CONTENT: DOCUMENTARY EVIDENCE */}
            {ingestTab === 'evidence' && (
              <div className="mt-4 space-y-3 animate-fade-in">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-1">
                  <span className="text-xs font-semibold text-slate-800 flex items-center gap-1.5">
                    <Upload className="w-3.5 h-3.5 text-amber-700" />
                    <span>Upload Documentary Evidence (PDFs, Images, Invoices, Bank Records):</span>
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
                  onDrop={async (e) => { e.preventDefault(); setIsDragging(false); await handleFileUpload(e.dataTransfer.files); }}
                  onClick={() => fileInputRef.current?.click()}
                  className={`border-2 border-dashed rounded-xl p-5 text-center cursor-pointer transition-all ${
                    isDragging ? 'border-amber-600 bg-amber-50' : 'border-beige-300 hover:border-amber-500 bg-beige-50/60 hover:bg-beige-100/60'
                  }`}
                >
                  <input
                    type="file"
                    ref={fileInputRef}
                    onChange={(e) => handleFileUpload(e.target.files)}
                    multiple
                    accept=".pdf,.png,.jpg,.jpeg,.txt,.csv,.doc,.docx"
                    className="hidden"
                  />
                  {isExtracting ? (
                    <div className="flex items-center justify-center gap-2 text-amber-700 py-1">
                      <Loader2 className="w-4 h-4 animate-spin" />
                      <span className="text-xs font-semibold">Attaching evidence file...</span>
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
                {uploadedDocuments.length > 0 && (
                  <div className="flex items-center gap-2 mt-3 flex-wrap">
                    <span className="text-[11px] font-mono text-slate-400 font-semibold uppercase">
                      Attached Evidence ({uploadedDocuments.length}):
                    </span>
                    {uploadedDocuments.map((d) => (
                      <div key={d.id} className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-beige-100 border border-beige-200 text-xs shadow-sm">
                        <span className="font-mono text-[10px] font-bold text-amber-900">{d.type}:</span>
                        <span className="text-slate-800 font-medium truncate max-w-[150px]">{d.name}</span>
                        <button
                          onClick={() => handleRemoveDoc(d.id)}
                          className="text-slate-400 hover:text-rose-600 ml-1"
                          title="Remove file"
                        >
                          <Trash2 className="w-3 h-3" />
                        </button>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Action Button */}
          <div className="mt-5 pt-4 border-t border-beige-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <span className="text-xs text-slate-500">
              {writtenSubmission.trim() || uploadedDocuments.length > 0
                ? `Ready: ${writtenSubmission.trim() ? 'Written submission attached. ' : ''}${uploadedDocuments.length} documentary file(s).`
                : 'Tip: Type or paste your written submission in Tab 1 and attach invoices/bank proof in Tab 2.'}
            </span>

            <button
              onClick={handleRunEvaluation}
              disabled={isLoading}
              className="flex items-center justify-center gap-2 px-6 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-700 disabled:opacity-50 text-white font-semibold text-xs shadow-md transition-all whitespace-nowrap"
            >
              <Zap className="w-4 h-4 fill-white" />
              <span>{isLoading ? 'Running Legal Agents...' : 'Run Legal Intelligence Engine'}</span>
            </button>
          </div>
        </div>

        
        {/* NON-NGTP SCOPE REJECTION BANNER */}
        {scopeRejection && (
          <div className="bg-rose-50 border-2 border-rose-300 rounded-2xl p-6 sm:p-7 shadow-md animate-fade-in space-y-4">
            <div className="flex items-start justify-between gap-3">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-rose-100 border border-rose-200 flex items-center justify-center flex-shrink-0 text-rose-700 font-bold text-lg">
                  ⛔
                </div>
                <div>
                  <span className="text-[11px] font-mono uppercase font-bold text-rose-800 tracking-wider">
                    Execution Halted &bull; Statutory Scope Filter
                  </span>
                  <h3 className="text-lg font-serif font-bold text-slate-900">
                    NOT APPLICABLE: Non-NGTP Matter Detected
                  </h3>
                </div>
              </div>
              <button
                onClick={() => setScopeRejection(null)}
                className="text-slate-400 hover:text-slate-700 p-1"
                title="Dismiss"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="p-4 rounded-xl bg-white border border-rose-200 space-y-2">
              <div className="text-xs text-slate-800 font-sans leading-relaxed">
                <strong className="text-rose-900">Detected Subject Domain:</strong>{' '}
                <span className="font-mono font-semibold px-2 py-0.5 rounded bg-rose-100 text-rose-900">
                  {scopeRejection.detectedDomain}
                </span>
              </div>
              <p className="text-xs text-slate-600 font-sans leading-relaxed">
                {scopeRejection.rejectionReason}
              </p>
            </div>

            <div className="pt-1">
              <span className="text-[11px] font-mono font-bold text-slate-700 uppercase block mb-2">
                Permitted NGTP Disputes for this Engine:
              </span>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                {scopeRejection.allowedTopics?.map((topic, i) => (
                  <div key={i} className="flex items-center gap-2 p-2 rounded-lg bg-white/80 border border-rose-100 text-slate-700">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0" />
                    <span>{topic}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="pt-2 flex justify-end">
              <button
                onClick={() => {
                  setScopeRejection(null);
                  handleResetWorkspace();
                }}
                className="px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold shadow-sm transition-all"
              >
                Reset to Clean NGTP Assessment
              </button>
            </div>
          </div>
        )}


      </main>

      {/* Clean Footer */}
      <footer className="border-t border-beige-200 bg-white/80 py-4 px-6 text-center text-xs text-slate-500 font-mono">
        NGTP Litigation Intelligence Engine • Automated Statutory Evidence Audit & Precedent Intelligence
      </footer>

      {/* New Assessment Modal */}
      <NewCaseModal
        isOpen={isNewCaseOpen}
        onClose={() => setIsNewCaseOpen(false)}
        onSubmitNewCase={handleCreateNewCaseFromModal}
      />

      {/* Slide-over Historical Cases Drawer */}
      <HistoricalCasesDrawer
        isOpen={isHistoryDrawerOpen}
        onClose={() => setIsHistoryDrawerOpen(false)}
        cases={cases}
        activeCaseId={activeCase?.id}
        onSelectCase={handleSelectHistoricalCase}
        onClearHistory={handleClearHistory}
        onDeleteSingleCase={(id) => setCases(prev => prev.filter(c => c.id !== id))}
      />

      {/* Export Modal */}
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
