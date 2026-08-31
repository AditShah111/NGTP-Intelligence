import os

code = """import { PrecedentAnalysis } from '../types';

export function getApplicablePrecedents(primaryIssue: string, financialYear: string): PrecedentAnalysis[] {
  return [
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
    }
  ];
}
"""
with open("src/service/precedent-engine.ts", "w", encoding="utf-8") as f:
    f.write(code)
print("Wrote precedent-engine.ts")