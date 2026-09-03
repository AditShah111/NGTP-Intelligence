import { 
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
import { generateAdversarialRedTeamWithGemini, fetchLatestPrecedentsWithGemini } from './gemini-client';
import { resolvePrecedentConflicts } from './hierarchy-engine';

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

  // Strict Document Type Gating
  const hasInvoices = documents.some(d => d.type === 'Invoice');
  const hasTransit = documents.some(d => d.type === 'E-Way Bill' || d.type === 'Transporter Bilty');
  const hasBank = documents.some(d => d.type === 'Bank Statement');
  const hasScn = documents.some(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07');
  const hasCaCert = documents.some(d => d.type === 'CA Certificate');

  // Step 1: Fact Matrix
  const factMatrix = extractFactMatrix(summary, primaryIssue, documents);

  // Step 3 & 4: Precedents & Article 141 Judicial Hierarchy Audit
  let precedents = getApplicablePrecedents(primaryIssue, financialYear);
  if (geminiApiKey || process.env.GEMINI_API_KEY) {
    try {
      const livePrecedents = await fetchLatestPrecedentsWithGemini(primaryIssue, financialYear, geminiApiKey, documents);
      if (livePrecedents && livePrecedents.length > 0) {
        precedents = [...livePrecedents, ...precedents];
      }
    } catch (e) {
      console.warn('Gemini live precedent research skipped.');
    }
  }
  precedents = resolvePrecedentConflicts(precedents, hasBank);

  // Step 2: Statutory Parameters (Calibrated by Judicial Authorities)
  const statutoryParameters = evaluateStatutoryParameters(
    financialYear, 
    primaryIssue, 
    hasInvoices, 
    hasTransit, 
    hasBank, 
    hasScn, 
    hasCaCert,
    precedents
  );

  // Step 5: Lower Authority Errors
  const lowerAuthorityErrors = analyzeLowerAuthorityErrors(noticeType, primaryIssue);

  // Step 6: Submission Improvement (Dynamically synthesizing all ingested High Court & Supreme Court precedents)
  const improvedSubmissions = improveSubmissions(
    primaryIssue,
    precedents,
    statutoryParameters,
    hasTransit,
    hasBank
  );

  // Step 7: Adversarial Red-Team
  let redTeamItems = runAdversarialRedTeamAnalysis();
  if (geminiApiKey || process.env.GEMINI_API_KEY) {
    try {
      const allDocText = documents.map(d => `${d.name} (${d.type}): ${d.extractedTextSnippet}`).join('\n');
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
  const viabilityScore = calculateViabilityScore(readinessScore.totalScore, hasBank, hasInvoices, hasTransit);

  // Step 11: Forward Decision
  const forwardDecision = calculateForwardDecision(readinessScore.totalScore, hasInvoices, hasBank, hasTransit);

  // Step 12: Draft Audit
  const draftAudit = auditDraft();

  // Step 13: Final Output
  let recommendation: Recommendation = 'DO NOT PROCEED';
  if (readinessScore.totalScore >= 80) {
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
      'CRITICAL DEFICIENCY: Bank payment proof (RTGS/NEFT) or physical delivery evidence is missing.',
      'Under 2nd Proviso to Section 16(2), payment within 180 days must be affirmatively proved through bank statements.',
      'Supreme Court affirmed Suncraft Energy protections CANNOT be invoked without demonstrating genuine banking payments.',
      'Burden of Proof under Section 155 is partially or entirely undischarged.',
      'Immediate action required: Attach official bank statement / RTGS payment vouchers to establish bona fides.'
    ];
  } else if (readinessScore.totalScore < 75) {
    top5Reasons = [
      'Invoices and bank payment established, but physical transit records (E-Way bills/LRs) are needed to defeat fake-billing allegations.',
      'Suncraft precedent applicable in principle subject to corroborating movement of goods.',
      'CBIC Circular 183/15/2022 CA Certificate should be obtained before filing appeal.',
      'Section 16(2)(aa) prospective application is viable.',
      'Proceed after rectifying evidence gaps.'
    ];
  } else {
    top5Reasons = [
      'Directly covered by Supreme Court affirmed Calcutta HC judgment in Suncraft Energy (SLP (C) 27927/2023).',
      'Under Article 141, Revenue is bound to exhaust recovery against the supplier before demanding reversal from buyer.',
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
      ? ['Article 141 Supreme Court binding rule: Suncraft supplier exhaustion condition precedent.', 'Lex non cogit ad impossibilia - Law does not compel a person to perform an impossible act.']
      : (hasInvoices ? ['Section 16(2)(a) Possession of Tax Invoice (Satisfied)'] : ['No strong legal parameters established until bank payment and invoices are uploaded.']),
    weakestParameters: !hasBank
      ? ['2nd Proviso to Section 16(2) Consideration & Tax Payment (Missing)', 'Section 155 Burden of Proof (Unmet)', 'Section 16(2)(c) Tax Payment (Unverified)']
      : (!hasTransit ? ['Section 16(2)(b) Actual Receipt of Goods (Uncorroborated by E-Way Bills)'] : ['Section 16(2)(c) literal tax-paid condition before lower departmental officers.']),
    strongestGroundsOfChallenge: hasBank && hasInvoices
      ? [
          { ground: 'Recovery from buyer without investigating supplier is illegal (Suncraft SC Affirmed)', rank: 1, strength: 95 },
          { ground: 'Safe-harbor relief under CBIC Circular 183/15/2022-GST', rank: 2, strength: 92 }
        ]
      : [
          { ground: 'Possession of valid tax invoice under Section 16(2)(a)', rank: 1, strength: 40 }
        ],
    strongestOpposingArguments: [
      'Section 155 CGST Act: Taxpayer has not proven consideration and tax payment through bank records.',
      'Section 16(2)(c) non-negotiable statutory condition precedent: Tax was not paid to the Government.'
    ],
    evidenceGapReport: forwardDecision.evidenceDependentImprovements,
    precedentMatrix: precedents.map(p => ({
      precedent: `${p.caseName} (${p.court}) [${p.article141Status || 'BINDING'}]`,
      applicability: hasBank ? (p.favourableApplicability === 'HIGH' ? 'Controlling / Direct Ratio (Art. 141)' : 'Persuasive') : 'Inapplicable (Bank Payment Unproven)',
      score: hasBank ? p.comparabilityScore.totalScore : 30
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
      shouldProceed: readinessScore.totalScore >= 75,
      proceedExplanation: readinessScore.totalScore >= 75 
        ? 'Case is substantiated with documentary evidence and backed by Supreme Court affirmed precedent under Article 141.' 
        : (readinessScore.totalScore >= 40 
            ? 'PROCEED AFTER RECTIFICATION. Taxpayer must attach bank statements and transit proof before filing.' 
            : 'DO NOT PROCEED. Taxpayer position lacks bank payment and transit evidence.'),
      singleBiggestRisk: !hasBank 
        ? 'Lack of bank RTGS payment proof to establish bona fides.' 
        : (!hasTransit ? 'Lack of E-Way bills to prove physical receipt' : 'Departmental bias at First Appellate stage.'),
      singleStrongestAdvantage: hasBank 
        ? 'Unbroken chain of tax invoices, E-way bills, and RTGS bank receipts anchored on Supreme Court Suncraft ruling.' 
        : (hasInvoices ? 'Possession of valid tax invoice.' : 'None until documents are uploaded.'),
      evidenceMostNeeded: !hasInvoices ? 'Tax Invoices under Rule 46' : (!hasBank ? 'Bank RTGS Payment Advice (MANDATORY P0)' : 'E-Way Bills / Circular 183 CA Certificate'),
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
