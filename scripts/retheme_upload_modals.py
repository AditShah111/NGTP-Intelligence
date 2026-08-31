code_doc_modal = """'use client';

import React, { useState, useRef } from 'react';
import { X, Upload, FileText, CheckCircle2, AlertTriangle, Trash2, Eye, FilePlus, Sparkles, Loader2 } from 'lucide-react';
import { CaseDocument } from '../types';

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
  const [isDragging, setIsDragging] = useState(false);
  const [isExtracting, setIsExtracting] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  if (!isOpen) return null;

  const processFile = async (file: File) => {
    setIsExtracting(true);
    try {
      let extractedText = '';
      const lowerName = file.name.toLowerCase();

      if (file.type.includes('text') || lowerName.endsWith('.txt') || lowerName.endsWith('.csv') || lowerName.endsWith('.json')) {
        extractedText = await file.text();
      } else {
        const buffer = await file.arrayBuffer();
        const decoder = new TextDecoder('utf-8', { fatal: false });
        const rawText = decoder.decode(buffer);
        extractedText = rawText.replace(/[\\x00-\\x08\\x0B\\x0C\\x0E-\\x1F\\x7F-\\x9F]/g, ' ').replace(/\\s+/g, ' ').slice(0, 4000);
        if (!extractedText.trim()) {
          extractedText = `File content from ${file.name} (Size: ${(file.size / 1024).toFixed(1)} KB)`;
        }
      }

      const fullText = (file.name + ' ' + extractedText).toLowerCase();
      let determinedType: CaseDocument['type'] = 'Other';
      if (fullText.includes('drc-07') || fullText.includes('order-in-original')) determinedType = 'DRC-07';
      else if (fullText.includes('drc-01') || fullText.includes('show cause') || fullText.includes('scn')) determinedType = 'SCN';
      else if (fullText.includes('invoice') || fullText.includes('bill no') || fullText.includes('taxable value') || fullText.includes('hsn')) determinedType = 'Invoice';
      else if (fullText.includes('bank') || fullText.includes('rtgs') || fullText.includes('neft') || fullText.includes('utr') || fullText.includes('statement')) determinedType = 'Bank Statement';
      else if (fullText.includes('e-way') || fullText.includes('eway') || fullText.includes('vehicle') || fullText.includes('transport')) determinedType = 'E-Way Bill';
      else if (fullText.includes('circular 183') || fullText.includes('chartered accountant') || fullText.includes('certificate')) determinedType = 'CA Certificate';

      const newDoc: CaseDocument = {
        id: `doc-${Date.now()}-${Math.random().toString(36).substr(2, 5)}`,
        name: file.name,
        type: determinedType,
        fileSize: `${(file.size / 1024).toFixed(1)} KB`,
        uploadedAt: new Date().toISOString().split('T')[0],
        ocrReadability: extractedText.length > 50 ? 'Clearly readable text' : 'Uncertain OCR text',
        extractedTextSnippet: extractedText.slice(0, 1000)
      };

      onAddDocument(newDoc);
    } catch (err) {
      console.error('File parsing error:', err);
    } finally {
      setIsExtracting(false);
    }
  };

  const handleFiles = async (files: FileList | null) => {
    if (!files || files.length === 0) return;
    for (let i = 0; i < files.length; i++) {
      await processFile(files[i]);
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = async (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    await handleFiles(e.dataTransfer.files);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm p-4 overflow-y-auto">
      <div className="bg-white border border-beige-300 rounded-2xl w-full max-w-3xl shadow-2xl p-6 relative my-8">
        <button
          onClick={onClose}
          className="absolute top-5 right-5 text-slate-400 hover:text-slate-700 transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-2.5 mb-4 pb-3 border-b border-beige-200">
          <div className="p-2 rounded-xl bg-amber-50 text-amber-700">
            <FilePlus className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-lg font-serif font-bold text-slate-900">Upload Real Case Documents & Evidence</h3>
            <p className="text-xs text-slate-500">Attach actual SCNs, Tax Invoices, Bank RTGS statements, and E-Way bills (PDF, TXT, CSV, Scans).</p>
          </div>
        </div>

        {/* Drag & Drop File Zone */}
        <div
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
          className={`border-2 border-dashed rounded-xl p-6 text-center cursor-pointer transition-all ${
            isDragging 
              ? 'border-amber-600 bg-amber-50' 
              : 'border-beige-300 hover:border-amber-500 bg-beige-50/70 hover:bg-beige-100/70'
          }`}
        >
          <input
            type="file"
            ref={fileInputRef}
            onChange={(e) => handleFiles(e.target.files)}
            multiple
            accept=".pdf,.png,.jpg,.jpeg,.txt,.csv,.json,.doc,.docx"
            className="hidden"
          />
          {isExtracting ? (
            <div className="flex flex-col items-center justify-center py-2 space-y-2">
              <Loader2 className="w-8 h-8 text-amber-600 animate-spin" />
              <div className="text-xs font-mono text-slate-700 font-semibold">Extracting text & OCR tokens from file...</div>
            </div>
          ) : (
            <div className="flex flex-col items-center justify-center space-y-2">
              <div className="p-3 rounded-full bg-white shadow-sm border border-beige-200 text-amber-700">
                <Upload className="w-6 h-6" />
              </div>
              <div className="font-serif font-bold text-sm text-slate-900">
                Drag & Drop Real PDF or Document Files Here, or <span className="text-amber-700 underline font-sans">Browse Files</span>
              </div>
              <p className="text-[11px] font-mono text-slate-500">
                Supports SCNs, Invoices, Bank Payment Slips, E-Way bills (.pdf, .png, .jpg, .txt, .csv)
              </p>
            </div>
          )}
        </div>

        {/* Existing Documents List */}
        <div className="mt-6 mb-4">
          <div className="text-xs font-mono uppercase text-slate-500 mb-2 font-semibold flex items-center justify-between">
            <span>Attached Case Files ({documents.length}):</span>
            <span className="text-emerald-700 text-[11px] font-semibold">
              {documents.length > 0 ? '✓ Evidence attached' : '⚠️ No documents attached (Score will be penalized)'}
            </span>
          </div>

          {documents.length === 0 ? (
            <div className="p-4 rounded-xl bg-rose-50 border border-rose-200 text-xs text-rose-900 flex items-start gap-2.5">
              <AlertTriangle className="w-4 h-4 text-rose-600 flex-shrink-0 mt-0.5" />
              <div>
                <strong>Zero Evidence Warning:</strong> Without actual tax invoices or bank statements, the litigation engine will strictly evaluate this case as <em>UNSUPPORTED (DO NOT PROCEED)</em> under Section 155.
              </div>
            </div>
          ) : (
            <div className="space-y-2 max-h-60 overflow-y-auto pr-1">
              {documents.map((d) => (
                <div key={d.id} className="flex items-center justify-between p-3 rounded-xl bg-beige-50 border border-beige-200 text-xs shadow-sm">
                  <div className="flex items-center gap-3">
                    <span className={`font-mono text-[10px] font-bold px-2.5 py-0.5 rounded-full border ${
                      d.type === 'Invoice' ? 'bg-emerald-50 text-emerald-800 border-emerald-200' :
                      d.type === 'Bank Statement' ? 'bg-blue-50 text-blue-800 border-blue-200' :
                      d.type === 'E-Way Bill' ? 'bg-purple-50 text-purple-800 border-purple-200' :
                      'bg-amber-50 text-amber-800 border-amber-200'
                    }`}>
                      {d.type}
                    </span>
                    <div>
                      <div className="font-semibold text-slate-900">{d.name}</div>
                      <div className="text-[11px] text-slate-500 flex items-center gap-2 mt-0.5 font-mono">
                        <span>Size: {d.fileSize}</span>
                        <span>•</span>
                        <span className="text-emerald-700 font-semibold">OCR: {d.ocrReadability}</span>
                      </div>
                      {d.extractedTextSnippet && (
                        <p className="text-[10px] text-slate-600 line-clamp-1 italic mt-1 bg-white p-1 rounded border border-beige-200 font-mono">
                          "{d.extractedTextSnippet.slice(0, 120)}..."
                        </p>
                      )}
                    </div>
                  </div>
                  <button
                    onClick={() => onRemoveDocument(d.id)}
                    className="text-slate-400 hover:text-rose-600 transition-colors p-1.5 ml-2"
                    title="Remove document"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="flex justify-end gap-2 pt-3 border-t border-beige-200">
          <button
            onClick={onClose}
            className="px-5 py-2 rounded-lg bg-amber-600 hover:bg-amber-700 text-white font-semibold transition-colors text-xs shadow-sm"
          >
            Done & Apply to Case
          </button>
        </div>
      </div>
    </div>
  );
};
"""

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
            <label className="block text-amber-900 font-semibold mb-1">
              Attach Real Evidence Files (Invoices, SCN, Bank Statements, E-Way bills)
            </label>
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
                  <span className="font-semibold">Extracting document text...</span>
                </div>
              ) : (
                <div className="flex flex-col items-center justify-center space-y-1">
                  <Upload className="w-5 h-5 text-amber-700" />
                  <span className="text-slate-800 font-medium">Click to attach real PDF / Invoices / Bank Proof</span>
                  <span className="text-[10px] text-slate-500">Without files, case will be marked as "Unsupported / Insufficient Evidence"</span>
                </div>
              )}
            </div>

            {/* Attached files preview */}
            {attachedDocs.length > 0 && (
              <div className="mt-2 space-y-1.5">
                {attachedDocs.map((doc, idx) => (
                  <div key={idx} className="flex items-center justify-between p-2 rounded-lg bg-beige-50 border border-beige-200 text-[11px]">
                    <span className="text-slate-800 font-mono font-semibold">{doc.name} ({doc.type})</span>
                    <span className="text-emerald-700 font-mono font-semibold">{doc.fileSize}</span>
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

with open("src/components/DocumentUploaderModal.tsx", "w", encoding="utf-8") as f:
    f.write(code_doc_modal)
with open("src/components/NewCaseModal.tsx", "w", encoding="utf-8") as f:
    f.write(code_new_modal)

print("Updated DocumentUploaderModal and NewCaseModal to clean beige theme!")