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
  // Strict Evidence-Gated Scoring Matrix:
  
  // 1. Statutory Position (Max 20):
  // Requires invoices (16(2)(a)), physical movement (16(2)(b)), and bank payment (2nd proviso)
  let statutoryPosition = 2;
  if (hasInvoices && hasBank && hasTransit) statutoryPosition = 20;
  else if (hasInvoices && hasBank) statutoryPosition = 10; // Penalized: Missing Section 16(2)(b) transit
  else if (hasInvoices && hasTransit) statutoryPosition = 8;
  else if (hasInvoices) statutoryPosition = 5;
  else if (hasBank) statutoryPosition = 4;

  // 2. Evidence Quality (Max 20):
  let evidence = 1;
  if (hasInvoices && hasBank && hasTransit) evidence = 20;
  else if (hasInvoices && hasBank) evidence = 8; // Heavy penalty for missing E-Way bills & weighment
  else if (hasInvoices && hasTransit) evidence = 9;
  else if (hasInvoices) evidence = 4;
  else if (hasBank) evidence = 4;

  // 3. Precedent Support (Max 15):
  // Suncraft and Halder Enterprises require bona fide physical receipt of goods!
  let precedent = 2;
  if (hasInvoices && hasBank && hasTransit) precedent = 15;
  else if (hasInvoices && hasBank) precedent = 7; // Suncraft weakened if physical receipt is disputed
  else if (hasInvoices) precedent = 3;

  // 4. Lower Authority Error Audit (Max 15):
  let lowerAuthorityError = 2;
  if (hasScn && hasInvoices && hasBank && hasTransit) lowerAuthorityError = 15;
  else if (hasScn && hasInvoices && hasBank) lowerAuthorityError = 10;
  else if (hasScn) lowerAuthorityError = 6;
  else if (hasInvoices && hasBank) lowerAuthorityError = 5;
  else if (hasInvoices) lowerAuthorityError = 2;

  // 5. Drafting Quality (Max 10):
  let draftingQuality = 2;
  if (hasInvoices && hasBank && hasTransit) draftingQuality = 10;
  else if (hasInvoices && hasBank) draftingQuality = 5;
  else if (hasInvoices) draftingQuality = 2;

  // 6. Counterargument Resilience (Max 10):
  // Without E-Way bills, case collapses under Section 74 circular trading attack
  let counterargumentResilience = 1;
  if (hasInvoices && hasBank && hasTransit) counterargumentResilience = 10;
  else if (hasInvoices && hasBank) counterargumentResilience = 3; // Fragile against fake-transit
  else if (hasInvoices) counterargumentResilience = 1;

  // 7. Procedural Position (Max 10):
  let proceduralPosition = 2;
  if (hasScn && hasInvoices && hasTransit) proceduralPosition = 10;
  else if (hasScn && hasInvoices) proceduralPosition = 7;
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

  const merits = hasInvoices && hasBank && hasTransit ? 20 : (hasInvoices && hasBank ? 9 : 5);
  const evidenceQuality = hasInvoices && hasBank && hasTransit ? 20 : (hasInvoices && hasBank ? 8 : 4);
  const precedentSupport = hasBank && hasTransit ? 15 : (hasBank ? 7 : 3);
  const proceduralSoundness = hasTransit ? 10 : 6;
  const opposingCaseDifficulty = hasTransit ? 13 : 4; // High vulnerability to circular trading attack
  const curabilityOfGaps = hasTransit ? 8 : 5;
  const appellateForumTrend = hasTransit ? 9 : 4;

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
