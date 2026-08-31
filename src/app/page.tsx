'use client';

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
import { Scale, Loader2, Sparkles } from 'lucide-react';

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
          documentTexts: []
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

  // Add document to active case
  const handleAddDocument = (doc: CaseDocument) => {
    const updatedDocs = [doc, ...activeCase.documents];
    const updatedCase = { ...activeCase, documents: updatedDocs };
    setActiveCase(updatedCase);
    setCases(prev => prev.map(c => c.id === updatedCase.id ? updatedCase : c));
  };

  // Remove document from active case
  const handleRemoveDocument = (id: string) => {
    const updatedDocs = activeCase.documents.filter(d => d.id !== id);
    const updatedCase = { ...activeCase, documents: updatedDocs };
    setActiveCase(updatedCase);
    setCases(prev => prev.map(c => c.id === updatedCase.id ? updatedCase : c));
  };

  return (
    <div className="min-h-screen bg-[#070b14] text-slate-100 flex flex-col font-sans">
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
            <Loader2 className="w-10 h-10 text-amber-400 animate-spin" />
            <div className="text-center font-serif text-lg text-white">
              Running 13-Step Legal Evaluator Engine...
            </div>
            <p className="text-xs font-mono text-slate-400 max-w-md text-center">
              Evaluating statutory parameters, extracting precedent ratios, stress-testing against Revenue counterarguments, and calculating readiness scores.
            </p>
          </div>
        ) : activeCase ? (
          <div>
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
          <div className="text-center py-20 text-slate-400">
            No case loaded. Click "New Assessment" to begin.
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-legal-800/60 bg-[#0c1322]/80 py-4 px-6 text-center text-xs text-slate-500 font-mono">
        NGTP Indian Tax & GST Appellate Intelligence Engine • Built with Codex & Harness Multi-Agent Architecture • Isolated Supabase PostgreSQL
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
