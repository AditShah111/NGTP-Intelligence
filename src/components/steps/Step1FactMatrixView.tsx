'use client';

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
