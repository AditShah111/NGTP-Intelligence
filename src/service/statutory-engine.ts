import { StatutoryParameter, CaseDocument } from '../types';

export function evaluateStatutoryParameters(
  financialYear: string,
  primaryIssue: string,
  hasInvoices: boolean,
  hasTransit: boolean,
  hasBank: boolean,
  hasScn: boolean = false
): StatutoryParameter[] {
  return [
    {
      id: 'sp-1',
      parameterCode: 'P1',
      title: 'Possession of Tax Invoice',
      statutoryProvision: 'Section 16(2)(a) CGST Act, 2017',
      statutoryRequirement: 'Registered person must be in possession of a valid tax invoice complying with Rule 46.',
      legalTest: 'Is a physical or digitally signed tax invoice available with all Rule 46 particulars?',
      burdenOfProof: 'Initial burden on Taxpayer under Section 155.',
      requiredEvidence: ['Tax Invoices', 'ERP Purchase Register'],
      availableEvidence: hasInvoices ? ['Tax Invoices on record'] : ['NONE SUBMITTED'],
      assessment: hasInvoices ? 'SATISFIED' : 'NOT SATISFIED',
      risk: hasInvoices ? 'LOW' : 'CRITICAL',
      reason: hasInvoices ? 'Valid tax invoice is attached.' : 'No tax invoices provided. Non-negotiable condition under Section 16(2)(a) is unmet.'
    },
    {
      id: 'sp-2',
      parameterCode: 'P2',
      title: 'Actual Receipt of Goods / Services',
      statutoryProvision: 'Section 16(2)(b) CGST Act, 2017',
      statutoryRequirement: 'Registered person must have actually received the goods or services.',
      legalTest: 'Is there contemporaneous proof of physical movement and delivery?',
      burdenOfProof: 'Taxpayer burden under Section 155.',
      requiredEvidence: ['E-Way Bills (Part A & B)', 'Lorry Receipts (LR)', 'Gate Inward Pass', 'Weighbridge Slips'],
      availableEvidence: hasTransit ? ['E-Way bills and inward delivery records'] : ['NONE SUBMITTED'],
      assessment: hasTransit ? 'SATISFIED' : 'NOT SATISFIED',
      risk: hasTransit ? 'LOW' : 'CRITICAL',
      reason: hasTransit ? 'Documentary transit trail is on record.' : 'No delivery or transit records provided. Serious risk of fake invoicing allegation.'
    },
    {
      id: 'sp-3',
      parameterCode: 'P3',
      title: 'Tax Actually Paid to Government',
      statutoryProvision: 'Section 16(2)(c) CGST Act, 2017',
      statutoryRequirement: 'Tax charged in respect of supply must be actually paid to the Government.',
      legalTest: 'Can ITC be recovered from buyer when supplier defaults, without first proceeding against supplier?',
      burdenOfProof: 'Revenue must establish seller default and attempt recovery from seller first (Suncraft / D.Y. Beathel).',
      requiredEvidence: ['Bank RTGS payment proof to supplier', 'GSTR-1 upload extract', 'DRC-01 issued to supplier'],
      availableEvidence: hasBank ? ['Bank RTGS payment advice', 'GSTR-1 status'] : ['NO BANK PROOF SUBMITTED'],
      assessment: hasBank ? 'PARTIALLY SATISFIED' : 'NOT SATISFIED',
      risk: hasBank ? 'MEDIUM' : 'CRITICAL',
      reason: hasBank ? 'Bona fide payment proven through bank channels; Suncraft doctrine applies.' : 'Without proof of bank payment, buyer cannot claim bona fides.'
    },
    {
      id: 'sp-4',
      parameterCode: 'P4',
      title: 'GSTR-2B Mandatory Matching Condition',
      statutoryProvision: 'Section 16(2)(aa) CGST Act, 2017',
      statutoryRequirement: 'Details of invoice communicated in Form GSTR-2B.',
      legalTest: 'Is Section 16(2)(aa) applicable to the relevant financial year?',
      burdenOfProof: 'Question of law.',
      requiredEvidence: ['Notification 39/2021-CT', 'Finance Act 2021 date of enforcement (01.01.2022)'],
      availableEvidence: ['Section 16(2)(aa) enforced w.e.f 01.01.2022 (prospective)'],
      assessment: 'SATISFIED',
      risk: 'LOW',
      reason: 'Section 16(2)(aa) cannot operate retrospectively to periods prior to 01.01.2022.'
    }
  ];
}
