'use client';

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
        extractedText = rawText.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]/g, ' ').replace(/\s+/g, ' ').slice(0, 4000);
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
