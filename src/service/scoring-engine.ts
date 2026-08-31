import { 
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
