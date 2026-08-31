'use client';

import React, { useState } from 'react';
import { X, Scale, PlusCircle } from 'lucide-react';
import { CaseStudy } from '../types';

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
  const [disputedAmount, setDisputedAmount] = useState('INR 50,00,000 + Penalty');
  const [noticeType, setNoticeType] = useState<'SCN / DRC-01' | 'Order-in-Original / DRC-07' | 'First Appeal / APL-01' | 'High Court Writ Petition'>('Order-in-Original / DRC-07');
  const [primaryIssue, setPrimaryIssue] = useState('Section 16(2)(c) GSTR-2A vs 3B mismatch without action on supplier.');
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
      disputedAmount,
      noticeType,
      primaryIssue,
      caseSummary: caseSummary || `${title} - Disputed amount of ${disputedAmount} for FY ${financialYear}.`
    });

    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 overflow-y-auto">
      <div className="bg-[#0c1322] border border-legal-700 rounded-2xl w-full max-w-2xl shadow-2xl p-6 relative my-8">
        <button
          onClick={onClose}
          className="absolute top-5 right-5 text-slate-400 hover:text-white transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-2 mb-4 pb-3 border-b border-legal-800">
          <Scale className="w-5 h-5 text-amber-400" />
          <div>
            <h3 className="text-lg font-serif font-bold text-white">Create New Legal Assessment</h3>
            <p className="text-xs text-slate-400">Initialize a 13-step statutory & judicial precedent evaluation for a GST matter.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-3.5 text-xs">
          <div>
            <label className="block text-slate-300 mb-1 font-medium">Matter / Case Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. Disallowance of ITC on Supplier GSTR-3B Default"
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
            <label className="block text-slate-300 mb-1 font-medium">Factual Narrative & Ground Summary</label>
            <textarea
              rows={3}
              value={caseSummary}
              onChange={(e) => setCaseSummary(e.target.value)}
              placeholder="Brief details of transaction, invoices, bank payments, and departmental allegation..."
              className="w-full bg-legal-950 border border-legal-700 rounded-lg p-3 text-slate-200 focus:outline-none focus:border-amber-400 leading-relaxed"
            />
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
              <span>Run 13-Step Evaluation</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
