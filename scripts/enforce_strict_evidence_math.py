import os

code_scoring_strict = """import { 
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
  // Strict Evidence-Gated Scoring Matrix:
  
  // 1. Statutory Position (Max 20):
  // Requires both invoices (16(2)(a)) AND bank payment (2nd proviso & 16(2)(c))
  let statutoryPosition = 2;
  if (hasInvoices && hasBank && hasTransit) statutoryPosition = 20;
  else if (hasInvoices && hasBank) statutoryPosition = 14;
  else if (hasInvoices) statutoryPosition = 6;
  else if (hasBank) statutoryPosition = 5;

  // 2. Evidence Quality (Max 20):
  // 7 pts for Invoices, 7 pts for Bank RTGS, 6 pts for E-Way Bills
  let evidence = 1;
  if (hasInvoices && hasBank && hasTransit) evidence = 20;
  else if (hasInvoices && hasBank) evidence = 13;
  else if (hasInvoices && hasTransit) evidence = 11;
  else if (hasInvoices) evidence = 5;
  else if (hasBank) evidence = 6;

  // 3. Precedent Support (Max 15):
  // Suncraft and D.Y. Beathel CANNOT be applied without genuine bank payment proof!
  let precedent = 2;
  if (hasInvoices && hasBank && hasTransit) precedent = 15;
  else if (hasInvoices && hasBank) precedent = 12;
  else if (hasInvoices) precedent = 3; // Invoices alone cannot invoke Suncraft

  // 4. Lower Authority Error Audit (Max 15):
  // Cannot audit officer errors without actual SCN / DRC-07 order!
  let lowerAuthorityError = 2;
  if (hasScn && hasInvoices && hasBank) lowerAuthorityError = 15;
  else if (hasScn) lowerAuthorityError = 8;
  else if (hasInvoices && hasBank) lowerAuthorityError = 7;
  else if (hasInvoices) lowerAuthorityError = 2;

  // 5. Drafting Quality (Max 10):
  let draftingQuality = 2;
  if (hasInvoices && hasBank && hasTransit) draftingQuality = 10;
  else if (hasInvoices && hasBank) draftingQuality = 6;
  else if (hasInvoices) draftingQuality = 2;

  // 6. Counterargument Resilience (Max 10):
  // Invoices alone immediately collapse against fake-transit and non-payment attacks
  let counterargumentResilience = 1;
  if (hasInvoices && hasBank && hasTransit) counterargumentResilience = 10;
  else if (hasInvoices && hasBank) counterargumentResilience = 5;
  else if (hasInvoices) counterargumentResilience = 2;

  // 7. Procedural Position (Max 10):
  let proceduralPosition = 2;
  if (hasScn && hasInvoices) proceduralPosition = 10;
  else if (hasInvoices) proceduralPosition = 3;

  const totalScore = statutoryPosition + evidence + precedent + lowerAuthorityError + draftingQuality + counterargumentResilience + proceduralPosition;

  let interpretation = '85-100: Highly litigation-ready';
  if (totalScore < 40) interpretation = 'Below 40: Not presently litigation-ready (Missing Bank RTGS & Transit Proof)';
  else if (totalScore < 60) interpretation = '40-59: High litigation risk; attach bank payment & delivery records';
  else if (totalScore < 75) interpretation = '60-74: Viable but requires supporting transit & CA certificate';
  else if (totalScore < 85) interpretation = '75-84: Strong, but targeted improvements required';

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

export function calculateViabilityScore(readinessTotal: number, hasBank: boolean, hasInvoices: boolean, hasTransit: boolean = false): ViabilityScoreBreakdown {
  if (readinessTotal < 40 || !hasBank) {
    return {
      merits: hasInvoices ? 8 : 3,
      evidenceQuality: hasInvoices ? 6 : 2,
      precedentSupport: 3,
      proceduralSoundness: 4,
      opposingCaseDifficulty: 2,
      curabilityOfGaps: 3,
      appellateForumTrend: 4,
      totalScore: hasInvoices ? 30 : 21,
      probabilityOfFavourableOutcome: 'LOW',
      probabilityNote: !hasBank 
        ? 'CRITICAL DEFICIENCY: Bank payment proof is absent. Suncraft Energy bona fide buyer doctrine CANNOT be invoked without RTGS/NEFT payment evidence.' 
        : 'FATAL DEFICIENCY: No core documents uploaded.'
    };
  }

  const merits = hasInvoices && hasBank && hasTransit ? 20 : (hasInvoices && hasBank ? 14 : 9);
  const evidenceQuality = hasInvoices && hasBank && hasTransit ? 20 : (hasInvoices && hasBank ? 13 : 8);
  const precedentSupport = hasBank ? 15 : 4;
  const proceduralSoundness = 10;
  const opposingCaseDifficulty = hasTransit ? 13 : 8;
  const curabilityOfGaps = 8;
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
  if (!hasBank) missingItems.push('Upload Bank Statements proving consideration and GST paid via RTGS/NEFT (P0 MANDATORY)');
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
    scoreReducers: !hasBank ? ['Fatal absence of bank payment vouchers (precludes Suncraft reliance)'] : (missingItems.length > 1 ? ['Absence of physical transit records'] : ['Supplier registration status at time of invoice unverified']),
    evidenceDependentImprovements: missingItems,
    nonCurableWeaknesses: currentScore < 30 ? ['Complete lack of documentary proof'] : ['None identified'],
    actionRequiredToAchievePotential: missingItems
  };
}
"""

with open("src/service/scoring-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_scoring_strict)

print("Updated scoring-engine.ts with strict evidence gating!")