import os

code_step1 = """'use client';

import React from 'react';
import { FactMatrixItem } from '@/types';
import { Table, CheckCircle, AlertCircle, HelpCircle, FileText, Check, AlertTriangle } from 'lucide-react';

interface Step1Props {
  factMatrix: FactMatrixItem[];
}

export const Step1FactMatrixView: React.FC<Step1Props> = ({ factMatrix }) => {
  const getStrengthBadge = (strength: string) => {
    switch (strength) {
      case 'Established':
        return 'bg-emerald-950/80 text-emerald-300 border-emerald-500/40';
      case 'Strongly supported':
        return 'bg-blue-950/80 text-blue-300 border-blue-500/40';
      case 'Probable':
        return 'bg-amber-950/80 text-amber-300 border-amber-500/40';
      case 'Disputed':
        return 'bg-orange-950/80 text-orange-300 border-orange-500/40';
      default:
        return 'bg-rose-950/80 text-rose-300 border-rose-500/40';
    }
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
            <Table className="w-4 h-4 text-amber-400" />
            STEP 1: Case Fact Matrix (Traceability & Evidentiary Discipline)
          </h3>
          <p className="text-xs text-slate-400">
            Every material factual assertion mapped to source documents, page numbers, and OCR status. Zero hallucinations permitted.
          </p>
        </div>
      </div>

      <div className="overflow-x-auto rounded-xl border border-legal-800 bg-[#0a0f1d] shadow-lg">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="border-b border-legal-800 bg-legal-900/90 text-slate-300 font-mono text-[11px] uppercase tracking-wider">
              <th className="py-3 px-4">Issue</th>
              <th className="py-3 px-4">Alleged Fact</th>
              <th className="py-3 px-4">Source Document & Reference</th>
              <th className="py-3 px-4">Evidence Strength</th>
              <th className="py-3 px-4">Contradiction / Conflict</th>
              <th className="py-3 px-4">Litigation Significance</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-legal-800/60 text-slate-200">
            {factMatrix.map((f, i) => (
              <tr key={f.id || i} className="hover:bg-legal-900/40 transition-colors">
                <td className="py-3 px-4 font-semibold text-amber-300 font-serif">
                  {f.issue}
                </td>
                <td className="py-3 px-4 leading-relaxed max-w-xs">
                  {f.allegedFact}
                </td>
                <td className="py-3 px-4 font-mono text-[11px]">
                  <div className="flex items-center gap-1.5 text-blue-300">
                    <FileText className="w-3.5 h-3.5 text-blue-400" />
                    <span>{f.sourceDocument}</span>
                  </div>
                  <div className="text-slate-400 text-[10px] mt-0.5">{f.pageParagraph}</div>
                  {f.ocrStatus && (
                    <span className="inline-block mt-1 text-[9px] px-1.5 py-0.5 rounded bg-legal-800/80 text-slate-400 border border-legal-700">
                      OCR: {f.ocrStatus}
                    </span>
                  )}
                </td>
                <td className="py-3 px-4">
                  <span className={`inline-flex items-center px-2 py-0.5 rounded text-[11px] font-mono border ${getStrengthBadge(f.evidenceStrength)}`}>
                    {f.evidenceStrength}
                  </span>
                </td>
                <td className="py-3 px-4 text-slate-300 max-w-xs leading-relaxed text-[11px]">
                  {f.contradiction}
                </td>
                <td className="py-3 px-4 text-slate-200 leading-relaxed font-medium text-[11px]">
                  {f.significance}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
"""

code_step2 = """'use client';

import React from 'react';
import { StatutoryParameter } from '@/types';
import { Scale, ShieldCheck, AlertTriangle, XCircle, HelpCircle } from 'lucide-react';

interface Step2Props {
  parameters: StatutoryParameter[];
}

export const Step2StatutoryEngineView: React.FC<Step2Props> = ({ parameters }) => {
  const getAssessmentPill = (status: string) => {
    switch (status) {
      case 'SATISFIED':
        return 'bg-emerald-950/80 text-emerald-300 border-emerald-500/50';
      case 'PARTIALLY SATISFIED':
        return 'bg-amber-950/80 text-amber-300 border-amber-500/50';
      case 'NOT SATISFIED':
        return 'bg-rose-950/80 text-rose-300 border-rose-500/50';
      default:
        return 'bg-slate-800 text-slate-300 border-slate-600';
    }
  };

  const getRiskBadge = (risk: string) => {
    switch (risk) {
      case 'LOW':
        return 'text-emerald-400 bg-emerald-950/60 border-emerald-800';
      case 'MEDIUM':
        return 'text-amber-400 bg-amber-950/60 border-amber-800';
      case 'HIGH':
        return 'text-orange-400 bg-orange-950/60 border-orange-800';
      case 'CRITICAL':
        return 'text-rose-400 bg-rose-950/60 border-rose-800';
      default:
        return 'text-slate-400 bg-slate-900 border-slate-700';
    }
  };

  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <Scale className="w-4 h-4 text-amber-400" />
          STEP 2: Statutory Parameter Engine (Section 16(2), 16C, 73/74, 155 Tests)
        </h3>
        <p className="text-xs text-slate-400">
          Conversion of Indian GST statutory mandates into operational legal parameters, burden-of-proof allocation, and required vs available evidence.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {parameters.map((p) => (
          <div key={p.id} className="legal-glass rounded-xl p-4 border border-legal-800 hover:border-legal-700 transition-all flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between gap-2 mb-2 pb-2 border-b border-legal-800/80">
                <div className="flex items-center gap-2">
                  <span className="font-mono font-bold text-xs px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 border border-amber-500/40">
                    {p.parameterCode}
                  </span>
                  <span className="font-serif font-bold text-sm text-white">{p.title}</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className={`text-[10px] font-mono font-bold px-2 py-0.5 rounded border ${getAssessmentPill(p.assessment)}`}>
                    {p.assessment}
                  </span>
                  <span className={`text-[10px] font-mono px-2 py-0.5 rounded border ${getRiskBadge(p.risk)}`}>
                    RISK: {p.risk}
                  </span>
                </div>
              </div>

              <div className="text-[11px] font-mono text-blue-300 mb-2">
                {p.statutoryProvision}
              </div>

              <div className="space-y-2 text-xs text-slate-300">
                <div>
                  <strong className="text-slate-400">Statutory Requirement:</strong>
                  <p className="text-slate-200 mt-0.5 leading-relaxed">{p.statutoryRequirement}</p>
                </div>
                <div>
                  <strong className="text-slate-400">Operational Legal Test:</strong>
                  <p className="text-amber-200/90 mt-0.5 leading-relaxed">{p.legalTest}</p>
                </div>
                <div>
                  <strong className="text-slate-400">Burden of Proof:</strong>
                  <p className="text-slate-300 mt-0.5 font-mono text-[11px]">{p.burdenOfProof}</p>
                </div>
                <div className="grid grid-cols-2 gap-2 pt-2 border-t border-legal-800/60">
                  <div>
                    <span className="text-[10px] font-mono text-slate-400 uppercase">Required Evidence</span>
                    <ul className="list-disc list-inside text-[11px] text-slate-300 mt-1 space-y-0.5">
                      {p.requiredEvidence.map((re, idx) => (
                        <li key={idx} className="truncate">{re}</li>
                      ))}
                    </ul>
                  </div>
                  <div>
                    <span className="text-[10px] font-mono text-emerald-400 uppercase">Available Evidence</span>
                    <ul className="list-disc list-inside text-[11px] text-emerald-200/90 mt-1 space-y-0.5">
                      {p.availableEvidence.map((ae, idx) => (
                        <li key={idx} className="truncate">{ae}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <div className="mt-3 pt-2.5 border-t border-legal-800/80 text-xs text-slate-400 bg-legal-950/40 p-2.5 rounded">
              <strong className="text-amber-400 font-mono text-[11px]">Assessment Rationale: </strong>
              {p.reason}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

code_step3 = """'use client';

import React from 'react';
import { PrecedentAnalysis } from '@/types';
import { BookOpen, Award, CheckCircle2, ShieldCheck, Scale } from 'lucide-react';

interface Step3Props {
  precedents: PrecedentAnalysis[];
}

export const Step3Step4PrecedentsView: React.FC<Step3Props> = ({ precedents }) => {
  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <BookOpen className="w-4 h-4 text-amber-400" />
          STEPS 3 & 4: Precedent Parameter Engine & Comparability Scoring (0–100)
        </h3>
        <p className="text-xs text-slate-400">
          Rigorous analysis of controlling judgments (Suncraft, D.Y. Beathel, Arise India, LGW Industries) with objective comparability scoring.
        </p>
      </div>

      <div className="space-y-4">
        {precedents.map((p) => {
          const comp = p.comparabilityScore;
          return (
            <div key={p.id} className="legal-glass rounded-xl p-5 border border-legal-800 shadow-xl">
              <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-3 pb-3 border-b border-legal-800">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="font-serif font-bold text-base text-amber-300">{p.caseName}</span>
                  </div>
                  <div className="text-xs font-mono text-slate-400 flex flex-wrap items-center gap-3">
                    <span className="text-blue-400 font-semibold">{p.court}</span>
                    <span>•</span>
                    <span className="text-slate-300">{p.citation}</span>
                    <span>•</span>
                    <span className="text-purple-400">{p.relevantProvision}</span>
                  </div>
                </div>

                {/* Comparability Score Card */}
                <div className="bg-legal-900/90 border border-amber-500/40 rounded-xl p-3 text-center min-w-[140px] shadow-lg">
                  <div className="text-[10px] font-mono uppercase tracking-wider text-amber-400/90 font-bold">Comparability</div>
                  <div className="text-2xl font-mono font-extrabold text-amber-300">
                    {comp.totalScore}<span className="text-xs text-slate-500">/100</span>
                  </div>
                  <div className="text-[10px] font-mono text-emerald-400 font-semibold mt-0.5">
                    {p.favourableApplicability === 'HIGH' ? 'Directly Controlling' : 'Persuasive'}
                  </div>
                </div>
              </div>

              {/* Ratio Decidendi & Legal Principle */}
              <div className="mt-3 bg-legal-950/70 p-3.5 rounded-lg border border-legal-800">
                <div className="text-[11px] font-mono text-amber-400 uppercase tracking-wider font-bold mb-1">
                  Ratio Decidendi / Legal Principle:
                </div>
                <p className="text-xs text-slate-200 leading-relaxed font-serif italic">
                  "{p.ratioLegalPrinciple}"
                </p>
              </div>

              {/* Conditions & Operational Deployment */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-3 text-xs">
                <div className="bg-legal-900/50 p-3 rounded-lg border border-legal-800/60">
                  <strong className="text-slate-300 font-mono text-[11px]">Necessary Conditions for Application:</strong>
                  <ul className="list-disc list-inside text-slate-300 mt-1.5 space-y-1">
                    {p.necessaryConditions.map((nc, idx) => (
                      <li key={idx} className="leading-tight">{nc}</li>
                    ))}
                  </ul>
                </div>
                <div className="bg-legal-900/50 p-3 rounded-lg border border-legal-800/60">
                  <strong className="text-slate-300 font-mono text-[11px]">Tactical Appellate Deployment:</strong>
                  <p className="text-slate-300 mt-1.5 leading-relaxed">{p.litigationUse}</p>
                </div>
              </div>

              {/* Comparability Dimension Breakdown */}
              <div className="mt-3 pt-3 border-t border-legal-800/80">
                <div className="text-[10px] font-mono text-slate-400 uppercase mb-2">Comparability Score Breakdown:</div>
                <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2 text-center text-xs font-mono">
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Statutory</div>
                    <div className="text-amber-400 font-bold">{comp.statutorySimilarity}/20</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Factual</div>
                    <div className="text-amber-400 font-bold">{comp.factualSimilarity}/25</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Evidentiary</div>
                    <div className="text-amber-400 font-bold">{comp.evidentiarySimilarity}/20</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Procedural</div>
                    <div className="text-amber-400 font-bold">{comp.proceduralSimilarity}/10</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Forum Binding</div>
                    <div className="text-amber-400 font-bold">{comp.courtAuthorityRelevance}/15</div>
                  </div>
                  <div className="bg-legal-950 p-2 rounded border border-legal-800">
                    <div className="text-slate-400 text-[10px]">Distinction Risk</div>
                    <div className="text-emerald-400 font-bold">{comp.distinguishabilityRisk}/10</div>
                  </div>
                </div>
                <p className="text-[11px] text-slate-400 mt-2 italic">
                  <strong className="text-slate-300">Scoring Note:</strong> {comp.explanation}
                </p>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
"""

code_step5 = """'use client';

import React from 'react';
import { LowerAuthorityError } from '@/types';
import { AlertOctagon, ShieldAlert, Gavel } from 'lucide-react';

interface Step5Props {
  errors: LowerAuthorityError[];
}

export const Step5LowerAuthorityErrorsView: React.FC<Step5Props> = ({ errors }) => {
  const getSeverityBadge = (strength: string) => {
    switch (strength) {
      case 'Fundamental':
        return 'bg-rose-950/80 text-rose-300 border-rose-500/50';
      case 'Serious':
        return 'bg-orange-950/80 text-orange-300 border-orange-500/50';
      case 'Material':
        return 'bg-amber-950/80 text-amber-300 border-amber-500/50';
      default:
        return 'bg-blue-950/80 text-blue-300 border-blue-500/50';
    }
  };

  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-base font-serif font-bold text-white flex items-center gap-2">
          <AlertOctagon className="w-4 h-4 text-rose-400" />
          STEP 5: Lower Authority Error Analysis & Defect Matrix
        </h3>
        <p className="text-xs text-slate-400">
          Identification of jurisdictional flaws, ignored documentary evidence, statutory misconstructions, and natural justice violations.
        </p>
      </div>

      <div className="space-y-3">
        {errors.map((e) => (
          <div key={e.id} className="legal-glass rounded-xl p-4 border border-legal-800 hover:border-rose-500/40 transition-all">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-2.5 border-b border-legal-800">
              <div className="font-serif font-bold text-sm text-white flex items-center gap-2">
                <Gavel className="w-4 h-4 text-rose-400 flex-shrink-0" />
                <span>{e.finding}</span>
              </div>
              <span className={`px-2.5 py-0.5 rounded text-[11px] font-mono font-bold border ${getSeverityBadge(e.strength)}`}>
                {e.strength} Error
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 text-xs">
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800/80">
                <strong className="text-slate-400 font-mono text-[10px] uppercase">Lower Authority Reasoning:</strong>
                <p className="text-slate-300 mt-1 leading-relaxed">{e.lowerAuthorityReasoning}</p>
              </div>
              <div className="bg-legal-950/60 p-3 rounded border border-legal-800/80">
                <strong className="text-amber-400 font-mono text-[10px] uppercase">Evidence Ignored / Misread:</strong>
                <p className="text-amber-200/90 mt-1 leading-relaxed">{e.evidenceIgnoredMisread}</p>
              </div>
            </div>

            <div className="mt-3 pt-2.5 border-t border-legal-800/60 flex flex-col sm:flex-row justify-between gap-2 text-xs">
              <div className="text-rose-300">
                <strong className="text-slate-400">Legal Error: </strong>
                {e.legalError}
              </div>
              <div className="font-mono text-blue-300 text-[11px] flex-shrink-0">
                <strong className="text-slate-400">Counter Authority: </strong>
                {e.relevantAuthority}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

os.makedirs("src/components/steps", exist_ok=True)
with open("src/components/steps/Step1FactMatrixView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step1)
with open("src/components/steps/Step2StatutoryEngineView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step2)
with open("src/components/steps/Step3Step4PrecedentsView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step3)
with open("src/components/steps/Step5LowerAuthorityErrorsView.tsx", "w", encoding="utf-8") as f:
    f.write(code_step5)

print("Wrote Step Views 1 to 5 successfully!")