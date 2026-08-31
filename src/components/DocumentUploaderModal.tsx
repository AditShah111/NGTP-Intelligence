'use client';

import React, { useState } from 'react';
import { X, Upload, FileText, CheckCircle2, AlertTriangle, Trash2, Eye } from 'lucide-react';
import { CaseDocument, OcrReadability } from '../types';

interface DocumentUploaderModalProps {
  isOpen: boolean;
  onClose: () => void;
  documents: CaseDocument[];
  onAddDocument: (doc: CaseDocument) => void;
  onRemoveDocument: (id: string) => void;
}

export const DocumentUploaderModal: React.FC<DocumentUploaderModalProps> = ({
  isOpen,
  onClose,
  documents,
  onAddDocument,
  onRemoveDocument
}) => {
  const [docName, setDocName] = useState('');
  const [docType, setDocType] = useState<CaseDocument['type']>('SCN');
  const [ocrStatus, setOcrStatus] = useState<OcrReadability>('Clearly readable text');
  const [snippet, setSnippet] = useState('');

  if (!isOpen) return null;

  const handleAdd = (e: React.FormEvent) => {
    e.preventDefault();
    if (!docName.trim()) return;

    const newDoc: CaseDocument = {
      id: `doc-${Date.now()}`,
      name: docName,
      type: docType,
      fileSize: '1.2 MB',
      uploadedAt: new Date().toISOString().split('T')[0],
      ocrReadability: ocrStatus,
      extractedTextSnippet: snippet || 'Document text extracted and indexed.'
    };

    onAddDocument(newDoc);
    setDocName('');
    setSnippet('');
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 overflow-y-auto">
      <div className="bg-[#0c1322] border border-legal-700 rounded-2xl w-full max-w-3xl shadow-2xl p-6 relative my-8">
        <button
          onClick={onClose}
          className="absolute top-5 right-5 text-slate-400 hover:text-white transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-2 mb-4 pb-3 border-b border-legal-800">
          <FileText className="w-5 h-5 text-amber-400" />
          <div>
            <h3 className="text-lg font-serif font-bold text-white">Case Documents & Evidentiary Artifacts</h3>
            <p className="text-xs text-slate-400">Attach and inspect SCNs, DRC-01/07, Tax Invoices, E-Way bills, Bank statements & OCR extractions.</p>
          </div>
        </div>

        {/* Existing Documents List */}
        <div className="mb-6">
          <div className="text-xs font-mono uppercase text-slate-400 mb-2 font-semibold">Attached Case Files ({documents.length}):</div>
          <div className="space-y-2 max-h-56 overflow-y-auto pr-1">
            {documents.map((d) => (
              <div key={d.id} className="flex items-center justify-between p-3 rounded-lg bg-legal-950/80 border border-legal-800 text-xs">
                <div className="flex items-center gap-3">
                  <span className="font-mono text-[10px] px-2 py-0.5 rounded bg-blue-950 text-blue-300 border border-blue-800">
                    {d.type}
                  </span>
                  <div>
                    <div className="font-semibold text-slate-200">{d.name}</div>
                    <div className="text-[11px] text-slate-400 flex items-center gap-2 mt-0.5">
                      <span>Size: {d.fileSize}</span>
                      <span>•</span>
                      <span className="text-amber-400/90 font-mono">OCR: {d.ocrReadability}</span>
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => onRemoveDocument(d.id)}
                  className="text-slate-500 hover:text-rose-400 transition-colors p-1.5"
                  title="Remove document"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            ))}
          </div>
        </div>

        {/* Add Document Form */}
        <form onSubmit={handleAdd} className="bg-legal-900/60 p-4 rounded-xl border border-legal-800/80 text-xs space-y-3">
          <div className="font-serif font-bold text-white text-sm">Add New Case Document or OCR Snippet</div>
          
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-300 mb-1">Document Title / File Name</label>
              <input
                type="text"
                value={docName}
                onChange={(e) => setDocName(e.target.value)}
                placeholder="e.g. Tax Invoices Nos 101-114"
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
                required
              />
            </div>
            <div>
              <label className="block text-slate-300 mb-1">Document Type</label>
              <select
                value={docType}
                onChange={(e) => setDocType(e.target.value as any)}
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
              >
                <option value="SCN">SCN (Show Cause Notice)</option>
                <option value="DRC-01">DRC-01 (Summary SCN)</option>
                <option value="DRC-07">DRC-07 (Adjudication Order)</option>
                <option value="Reply">DRC-06 (Reply to SCN)</option>
                <option value="APL-01">APL-01 (First Appeal Memo)</option>
                <option value="Invoice">Tax Invoice (Rule 46)</option>
                <option value="E-Way Bill">E-Way Bill (Part A & B)</option>
                <option value="GSTR-1">GSTR-1 Supplier Return</option>
                <option value="GSTR-2B">GSTR-2B Auto-Drafted ITC</option>
                <option value="GSTR-3B">GSTR-3B Summary Return</option>
                <option value="Bank Statement">Bank Payment & RTGS Statement</option>
                <option value="Transporter Bilty">Transporter Lorry Receipt (LR)</option>
                <option value="CA Certificate">Circular 183 CA Certificate</option>
                <option value="Other">Other Evidentiary Proof</option>
              </select>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label className="block text-slate-300 mb-1">OCR Readability Quality</label>
              <select
                value={ocrStatus}
                onChange={(e) => setOcrStatus(e.target.value as any)}
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
              >
                <option value="Clearly readable text">Clearly readable text (Established)</option>
                <option value="Uncertain OCR text">Uncertain OCR text (Needs verification)</option>
                <option value="Potentially misread text">Potentially misread text (Caution)</option>
                <option value="Missing text">Missing text / Partial page</option>
              </select>
            </div>
            <div>
              <label className="block text-slate-300 mb-1">Extracted Text Content / Summary</label>
              <input
                type="text"
                value={snippet}
                onChange={(e) => setSnippet(e.target.value)}
                placeholder="Key extracted details, dates, or amounts"
                className="w-full bg-legal-950 border border-legal-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-amber-400"
              />
            </div>
          </div>

          <div className="flex justify-end gap-2 pt-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-lg bg-legal-800 text-slate-300 hover:bg-legal-700 transition-colors"
            >
              Close
            </button>
            <button
              type="submit"
              className="px-4 py-2 rounded-lg bg-amber-500 hover:bg-amber-400 text-black font-semibold transition-colors"
            >
              Attach Document
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
