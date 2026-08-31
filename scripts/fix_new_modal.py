code_new_modal = """'use client';

import React, { useState, useRef } from 'react';
import { X, Scale, PlusCircle, Upload, FileText, AlertTriangle, CheckCircle2, Loader2 } from 'lucide-react';
import { CaseDocument } from '../types';

interface NewCaseModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmitNewCase: (data: {
    title: string;
    taxpayerName: string;
    gstin: string;
    financialYear: string;
    disputedAmount: string;
    noticeType: 'SCN / DRC-01' | 'Order-in-Original / DRC-07' | 'First Appeal / APL-01' | 'High Court Writ Petition';
    primaryIssue: string;
    caseSummary: string;
    documents: CaseDocument[];
  }) => void;
}

export const NewCaseModal: React.FC<NewCaseModalProps> = ({
  isOpen,
  onClose,
  onSubmitNewCase
}) => {
  const [title, setTitle] = useState('');
  const [taxpayerName, setTaxpayerName] = useState('');
  const [gstin, setGstin] = useState('');
  const [financialYear, setFinancialYear] = useState('2018-19');
  const [disputedAmount, setDisputedAmount] = useState('');
  const [noticeType, setNoticeType] = useState<'SCN / DRC-01' | 'Order-in-Original / DRC-07' | 'First Appeal / APL-01' | 'High Court Writ Petition'>('Order-in-Original / DRC-07');
  const [primaryIssue, setPrimaryIssue] = useState('Section 16(2)(c) GSTR-2A vs 3B mismatch without action on supplier');
  const [caseSummary, setCaseSummary] = useState('');
  
  const [attachedDocs, setAttachedDocs] = useState<CaseDocument[]>([]);
  const [isExtracting, setIsExtracting] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  if (!isOpen) return null;

  const handleFileUpload = async (files: FileList | null) => {
    if (!files || files.length === 0) return;
    setIsExtracting(true);
    try {
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        let text = '';
        if (file.type.includes('text') || file.name.endsWith('.txt') || file.name.endsWith('.csv')) {
          text = await file.text();
        } else {
          const buffer = await file.arrayBuffer();
          const decoder = new TextDecoder('utf-8', { fatal: false });
          text = decoder.decode(buffer).replace(/[\\x00-\\x08\\x0B\\x0C\\x0E-\\x1F\\x7F-\\x9F]/g, ' ').replace(/\\s+/g, ' ').slice(0, 3000);
        }

        const lower = (file.name + ' ' + text).toLowerCase();
        let determinedType: CaseDocument['type'] = 'Other';
        if (lower.includes('invoice') || lower.includes('bill')) determinedType = 'Invoice';
        else if (lower.includes('bank') || lower.includes('rtgs') || lower.includes('neft')) determinedType = 'Bank Statement';
        else if (lower.includes('e-way') || lower.includes('eway') || lower.includes('transit')) determinedType = 'E-Way Bill';
        else if (lower.includes('drc-07') || lower.includes('order')) determinedType = 'DRC-07';
        else if (lower.includes('scn') || lower.includes('drc-01')) determinedType = 'SCN';

        const newDoc: CaseDocument = {
          id: `doc-${Date.now()}-${i}`,
          name: file.name,
          type: determinedType,
          fileSize: `${(file.size / 1024).toFixed(1)} KB`,
          uploadedAt: new Date().toISOString().split('T')[0],
          ocrReadability: text.length > 50 ? 'Clearly readable text' : 'Uncertain OCR text',
          extractedTextSnippet: text.slice(0, 800) || `Uploaded file ${file.name}`
        };

        setAttachedDocs(prev => [...prev, newDoc]);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setIsExtracting(false);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title || !taxpayerName || !gstin) return;

    onSubmitNewCase({
      title,
      taxpayerName,
      gstin,
      financialYear,
      disputedAmount: disputedAmount || 'INR 0 (Unspecified)',
      noticeType,
      primaryIssue,
      caseSummary: caseSummary || `${title} - Assessment for ${taxpayerName} (FY ${financialYear}).`,
      documents: attachedDocs
    });

    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 overflow-y-auto">
      <div className="bg-[#0c1322] border border-legal-700 rounded-2xl w-full max-w-3xl shadow-2xl p-6 relative my-8 max-h-[90vh] overflow-y-auto">
        <button
          onClick={onClose}
          className="absolute top-5 right-5 text-slate-400 hover:text-white transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-2 mb-4 pb-3 border-b border-legal-800">
          <Scale className="w-5 h-5 text-amber-400" />
          <div>
            <h3 className="text-lg font-serif font-bold text-white">Create Rigorous Legal Assessment</h3>
            <p className="text-xs text-slate-400">Initialize a 13-step statutory evaluation. Upload real evidence to avoid score disqualification.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-3.5 text-xs">
          <div>
            <label className="block text-slate-300 mb-1 font-medium">Matter / Case Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. SCN Disallowance under Section 16(2)(c)"
              className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
              required
            />
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-300 mb-1 font-medium">Taxpayer Legal Name</label>
              <input
                type="text"
                value={taxpayerName}
                onChange={(e) => setTaxpayerName(e.target.value)}
                placeholder="e.g. Zenith Tech Industries Ltd"
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
                required
              />
            </div>
            <div>
              <label className="block text-slate-300 mb-1 font-medium">GSTIN (15 Digits)</label>
              <input
                type="text"
                value={gstin}
                onChange={(e) => setGstin(e.target.value)}
                placeholder="e.g. 27AAACZ1234F1Z0"
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400 font-mono"
                required
              />
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div>
              <label className="block text-slate-300 mb-1 font-medium">Financial Year</label>
              <select
                value={financialYear}
                onChange={(e) => setFinancialYear(e.target.value)}
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
              >
                <option value="2017-18">2017-18</option>
                <option value="2018-19">2018-19</option>
                <option value="2019-20">2019-20</option>
                <option value="2020-21">2020-21</option>
                <option value="2021-22">2021-22</option>
                <option value="2022-23">2022-23</option>
                <option value="2023-24">2023-24</option>
              </select>
            </div>
            <div>
              <label className="block text-slate-300 mb-1 font-medium">Disputed Amount</label>
              <input
                type="text"
                value={disputedAmount}
                onChange={(e) => setDisputedAmount(e.target.value)}
                placeholder="e.g. INR 45,00,000"
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400 font-mono"
              />
            </div>
            <div>
              <label className="block text-slate-300 mb-1 font-medium">Stage / Notice Type</label>
              <select
                value={noticeType}
                onChange={(e) => setNoticeType(e.target.value as any)}
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
              >
                <option value="SCN / DRC-01">SCN / DRC-01</option>
                <option value="Order-in-Original / DRC-07">Order-in-Original / DRC-07</option>
                <option value="First Appeal / APL-01">First Appeal / APL-01</option>
                <option value="High Court Writ Petition">High Court Writ Petition</option>
              </select>
            </div>
          </div>

          <div>
            <label className="block text-slate-300 mb-1 font-medium">Primary Legal Issue</label>
            <input
              type="text"
              value={primaryIssue}
              onChange={(e) => setPrimaryIssue(e.target.value)}
              placeholder="e.g. Recovery from recipient under Sec 16(2)(c) without pursuing supplier"
              className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
            />
          </div>

          <div>
            <label className="block text-slate-300 mb-1 font-medium">Factual Summary / Ground Narrative</label>
            <textarea
              rows={2}
              value={caseSummary}
              onChange={(e) => setCaseSummary(e.target.value)}
              placeholder="Brief details of the transactions, supplier status, and impugned departmental demand..."
              className="w-full bg-legal-950 border border-legal-700 rounded-lg p-3 text-slate-200 focus:outline-none focus:border-amber-400 leading-relaxed"
            />
          </div>

          <div className="pt-2 border-t border-legal-800">
            <label className="block text-amber-300 font-semibold mb-1">
              Attach Real Evidence Files (Invoices, SCN, Bank Statements, E-Way bills)
            </label>
            <div
              onClick={() => fileInputRef.current?.click()}
              className="border-2 border-dashed border-legal-700 hover:border-amber-400 bg-legal-950 p-4 rounded-xl text-center cursor-pointer transition-all"
            >
              <input
                type="file"
                ref={fileInputRef}
                onChange={(e) => handleFileUpload(e.target.files)}
                multiple
                accept=".pdf,.png,.jpg,.jpeg,.txt,.csv,.json,.doc,.docx"
                className="hidden"
              />
              {isExtracting ? (
                <div className="flex items-center justify-center gap-2 text-amber-400">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Extracting document text...</span>
                </div>
              ) : (
                <div className="flex flex-col items-center justify-center space-y-1">
                  <Upload className="w-5 h-5 text-amber-400" />
                  <span className="text-slate-300 font-medium">Click to attach real PDF / Invoices / Bank Proof</span>
                  <span className="text-[10px] text-slate-500">Without files, case will be marked as "Unsupported / Insufficient Evidence"</span>
                </div>
              )}
            </div>

            {attachedDocs.length > 0 && (
              <div className="mt-2 space-y-1.5">
                {attachedDocs.map((doc, idx) => (
                  <div key={idx} className="flex items-center justify-between p-2 rounded bg-legal-900 border border-legal-800 text-[11px]">
                    <span className="text-slate-200 font-mono font-semibold">{doc.name} ({doc.type})</span>
                    <span className="text-emerald-400 font-mono">{doc.fileSize}</span>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="flex justify-end gap-2 pt-3 border-t border-legal-800">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-lg bg-legal-800 text-slate-300 hover:bg-legal-700 transition-colors"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="flex items-center gap-1.5 px-4 py-2 rounded-lg bg-amber-500 hover:bg-amber-400 text-black font-semibold transition-colors"
            >
              <PlusCircle className="w-4 h-4" />
              <span>Run Strict 13-Step Evaluation</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
"""

with open("src/components/NewCaseModal.tsx", "w", encoding="utf-8") as f:
    f.write(code_new_modal)
print("Updated NewCaseModal.tsx")