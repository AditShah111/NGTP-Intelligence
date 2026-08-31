'use client';

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

  const reasons = activeCase.finalOutput.executiveVerdict.top5Reasons.map((r, i) => `${i + 1}. ${r}`).join('\n');
  const strongParams = activeCase.finalOutput.strongestLegalParameters.map((p) => `* ${p}`).join('\n');
  const weakParams = activeCase.finalOutput.weakestParameters.map((p) => `* ${p}`).join('\n');
  const strongGrounds = activeCase.finalOutput.strongestGroundsOfChallenge.map(g => `* [Rank #${g.rank} - Strength ${g.strength}/100] ${g.ground}`).join('\n');
  const opposingArgs = activeCase.finalOutput.strongestOpposingArguments.map(oa => `* ${oa}`).join('\n');
  const gapReport = activeCase.finalOutput.evidenceGapReport.map(eg => `* ${eg}`).join('\n');
  const precedentMatrix = activeCase.finalOutput.precedentMatrix.map(pm => `* **${pm.precedent}** - ${pm.applicability} (Comparability Score: ${pm.score}/100)`).join('\n');
  const errorMatrix = activeCase.finalOutput.lowerAuthorityErrorMatrix.map(em => `* **${em.error}** - ${em.significance}`).join('\n');
  const draftDefects = activeCase.finalOutput.draftDefects.map(dd => `* [${dd.severity}] ${dd.defect}`).join('\n');
  const p0Plan = activeCase.finalOutput.litigationImprovementPlan.p0MustFixBeforeFiling.map(i => `* ${i}`).join('\n');
  const p1Plan = activeCase.finalOutput.litigationImprovementPlan.p1StronglyRecommended.map(i => `* ${i}`).join('\n');
  const p2Plan = activeCase.finalOutput.litigationImprovementPlan.p2AdditionalStrengthening.map(i => `* ${i}`).join('\n');

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
${reasons}

---

## 2. STRONGEST LEGAL PARAMETERS
${strongParams}

---

## 3. WEAKEST PARAMETERS (LITIGATION RISKS)
${weakParams}

---

## 4. STRONGEST GROUNDS OF CHALLENGE
${strongGrounds}

---

## 5. REVENUE COUNTERARGUMENTS & RED-TEAM RESILIENCE
${opposingArgs}

---

## 6. EVIDENCE GAP REPORT & REMEDIATION
${gapReport}

---

## 7. PRECEDENT MATRIX
${precedentMatrix}

---

## 8. LOWER AUTHORITY ERROR MATRIX
${errorMatrix}

---

## 9. DRAFT DEFECT AUDIT
${draftDefects}

---

## 10. LITIGATION IMPROVEMENT PLAN
### P0 — Must Fix Before Filing:
${p0Plan}

### P1 — Strongly Recommended:
${p1Plan}

### P2 — Additional Strengthening:
${p2Plan}

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