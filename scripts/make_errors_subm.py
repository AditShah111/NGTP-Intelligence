import os

code_err = """import { LowerAuthorityError } from '../types';

export function analyzeLowerAuthorityErrors(
  noticeType: string,
  primaryIssue: string
): LowerAuthorityError[] {
  return [
    {
      id: 'err-1',
      finding: 'Disallowance of ITC solely based on GSTR-2A vs GSTR-3B mismatch.',
      lowerAuthorityReasoning: 'Supplier did not deposit tax in GSTR-3B; hence Section 16(2)(c) condition is violated and credit must be reversed by buyer.',
      evidenceIgnoredMisread: 'Ignored valid tax invoices, E-way bills, bank RTGS statements, and ledger reconciliations submitted in reply.',
      legalError: 'Failed to follow binding Supreme Court affirmed Calcutta HC ruling in Suncraft Energy and CBIC Circular No. 183/15/2022-GST.',
      relevantAuthority: 'Suncraft Energy (Cal HC / SC) & Circular No. 183/15/2022-GST',
      strength: 'Fundamental'
    },
    {
      id: 'err-2',
      finding: 'Failure to initiate inquiry or recovery against defaulting selling dealer.',
      lowerAuthorityReasoning: 'Adjudicating Officer chose easy recovery path against purchasing beneficiary without issuing summons or recovery notices to supplier.',
      evidenceIgnoredMisread: 'Ignored supplier GSTR-1 upload status which confirmed supplier acknowledged liability.',
      legalError: 'Breach of condition precedent established by Madras HC in D.Y. Beathel Enterprises.',
      relevantAuthority: 'D.Y. Beathel Enterprises (Mad HC)',
      strength: 'Fundamental'
    },
    {
      id: 'err-3',
      finding: 'Mechanical imposition of maximum penalty under Section 73 / 74.',
      lowerAuthorityReasoning: 'Availment of mismatched credit automatically treated as improper claim attracting statutory penalty.',
      evidenceIgnoredMisread: 'Ignored complete absence of mens rea, fraud, or intentional evasion by the taxpayer.',
      legalError: 'Penalty cannot be levied mechanically in absence of deliberate defiance of law or fraud.',
      relevantAuthority: 'Hindustan Steel Ltd. v. State of Orissa (1969) 2 SCC 627 (SC)',
      strength: 'Serious'
    }
  ];
}
"""

code_sub = """import { ImprovedSubmissionGround } from '../types';

export function improveSubmissions(primaryIssue: string): ImprovedSubmissionGround[] {
  return [
    {
      groundNumber: 'Ground 1',
      title: 'Recovery from Recipient without Exhausting Remedies against Selling Dealer is Illegal and Unenforceable',
      proposition: 'The Adjudicating Authority erred in demanding tax from the Appellant under Section 16(2)(c) without first initiating any recovery proceedings against the defaulting supplier.',
      supportingFacts: [
        'Appellant purchased goods under genuine tax invoices.',
        'Appellant paid full consideration including GST through RTGS banking channels.',
        'Supplier reported invoices in GSTR-1 which populated in GSTR-2A.',
        'Department has not issued DRC-01 or attached assets of the supplier.'
      ],
      evidence: ['Annexure A-1 (Invoices)', 'Annexure A-2 (Bank Statements)', 'Annexure A-3 (GSTR-2A)'],
      statutoryBasis: 'Section 16(2)(c) CGST Act read with Press Release dated 04.05.2018',
      precedent: 'Suncraft Energy Pvt. Ltd. (Cal HC, affirmed by SC in SLP 27927/2023) & D.Y. Beathel Enterprises (Mad HC)',
      application: 'The Appellant is an innocent bona fide purchaser. Under established law, the Department cannot shift the collection burden onto the buyer without exhausting remedies against the supplier.',
      likelyRevenueCounterargument: 'Section 16(2)(c) is a non-negotiable statutory condition precedent; if tax is not deposited in the government treasury, no credit can be allowed regardless of bona fides (citing ALD Automotive / Bharti Telemedia).',
      response: 'The Honble Supreme Court in Suncraft Energy has specifically settled this issue under the CGST Act, 2017. Furthermore, CBIC Circular 183/15/2022-GST provides that for FY 2017-18 and 2018-19, where supplier has filed GSTR-1 and buyer produces CA Certificate / Bank proof, ITC cannot be denied.',
      residualWeakness: 'If the supplier GSTIN is found to be non-existent or cancelled ab-initio.',
      groundStrength: 94
    },
    {
      groundNumber: 'Ground 2',
      title: 'Prospective Applicability of Section 16(2)(aa) & Entitlement to Circular 183 Safe-Harbor',
      proposition: 'The Proper Officer erred in applying GSTR-2B mandatory matching condition to periods prior to 01.01.2022 and in ignoring CBIC Circular 183/15/2022-GST.',
      supportingFacts: [
        'Invoices pertain to periods prior to 01.01.2022 when GSTR-2A was purely a view facility.',
        'Taxpayer satisfies all conditions of Circular 183/15/2022-GST paragraph 4.'
      ],
      evidence: ['GSTR-2A portal extract', 'Circular 183 Chartered Accountant Certificate'],
      statutoryBasis: 'Section 16(2)(aa) CGST Act (w.e.f. 01.01.2022) & Circular No. 183/15/2022-GST',
      precedent: 'M. Trade Links v. UOI (Ker HC) & Diya Agencies (Ker HC)',
      application: 'Substantive amendments creating new restrictions cannot operate retrospectively. Circular 183 is binding on Departmental officers.',
      likelyRevenueCounterargument: 'Circular 183 only applies if the taxpayer produces verification certificates from the supplier auditor.',
      response: 'Appellant has duly tendered the requisite CA certificate certifying tax payment.',
      residualWeakness: 'Requires physical procurement and signing of CA Certificate.',
      groundStrength: 91
    },
    {
      groundNumber: 'Ground 3',
      title: 'Quashing of Penalty under Section 73(9) / 74(9) in Absence of Mens Rea',
      proposition: 'The Adjudicating Authority erred in mechanically imposing penalty without establishing any fraud, suppression, or willful misstatement.',
      supportingFacts: [
        'Taxpayer disclosed all transactions in regular GSTR-3B returns.',
        'No clandestine removal or unaccounted cash trail discovered.'
      ],
      evidence: ['Audited Financial Accounts', 'GSTR-3B filings'],
      statutoryBasis: 'Section 73(9) / 74(1) CGST Act, 2017',
      precedent: 'Hindustan Steel Ltd. (SC) & Uniworth Textiles (SC)',
      application: 'Penalty cannot be imposed as a matter of course. Bona fide availment of credit in terms of statutory returns negates mens rea.',
      likelyRevenueCounterargument: 'Under GST statutory scheme, incorrect availment of ITC attracts mandatory minimum penalty.',
      response: 'Settled jurisprudence of the Honble Supreme Court dictates that quasi-judicial penalty requires culpable mental state.',
      residualWeakness: 'None.',
      groundStrength: 89
    }
  ];
}
"""

with open("src/service/error-analysis-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_err)
with open("src/service/submission-optimizer.ts", "w", encoding="utf-8") as f:
    f.write(code_sub)
print("Wrote error-analysis-engine.ts & submission-optimizer.ts")