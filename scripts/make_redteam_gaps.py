import os

code_rt = """import { AdversarialRedTeamItem } from '../types';

export function runAdversarialRedTeamAnalysis(): AdversarialRedTeamItem[] {
  return [
    {
      id: 'rt-1',
      category: 'Statutory Non-Obstante Override',
      opposingArgument: 'Section 16(2) begins with "Notwithstanding anything contained in this section...". Clause (c) unequivocally mandates that tax charged must actually be paid to the Government treasury. In fiscal interpretation, literal meaning must prevail without equitable relief.',
      strengthOfOpposingArgument: 82,
      taxpayerResponse: 'While Section 16(2) contains a non-obstante clause, the statutory doctrine of impossibility ("lex non cogit ad impossibilia") is a recognized canon of statutory construction in tax jurisprudence (Arise India v. CTT, upheld by SC). A buyer who paid tax to a registered seller cannot be compelled to perform the impossible task of ensuring seller remits tax to the treasury.',
      evidenceSupportingResponse: 'Bank RTGS receipts, Supplier GSTR-1 upload extract, and CA certificate under Circular 183.',
      residualRisk: 'LOW',
      survivesAttack: true
    },
    {
      id: 'rt-2',
      category: 'Burden of Proof under Section 155',
      opposingArgument: 'Under Section 155 CGST Act, the burden of proving that ITC has been lawfully availed lies squarely on the person claiming it. Merely producing an invoice and a bank payment advice does not discharge the burden of proving that tax reached the government.',
      strengthOfOpposingArgument: 76,
      taxpayerResponse: 'The taxpayer discharges the initial burden by demonstrating invoice, physical movement (E-way bill), and bank payment. Under Section 106 of the Indian Evidence Act, facts within the exclusive knowledge of the Department (whether supplier paid GSTR-3B tax) shift the burden to the Revenue.',
      evidenceSupportingResponse: 'Section 106 Indian Evidence Act, 1872 & CBIC Circular 183/15/2022.',
      residualRisk: 'LOW',
      survivesAttack: true
    },
    {
      id: 'rt-3',
      category: 'Circular Invoicing & Sub-Tier Shell Allegation',
      opposingArgument: 'Upstream investigation reveals that 2nd-tier suppliers were dummy entities without physical godowns. The taxpayer is part of an artificial credit chain.',
      strengthOfOpposingArgument: 80,
      taxpayerResponse: 'The direct supplier was active and registered on the date of transaction. Taxpayer physically consumed the goods in manufacturing and exported finished products under customs supervision. Retrospective cancellation of upstream entities cannot taint genuine purchases (LGW Industries v. UOI).',
      evidenceSupportingResponse: 'Cost Auditor Input-Output Certificate, Shipping Bills, and Electronic Weighbridge Gate Passes.',
      residualRisk: 'MEDIUM',
      survivesAttack: true
    },
    {
      id: 'rt-4',
      category: 'Lack of Transporter Physical Corroboration',
      opposingArgument: 'Transporter bilty lacks vehicle toll FASTag records and driver signature, suggesting goods transit was non-existent.',
      strengthOfOpposingArgument: 70,
      taxpayerResponse: 'E-Way bills were generated in Part-A and Part-B with valid registration numbers. No vehicle interception or adverse report was recorded during transit. Inward gate passes and store consumption prove physical delivery.',
      evidenceSupportingResponse: 'Part-B E-Way bills with timestamp, Store Inward Gate Registers.',
      residualRisk: 'LOW',
      survivesAttack: true
    }
  ];
}
"""

code_gaps = """import { EvidenceGapItem } from '../types';

export function analyzeEvidenceGaps(): EvidenceGapItem[] {
  return [
    {
      id: 'eg-1',
      missingEvidence: 'Chartered Accountant Certificate in terms of Circular No. 183/15/2022-GST confirming supplier non-payment was not fraudulent.',
      legalRelevance: 'CBIC Circular 183 provides a statutory safe harbor for FY 2017-18 and 2018-19 mismatches where difference exceeds Rs. 5 Lakhs.',
      whyItMatters: 'Mandatory under CBIC guidelines to compel First Appellate Authority to grant relief without requiring High Court intervention.',
      possibleSource: 'Statutory Auditor of Supplier or Taxpayer CA.',
      impactIfObtained: 'Converts assessment to 100% compliant with CBIC binding circular.',
      impactIfUnavailable: 'Appellant must rely solely on High Court judicial precedents.',
      priority: 'CRITICAL',
      category: 'Should be obtained'
    },
    {
      id: 'eg-2',
      missingEvidence: 'GST Portal Active Registration Status Screenshot on Invoice Dates.',
      legalRelevance: 'Establishes that supplier was fully registered when invoices were issued, invoking LGW Industries doctrine against retrospective cancellation.',
      whyItMatters: 'Defeats departmental argument that buyer dealt with an unregistered or cancelled dealer.',
      possibleSource: 'GST Portal "Search Taxpayer" audit history.',
      impactIfObtained: 'Conclusive evidence of bona fides on invoice date.',
      impactIfUnavailable: 'Risk of Revenue alleging buyer failed to exercise KYC due diligence.',
      priority: 'HIGH',
      category: 'Exists but not relied upon'
    },
    {
      id: 'eg-3',
      missingEvidence: 'NHAI FASTag Toll Transit logs for commercial vehicles.',
      legalRelevance: 'Decisively corroborates physical movement of goods through toll plazas.',
      whyItMatters: 'Eliminates any residual doubt regarding phantom vehicle movement.',
      possibleSource: 'Transporter / NHAI NETC portal.',
      impactIfObtained: 'Demolishes bogus transport allegations.',
      impactIfUnavailable: 'Secondary reliance on E-Way bills and inward gate passes.',
      priority: 'MEDIUM',
      category: 'Should be obtained'
    }
  ];
}
"""

with open("src/service/adversarial-redteam-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_rt)
with open("src/service/evidence-gap-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_gaps)
print("Wrote redteam-engine.ts & evidence-gap-engine.ts")