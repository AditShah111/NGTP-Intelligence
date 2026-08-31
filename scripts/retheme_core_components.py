# 1. Update src/components/Header.tsx
header_code = """'use client';

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
"""
with open("src/components/Header.tsx", "w", encoding="utf-8") as f:
    f.write(header_code)

# 2. Update src/components/CaseOverviewCard.tsx
card_code = """'use client';

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
"""
with open("src/components/CaseOverviewCard.tsx", "w", encoding="utf-8") as f:
    f.write(card_code)

# 3. Update src/components/StepProgressNav.tsx
nav_code = """'use client';

import React from 'react';
import { 
  FileSearch, 
  Scale, 
  BookOpen, 
  AlertOctagon, 
  FileEdit, 
  Swords, 
  SearchX, 
  Gauge, 
  Compass, 
  CheckCircle2, 
  Trophy 
} from 'lucide-react';

interface StepProgressNavProps {
  activeStep: number;
  onSelectStep: (step: number) => void;
}

const STEPS = [
  { step: 1, label: 'Fact Matrix', icon: FileSearch },
  { step: 2, label: 'Statutory Tests', icon: Scale },
  { step: 3, label: 'Precedents', icon: BookOpen },
  { step: 5, label: 'Lower Errors', icon: AlertOctagon },
  { step: 6, label: 'Submissions', icon: FileEdit },
  { step: 7, label: 'Red-Team War Room', icon: Swords },
  { step: 8, label: 'Evidence Gaps', icon: SearchX },
  { step: 9, label: 'Readiness & Viability', icon: Gauge },
  { step: 11, label: 'Forward Plan', icon: Compass },
  { step: 12, label: 'Draft Audit', icon: CheckCircle2 },
  { step: 13, label: 'Executive Verdict', icon: Trophy },
];

export const StepProgressNav: React.FC<StepProgressNavProps> = ({
  activeStep,
  onSelectStep
}) => {
  return (
    <div className="bg-white border border-beige-200 rounded-2xl p-2 mb-6 shadow-sm overflow-x-auto">
      <div className="flex items-center gap-1.5 min-w-max">
        {STEPS.map((s) => {
          const Icon = s.icon;
          const isActive = activeStep === s.step;
          return (
            <button
              key={s.step}
              onClick={() => onSelectStep(s.step)}
              className={`flex items-center gap-2 px-3.5 py-2.5 rounded-xl text-xs font-medium transition-all ${
                isActive
                  ? 'bg-amber-600 text-white font-semibold shadow-sm'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-beige-50'
              }`}
            >
              <Icon className={`w-4 h-4 ${isActive ? 'text-white' : 'text-slate-400'}`} />
              <span>{s.label}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
"""
with open("src/components/StepProgressNav.tsx", "w", encoding="utf-8") as f:
    f.write(nav_code)

# 4. Update src/app/page.tsx with beige canvas
page_code = """'use client';

import React, { useState, useEffect } from 'react';
import { Header } from '../components/Header';
import { CaseOverviewCard } from '../components/CaseOverviewCard';
import { StepProgressNav } from '../components/StepProgressNav';
import { DocumentUploaderModal } from '../components/DocumentUploaderModal';
import { NewCaseModal } from '../components/NewCaseModal';
import { ExportDossierModal } from '../components/ExportDossierModal';

import { Step1FactMatrixView } from '../components/steps/Step1FactMatrixView';
import { Step2StatutoryEngineView } from '../components/steps/Step2StatutoryEngineView';
import { Step3Step4PrecedentsView } from '../components/steps/Step3Step4PrecedentsView';
import { Step5LowerAuthorityErrorsView } from '../components/steps/Step5LowerAuthorityErrorsView';
import { Step6SubmissionOptimizerView } from '../components/steps/Step6SubmissionOptimizerView';
import { Step7RedTeamBattleView } from '../components/steps/Step7RedTeamBattleView';
import { Step8EvidenceGapView } from '../components/steps/Step8EvidenceGapView';
import { Step9Step10ScoresView } from '../components/steps/Step9Step10ScoresView';
import { Step11ForwardDecisionView } from '../components/steps/Step11ForwardDecisionView';
import { Step12DraftAuditView } from '../components/steps/Step12DraftAuditView';
import { Step13FinalVerdictView } from '../components/steps/Step13FinalVerdictView';

import { CaseStudy, CaseDocument } from '../types';
import { BENCHMARK_CASES } from '../repo/benchmark-data';
import { Scale, Loader2, Sparkles, AlertCircle } from 'lucide-react';

export default function HomePage() {
  const [cases, setCases] = useState<CaseStudy[]>(BENCHMARK_CASES);
  const [activeCase, setActiveCase] = useState<CaseStudy>(BENCHMARK_CASES[0]);
  const [activeStep, setActiveStep] = useState<number>(1);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isDbConnected, setIsDbConnected] = useState<boolean>(true);

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

  // Re-evaluate a case with updated parameters or documents
  const reEvaluateCase = async (current: CaseStudy, updatedDocs: CaseDocument[]) => {
    setIsLoading(true);
    try {
      const geminiApiKey = typeof window !== 'undefined' ? (localStorage.getItem('ngtp_gemini_api_key') || undefined) : undefined;
      const res = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
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

      if (res.ok) {
        const data = await res.json();
        if (data.evaluatedCase) {
          const updated = { ...data.evaluatedCase, id: current.id };
          setActiveCase(updated);
          setCases(prev => prev.map(c => c.id === current.id ? updated : c));
        }
      }
    } catch (err) {
      console.error('Re-evaluation error:', err);
    } finally {
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
    try {
      const geminiApiKey = typeof window !== 'undefined' ? (localStorage.getItem('ngtp_gemini_api_key') || undefined) : undefined;
      const res = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...formData,
          geminiApiKey,
          documents: formData.documents || []
        })
      });

      if (res.ok) {
        const data = await res.json();
        if (data.evaluatedCase) {
          setCases(prev => [data.evaluatedCase, ...prev]);
          setActiveCase(data.evaluatedCase);
          setActiveStep(13); // jump to verdict!
        }
      }
    } catch (err) {
      console.error('Analysis failed:', err);
    } finally {
      setIsLoading(false);
    }
  };

  // Add real document to active case & trigger instant re-evaluation
  const handleAddDocument = (doc: CaseDocument) => {
    const updatedDocs = [doc, ...activeCase.documents];
    reEvaluateCase(activeCase, updatedDocs);
  };

  // Remove document from active case & trigger instant re-evaluation
  const handleRemoveDocument = (id: string) => {
    const updatedDocs = activeCase.documents.filter(d => d.id !== id);
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

      {/* Main Container */}
      <main className="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 py-6">
        {isLoading ? (
          <div className="flex flex-col items-center justify-center py-24 space-y-4">
            <Loader2 className="w-10 h-10 text-amber-600 animate-spin" />
            <div className="text-center font-serif text-lg font-bold text-slate-900">
              Running Rigorous 13-Step Evidentiary & Statutory Audit...
            </div>
            <p className="text-xs font-sans text-slate-600 max-w-md text-center">
              Auditing uploaded documents against Section 16(2) non-obstante tests, Section 155 burden of proof, bank RTGS trails, and Supreme Court precedent ratios.
            </p>
          </div>
        ) : activeCase ? (
          <div className="animate-fade-in">
            {/* Case Overview Summary Card */}
            <CaseOverviewCard activeCase={activeCase} />

            {/* 13-Step Navigation Bar */}
            <StepProgressNav
              activeStep={activeStep}
              onSelectStep={setActiveStep}
            />

            {/* Step View Render */}
            <div className="transition-all duration-200">
              {activeStep === 1 && (
                <Step1FactMatrixView factMatrix={activeCase.factMatrix} />
              )}
              {activeStep === 2 && (
                <Step2StatutoryEngineView parameters={activeCase.statutoryParameters} />
              )}
              {activeStep === 3 && (
                <Step3Step4PrecedentsView precedents={activeCase.precedents} />
              )}
              {activeStep === 5 && (
                <Step5LowerAuthorityErrorsView errors={activeCase.lowerAuthorityErrors} />
              )}
              {activeStep === 6 && (
                <Step6SubmissionOptimizerView grounds={activeCase.improvedSubmissions} />
              )}
              {activeStep === 7 && (
                <Step7RedTeamBattleView redTeamItems={activeCase.redTeamItems} />
              )}
              {activeStep === 8 && (
                <Step8EvidenceGapView evidenceGaps={activeCase.evidenceGaps} />
              )}
              {activeStep === 9 && (
                <Step9Step10ScoresView
                  readiness={activeCase.readinessScore}
                  viability={activeCase.viabilityScore}
                />
              )}
              {activeStep === 11 && (
                <Step11ForwardDecisionView decision={activeCase.forwardDecision} />
              )}
              {activeStep === 12 && (
                <Step12DraftAuditView defects={activeCase.draftAudit} />
              )}
              {activeStep === 13 && (
                <Step13FinalVerdictView output={activeCase.finalOutput} />
              )}
            </div>
          </div>
        ) : (
          <div className="text-center py-20 text-slate-500">
            No case loaded. Click "New Assessment" to begin.
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-beige-200 bg-white/80 py-4 px-6 text-center text-xs text-slate-500 font-mono">
        NGTP Indian Tax & GST Appellate Intelligence Engine • Strict Evidentiary & Statutory Discipline • Zero Hallucinations
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
    f.write(page_code)

print("Updated Header, CaseOverviewCard, StepProgressNav, and Page to off-white/beige aesthetic!")