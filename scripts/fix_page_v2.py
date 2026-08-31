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
    const updatedDocs = [doc, ...(activeCase?.documents || [])];
    reEvaluateCase(activeCase, updatedDocs);
  };

  // Remove document from active case & trigger instant re-evaluation
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

      {/* Main Container */}
      <main className="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 py-6">
        {isLoading && (
          <div className="mb-4 p-3.5 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-between text-xs text-amber-900 font-medium animate-pulse shadow-sm">
            <div className="flex items-center gap-2">
              <Loader2 className="w-4 h-4 text-amber-700 animate-spin" />
              <span>Auditing evidence changes against Section 16(2) statutory tests and Suncraft doctrine...</span>
            </div>
            <span className="font-mono text-[11px] font-semibold text-amber-800">Recalculating Scores...</span>
          </div>
        )}

        {activeCase ? (
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
print("Updated page.tsx successfully!")