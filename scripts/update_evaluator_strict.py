import os

code_eval = """import { 
  CaseStudy, 
  FinalEvaluatorOutput, 
  Recommendation,
  CaseDocument 
} from '../types';
import { extractFactMatrix } from './fact-matrix-engine';
import { evaluateStatutoryParameters } from './statutory-engine';
import { getApplicablePrecedents } from './precedent-engine';
import { analyzeLowerAuthorityErrors } from './error-analysis-engine';
import { improveSubmissions } from './submission-optimizer';
import { runAdversarialRedTeamAnalysis } from './adversarial-redteam-engine';
import { analyzeEvidenceGaps } from './evidence-gap-engine';
import { 
  calculateReadinessScore, 
  calculateViabilityScore, 
  calculateForwardDecision 
} from './scoring-engine';
import { auditDraft } from './draft-audit-engine';
import { generateAdversarialRedTeamWithGemini } from './gemini-client';

export async function runComplete13StepEvaluation(
  title: string,
  taxpayerName: string,
  gstin: string,
  financialYear: string,
  disputedAmount: string,
  noticeType: 'SCN / DRC-01' | 'Order-in-Original / DRC-07' | 'First Appeal / APL-01' | 'High Court Writ Petition',
  primaryIssue: string,
  summary: string,
  documents: CaseDocument[] = [],
  geminiApiKey?: string
): Promise<CaseStudy> {
  const caseId = `case-${Date.now()}`;

  // Rigorous Document Evidentiary Audit
  const hasInvoices = documents.some(d => d.type === 'Invoice') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('invoice'));
  const hasTransit = documents.some(d => d.type === 'E-Way Bill') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('e-way') || d.extractedTextSnippet.toLowerCase().includes('vehicle'));
  const hasBank = documents.some(d => d.type === 'Bank Statement') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('bank') || d.extractedTextSnippet.toLowerCase().includes('rtgs'));
  const hasScn = documents.some(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07');
  const hasCaCert = documents.some(d => d.type === 'CA Certificate');

  // Step 1: Fact Matrix (Evidence Traceability)
  const factMatrix = extractFactMatrix(summary, primaryIssue, documents);

  // Step 2: Statutory Parameters
  const statutoryParameters = evaluateStatutoryParameters(financialYear, primaryIssue, hasInvoices, hasTransit, hasBank, hasScn);

  // Step 3 & 4: Precedents & Comparability Score
  const precedents = getApplicablePrecedents(primaryIssue, financialYear);

  // Step 5: Lower Authority Errors
  const lowerAuthorityErrors = analyzeLowerAuthorityErrors(noticeType, primaryIssue);

  // Step 6: Submission Improvement
  const improvedSubmissions = improveSubmissions(primaryIssue);

  // Step 7: Adversarial Red-Team
  let redTeamItems = runAdversarialRedTeamAnalysis();
  if (geminiApiKey || process.env.GEMINI_API_KEY) {
    try {
      const allDocText = documents.map(d => `${d.name}: ${d.extractedTextSnippet}`).join('\n');
      const aiItems = await generateAdversarialRedTeamWithGemini(
        `${summary}\nUploaded Evidence:\n${allDocText}`, 
        primaryIssue, 
        geminiApiKey
      );
      if (aiItems && aiItems.length > 0) {
        redTeamItems = [...aiItems, ...redTeamItems];
      }
    } catch (e) {
      console.warn('Gemini Red Team generation skipped.');
    }
  }

  // Step 8: Evidence Gaps
  const evidenceGaps = analyzeEvidenceGaps();

  // Step 9 & 10: Scores (Strict Evidentiary Math)
  const readinessScore = calculateReadinessScore(statutoryParameters.length, hasInvoices, hasTransit, hasBank, hasScn);
  const viabilityScore = calculateViabilityScore(readinessScore.totalScore, hasBank, hasInvoices);

  // Step 11: Forward Decision
  const forwardDecision = calculateForwardDecision(readinessScore.totalScore, hasInvoices, hasBank, hasTransit);

  // Step 12: Draft Audit
  const draftAudit = auditDraft();

  // Step 13: Final Output (Rigorous Decision Logic)
  let recommendation: Recommendation = 'DO NOT PROCEED';
  if (readinessScore.totalScore >= 85) {
    recommendation = 'PROCEED';
  } else if (readinessScore.totalScore >= 55) {
    recommendation = 'PROCEED AFTER RECTIFICATION';
  } else if (readinessScore.totalScore >= 35) {
    recommendation = 'HOLD';
  } else {
    recommendation = 'DO NOT PROCEED';
  }

  let top5Reasons: string[] = [];
  if (readinessScore.totalScore < 40) {
    top5Reasons = [
      'FATAL DEFICIENCY: Zero or insufficient primary evidence (invoices, bank RTGS proof, E-way bills) uploaded.',
      'Burden of Proof under Section 155 is entirely undischarged by the taxpayer.',
      'Suncraft Energy and D.Y. Beathel protections cannot be invoked without proof of 100% banking payment.',
      'Statutory non-obstante Section 16(2) requirements remain unproven on the case record.',
      'Immediate action required: Upload actual tax invoices, bank statements, and impugned SCN/DRC-07.'
    ];
  } else {
    top5Reasons = [
      'Directly covered by Supreme Court affirmed Calcutta HC judgment in Suncraft Energy.',
      'Revenue committed fundamental error by demanding tax from buyer without taking any recovery steps against seller.',
      'Full physical receipt and genuine banking payment proven with unassailable documentary evidence.',
      'Section 16(2)(aa) cannot be applied retrospectively to periods prior to 01.01.2022.',
      'CBIC Circular 183/15/2022-GST provides an executive safe-harbor once CA certificate is placed on record.'
    ];
  }

  const finalOutput: FinalEvaluatorOutput = {
    executiveVerdict: {
      litigationReadiness: readinessScore.totalScore,
      litigationViability: viabilityScore.totalScore,
      recommendation,
      top5Reasons
    },
    strongestLegalParameters: hasBank 
      ? ['Lex non cogit ad impossibilia - Law does not compel a person to perform an impossible act.', 'Suncraft / D.Y. Beathel seller exhaustion condition precedent.']
      : ['No strong legal parameters established until bank payment and invoices are uploaded.'],
    weakestParameters: !hasInvoices || !hasBank
      ? ['Section 155 Burden of Proof (Fatal)', 'Section 16(2)(a) Possession of Invoice (Unproven)', 'Section 16(2)(c) Tax Payment (Unverified)']
      : ['Section 16(2)(c) literal tax-paid condition before lower departmental officers.'],
    strongestGroundsOfChallenge: hasBank && hasInvoices
      ? [
          { ground: 'Recovery from buyer without investigating supplier is illegal (Suncraft)', rank: 1, strength: 95 },
          { ground: 'Safe-harbor relief under CBIC Circular 183/15/2022-GST', rank: 2, strength: 92 }
        ]
      : [
          { ground: 'Grounds cannot be drafted without basic invoice and payment documentation', rank: 1, strength: 20 }
        ],
    strongestOpposingArguments: [
      'Section 155 CGST Act: Taxpayer has completely failed to discharge burden of proof.',
      'Section 16(2)(c) non-negotiable statutory condition precedent: Tax was not paid to the Government.'
    ],
    evidenceGapReport: forwardDecision.evidenceDependentImprovements,
    precedentMatrix: precedents.map(p => ({
      precedent: `${p.caseName} (${p.court})`,
      applicability: hasBank ? (p.favourableApplicability === 'HIGH' ? 'Controlling / Direct Ratio' : 'Persuasive') : 'Inapplicable (Facts Unproven)',
      score: hasBank ? p.comparabilityScore.totalScore : 20
    })),
    lowerAuthorityErrorMatrix: lowerAuthorityErrors.map(e => ({
      error: e.finding,
      significance: `${e.strength} - ${e.legalError}`
    })),
    draftDefects: draftAudit.map(d => ({
      defect: d.issueDetected,
      severity: d.severity
    })),
    litigationImprovementPlan: {
      p0MustFixBeforeFiling: forwardDecision.evidenceDependentImprovements.slice(0, 2),
      p1StronglyRecommended: forwardDecision.evidenceDependentImprovements.slice(2),
      p2AdditionalStrengthening: ['Attach vehicle FASTag transit toll receipts and factory store inward registers.']
    },
    finalLitigationAssessment: {
      shouldProceed: readinessScore.totalScore >= 55,
      proceedExplanation: readinessScore.totalScore >= 55 
        ? 'Case is substantiated with documentary evidence and supported by Supreme Court affirmed precedents.' 
        : 'DO NOT PROCEED. Taxpayer position lacks primary documentary evidence. Furnish invoices and bank statements before filing.',
      singleBiggestRisk: !hasBank 
        ? 'Lack of bank RTGS payment proof to establish bona fides.' 
        : 'Departmental bias at First Appellate stage; may require pursuit to Tribunal / High Court.',
      singleStrongestAdvantage: hasBank 
        ? 'Unbroken chain of tax invoices, E-way bills, and RTGS bank receipts.' 
        : 'None until documents are uploaded.',
      evidenceMostNeeded: !hasInvoices ? 'Tax Invoices under Rule 46' : (!hasBank ? 'Bank RTGS Payment Advice' : 'Circular 183 CA Certificate'),
      propositionRequiringCarefulDrafting: 'Framing Section 16(2)(c) through the lens of impossibility of performance without conceding non-remittance.'
    }
  };

  return {
    id: caseId,
    title,
    taxpayerName,
    gstin,
    financialYear,
    disputedAmount,
    noticeType,
    primaryIssue,
    summary,
    documents,
    factMatrix,
    statutoryParameters,
    precedents,
    lowerAuthorityErrors,
    improvedSubmissions,
    redTeamItems,
    evidenceGaps,
    readinessScore,
    viabilityScore,
    forwardDecision,
    draftAudit,
    finalOutput
  };
}
"""

with open("src/service/evaluator-agent.ts", "w", encoding="utf-8") as f:
    f.write(code_eval)

print("Updated evaluator-agent.ts with strict evidentiary evaluation!")