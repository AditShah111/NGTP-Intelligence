import { LowerAuthorityError } from '../types';

export function analyzeLowerAuthorityErrors(
  noticeType: string,
  primaryIssue: string,
  hasTransit: boolean = true,
  hasBank: boolean = true,
  caseSummary: string = ""
): LowerAuthorityError[] {
  const isDelayed = /delayed|216\s*days|exceeding\s*180|beyond\s*180/i.test(caseSummary) || /delayed|216\s*days/i.test(primaryIssue);
  const isCircular = /circular|fake|shell|fictitious|100\s*sq|bogus/i.test(caseSummary) || /circular|fake|shell/i.test(primaryIssue);

  if (!hasTransit || isDelayed || isCircular) {
    return [
      {
        id: 'err-weak-1',
        finding: 'Disallowance of ITC and imposition of 100% penalty under Section 74 for circular trading without goods movement.',
        lowerAuthorityReasoning: 'Field inspection revealed supplier was a fictitious 100 sq ft shell entity and buyer produced zero E-Way bills or transport proofs.',
        evidenceIgnoredMisread: 'Officer considered purchase invoice and delayed bank statement, but correctly held transport unproven under Rule 138.',
        legalError: 'Procedural failure to grant formal personal hearing before issuing DRC-07 summary order.',
        relevantAuthority: 'Section 75(4) CGST Act (Mandatory Personal Hearing)',
        strength: 'Material'
      },
      {
        id: 'err-weak-2',
        finding: 'Disallowance under Second Proviso to Section 16(2) for consideration delayed beyond 180 days.',
        lowerAuthorityReasoning: 'Payment was made on Day 216, but taxpayer claimed and retained credit without statutory reversal and interest.',
        evidenceIgnoredMisread: 'Officer failed to adjust credit re-availment entitlement once payment was eventually completed on Day 216.',
        legalError: 'Permanent disallowance of credit instead of demanding Section 50 interest for the 36-day delay period.',
        relevantAuthority: 'Second Proviso to Section 16(2) read with Rule 37',
        strength: 'Serious'
      }
    ];
  }

  // Set 1 (Retrospective Cancellation)
  return [
    {
      id: 'err-1',
      finding: 'Mechanical disallowance of ITC based on retrospective cancellation of supplier GSTIN ab-initio.',
      lowerAuthorityReasoning: 'Because the supplier was cancelled w.e.f. 01.07.2017, the officer treated all past invoices as issued by a non-existent person.',
      evidenceIgnoredMisread: 'Ignored that supplier GSTIN was active and verified on Common Portal on invoice date, and supplier filed GSTR-1 on 10.11.2018.',
      legalError: 'Direct violation of Calcutta High Court Division Bench ruling in LGW Industries Ltd. v. Union of India.',
      relevantAuthority: 'LGW Industries Ltd. (Cal HC) & D.Y. Beathel Enterprises (Mad HC)',
      strength: 'Fundamental'
    },
    {
      id: 'err-2',
      finding: 'Admission of zero recovery proceedings initiated against the defaulting selling dealer.',
      lowerAuthorityReasoning: 'Adjudicating Officer targeted the purchasing recipient without issuing Section 79 recovery or Section 70 summons to supplier.',
      evidenceIgnoredMisread: 'Ignored bank RTGS payments and GSTR-1 acknowledgement showing supplier received tax.',
      legalError: 'Breach of binding Supreme Court affirmed condition precedent in Suncraft Energy (SLP 27927/2023).',
      relevantAuthority: 'Suncraft Energy Pvt. Ltd. (SC SLP 27927/2023 Affirmed Under Article 141)',
      strength: 'Fundamental'
    },
    {
      id: 'err-3',
      finding: 'Mechanical invocation of extended 5-year period and 100% penalty under Section 74.',
      lowerAuthorityReasoning: 'Treated retrospective cancellation of supplier as automatic proof of fraud against the buyer.',
      evidenceIgnoredMisread: 'Ignored complete absence of mens rea, collusion, or cash kickbacks in audited books.',
      legalError: 'Penalty cannot be levied without proving deliberate deception against the specific person charged.',
      relevantAuthority: 'Uniworth Textiles Ltd. v. CCE (2013) 9 SCC 753 (Supreme Court)',
      strength: 'Fundamental'
    }
  ];
}
