import os

code_precedents = """import { PrecedentAnalysis } from '../types';

export const BENCHMARK_PRECEDENTS: PrecedentAnalysis[] = [
  {
    id: 'prec-suncraft',
    caseName: 'Suncraft Energy Pvt. Ltd. v. Assistant Commissioner of State Tax',
    court: 'Calcutta High Court (Affirmed by Supreme Court in SLP (C) No. 27927/2023)',
    citation: '(2023) 9 Centax 48 (Cal.) / 2023-VIL-489-CAL',
    relevantProvision: 'Section 16(2)(c) CGST Act, 2017 & Press Release dt 04.05.2018',
    materialFacts: 'Purchaser claimed ITC. Supplier defaulted in depositing tax in GSTR-3B despite uploading in GSTR-1. Revenue demanded reversal from purchaser without inquiring into or pursuing the seller.',
    ratioLegalPrinciple: 'Before directing the recipient to reverse ITC or paying the tax, the proper officer should first proceed against the selling dealer. Only in exceptional cases of collusion or missing seller can recipient be directly fastened with liability.',
    necessaryConditions: [
      'Purchaser is bona fide and has genuine tax invoices',
      'Purchaser paid full consideration and tax through banking channels',
      'Supplier reported transaction in GSTR-1',
      'Revenue took no recovery steps or summons against supplier'
    ],
    distinguishingFacts: ['None if seller was registered on the invoice date and tax was paid through bank.'],
    favourableApplicability: 'HIGH',
    adverseApplicability: 'NONE',
    parameterExtracted: 'Department must exhaust all recovery proceedings against the defaulting supplier before demanding tax from the purchasing recipient.',
    presentCaseEvidenceSatisfying: ['Invoices', 'RTGS bank statements', 'GSTR-1 data', 'Impugned order showing no action on seller'],
    presentCaseEvidenceFailing: [],
    litigationUse: 'Primary binding anchor in appeals and writ petitions for Section 16(2)(c) recovery challenges.',
    comparabilityScore: {
      statutorySimilarity: 20,
      factualSimilarity: 25,
      evidentiarySimilarity: 20,
      proceduralSimilarity: 10,
      courtAuthorityRelevance: 15,
      distinguishabilityRisk: 10,
      totalScore: 100,
      explanation: 'Supreme Court affirmed binding precedent directly addressing supplier default under Section 16(2)(c).'
    }
  },
  {
    id: 'prec-beathel',
    caseName: 'D.Y. Beathel Enterprises v. State Tax Officer',
    court: 'Madras High Court',
    citation: '(2021) 127 taxmann.com 80 (Mad.) / 2021-VIL-230-MAD',
    relevantProvision: 'Section 16(2)(c) CGST Act & Section 73/74',
    materialFacts: 'Sellers omitted to pay tax collected from buyer. Department issued orders against purchasing dealers without examining the sellers.',
    ratioLegalPrinciple: 'When the sellers have collected tax, the Proper Officer is bound to initiate recovery against the sellers and examine them in inquiry before burdening the purchasing dealer.',
    necessaryConditions: ['Tax collected by supplier in invoice', 'Purchaser paid consideration through bank'],
    distinguishingFacts: ['None.'],
    favourableApplicability: 'HIGH',
    adverseApplicability: 'NONE',
    parameterExtracted: 'Seller examination and recovery is a mandatory condition precedent before recipient reversal.',
    presentCaseEvidenceSatisfying: ['Bank payment proof', 'CA Certificate of payment'],
    presentCaseEvidenceFailing: [],
    litigationUse: 'Secondary binding authority on jurisdictional condition precedent.',
    comparabilityScore: {
      statutorySimilarity: 20,
      factualSimilarity: 24,
      evidentiarySimilarity: 19,
      proceduralSimilarity: 10,
      courtAuthorityRelevance: 14,
      distinguishabilityRisk: 9,
      totalScore: 96,
      explanation: 'Extremely high comparability; establishes duty of officer to recover from seller first.'
    }
  },
  {
    id: 'prec-arise',
    caseName: 'Arise India Ltd. v. Commissioner of Trade & Taxes',
    court: 'Delhi High Court (Affirmed by Supreme Court in SLP (C) No. 36717/2017)',
    citation: '(2017) 103 VST 477 (Del.)',
    relevantProvision: 'Bona Fide Buyer Protection & Impossibility of Performance (Lex Non Cogit Ad Impossibilia)',
    materialFacts: 'Purchasing dealer verified registration of selling dealer and paid price + tax through banking channels. Selling dealer failed to deposit tax.',
    ratioLegalPrinciple: 'A purchasing dealer who has acted bona fide cannot be expected to know whether the selling dealer would deposit the tax or not. Denying ITC to a bona fide purchaser for seller default is arbitrary and unconstitutional under Article 14.',
    necessaryConditions: ['Valid invoice', 'Payment through banking channels', 'Active supplier registration at transaction date'],
    distinguishingFacts: ['None.'],
    favourableApplicability: 'HIGH',
    adverseApplicability: 'NONE',
    parameterExtracted: 'Bona fide purchaser cannot be penalized for subsequent default of registered seller.',
    presentCaseEvidenceSatisfying: ['Valid Tax Invoices', 'Bank Statements'],
    presentCaseEvidenceFailing: [],
    litigationUse: 'Constitutional basis against arbitrary ITC disallowances.',
    comparabilityScore: {
      statutorySimilarity: 19,
      factualSimilarity: 23,
      evidentiarySimilarity: 19,
      proceduralSimilarity: 10,
      courtAuthorityRelevance: 15,
      distinguishabilityRisk: 8,
      totalScore: 94,
      explanation: 'Supreme Court affirmed landmark ruling on the doctrine of impossibility.'
    }
  },
  {
    id: 'prec-lgw',
    caseName: 'LGW Industries Limited v. Union of India',
    court: 'Calcutta High Court',
    citation: '(2022) 134 taxmann.com 42 (Cal.)',
    relevantProvision: 'Section 16(2)(c) & Retrospective Cancellation of Supplier Registration',
    materialFacts: 'ITC denied on grounds that supplier registration was cancelled retrospectively by Revenue after invoice date.',
    ratioLegalPrinciple: 'If at the time of transaction the supplier was registered and active on the GST portal, retrospective cancellation of supplier cannot be a ground to deny ITC to the genuine purchaser.',
    necessaryConditions: ['Active portal status at invoice date', 'Genuine movement of goods', 'Bank payment'],
    distinguishingFacts: ['None.'],
    favourableApplicability: 'HIGH',
    adverseApplicability: 'NONE',
    parameterExtracted: 'Retrospective cancellation cannot extinguish accrued ITC of bona fide purchaser.',
    presentCaseEvidenceSatisfying: ['Invoices and GST Portal registration logs'],
    presentCaseEvidenceFailing: [],
    litigationUse: 'Defense against retrospective cancellation allegations.',
    comparabilityScore: {
      statutorySimilarity: 19,
      factualSimilarity: 24,
      evidentiarySimilarity: 18,
      proceduralSimilarity: 9,
      courtAuthorityRelevance: 13,
      distinguishabilityRisk: 9,
      totalScore: 92,
      explanation: 'Directly on point for cases involving retrospective supplier cancellation.'
    }
  }
];

export function getApplicablePrecedents(primaryIssue: string, financialYear: string): PrecedentAnalysis[] {
  return BENCHMARK_PRECEDENTS;
}
"""

with open("src/service/precedent-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_precedents)

print("Updated precedent-engine.ts with expanded precedent suite!")