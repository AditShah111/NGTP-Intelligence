doc_modal = """'use client';

import React, { useState, useRef } from 'react';
import { X, Upload, FileText, CheckCircle2, AlertTriangle, Trash2, FilePlus, Sparkles, Loader2, Plus } from 'lucide-react';
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
  const [selectedDocType, setSelectedDocType] = useState<CaseDocument['type']>('Invoice');
  const [pasteText, setPasteText] = useState('');
  const [pasteDocName, setPasteDocName] = useState('');
  const [activeTab, setActiveTab] = useState<'upload' | 'paste'>('upload');
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
        extractedText = `Attached file: ${file.name} (Type: ${file.type || 'binary/pdf'}, Size: ${(file.size / 1024).toFixed(1)} KB)`;
      }

      let determinedType = selectedDocType;
      if (lowerName.includes('drc-07') || lowerName.includes('order')) determinedType = 'DRC-07';
      else if (lowerName.includes('scn') || lowerName.includes('drc-01')) determinedType = 'SCN';
      else if (lowerName.includes('bank') || lowerName.includes('rtgs') || lowerName.includes('statement')) determinedType = 'Bank Statement';
      else if (lowerName.includes('e-way') || lowerName.includes('eway') || lowerName.includes('transit')) determinedType = 'E-Way Bill';
      else if (lowerName.includes('invoice') || lowerName.includes('bill')) determinedType = 'Invoice';

      const newDoc: CaseDocument = {
        id: `doc-${Date.now()}-${Math.random().toString(36).substring(2, 6)}`,
        name: file.name,
        type: determinedType,
        fileSize: `${(file.size / 1024).toFixed(1)} KB`,
        uploadedAt: new Date().toISOString().split('T')[0],
        ocrReadability: 'Clearly readable text',
        extractedTextSnippet: extractedText.slice(0, 1000)
      };

      onAddDocument(newDoc);
    } catch (err) {
      console.error('File parsing error:', err);
    } finally {
      setIsExtracting(false);
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  };

  const handleFiles = async (files: FileList | null) => {
    if (!files || files.length === 0) return;
    for (let i = 0; i < files.length; i++) {
      await processFile(files[i]);
    }
  };

  const handleAddPastedText = () => {
    if (!pasteText.trim()) return;
    const docName = pasteDocName.trim() || `${selectedDocType} Notes / Text Extract`;
    const newDoc: CaseDocument = {
      id: `doc-${Date.now()}-${Math.random().toString(36).substring(2, 6)}`,
      name: docName,
      type: selectedDocType,
      fileSize: `${(new Blob([pasteText]).size / 1024).toFixed(1)} KB`,
      uploadedAt: new Date().toISOString().split('T')[0],
      ocrReadability: 'Clearly readable text',
      extractedTextSnippet: pasteText.slice(0, 1000)
    };
    onAddDocument(newDoc);
    setPasteText('');
    setPasteDocName('');
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
            <h3 className="text-lg font-serif font-bold text-slate-900">Case Documents & Evidentiary Files</h3>
            <p className="text-xs text-slate-500">Upload actual SCNs, Tax Invoices, Bank Statements, and E-Way bills to calculate exact legal scores.</p>
          </div>
        </div>

        {/* Tab Selection */}
        <div className="flex items-center gap-2 mb-4 border-b border-beige-200 pb-2">
          <button
            onClick={() => setActiveTab('upload')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
              activeTab === 'upload' ? 'bg-amber-600 text-white' : 'text-slate-600 hover:bg-beige-100'
            }`}
          >
            Upload File (PDF / Images / Docs)
          </button>
          <button
            onClick={() => setActiveTab('paste')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
              activeTab === 'paste' ? 'bg-amber-600 text-white' : 'text-slate-600 hover:bg-beige-100'
            }`}
          >
            Paste Text Extract / SCN Directly
          </button>
        </div>

        {/* Document Type Selector */}
        <div className="mb-4 bg-beige-50 p-3 rounded-xl border border-beige-200">
          <label className="block text-xs font-semibold text-slate-700 mb-1">
            Specify Evidence Type for Upload:
          </label>
          <select
            value={selectedDocType}
            onChange={(e) => setSelectedDocType(e.target.value as any)}
            className="w-full bg-white border border-beige-300 rounded-lg px-3 py-2 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm"
          >
            <option value="Invoice">Tax Invoice (Satisfies Section 16(2)(a))</option>
            <option value="Bank Statement">Bank Statement / RTGS Advice (Satisfies 2nd Proviso & Suncraft Doctrine)</option>
            <option value="E-Way Bill">E-Way Bill / Transit Log (Satisfies Section 16(2)(b) Physical Movement)</option>
            <option value="SCN">Show Cause Notice / DRC-01 (Audits Lower Authority Allegations)</option>
            <option value="DRC-07">Order-in-Original / DRC-07 (Audits Appellate Grounds)</option>
            <option value="CA Certificate">Chartered Accountant Certificate (Circular 183 Safe-Harbor)</option>
            <option value="Other">Other Supporting Document</option>
          </select>
        </div>

        {activeTab === 'upload' ? (
          <div
            onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
            onDragLeave={() => setIsDragging(false)}
            onDrop={async (e) => { e.preventDefault(); setIsDragging(false); await handleFiles(e.dataTransfer.files); }}
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
                <div className="text-xs font-mono text-slate-700 font-semibold">Attaching & parsing document...</div>
              </div>
            ) : (
              <div className="flex flex-col items-center justify-center space-y-2">
                <div className="p-3 rounded-full bg-white shadow-sm border border-beige-200 text-amber-700">
                  <Upload className="w-6 h-6" />
                </div>
                <div className="font-serif font-bold text-sm text-slate-900">
                  Click to Browse Files or Drag & Drop Here
                </div>
                <p className="text-[11px] font-mono text-slate-500">
                  Selected Type: <span className="font-bold text-amber-800">{selectedDocType}</span> (.pdf, .png, .jpg, .txt, .csv)
                </p>
              </div>
            )}
          </div>
        ) : (
          <div className="space-y-3 bg-beige-50/50 p-4 rounded-xl border border-beige-200">
            <input
              type="text"
              value={pasteDocName}
              onChange={(e) => setPasteDocName(e.target.value)}
              placeholder="Document Title (e.g. DRC-01 Notice dated 15.03.2023 or HDFC RTGS Advice)"
              className="w-full bg-white border border-beige-300 rounded-lg px-3 py-2 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm"
            />
            <textarea
              rows={4}
              value={pasteText}
              onChange={(e) => setPasteText(e.target.value)}
              placeholder="Paste the text of the SCN, invoice numbers, bank RTGS transaction UTR numbers, or order findings here..."
              className="w-full bg-white border border-beige-300 rounded-lg p-3 text-xs text-slate-800 focus:outline-none focus:border-amber-600 leading-relaxed shadow-inner"
            />
            <div className="flex justify-end">
              <button
                type="button"
                onClick={handleAddPastedText}
                disabled={!pasteText.trim()}
                className="flex items-center gap-1.5 px-4 py-2 rounded-lg bg-amber-600 hover:bg-amber-700 disabled:opacity-50 text-white font-semibold text-xs shadow-sm transition-all"
              >
                <Plus className="w-4 h-4" />
                <span>Attach Text Document</span>
              </button>
            </div>
          </div>
        )}

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
                <strong>Zero Evidence Warning:</strong> Without tax invoices, bank statements, and E-Way bills, the litigation engine will strictly evaluate this case as <em>UNSUPPORTED (DO NOT PROCEED)</em> with a score of ~18/100 under Section 155.
              </div>
            </div>
          ) : (
            <div className="space-y-2 max-h-56 overflow-y-auto pr-1">
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
                        <span className="text-emerald-700 font-semibold">{d.uploadedAt}</span>
                      </div>
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
with open("src/components/DocumentUploaderModal.tsx", "w", encoding="utf-8") as f:
    f.write(doc_modal)
print("Updated DocumentUploaderModal.tsx successfully!")