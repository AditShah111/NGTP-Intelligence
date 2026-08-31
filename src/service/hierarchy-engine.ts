import { 
  PrecedentAnalysis, 
  BenchType, 
  Article141Precedence, 
  SlpStatus, 
  CompetingConflictAnalysis 
} from '../types';

export function calculateJudicialAuthorityStrength(
  benchType: BenchType,
  slpStatus: SlpStatus,
  benchStrength: number = 2
): number {
  let score = 70;

  if (benchType.includes('Supreme Court Full')) score = 100;
  else if (benchType.includes('Supreme Court Division')) score = 98;
  else if (benchType.includes('High Court Full')) score = 92;
  else if (benchType.includes('High Court Division')) score = 86;
  else if (benchType.includes('High Court Single')) score = 74;
  else score = 55;

  if (slpStatus === 'Affirmed by Supreme Court') {
    score = Math.max(score, 96);
  } else if (slpStatus === 'Stayed by Supreme Court') {
    score = Math.min(score, 45);
  } else if (slpStatus === 'Pending before Supreme Court') {
    score = Math.min(score, 80);
  }

  return score;
}

export function resolvePrecedentConflicts(
  precedents: PrecedentAnalysis[],
  hasBankProof: boolean
): PrecedentAnalysis[] {
  return precedents.map(p => {
    const isSuncraft = p.caseName.toLowerCase().includes('suncraft');
    const isArise = p.caseName.toLowerCase().includes('arise');
    const isBeathel = p.caseName.toLowerCase().includes('beathel');
    const isLgw = p.caseName.toLowerCase().includes('lgw');

    let benchType: BenchType = 'High Court Division Bench';
    let benchStrength = 2;
    let slpStatus: SlpStatus = 'No SLP Filed';
    let article141Status: Article141Precedence = 'HIGH_COURT_BINDING';
    let conflictAnalysis: CompetingConflictAnalysis | undefined = undefined;

    if (isSuncraft) {
      benchType = 'High Court Division Bench';
      slpStatus = 'Affirmed by Supreme Court';
      article141Status = 'SUPREME_BINDING';
      conflictAnalysis = {
        conflictWith: 'Aastha Enterprises v. State of Bihar (Patna HC - Adverse to recipient)',
        conflictingCourt: 'Patna High Court (Division Bench)',
        conflictReason: 'Patna HC in Aastha Enterprises held that Section 16(2)(c) is an absolute condition precedent where recipient was denied ITC.',
        whyThisPrecedentPrevails: 'In Aastha Enterprises, the purchaser failed to prove banking payment and supplier registration on invoice date. Suncraft Energy was specifically affirmed by the Supreme Court in SLP (C) No. 27927/2023 on 14.12.2023, establishing the binding principle under Article 141 that Revenue must first exhaust remedies against the supplier.',
        article141Resolution: 'Supreme Court affirmation of Suncraft Energy controls all Section 16(2)(c) recovery actions across India.'
      };
    } else if (isArise) {
      benchType = 'High Court Division Bench';
      slpStatus = 'Affirmed by Supreme Court';
      article141Status = 'SUPREME_BINDING';
      conflictAnalysis = {
        conflictWith: 'ALD Automotive Pvt. Ltd. (Supreme Court under TN VAT)',
        conflictingCourt: 'Supreme Court (Earlier 2-Judge Bench on statutory time-limits)',
        conflictReason: 'Revenue argues ALD Automotive dictates strict literal interpretation of tax conditions without equity.',
        whyThisPrecedentPrevails: 'Arise India establishes the constitutional doctrine of impossibility (Article 14) which was affirmed by the Supreme Court in SLP (C) No. 36717/2017. A bona fide buyer cannot be penalized for default of a registered seller beyond the buyer control.',
        article141Resolution: 'Supreme Court affirmation validates doctrine of impossibility under Article 14.'
      };
    } else if (isBeathel) {
      benchType = 'High Court Single Bench';
      benchStrength = 1;
      slpStatus = 'No SLP Filed';
      article141Status = 'HIGH_COURT_BINDING';
    } else if (isLgw) {
      benchType = 'High Court Single Bench';
      benchStrength = 1;
      slpStatus = 'No SLP Filed';
      article141Status = 'HIGH_COURT_BINDING';
    }

    const authorityScore = calculateJudicialAuthorityStrength(benchType, slpStatus, benchStrength);

    return {
      ...p,
      benchType,
      benchStrength,
      slpStatus,
      article141Status,
      judicialAuthorityStrengthScore: authorityScore,
      competingConflictAnalysis: conflictAnalysis
    };
  });
}