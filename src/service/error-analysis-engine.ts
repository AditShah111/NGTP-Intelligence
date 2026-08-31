import { LowerAuthorityError } from '../types';

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
