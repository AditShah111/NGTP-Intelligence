new_case_modal = """'use client';

import React, { useState, useRef } from 'react';
import { X, Scale, PlusCircle, Upload, FileText, AlertTriangle, CheckCircle2, Loader2, Plus, Trash2 } from 'lucide-react';
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
  const [selectedDocType, setSelectedDocType] = useState<CaseDocument['type']>('Invoice');
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
          text = `Attached file ${file.name} (Size: ${(file.size / 1024).toFixed(1)} KB)`;
        }

        const newDoc: CaseDocument = {
          id: `doc-${Date.now()}-${i}`,
          name: file.name,
          type: selectedDocType,
          fileSize: `${(file.size / 1024).toFixed(1)} KB`,
          uploadedAt: new Date().toISOString().split('T')[0],
          ocrReadability: 'Clearly readable text',
          extractedTextSnippet: text.slice(0, 800)
        };

        setAttachedDocs(prev => [...prev, newDoc]);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setIsExtracting(false);
      if (fileInputRef.current) fileInputRef.current.value = '';
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
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4 overflow-y-auto">
      <div className="bg-white border border-beige-300 rounded-2xl w-full max-w-3xl shadow-2xl p-6 relative my-8 max-h-[90vh] overflow-y-auto">
        <button
          onClick={onClose}
          className="absolute top-5 right-5 text-slate-400 hover:text-slate-700 transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-2.5 mb-4 pb-3 border-b border-beige-200">
          <div className="p-2 rounded-xl bg-amber-50 text-amber-700">
            <Scale className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-lg font-serif font-bold text-slate-900">Create Rigorous Legal Assessment</h3>
            <p className="text-xs text-slate-500">Initialize a 13-step statutory evaluation. Upload real evidence to avoid score disqualification.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-3.5 text-xs">
          <div>
            <label className="block text-slate-700 mb-1 font-semibold">Matter / Case Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. SCN Disallowance under Section 16(2)(c)"
              className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600 font-medium"
              required
            />
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-700 mb-1 font-semibold">Taxpayer Legal Name</label>
              <input
                type="text"
                value={taxpayerName}
                onChange={(e) => setTaxpayerName(e.target.value)}
                placeholder="e.g. Zenith Tech Industries Ltd"
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600 font-medium"
                required
              />
            </div>
            <div>
              <label className="block text-slate-700 mb-1 font-semibold">GSTIN (15 Digits)</label>
              <input
                type="text"
                value={gstin}
                onChange={(e) => setGstin(e.target.value)}
                placeholder="e.g. 27AAACZ1234F1Z0"
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600 font-mono"
                required
              />
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div>
              <label className="block text-slate-700 mb-1 font-semibold">Financial Year</label>
              <select
                value={financialYear}
                onChange={(e) => setFinancialYear(e.target.value)}
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600 font-medium"
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
              <label className="block text-slate-700 mb-1 font-semibold">Disputed Amount</label>
              <input
                type="text"
                value={disputedAmount}
                onChange={(e) => setDisputedAmount(e.target.value)}
                placeholder="e.g. INR 45,00,000"
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600 font-mono"
              />
            </div>
            <div>
              <label className="block text-slate-700 mb-1 font-semibold">Stage / Notice Type</label>
              <select
                value={noticeType}
                onChange={(e) => setNoticeType(e.target.value as any)}
                className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600 font-medium"
              >
                <option value="SCN / DRC-01">SCN / DRC-01</option>
                <option value="Order-in-Original / DRC-07">Order-in-Original / DRC-07</option>
                <option value="First Appeal / APL-01">First Appeal / APL-01</option>
                <option value="High Court Writ Petition">High Court Writ Petition</option>
              </select>
            </div>
          </div>

          <div>
            <label className="block text-slate-700 mb-1 font-semibold">Primary Legal Issue</label>
            <input
              type="text"
              value={primaryIssue}
              onChange={(e) => setPrimaryIssue(e.target.value)}
              placeholder="e.g. Recovery from recipient under Sec 16(2)(c) without pursuing supplier"
              className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600"
            />
          </div>

          <div>
            <label className="block text-slate-700 mb-1 font-semibold">Factual Summary / Ground Narrative</label>
            <textarea
              rows={2}
              value={caseSummary}
              onChange={(e) => setCaseSummary(e.target.value)}
              placeholder="Brief details of the transactions, supplier status, and impugned departmental demand..."
              className="w-full bg-beige-50 border border-beige-300 rounded-lg p-3 text-slate-900 focus:outline-none focus:border-amber-600 leading-relaxed"
            />
          </div>

          {/* Document Upload Dropzone */}
          <div className="pt-2 border-t border-beige-200">
            <div className="flex items-center justify-between mb-1.5">
              <label className="block text-amber-900 font-semibold">
                Attach Evidence Files:
              </label>
              <select
                value={selectedDocType}
                onChange={(e) => setSelectedDocType(e.target.value as any)}
                className="bg-beige-50 border border-beige-300 rounded px-2 py-1 text-[11px] font-semibold text-slate-800"
              >
                <option value="Invoice">Tax Invoices</option>
                <option value="Bank Statement">Bank Statement / RTGS Voucher</option>
                <option value="E-Way Bill">E-Way Bills / Transit</option>
                <option value="SCN">SCN / DRC-01 Notice</option>
                <option value="DRC-07">Order-in-Original (DRC-07)</option>
                <option value="CA Certificate">Circular 183 CA Certificate</option>
              </select>
            </div>

            <div
              onClick={() => fileInputRef.current?.click()}
              className="border-2 border-dashed border-beige-300 hover:border-amber-600 bg-beige-50 p-4 rounded-xl text-center cursor-pointer transition-all"
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
                <div className="flex items-center justify-center gap-2 text-amber-700">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span className="font-semibold">Attaching document...</span>
                </div>
              ) : (
                <div className="flex flex-col items-center justify-center space-y-1">
                  <Upload className="w-5 h-5 text-amber-700" />
                  <span className="text-slate-800 font-medium">Click to attach as {selectedDocType}</span>
                  <span className="text-[10px] text-slate-500">Attach Invoices + Bank Statements to unlock Suncraft scores</span>
                </div>
              )}
            </div>

            {/* Attached files preview */}
            {attachedDocs.length > 0 && (
              <div className="mt-2 space-y-1.5 max-h-32 overflow-y-auto">
                {attachedDocs.map((doc, idx) => (
                  <div key={idx} className="flex items-center justify-between p-2 rounded-lg bg-beige-50 border border-beige-200 text-[11px]">
                    <span className="text-slate-800 font-mono font-semibold">{doc.name} ({doc.type})</span>
                    <button
                      type="button"
                      onClick={() => setAttachedDocs(prev => prev.filter((_, i) => i !== idx))}
                      className="text-slate-400 hover:text-rose-600"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="flex justify-end gap-2 pt-3 border-t border-beige-200">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-lg bg-beige-100 text-slate-700 hover:bg-beige-200 font-medium transition-colors"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="flex items-center gap-1.5 px-4 py-2 rounded-lg bg-amber-600 hover:bg-amber-700 text-white font-semibold transition-colors shadow-sm"
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
    f.write(new_case_modal)
print("Updated NewCaseModal.tsx successfully!")