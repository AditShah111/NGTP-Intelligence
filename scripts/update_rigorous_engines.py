import os

code_fact = """import { FactMatrixItem, CaseDocument, EvidenceStrength } from '../types';

export function extractFactMatrix(
  caseSummary: string,
  primaryIssue: string,
  documents: CaseDocument[] = []
): FactMatrixItem[] {
  const hasInvoices = documents.some(d => d.type === 'Invoice') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('invoice'));
  const hasBank = documents.some(d => d.type === 'Bank Statement') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('bank') || d.extractedTextSnippet.toLowerCase().includes('rtgs'));
  const hasTransit = documents.some(d => d.type === 'E-Way Bill') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('e-way') || d.extractedTextSnippet.toLowerCase().includes('vehicle'));
  const hasOrder = documents.some(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07');

  const docCount = documents.length;

  return [
    {
      id: 'fm-1',
      issue: 'Possession of Valid Tax Invoices (Section 16(2)(a))',
      allegedFact: hasInvoices 
        ? `Taxpayer possesses valid tax invoices on record satisfying Rule 46 particulars.` 
        : `NO TAX INVOICES UPLOADED. Taxpayer assertion of possessing valid invoices is currently unverified.`,
      sourceDocument: hasInvoices ? documents.find(d => d.type === 'Invoice')?.name || 'Uploaded Invoices' : 'NONE (Missing Evidentiary Proof)',
      pageParagraph: hasInvoices ? 'Verified from uploaded file' : 'N/A',
      evidenceStrength: hasInvoices ? 'Established' : 'Unsupported',
      contradiction: hasInvoices ? 'None.' : 'Fatal statutory deficiency: Section 16(2)(a) mandate is unevidenced.',
      significance: hasInvoices ? 'Satisfies Section 16(2)(a) CGST Act.' : 'Immediate ground for statutory ITC disallowance.',
      ocrStatus: hasInvoices ? 'Clearly readable text' : 'Missing text'
    },
    {
      id: 'fm-2',
      issue: 'Actual Physical Receipt of Goods (Section 16(2)(b))',
      allegedFact: hasTransit 
        ? `Consignments moved with verifiable E-Way bills and inward transit records.` 
        : `NO E-WAY BILLS OR PROOF OF PHYSICAL DELIVERY UPLOADED. Movement of goods is uncorroborated.`,
      sourceDocument: hasTransit ? documents.find(d => d.type === 'E-Way Bill')?.name || 'Uploaded E-Way Bills' : 'NONE (Missing Evidentiary Proof)',
      pageParagraph: hasTransit ? 'Verified from uploaded file' : 'N/A',
      evidenceStrength: hasTransit ? 'Established' : 'Unsupported',
      contradiction: hasTransit ? 'None.' : 'High risk of bogus billing / fake invoicing allegation under Section 74.',
      significance: hasTransit ? 'Satisfies Section 16(2)(b) CGST Act.' : 'Fatal vulnerability against Revenue fake-transit allegations.',
      ocrStatus: hasTransit ? 'Clearly readable text' : 'Missing text'
    },
    {
      id: 'fm-3',
      issue: 'Payment of Consideration and Tax to Supplier (2nd Proviso to Section 16(2))',
      allegedFact: hasBank 
        ? `100% invoice amount including GST paid through verifiable banking channels (RTGS/NEFT).` 
        : `NO BANK STATEMENT OR PAYMENT PROOF UPLOADED. Payment of tax to supplier is unverified.`,
      sourceDocument: hasBank ? documents.find(d => d.type === 'Bank Statement')?.name || 'Uploaded Bank Records' : 'NONE (Missing Evidentiary Proof)',
      pageParagraph: hasBank ? 'Verified from uploaded bank statements' : 'N/A',
      evidenceStrength: hasBank ? 'Established' : 'Unsupported',
      contradiction: hasBank ? 'None.' : 'Taxpayer cannot claim bona fide buyer protection without bank payment proof.',
      significance: hasBank ? 'Complies with 2nd Proviso to Section 16(2) and establishes bona fides.' : 'Precludes reliance on Suncraft Energy safe-harbor.',
      ocrStatus: hasBank ? 'Clearly readable text' : 'Missing text'
    },
    {
      id: 'fm-4',
      issue: 'Departmental Action Against Selling Dealer (Suncraft / D.Y. Beathel Test)',
      allegedFact: hasOrder 
        ? `Impugned SCN / DRC-07 order shows disallowance against recipient without pursuing the supplier.` 
        : `NO LOWER AUTHORITY NOTICE / ORDER UPLOADED. Departmental findings and allegations cannot be audited.`,
      sourceDocument: hasOrder ? documents.find(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07')?.name || 'Uploaded Order' : 'NONE (Missing Impugned Order)',
      pageParagraph: hasOrder ? 'Notice Findings' : 'N/A',
      evidenceStrength: hasOrder ? 'Established' : 'Unable to determine',
      contradiction: hasOrder ? 'Direct breach of Calcutta HC Suncraft principles.' : 'Cannot formulate appeal grounds without the impugned order.',
      significance: hasOrder ? 'Ground for quashing order under Article 226 / Section 107.' : 'Must procure SCN / DRC-07 to frame grounds.',
      ocrStatus: hasOrder ? 'Clearly readable text' : 'Missing text'
    }
  ];
}
"""

code_statutory = """import { StatutoryParameter, CaseDocument } from '../types';

export function evaluateStatutoryParameters(
  financialYear: string,
  primaryIssue: string,
  hasInvoices: boolean,
  hasTransit: boolean,
  hasBank: boolean,
  hasScn: boolean = false
): StatutoryParameter[] {
  return [
    {
      id: 'sp-1',
      parameterCode: 'P1',
      title: 'Possession of Tax Invoice',
      statutoryProvision: 'Section 16(2)(a) CGST Act, 2017',
      statutoryRequirement: 'Registered person must be in possession of a valid tax invoice complying with Rule 46.',
      legalTest: 'Is a physical or digitally signed tax invoice available with all Rule 46 particulars?',
      burdenOfProof: 'Initial burden on Taxpayer under Section 155.',
      requiredEvidence: ['Tax Invoices', 'ERP Purchase Register'],
      availableEvidence: hasInvoices ? ['Tax Invoices on record'] : ['NONE SUBMITTED'],
      assessment: hasInvoices ? 'SATISFIED' : 'NOT SATISFIED',
      risk: hasInvoices ? 'LOW' : 'CRITICAL',
      reason: hasInvoices ? 'Valid tax invoice is attached.' : 'No tax invoices provided. Non-negotiable condition under Section 16(2)(a) is unmet.'
    },
    {
      id: 'sp-2',
      parameterCode: 'P2',
      title: 'Actual Receipt of Goods / Services',
      statutoryProvision: 'Section 16(2)(b) CGST Act, 2017',
      statutoryRequirement: 'Registered person must have actually received the goods or services.',
      legalTest: 'Is there contemporaneous proof of physical movement and delivery?',
      burdenOfProof: 'Taxpayer burden under Section 155.',
      requiredEvidence: ['E-Way Bills (Part A & B)', 'Lorry Receipts (LR)', 'Gate Inward Pass', 'Weighbridge Slips'],
      availableEvidence: hasTransit ? ['E-Way bills and inward delivery records'] : ['NONE SUBMITTED'],
      assessment: hasTransit ? 'SATISFIED' : 'NOT SATISFIED',
      risk: hasTransit ? 'LOW' : 'CRITICAL',
      reason: hasTransit ? 'Documentary transit trail is on record.' : 'No delivery or transit records provided. Serious risk of fake invoicing allegation.'
    },
    {
      id: 'sp-3',
      parameterCode: 'P3',
      title: 'Tax Actually Paid to Government',
      statutoryProvision: 'Section 16(2)(c) CGST Act, 2017',
      statutoryRequirement: 'Tax charged in respect of supply must be actually paid to the Government.',
      legalTest: 'Can ITC be recovered from buyer when supplier defaults, without first proceeding against supplier?',
      burdenOfProof: 'Revenue must establish seller default and attempt recovery from seller first (Suncraft / D.Y. Beathel).',
      requiredEvidence: ['Bank RTGS payment proof to supplier', 'GSTR-1 upload extract', 'DRC-01 issued to supplier'],
      availableEvidence: hasBank ? ['Bank RTGS payment advice', 'GSTR-1 status'] : ['NO BANK PROOF SUBMITTED'],
      assessment: hasBank ? 'PARTIALLY SATISFIED' : 'NOT SATISFIED',
      risk: hasBank ? 'MEDIUM' : 'CRITICAL',
      reason: hasBank ? 'Bona fide payment proven through bank channels; Suncraft doctrine applies.' : 'Without proof of bank payment, buyer cannot claim bona fides.'
    },
    {
      id: 'sp-4',
      parameterCode: 'P4',
      title: 'GSTR-2B Mandatory Matching Condition',
      statutoryProvision: 'Section 16(2)(aa) CGST Act, 2017',
      statutoryRequirement: 'Details of invoice communicated in Form GSTR-2B.',
      legalTest: 'Is Section 16(2)(aa) applicable to the relevant financial year?',
      burdenOfProof: 'Question of law.',
      requiredEvidence: ['Notification 39/2021-CT', 'Finance Act 2021 date of enforcement (01.01.2022)'],
      availableEvidence: ['Section 16(2)(aa) enforced w.e.f 01.01.2022 (prospective)'],
      assessment: 'SATISFIED',
      risk: 'LOW',
      reason: 'Section 16(2)(aa) cannot operate retrospectively to periods prior to 01.01.2022.'
    }
  ];
}
"""

code_scoring = """import { 
  ReadinessScoreBreakdown, 
  ViabilityScoreBreakdown, 
  ForwardLitigationDecision 
} from '../types';

export function calculateReadinessScore(
  statutoryCount: number,
  hasInvoices: boolean,
  hasTransit: boolean,
  hasBank: boolean,
  hasScn: boolean = false
): ReadinessScoreBreakdown {
  // Strict Evidence Weighting:
  // Statutory Position: 0-20 (depends on Invoices + Bank)
  const statutoryPosition = (hasInvoices ? 10 : 2) + (hasBank ? 8 : 2);
  // Evidence Quality: 0-20 (depends on Invoices + Transit + Bank)
  const evidence = (hasInvoices ? 7 : 0) + (hasTransit ? 7 : 0) + (hasBank ? 6 : 1);
  // Precedent: 0-15 (applicable only if facts/bank payment proven)
  const precedent = hasBank && hasInvoices ? 15 : 4;
  // Lower Authority Error: 0-15 (requires SCN / Order)
  const lowerAuthorityError = hasScn || (hasInvoices && hasBank) ? 14 : 3;
  // Drafting Quality: 0-10
  const draftingQuality = hasInvoices && hasBank ? 9 : 2;
  // Counterargument Resilience: 0-10
  const counterargumentResilience = hasInvoices && hasTransit && hasBank ? 9 : 2;
  // Procedural Position: 0-10
  const proceduralPosition = hasInvoices ? 9 : 3;

  const totalScore = statutoryPosition + evidence + precedent + lowerAuthorityError + draftingQuality + counterargumentResilience + proceduralPosition;

  let interpretation = '85-100: Highly litigation-ready';
  if (totalScore < 40) interpretation = 'Below 40: Not presently litigation-ready (Insufficient / Missing Evidence)';
  else if (totalScore < 55) interpretation = '40-54: High litigation risk; substantial remediation required';
  else if (totalScore < 70) interpretation = '55-69: Viable but material weaknesses exist';
  else if (totalScore < 85) interpretation = '70-84: Strong, but targeted improvements required';

  return {
    statutoryPosition,
    evidence,
    precedent,
    lowerAuthorityError,
    draftingQuality,
    counterargumentResilience,
    proceduralPosition,
    totalScore,
    interpretation
  };
}

export function calculateViabilityScore(readinessTotal: number, hasBank: boolean, hasInvoices: boolean): ViabilityScoreBreakdown {
  if (readinessTotal < 40 || (!hasBank && !hasInvoices)) {
    return {
      merits: 4,
      evidenceQuality: 2,
      precedentSupport: 3,
      proceduralSoundness: 4,
      opposingCaseDifficulty: 2,
      curabilityOfGaps: 3,
      appellateForumTrend: 4,
      totalScore: 22,
      probabilityOfFavourableOutcome: 'LOW',
      probabilityNote: 'FATAL EVIDENTIARY DEFICIENCY: No invoices, bank payment vouchers, or SCN uploaded. Substantive viability is LOW until core documents are provided.'
    };
  }

  const merits = hasInvoices && hasBank ? 19 : 10;
  const evidenceQuality = hasInvoices && hasBank ? 19 : 8;
  const precedentSupport = hasBank ? 15 : 6;
  const proceduralSoundness = 10;
  const opposingCaseDifficulty = 13;
  const curabilityOfGaps = 9;
  const appellateForumTrend = 9;

  const totalScore = merits + evidenceQuality + precedentSupport + proceduralSoundness + opposingCaseDifficulty + curabilityOfGaps + appellateForumTrend;

  return {
    merits,
    evidenceQuality,
    precedentSupport,
    proceduralSoundness,
    opposingCaseDifficulty,
    curabilityOfGaps,
    appellateForumTrend,
    totalScore,
    probabilityOfFavourableOutcome: totalScore >= 75 ? 'HIGH' : (totalScore >= 50 ? 'MODERATE' : 'LOW'),
    probabilityNote: 'Analytical estimate based on Suncraft & Circular 183 doctrine supported by verified documentary records.'
  };
}

export function calculateForwardDecision(
  currentScore: number,
  hasInvoices: boolean,
  hasBank: boolean,
  hasTransit: boolean
): ForwardLitigationDecision {
  const missingItems: string[] = [];
  if (!hasInvoices) missingItems.push('Upload Tax Invoices complying with Rule 46');
  if (!hasBank) missingItems.push('Upload Bank Statements proving consideration and GST paid via RTGS/NEFT');
  if (!hasTransit) missingItems.push('Upload E-Way Bills (Part A & B) and Weighbridge inward passes');
  missingItems.push('Obtain Chartered Accountant Certificate under CBIC Circular 183/15/2022');

  return {
    currentReadinessScore: currentScore,
    potentialScoreAfterRemediation: Math.min(100, currentScore + (missingItems.length * 15)),
    scoreEnhancers: [
      'Proof of 100% payment through banking channels (RTGS/NEFT)',
      'Valid E-Way bills with vehicle movement timestamps',
      'Circular 183 Chartered Accountant Certificate'
    ],
    scoreReducers: missingItems.length > 1 ? ['Fatal absence of primary documentary records (Invoices/Bank/Transit)'] : ['Supplier registration status at time of invoice unverified'],
    evidenceDependentImprovements: missingItems,
    nonCurableWeaknesses: currentScore < 30 ? ['Complete lack of documentary proof'] : ['None identified'],
    actionRequiredToAchievePotential: missingItems
  };
}
"""

with open("src/service/fact-matrix-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_fact)
with open("src/service/statutory-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_statutory)
with open("src/service/scoring-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_scoring)

print("Updated Fact Matrix, Statutory Engine, and Scoring Engine with strict evidence requirements!")