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

  if (benchType.includes('Supreme Court Full') || benchType.includes('Constitution')) score = 100;
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
    const lowerCourt = (p.court || '').toLowerCase();
    const lowerName = (p.caseName || '').toLowerCase();
    const lowerCit = (p.citation || '').toLowerCase();

    // 1. Dynamically determine bench type
    let benchType: BenchType = p.benchType || 'High Court Division Bench';
    let benchStrength = p.benchStrength || 2;
    let slpStatus: SlpStatus = p.slpStatus || 'No SLP Filed';
    let article141Status: Article141Precedence = p.article141Status || 'HIGH_COURT_BINDING';

    if (lowerCourt.includes('supreme court') || lowerCourt.includes('sc') || lowerCit.includes('scc')) {
      if (lowerCourt.includes('full') || lowerCourt.includes('constitution') || benchStrength >= 3) {
        benchType = 'Supreme Court Full/Constitution Bench';
        benchStrength = 3;
      } else {
        benchType = 'Supreme Court Division Bench';
        benchStrength = 2;
      }
      article141Status = 'SUPREME_BINDING';
      slpStatus = 'Affirmed by Supreme Court';
    } else if (lowerCourt.includes('single')) {
      benchType = 'High Court Single Bench';
      benchStrength = 1;
    } else if (lowerCourt.includes('full')) {
      benchType = 'High Court Full Bench';
      benchStrength = 3;
    } else {
      benchType = 'High Court Division Bench';
      benchStrength = 2;
    }

    // Check if High Court decision was affirmed by SC
    if (lowerCourt.includes('affirmed by supreme court') || lowerName.includes('suncraft') || lowerName.includes('arise india')) {
      slpStatus = 'Affirmed by Supreme Court';
      article141Status = 'SUPREME_BINDING';
    } else if (lowerCourt.includes('tribunal') || lowerCourt.includes('cstat') || lowerCourt.includes('gstat')) {
      benchType = 'Appellate Tribunal (CESTAT / GSTAT)';
      article141Status = 'PERSUASIVE';
    }

    const authorityScore = calculateJudicialAuthorityStrength(benchType, slpStatus, benchStrength);

    // 2. Generate dynamic conflict analysis if precedent is a leading authority
    let conflictAnalysis = p.competingConflictAnalysis;
    if (!conflictAnalysis) {
      if (lowerName.includes('suncraft') || (article141Status === 'SUPREME_BINDING' && p.relevantProvision.includes('16(2)(c)'))) {
        conflictAnalysis = {
          conflictWith: 'Aastha Enterprises v. State of Bihar (Patna HC - Adverse to recipient)',
          conflictingCourt: 'Patna High Court (Division Bench)',
          conflictReason: 'Patna HC in Aastha Enterprises held that Section 16(2)(c) is an absolute condition precedent where recipient was denied ITC.',
          whyThisPrecedentPrevails: 'In Aastha Enterprises, the purchaser failed to prove banking payment and supplier registration on invoice date. Suncraft Energy was specifically affirmed by the Supreme Court in SLP (C) No. 27927/2023 on 14.12.2023, establishing the binding principle under Article 141 that Revenue must first exhaust remedies against the supplier.',
          article141Resolution: 'Supreme Court affirmation of Suncraft Energy controls all Section 16(2)(c) recovery actions across India.'
        };
      } else if (lowerName.includes('arise') || lowerName.includes('impossib')) {
        conflictAnalysis = {
          conflictWith: 'ALD Automotive Pvt. Ltd. (Supreme Court under TN VAT)',
          conflictingCourt: 'Supreme Court (Earlier 2-Judge Bench on statutory time-limits)',
          conflictReason: 'Revenue argues ALD Automotive dictates strict literal interpretation of tax conditions without equity.',
          whyThisPrecedentPrevails: 'Arise India establishes the constitutional doctrine of impossibility (Article 14) which was affirmed by the Supreme Court in SLP (C) No. 36717/2017. A bona fide buyer cannot be penalized for default of a registered seller beyond the buyer control.',
          article141Resolution: 'Supreme Court affirmation validates doctrine of impossibility under Article 14.'
        };
      } else if (lowerName.includes('lgw') || lowerName.includes('retrospective')) {
        conflictAnalysis = {
          conflictWith: 'Departmental Retrospective Cancellation Orders',
          conflictingCourt: 'State GST Adjudicating Authorities',
          conflictReason: 'Revenue cancels supplier registration retrospectively and attempts to extinguish buyer ITC retroactively.',
          whyThisPrecedentPrevails: 'LGW Industries (Cal HC) establishes that if the supplier was active and registered on the date of transaction, subsequent retrospective cancellation cannot invalidate genuine purchases.',
          article141Resolution: 'Protects bona fide accrued ITC against subsequent retrospective cancellations.'
        };
      }
    }

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
