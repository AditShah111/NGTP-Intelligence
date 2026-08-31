'use client';

import React from 'react';
import { StatutoryParameter } from '../../types';
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
