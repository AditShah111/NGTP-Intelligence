import os

# Step 1: Fact Matrix
s1 = """'use client';

import React from 'react';
import { FactMatrixItem } from '../../types';
import { CheckCircle2, AlertTriangle, HelpCircle, FileText, Sparkles, ShieldCheck } from 'lucide-react';

interface Props {
  factMatrix: FactMatrixItem[];
}

export const Step1FactMatrixView: React.FC<Props> = ({ factMatrix }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 1: Fact Matrix & Evidence Traceability</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Auditing every material factual proposition against attached documentary proof and OCR tokens.
            </p>
          </div>
          <span className="text-xs font-mono px-3 py-1 rounded-full bg-amber-50 text-amber-900 border border-amber-200 font-semibold">
            {factMatrix.length} Core Propositions Audited
          </span>
        </div>

        <div className="mt-6 overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-beige-200 bg-beige-50/80 text-slate-700 font-mono">
                <th className="py-3 px-4 font-semibold">Legal Proposition / Issue</th>
                <th className="py-3 px-4 font-semibold">Alleged Fact on Record</th>
                <th className="py-3 px-4 font-semibold">Source Document & OCR</th>
                <th className="py-3 px-4 font-semibold">Evidence Strength</th>
                <th className="py-3 px-4 font-semibold">Audit Finding & Significance</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-beige-200">
              {factMatrix.map((item) => (
                <tr key={item.id} className="hover:bg-beige-50/50 transition-colors">
                  <td className="py-4 px-4 font-semibold text-slate-900 align-top max-w-[220px]">
                    {item.issue}
                  </td>
                  <td className="py-4 px-4 text-slate-700 align-top leading-relaxed max-w-[260px]">
                    {item.allegedFact}
                  </td>
                  <td className="py-4 px-4 align-top max-w-[180px]">
                    <div className="font-mono text-slate-800 font-medium">{item.sourceDocument}</div>
                    <div className="text-[11px] text-slate-500 mt-0.5">{item.pageParagraph}</div>
                    {item.ocrStatus && (
                      <span className={`inline-block mt-1.5 text-[10px] font-mono px-2 py-0.5 rounded border ${
                        item.ocrStatus === 'Clearly readable text' 
                          ? 'bg-emerald-50 text-emerald-800 border-emerald-200' 
                          : 'bg-rose-50 text-rose-800 border-rose-200'
                      }`}>
                        {item.ocrStatus}
                      </span>
                    )}
                  </td>
                  <td className="py-4 px-4 align-top whitespace-nowrap">
                    <span className={`inline-flex items-center gap-1 text-[11px] font-semibold px-2.5 py-1 rounded-full border ${
                      item.evidenceStrength === 'Established' 
                        ? 'bg-emerald-50 text-emerald-800 border-emerald-200' :
                      item.evidenceStrength === 'Strongly supported' 
                        ? 'bg-blue-50 text-blue-800 border-blue-200' :
                      item.evidenceStrength === 'Disputed' 
                        ? 'bg-amber-50 text-amber-800 border-amber-200' :
                        'bg-rose-50 text-rose-800 border-rose-200'
                    }`}>
                      {item.evidenceStrength === 'Established' && <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />}
                      {item.evidenceStrength === 'Unsupported' && <AlertTriangle className="w-3.5 h-3.5 text-rose-600" />}
                      {item.evidenceStrength}
                    </span>
                  </td>
                  <td className="py-4 px-4 text-slate-700 align-top max-w-[260px] leading-relaxed">
                    <div className="font-medium text-slate-900">{item.significance}</div>
                    <div className="text-[11px] text-rose-700 mt-1 italic">{item.contradiction}</div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
"""
with open("src/components/steps/Step1FactMatrixView.tsx", "w", encoding="utf-8") as f:
    f.write(s1)

# Step 2: Statutory Tests
s2 = """'use client';

import React from 'react';
import { StatutoryParameter } from '../../types';
import { ShieldCheck, AlertTriangle, XCircle, CheckCircle2, BookOpen } from 'lucide-react';

interface Props {
  parameters: StatutoryParameter[];
}

export const Step2StatutoryEngineView: React.FC<Props> = ({ parameters }) => {
  return (
    <div className="space-y-6">
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex items-center justify-between pb-4 border-b border-beige-200">
          <div>
            <h3 className="text-xl font-serif font-bold text-slate-900">Step 2: Statutory Parameter & Legal Burden Engine (P1–P8)</h3>
            <p className="text-xs text-slate-600 mt-0.5">
              Evaluating mandatory statutory conditions under Section 16(2), Section 74, and Section 155 of the CGST Act.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          {parameters.map((param) => {
            const isSatisfied = param.assessment === 'SATISFIED';
            const isCritical = param.risk === 'CRITICAL' || param.risk === 'HIGH';

            return (
              <div
                key={param.id}
                className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between gap-2 mb-3">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-900 border border-amber-200">
                        {param.parameterCode}
                      </span>
                      <h4 className="font-serif font-bold text-sm text-slate-900">{param.title}</h4>
                    </div>
                    <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full border ${
                      isSatisfied 
                        ? 'bg-emerald-50 text-emerald-800 border-emerald-200' :
                      param.assessment === 'PARTIALLY SATISFIED' 
                        ? 'bg-amber-50 text-amber-800 border-amber-200' :
                        'bg-rose-50 text-rose-800 border-rose-200'
                    }`}>
                      {param.assessment}
                    </span>
                  </div>

                  <div className="text-xs space-y-2 mb-4">
                    <div>
                      <span className="text-slate-500 font-mono text-[11px] uppercase">Provision: </span>
                      <span className="font-semibold text-slate-800">{param.statutoryProvision}</span>
                    </div>
                    <p className="text-slate-700 leading-relaxed text-xs">
                      {param.statutoryRequirement}
                    </p>
                    <div className="bg-white p-2.5 rounded-lg border border-beige-200 text-[11px] text-slate-700">
                      <strong className="text-slate-900">Legal Test:</strong> {param.legalTest}
                    </div>
                  </div>
                </div>

                <div className="pt-3 border-t border-beige-200 flex items-center justify-between text-xs">
                  <span className="text-slate-500 font-mono text-[11px]">
                    Burden: <strong className="text-slate-800">{param.burdenOfProof}</strong>
                  </span>
                  <span className={`font-mono text-[11px] font-semibold ${
                    isCritical ? 'text-rose-700' : 'text-emerald-700'
                  }`}>
                    Risk: {param.risk}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
"""
with open("src/components/steps/Step2StatutoryEngineView.tsx", "w", encoding="utf-8") as f:
    f.write(s2)

print("Step 1 & Step 2 rethemed.")