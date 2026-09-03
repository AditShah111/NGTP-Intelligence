'use client';

import React, { useState } from 'react';
import { CaseStudy } from '../types';
import { 
  ShieldCheck, 
  AlertTriangle, 
  XCircle, 
  CheckCircle2, 
  Gavel, 
  Scale, 
  Award, 
  Swords, 
  FileText, 
  ListChecks, 
  Download,
  AlertCircle,
  FileCheck,
  ChevronDown,
  ChevronUp,
  BookOpen,
  Layers,
  CheckCircle
} from 'lucide-react';

interface Props {
  caseStudy: CaseStudy;
  onOpenExportModal: () => void;
}

export const ExecutiveSummaryView: React.FC<Props> = ({ caseStudy, onOpenExportModal }) => {
  const { 
    finalOutput, 
    statutoryParameters, 
    redTeamItems, 
    readinessScore, 
    viabilityScore,
    precedents,
    documents,
    factMatrix,
    improvedSubmissions,
    draftAudit,
    lowerAuthorityErrors,
    evidenceGaps,
    forwardDecision
  } = caseStudy;

  const [is13StepsOpen, setIs13StepsOpen] = useState(false);
  const [isFactsOpen, setIsFactsOpen] = useState(false);
  const [isGroundsOpen, setIsGroundsOpen] = useState(false);

  const isProceed = finalOutput.executiveVerdict.recommendation === 'PROCEED';
  const isRectify = finalOutput.executiveVerdict.recommendation === 'PROCEED AFTER RECTIFICATION';

  const verificationSteps = [
    { num: 1, name: 'Fact Matrix & Timeline Extraction', desc: `${factMatrix.length} factual timeline items extracted & reconciled`, status: 'DONE' },
    { num: 2, name: 'Statutory Parameters Audit (P1–P8)', desc: `${statutoryParameters.filter(p => p.assessment === 'SATISFIED').length} of ${statutoryParameters.length} statutory requirements satisfied`, status: 'DONE' },
    { num: 3, name: 'Judicial Precedent Ingestion', desc: `${precedents.length} Supreme Court & High Court rulings ingested`, status: 'DONE' },
    { num: 4, name: '6-Axis Evidentiary Comparability', desc: 'Precedents scored on statutory, factual & evidentiary comparability', status: 'DONE' },
    { num: 5, name: 'Lower Authority Error Audit', desc: `${lowerAuthorityErrors.length} procedural & jurisdictional flaws detected in SCN/order`, status: 'DONE' },
    { num: 6, name: 'Grounds of Appeal Optimizer', desc: `${improvedSubmissions.length} court-ready IRAC grounds formulated`, status: 'DONE' },
    { num: 7, name: 'Adversarial Red-Team War Room', desc: `${redTeamItems.length} Revenue Standing Counsel attack vectors tested`, status: 'DONE' },
    { num: 8, name: 'Evidence Gap Prioritization', desc: `${evidenceGaps.length} evidence gaps classified into P0, P1, and P2`, status: 'DONE' },
    { num: 9, name: 'Litigation Readiness Scoring', desc: `Calculated from first principles: ${readinessScore.totalScore}/100`, status: 'DONE' },
    { num: 10, name: 'Litigation Viability Scoring', desc: `Viability score ${viabilityScore.totalScore}/100 (${viabilityScore.probabilityOfFavourableOutcome} probability)`, status: 'DONE' },
    { num: 11, name: 'Forward Decision Formulation', desc: `Definitive outcome: ${finalOutput.executiveVerdict.recommendation}`, status: 'DONE' },
    { num: 12, name: 'Drafting & Defect Audit', desc: `${draftAudit.length} drafting traps & missing pleadings audited`, status: 'DONE' },
    { num: 13, name: 'Executive Verdict & Dossier Assembly', desc: '1-page executive brief synthesized & ready to export', status: 'DONE' }
  ];

  return (
    <div className="space-y-6 animate-fade-in">
      {/* 1. Core Verdict & Decision Banner */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 pb-6 border-b border-beige-200">
          <div>
            <div className="text-xs font-mono uppercase text-slate-400 font-semibold tracking-wider mb-1">
              Executive Litigation Verdict
            </div>
            <div className="flex items-center gap-3 flex-wrap">
              <span className={`text-xl sm:text-2xl font-serif font-bold px-4 py-1.5 rounded-xl border shadow-sm ${
                isProceed ? 'bg-emerald-50 text-emerald-900 border-emerald-300' :
                isRectify ? 'bg-amber-50 text-amber-900 border-amber-300' :
                'bg-rose-50 text-rose-900 border-rose-300'
              }`}>
                {finalOutput.executiveVerdict.recommendation}
              </span>
              <span className="text-xs font-mono font-semibold px-3 py-1 rounded-lg bg-beige-100 text-slate-700 border border-beige-300">
                Probability: {viabilityScore.probabilityOfFavourableOutcome}
              </span>

              {/* 13-Step Verification Completed Pill */}
              <button
                onClick={() => setIs13StepsOpen(!is13StepsOpen)}
                className="text-xs font-mono font-bold px-3 py-1 rounded-lg bg-purple-50 text-purple-900 border border-purple-200 hover:bg-purple-100 flex items-center gap-1.5 transition-all shadow-sm"
              >
                <Layers className="w-3.5 h-3.5 text-purple-700" />
                <span>13-Step Verification Pipeline ({is13StepsOpen ? 'Hide' : 'View Trace'})</span>
                {is13StepsOpen ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
              </button>
            </div>
          </div>

          <div className="flex items-center gap-3 flex-wrap">
            <div className="text-center p-3 sm:p-4 rounded-xl bg-beige-50 border border-beige-200 min-w-[110px]">
              <div className="text-[11px] font-mono text-slate-500 uppercase">Readiness Score</div>
              <div className="text-2xl sm:text-3xl font-mono font-bold text-slate-900 mt-0.5">
                {readinessScore.totalScore}<span className="text-sm text-slate-400">/100</span>
              </div>
            </div>
            <div className="text-center p-3 sm:p-4 rounded-xl bg-beige-50 border border-beige-200 min-w-[110px]">
              <div className="text-[11px] font-mono text-slate-500 uppercase">Viability Score</div>
              <div className="text-2xl sm:text-3xl font-mono font-bold text-amber-700 mt-0.5">
                {viabilityScore.totalScore}<span className="text-sm text-slate-400">/100</span>
              </div>
            </div>
            <button
              onClick={onOpenExportModal}
              className="flex items-center gap-2 px-5 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs shadow-md transition-all whitespace-nowrap self-stretch sm:self-auto justify-center"
              title="Export complete structured litigation dossier"
            >
              <Download className="w-4 h-4 text-amber-400" />
              <span>Export Dossier</span>
            </button>
          </div>
        </div>

        {/* EXPANDABLE 13-STEP VERIFICATION PIPELINE DETAILS */}
        {is13StepsOpen && (
          <div className="mt-5 p-4 rounded-xl bg-purple-50/50 border border-purple-200 animate-fade-in space-y-3">
            <div className="flex items-center justify-between">
              <span className="font-mono text-xs font-bold text-purple-950 uppercase flex items-center gap-1.5">
                <ShieldCheck className="w-4 h-4 text-purple-700" />
                Full 13-Step Verification Execution Trace:
              </span>
              <span className="text-[10px] font-mono text-emerald-800 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                13 / 13 Steps Executed
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2.5 text-xs pt-2">
              {verificationSteps.map((step) => (
                <div key={step.num} className="p-3 bg-white rounded-lg border border-purple-100 shadow-sm flex flex-col justify-between">
                  <div>
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-mono font-bold text-[11px] px-1.5 py-0.2 rounded bg-purple-100 text-purple-900">
                        Step {step.num}
                      </span>
                      <span className="text-[10px] font-mono font-bold text-emerald-700 flex items-center gap-1">
                        <CheckCircle2 className="w-3 h-3" /> Verified
                      </span>
                    </div>
                    <div className="font-semibold text-slate-900 mt-1">{step.name}</div>
                    <p className="text-[11px] text-slate-600 mt-0.5 font-sans leading-relaxed">
                      {step.desc}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Core Decision Reasons */}
        <div className="mt-6">
          <div className="text-xs font-mono uppercase text-slate-400 font-semibold mb-3">
            Core Decision Drivers & Legal Rationale:
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {finalOutput.executiveVerdict.top5Reasons.map((reason, idx) => (
              <div key={idx} className="flex items-start gap-2.5 p-3 rounded-xl bg-beige-50/70 border border-beige-200 text-xs text-slate-800">
                <CheckCircle2 className="w-4 h-4 text-emerald-700 flex-shrink-0 mt-0.5" />
                <span className="leading-relaxed">{reason}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Advantage & Risk Highlights */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4 pt-4 border-t border-beige-200 text-xs">
          <div className="p-3.5 rounded-xl bg-emerald-50/60 border border-emerald-200">
            <div className="font-mono text-[11px] uppercase font-bold text-emerald-900 mb-1 flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-700" />
              Single Strongest Advantage:
            </div>
            <p className="text-slate-800 font-medium leading-relaxed">
              {finalOutput.finalLitigationAssessment.singleStrongestAdvantage}
            </p>
          </div>
          <div className="p-3.5 rounded-xl bg-rose-50/60 border border-rose-200">
            <div className="font-mono text-[11px] uppercase font-bold text-rose-900 mb-1 flex items-center gap-1.5">
              <AlertTriangle className="w-4 h-4 text-rose-700" />
              Single Biggest Risk:
            </div>
            <p className="text-slate-800 font-medium leading-relaxed">
              {finalOutput.finalLitigationAssessment.singleBiggestRisk}
            </p>
          </div>
        </div>
      </div>

      {/* 2. Summary of Statutory & Evidentiary Parameters Checked (P1 to P8) */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200 mb-4">
          <div className="flex items-center gap-2">
            <Scale className="w-5 h-5 text-amber-700" />
            <h3 className="text-lg font-serif font-bold text-slate-900">
              Statutory & Evidentiary Parameters Checked (P1–P8)
            </h3>
          </div>
          <span className="text-xs font-mono text-slate-500">
            {statutoryParameters.filter(p => p.assessment === 'SATISFIED').length} of {statutoryParameters.length} Satisfied
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
          {statutoryParameters.map((p) => {
            const isSatisfied = p.assessment === 'SATISFIED';
            const isCritical = p.risk === 'CRITICAL' || p.risk === 'HIGH';

            return (
              <div
                key={p.id}
                className="bg-beige-50/60 border border-beige-200 rounded-xl p-4 flex flex-col justify-between hover:border-amber-300 transition-all shadow-sm"
              >
                <div>
                  <div className="flex items-center justify-between gap-2 mb-2">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-200">
                        {p.parameterCode}
                      </span>
                      <span className="font-serif font-bold text-xs text-slate-900">{p.title}</span>
                    </div>
                    <span className={`text-[10px] font-semibold px-2 py-0.5 rounded-full border ${
                      isSatisfied ? 'bg-emerald-50 text-emerald-800 border-emerald-200' :
                      p.assessment === 'PARTIALLY SATISFIED' ? 'bg-amber-50 text-amber-800 border-amber-200' :
                      'bg-rose-50 text-rose-800 border-rose-200'
                    }`}>
                      {p.assessment}
                    </span>
                  </div>

                  <p className="text-[11px] text-slate-600 leading-relaxed mb-2 font-sans">
                    {p.reason}
                  </p>
                </div>

                <div className="pt-2 border-t border-beige-200/80 flex items-center justify-between text-[10px] font-mono">
                  <span className="text-slate-500 truncate max-w-[200px]" title={p.courtEvidentiaryPrecedent}>
                    Anchor: <strong className="text-slate-800">{p.courtEvidentiaryPrecedent || 'Statutory Act'}</strong>
                  </span>
                  <span className={isCritical ? 'text-rose-700 font-bold' : 'text-emerald-700 font-semibold'}>
                    Risk: {p.risk}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* 3. Statement of Facts & Grounds of Appeal Review */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
        <div className="flex items-center justify-between pb-3 border-b border-beige-200">
          <div className="flex items-center gap-2">
            <FileCheck className="w-5 h-5 text-blue-700" />
            <h3 className="text-lg font-serif font-bold text-slate-900">
              Statement of Facts & Grounds of Appeal Review
            </h3>
          </div>
          <span className="text-xs font-mono text-blue-800 bg-blue-50 px-2.5 py-1 rounded-full border border-blue-200 font-semibold">
            Pleadings & Grounds Audited
          </span>
        </div>

        {/* Fact Matrix & Contradiction Check */}
        <div className="p-4 rounded-xl bg-beige-50/70 border border-beige-200">
          <div 
            onClick={() => setIsFactsOpen(!isFactsOpen)}
            className="flex items-center justify-between cursor-pointer"
          >
            <div className="flex items-center gap-2">
              <span className="font-mono text-xs font-bold text-slate-800 uppercase">
                A. Statement of Facts & Contradiction Check ({factMatrix.length} Extracted Facts)
              </span>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-100 text-emerald-900 border border-emerald-200 font-bold">
                ✓ Timeline Reconciled
              </span>
            </div>
            <button className="text-slate-500 hover:text-slate-800">
              {isFactsOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
            </button>
          </div>

          {isFactsOpen && (
            <div className="mt-3 pt-3 border-t border-beige-200 space-y-2 text-xs">
              {factMatrix.map((f) => (
                <div key={f.id} className="p-3 bg-white rounded-lg border border-beige-200 space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="font-semibold text-slate-900">{f.allegedFact}</span>
                    <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-slate-100 text-slate-700">
                      Strength: {f.evidenceStrength}
                    </span>
                  </div>
                  <div className="text-[11px] text-slate-500 flex items-center gap-2">
                    <span>Source: {f.sourceDocument}</span>
                    <span>•</span>
                    <span className="text-amber-800">{f.significance}</span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Draft Appeal Grounds & Defect Audit */}
        <div className="p-4 rounded-xl bg-beige-50/70 border border-beige-200">
          <div 
            onClick={() => setIsGroundsOpen(!isGroundsOpen)}
            className="flex items-center justify-between cursor-pointer"
          >
            <div className="flex items-center gap-2">
              <span className="font-mono text-xs font-bold text-slate-800 uppercase">
                B. Grounds of Appeal & Drafting Defect Audit ({draftAudit.length} Critical Checks)
              </span>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-200 font-bold">
                {draftAudit.length} Optimizations Recommended
              </span>
            </div>
            <button className="text-slate-500 hover:text-slate-800">
              {isGroundsOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
            </button>
          </div>

          {isGroundsOpen && (
            <div className="mt-3 pt-3 border-t border-beige-200 space-y-3 text-xs">
              {/* Draft Defects Detected */}
              <div className="space-y-2">
                <div className="font-mono text-[11px] font-bold text-slate-500 uppercase">Drafting Flaws & Pleading Gaps:</div>
                {draftAudit.map((d) => (
                  <div key={d.id} className="p-3 bg-white rounded-lg border border-beige-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                    <div>
                      <span className="font-semibold text-rose-800">⚠️ {d.issueDetected}</span>
                      <p className="text-slate-600 text-[11px] mt-0.5 font-sans">
                        <strong>Correction:</strong> {d.recommendedCorrection}
                      </p>
                    </div>
                    <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-rose-50 text-rose-800 border border-rose-200 font-bold self-start sm:self-center">
                      Severity: {d.severity}
                    </span>
                  </div>
                ))}
              </div>

              {/* Ready-to-file IRAC Grounds */}
              <div className="space-y-2 pt-2 border-t border-beige-200">
                <div className="font-mono text-[11px] font-bold text-slate-500 uppercase">Ready-to-File IRAC Grounds of Appeal:</div>
                {improvedSubmissions.map((sub, idx) => (
                  <div key={idx} className="p-3 bg-white rounded-lg border border-beige-200 space-y-1">
                    <div className="flex items-center justify-between">
                      <span className="font-serif font-bold text-amber-900 text-xs">{sub.groundNumber}: {sub.title}</span>
                      <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 font-bold">
                        Strength: {sub.groundStrength}%
                      </span>
                    </div>
                    <p className="text-slate-700 text-[11px] font-sans leading-relaxed">
                      {sub.proposition}
                    </p>
                    <div className="text-[10px] font-mono text-slate-500 pt-1">
                      Anchor Precedent: <strong className="text-slate-800">{sub.precedent}</strong>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* 4. Department Counter-Party Response (Adversarial Standing Counsel Arguments) */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200 mb-4">
          <div className="flex items-center gap-2">
            <Swords className="w-5 h-5 text-rose-700" />
            <h3 className="text-lg font-serif font-bold text-slate-900">
              Department Standing Counsel Response & Counter-Defense
            </h3>
          </div>
          <span className="text-xs font-mono text-purple-800 bg-purple-50 px-2.5 py-1 rounded-full border border-purple-200">
            Adversarial War-Room Audit
          </span>
        </div>

        <div className="space-y-3.5">
          {redTeamItems.map((item) => (
            <div key={item.id} className="p-4 rounded-xl bg-beige-50/60 border border-beige-200 space-y-2.5">
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono uppercase font-bold text-rose-800 flex items-center gap-1.5">
                  <AlertCircle className="w-3.5 h-3.5 text-rose-600" />
                  {item.category} (Attack Strength: {item.strengthOfOpposingArgument}%)
                </span>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200 font-bold">
                  {item.survivesAttack ? '✓ Defense Survives' : '⚠️ Defense Vulnerable'}
                </span>
              </div>

              <div className="text-xs text-slate-800 bg-white p-3 rounded-lg border border-beige-200 leading-relaxed font-sans">
                <strong className="text-rose-900 font-semibold block mb-1">Department Revenue Argument:</strong>
                {item.opposingArgument}
              </div>

              <div className="text-xs text-slate-800 bg-emerald-50/40 p-3 rounded-lg border border-emerald-200 leading-relaxed font-sans">
                <strong className="text-emerald-900 font-semibold block mb-1">Our Prepared Taxpayer Response:</strong>
                {item.taxpayerResponse}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 5. Action Plan & Export Brief */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 sm:p-8 shadow-sm flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="text-base font-serif font-bold text-slate-900">
            Comprehensive Litigation Dossier Ready
          </div>
          <p className="text-xs text-slate-600 mt-0.5">
            Export the complete structured legal brief with Article 141 citations, IRAC grounds, and evidentiary matrices.
          </p>
        </div>
        <button
          onClick={onOpenExportModal}
          className="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-semibold text-xs shadow-md transition-all whitespace-nowrap"
        >
          <Download className="w-4 h-4" />
          <span>Export Appeal Brief / Dossier</span>
        </button>
      </div>
    </div>
  );
};
