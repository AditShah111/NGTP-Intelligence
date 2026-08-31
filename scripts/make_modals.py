import os

code_doc_modal = """'use client';

import React, { useState } from 'react';
import { X, Upload, FileText, CheckCircle2, AlertTriangle, Trash2, Eye } from 'lucide-react';
import { CaseDocument, OcrReadability } from '@/types';

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
"""

code_new_case = """'use client';

import React, { useState } from 'react';
import { X, Scale, PlusCircle } from 'lucide-react';
import { CaseStudy } from '@/types';

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
"""

code_export_modal = """'use client';

import React, { useState } from 'react';
import { X, Download, Copy, Check, FileText } from 'lucide-react';
import { CaseStudy } from '@/types';

interface ExportDossierModalProps {
  isOpen: boolean;
  onClose: () => void;
  activeCase: CaseStudy;
}

export const ExportDossierModal: React.FC<ExportDossierModalProps> = ({
  isOpen,
  onClose,
  activeCase
}) => {
  const [copied, setCopied] = useState(false);

  if (!isOpen) return null;

  const markdownContent = `# NGTP LITIGATION READINESS & VIABILITY DOSSIER
**Case Title:** ${activeCase.title}
**Taxpayer:** ${activeCase.taxpayerName} | **GSTIN:** ${activeCase.gstin}
**Financial Year:** ${activeCase.financialYear} | **Disputed Tax:** ${activeCase.disputedAmount}
**Notice Type:** ${activeCase.noticeType}

---

## 1. EXECUTIVE VERDICT
* **Litigation Readiness Score:** ${activeCase.readinessScore.totalScore}/100
* **Litigation Viability Score:** ${activeCase.viabilityScore.totalScore}/100
* **Recommendation:** ${activeCase.finalOutput.executiveVerdict.recommendation}

### Top 5 Evaluative Reasons:
${activeCase.finalOutput.executiveVerdict.top5Reasons.map((r, i) => `${i + 1}. ${r}`).join('\n')}

---

## 2. STRONGEST LEGAL PARAMETERS
${activeCase.finalOutput.strongestLegalParameters.map((p, i) => `* ${p}`).join('\n')}

---

## 3. WEAKEST PARAMETERS (LITIGATION RISKS)
${activeCase.finalOutput.weakestParameters.map((p, i) => `* ${p}`).join('\n')}

---

## 4. STRONGEST GROUNDS OF CHALLENGE
${activeCase.finalOutput.strongestGroundsOfChallenge.map(g => `* [Rank #${g.rank} - Strength ${g.strength}/100] ${g.ground}`).join('\n')}

---

## 5. REVENUE COUNTERARGUMENTS & RED-TEAM RESILIENCE
${activeCase.finalOutput.strongestOpposingArguments.map(oa => `* ${oa}`).join('\n')}

---

## 6. EVIDENCE GAP REPORT & REMEDIATION
${activeCase.finalOutput.evidenceGapReport.map(eg => `* ${eg}`).join('\n')}

---

## 7. PRECEDENT MATRIX
${activeCase.finalOutput.precedentMatrix.map(pm => `* **${pm.precedent}** - ${pm.applicability} (Comparability Score: ${pm.score}/100)`).join('\n')}

---

## 8. LOWER AUTHORITY ERROR MATRIX
${activeCase.finalOutput.lowerAuthorityErrorMatrix.map(em => `* **${em.error}** - ${em.significance}`).join('\n')}

---

## 9. DRAFT DEFECT AUDIT
${activeCase.finalOutput.draftDefects.map(dd => `* [${dd.severity}] ${dd.defect}`).join('\n')}

---

## 10. LITIGATION IMPROVEMENT PLAN
### P0 — Must Fix Before Filing:
${activeCase.finalOutput.litigationImprovementPlan.p0MustFixBeforeFiling.map(i => `* ${i}`).join('\n')}

### P1 — Strongly Recommended:
${activeCase.finalOutput.litigationImprovementPlan.p1StronglyRecommended.map(i => `* ${i}`).join('\n')}

### P2 — Additional Strengthening:
${activeCase.finalOutput.litigationImprovementPlan.p2AdditionalStrengthening.map(i => `* ${i}`).join('\n')}

---

## 11. FINAL LITIGATION ASSESSMENT
* **Should the matter proceed to litigation?** ${activeCase.finalOutput.finalLitigationAssessment.shouldProceed ? 'YES' : 'NO'} - ${activeCase.finalOutput.finalLitigationAssessment.proceedExplanation}
* **Single Biggest Risk:** ${activeCase.finalOutput.finalLitigationAssessment.singleBiggestRisk}
* **Single Strongest Advantage:** ${activeCase.finalOutput.finalLitigationAssessment.singleStrongestAdvantage}
* **Evidence Most Needed:** ${activeCase.finalOutput.finalLitigationAssessment.evidenceMostNeeded}
* **Proposition Requiring Most Careful Drafting:** ${activeCase.finalOutput.finalLitigationAssessment.propositionRequiringCarefulDrafting}
`;

  const handleCopy = () => {
    navigator.clipboard.writeText(markdownContent);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownload = () => {
    const blob = new Blob([markdownContent], { type: 'text/markdown;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `NGTP-Litigation-Dossier-${activeCase.taxpayerName.replace(/\\s+/g, '_')}.md`;
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 overflow-y-auto">
      <div className="bg-[#0c1322] border border-legal-700 rounded-2xl w-full max-w-4xl shadow-2xl p-6 relative my-8 flex flex-col max-h-[88vh]">
        <button
          onClick={onClose}
          className="absolute top-5 right-5 text-slate-400 hover:text-white transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center justify-between gap-2 mb-4 pb-3 border-b border-legal-800">
          <div className="flex items-center gap-2">
            <Download className="w-5 h-5 text-amber-400" />
            <div>
              <h3 className="text-lg font-serif font-bold text-white">Full Legal Litigation Dossier</h3>
              <p className="text-xs text-slate-400">Complete 13-step assessment report formatted for senior tax counsel & filing.</p>
            </div>
          </div>
          <div className="flex items-center gap-2 pr-8">
            <button
              onClick={handleCopy}
              className="flex items-center gap-1.5 text-xs bg-legal-800 hover:bg-legal-700 text-slate-200 border border-legal-600 px-3 py-1.5 rounded-lg transition-all"
            >
              {copied ? <Check className="w-4 h-4 text-emerald-400" /> : <Copy className="w-4 h-4" />}
              <span>{copied ? 'Copied!' : 'Copy Markdown'}</span>
            </button>
            <button
              onClick={handleDownload}
              className="flex items-center gap-1.5 text-xs bg-amber-500 hover:bg-amber-400 text-black font-semibold px-3 py-1.5 rounded-lg transition-all"
            >
              <Download className="w-4 h-4" />
              <span>Download .md</span>
            </button>
          </div>
        </div>

        {/* Content Box */}
        <div className="overflow-y-auto bg-legal-950 p-4 rounded-xl border border-legal-800 text-xs font-mono text-slate-300 whitespace-pre-wrap leading-relaxed flex-grow">
          {markdownContent}
        </div>
      </div>
    </div>
  );
};
"""

with open("src/components/DocumentUploaderModal.tsx", "w", encoding="utf-8") as f:
    f.write(code_doc_modal)
with open("src/components/NewCaseModal.tsx", "w", encoding="utf-8") as f:
    f.write(code_new_case)
with open("src/components/ExportDossierModal.tsx", "w", encoding="utf-8") as f:
    f.write(code_export_modal)

print("Wrote all Modals successfully!")