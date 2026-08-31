'use client';

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
