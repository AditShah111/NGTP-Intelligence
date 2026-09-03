'use client';

import React, { useState } from 'react';
import { X, Scale, CheckCircle2 } from 'lucide-react';

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

  if (!isOpen) return null;

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
      caseSummary: caseSummary || `${title} - NGTP Assessment for ${taxpayerName} (FY ${financialYear}).`
    });

    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4 overflow-y-auto">
      <div className="bg-white border border-beige-300 rounded-2xl w-full max-w-2xl shadow-2xl p-6 relative my-8 max-h-[90vh] overflow-y-auto">
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
            <h3 className="text-lg font-serif font-bold text-slate-900">Create New NGTP Assessment</h3>
            <p className="text-xs text-slate-500">Initialize matter master data. Evidence & submissions are attached in the main workspace.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4 text-xs">
          <div>
            <label className="block text-slate-700 mb-1 font-semibold">Matter / Assessment Title</label>
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
            <label className="block text-slate-700 mb-1 font-semibold">Primary NGTP Legal Issue</label>
            <input
              type="text"
              value={primaryIssue}
              onChange={(e) => setPrimaryIssue(e.target.value)}
              placeholder="e.g. Recovery from recipient under Sec 16(2)(c) without pursuing supplier"
              className="w-full bg-beige-50 border border-beige-300 rounded-lg px-3 py-2 text-slate-900 focus:outline-none focus:border-amber-600"
            />
          </div>

          <div>
            <label className="block text-slate-700 mb-1 font-semibold">Matter Brief / Ground Narrative</label>
            <textarea
              rows={3}
              value={caseSummary}
              onChange={(e) => setCaseSummary(e.target.value)}
              placeholder="Brief summary of the matter, supplier details, or departmental allegations..."
              className="w-full bg-beige-50 border border-beige-300 rounded-lg p-3 text-slate-900 focus:outline-none focus:border-amber-600 leading-relaxed"
            />
          </div>

          <div className="p-3 rounded-xl bg-amber-50/70 border border-amber-200/80 text-[11px] text-amber-900 font-sans leading-relaxed">
            💡 <strong>Next Step:</strong> Submitting this form initializes your master data on the workspace. You will attach written submissions and documentary evidence on the main screen, then run the 13-step evaluation once with full evidence.
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
              className="flex items-center gap-1.5 px-5 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-white font-semibold transition-colors shadow-sm"
            >
              <CheckCircle2 className="w-4 h-4 text-emerald-400" />
              <span>Create Assessment Workspace</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};