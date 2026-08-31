import os

base = os.getcwd()

def write_file(rel_path, content):
    p = os.path.join(base, rel_path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote:", rel_path)

# 1. Fact Matrix Engine
fact_matrix_code = """import { CaseDocument, FactMatrixItem, OcrReadability } from '../types';

export function extractFactMatrix(
  caseSummary: string,
  primaryIssue: string,
  documents: CaseDocument[]
): FactMatrixItem[] {
  const items: FactMatrixItem[] = [];

  // 1. Invoice & Possession Fact
  const hasInvoices = documents.some(d => d.type === 'Invoice');
  items.push({
    id: `fm-${Date.now()}-1`,
    issue: 'Possession of Valid Tax Invoices (Rule 46)',
    allegedFact: hasInvoices 
      ? 'Taxpayer holds original serialized tax invoices with GSTIN, HSN codes, and tax breakdowns.'
      : 'Taxpayer asserts possession of invoices; primary copies are attached in records.',
    sourceDocument: hasInvoices ? 'Tax Invoices / Purchase Register' : 'Statement of Facts',
    pageParagraph: 'Annexure A, Invoices',
    evidenceStrength: hasInvoices ? 'Established' : 'Probable',
    contradiction: 'None on record. Revenue did not allege forgery of invoice paper.',
    significance: 'Fundamental requirement under Section 16(2)(a) CGST Act, 2017.',
    ocrStatus: 'Clearly readable text'
  });

  // 2. Receipt & Movement of Goods
  const hasTransport = documents.some(d => d.type === 'E-Way Bill' || d.type === 'Transporter Bilty' || d.name.toLowerCase().includes('way'));
  items.push({
    id: `fm-${Date.now()}-2`,
    issue: 'Physical Receipt and Transit of Goods',
    allegedFact: hasTransport
      ? 'Consignments transported with valid Part-A & Part-B E-Way bills and inward gate passes.'
      : 'Goods were received at taxpayer factory/warehouse and accounted for in stock register.',
    sourceDocument: hasTransport ? 'E-Way Bills / Inward Material Gate Pass' : 'Purchase & Stock Ledger',
    pageParagraph: 'Annexure B, Transit Records',
    evidenceStrength: hasTransport ? 'Established' : 'Strongly supported',
    contradiction: 'Revenue raised suspicion without physical stock verification or transport toll check.',
    significance: 'Critical condition precedent under Section 16(2)(b) CGST Act, 2017.',
    ocrStatus: 'Clearly readable text'
  });

  // 3. Payment of Consideration and Tax
  const hasBank = documents.some(d => d.type === 'Bank Statement' || d.name.toLowerCase().includes('bank') || d.name.toLowerCase().includes('rtgs'));
  items.push({
    id: `fm-${Date.now()}-3`,
    issue: 'Payment of Consideration and Tax via Banking Channels',
    allegedFact: hasBank
      ? 'Full payment including CGST and SGST transferred through RTGS/NEFT banking channels within statutory 180 days.'
      : 'Consideration and applicable taxes paid via audited banking channels.',
    sourceDocument: hasBank ? 'Bank Statements & RTGS Advices' : 'Audited Books of Account',
    pageParagraph: 'Annexure C, Banking Proofs',
    evidenceStrength: hasBank ? 'Established' : 'Strongly supported',
    contradiction: 'None. Proper Officer did not find any cash-back or circular monetary flow.',
    significance: 'Complies with 2nd Proviso to Section 16(2) CGST Act, 2017.',
    ocrStatus: 'Clearly readable text'
  });

  // 4. Action Against Selling Dealer
  items.push({
    id: `fm-${Date.now()}-4`,
    issue: 'Exhaustion of Recovery Remedies Against Supplier',
    allegedFact: 'Proper Officer issued notice/order against recipient without taking recovery proceedings or attachment against defaulting supplier.',
    sourceDocument: 'Show Cause Notice / Impugned Order',
    pageParagraph: 'Adjudication Order Findings',
    evidenceStrength: 'Established',
    contradiction: 'Direct contravention of binding Calcutta HC (Suncraft) and Madras HC (D.Y. Beathel) precedents.',
    significance: 'Jurisdictional defect in departmental recovery mechanism.',
    ocrStatus: 'Clearly readable text'
  });

  return items;
}
"""
write_file("src/service/fact-matrix-engine.ts", fact_matrix_code)

# 2. Statutory Engine
statutory_code = """import { StatutoryParameter, AssessmentStatus, RiskLevel } from '../types';

export function evaluateStatutoryParameters(
  financialYear: string,
  primaryIssue: string,
  hasInvoice: boolean,
  hasTransit: boolean,
  hasBank: boolean
): StatutoryParameter[] {
  const isPre2022 = financialYear.includes('2017') || financialYear.includes('2018') || financialYear.includes('2019') || financialYear.includes('2020') || financialYear.includes('2021');

  const parameters: StatutoryParameter[] = [
    {
      id: 'sp-1',
      parameterCode: 'P1',
      title: 'Possession of Valid Tax Invoice / Debit Note',
      statutoryProvision: 'Section 16(2)(a) CGST Act, 2017 read with Rule 36 & Rule 46',
      statutoryRequirement: 'The registered person claiming ITC must be in possession of a tax invoice or debit note containing prescribed particulars.',
      legalTest: 'Does the document state the GSTIN of supplier and recipient, description of goods/services, total value, tax rate, and tax charged?',
      burdenOfProof: 'Initial burden is upon the taxpayer under Section 155 CGST Act.',
      requiredEvidence: ['Original Tax Invoices', 'Purchase Register Extract', 'Rule 46 compliance verification'],
      availableEvidence: hasInvoice ? ['Original serialized tax invoices on record', 'Audited purchase register'] : ['Purchase register entries'],
      assessment: hasInvoice ? 'SATISFIED' : 'PARTIALLY SATISFIED',
      risk: hasInvoice ? 'LOW' : 'MEDIUM',
      reason: hasInvoice ? 'Valid invoices produced with full statutory details.' : 'Invoices must be placed on formal record.'
    },
    {
      id: 'sp-2',
      parameterCode: 'P2',
      title: 'Actual Receipt of Goods or Services',
      statutoryProvision: 'Section 16(2)(b) CGST Act, 2017',
      statutoryRequirement: 'The registered person must have actually received the goods or services.',
      legalTest: 'Is there verifiable documentary evidence showing physical transit, delivery at registered premises, and entry in stock registers?',
      burdenOfProof: 'Taxpayer must demonstrate actual delivery upon challenge by Revenue.',
      requiredEvidence: ['E-Way Bills (Part A & B)', 'Lorry Receipts (LR)', 'Factory Gate Inward Slips', 'Weighbridge Slips'],
      availableEvidence: hasTransit ? ['E-Way bills with vehicle registration numbers', 'Store inward vouchers', 'Consumption logs'] : ['Stock ledger entries'],
      assessment: hasTransit ? 'SATISFIED' : 'PARTIALLY SATISFIED',
      risk: hasTransit ? 'LOW' : 'MEDIUM',
      reason: hasTransit ? 'Documentary chain of transport and receipt is complete.' : 'FASTag or gate pass documentation recommended to reinforce delivery.'
    },
    {
      id: 'sp-3',
      parameterCode: 'P3',
      title: 'Tax Charged Actually Paid to Government',
      statutoryProvision: 'Section 16(2)(c) CGST Act, 2017 read with Section 41',
      statutoryRequirement: 'Subject to Section 41, the tax charged in respect of supply must have been actually paid to the Government, either in cash or through utilization of admissible input tax credit.',
      legalTest: 'Where the buyer paid tax to the supplier but the supplier defaulted in depositing it in GSTR-3B, can ITC be denied to the buyer without first pursuing the seller?',
      burdenOfProof: 'Revenue must establish seller default and attempt recovery from seller before penalizing bona fide buyer (Suncraft / D.Y. Beathel / Arise India).',
      requiredEvidence: ['Proof of seller GSTR-1 filing', 'Bank payment of tax to seller', 'Record of departmental action against seller'],
      availableEvidence: ['Taxpayer paid 100% tax to seller via bank', 'Seller reported invoice in GSTR-1', 'Revenue took zero recovery steps against seller'],
      assessment: 'PARTIALLY SATISFIED',
      risk: 'MEDIUM',
      reason: 'Statutory clause requires payment to treasury, but judicial doctrine of impossibility (lex non cogit ad impossibilia) and Supreme Court affirmed Suncraft ruling protect bona fide buyers where Department fails to investigate the seller.'
    },
    {
      id: 'sp-4',
      parameterCode: 'P4',
      title: 'Mandatory GSTR-2B Matching Condition',
      statutoryProvision: 'Section 16(2)(aa) CGST Act, 2017 (enacted via Finance Act 2021)',
      statutoryRequirement: 'The details of the invoice or debit note must have been communicated to the recipient in Form GSTR-2B.',
      legalTest: 'Is Section 16(2)(aa) applicable retrospectively to periods prior to 01.01.2022?',
      burdenOfProof: 'Statutory interpretation question.',
      requiredEvidence: ['Notification No. 39/2021-Central Tax dt 21.12.2021 appointing enforcement date as 01.01.2022'],
      availableEvidence: isPre2022 ? ['Period under dispute is prior to 01.01.2022; GSTR-2A was merely a facilitation view'] : ['GSTR-2B filing reports'],
      assessment: 'SATISFIED',
      risk: 'LOW',
      reason: isPre2022 ? 'Section 16(2)(aa) was brought into force prospectively on 01.01.2022 and cannot be applied retrospectively (Calcutta & Madras HC).' : 'Invoices are matched in GSTR-2B.'
    },
    {
      id: 'sp-5',
      parameterCode: 'P5',
      title: 'Payment within 180 Days (2nd Proviso)',
      statutoryProvision: 'Second Proviso to Section 16(2) CGST Act, 2017 read with Rule 37',
      statutoryRequirement: 'Where a recipient fails to pay to the supplier the amount towards the value of supply along with tax within 180 days, an amount equal to ITC availed shall be added to output tax liability.',
      legalTest: 'Was full consideration and tax remitted to supplier within 180 days of invoice date?',
      burdenOfProof: 'Taxpayer burden via bank payment records.',
      requiredEvidence: ['Bank Statements', 'Payment Vouchers', 'CA Certificate'],
      availableEvidence: hasBank ? ['Bank RTGS/NEFT statements showing payment within 30-60 days'] : ['Ledger accounts'],
      assessment: hasBank ? 'SATISFIED' : 'PARTIALLY SATISFIED',
      risk: hasBank ? 'LOW' : 'MEDIUM',
      reason: hasBank ? 'Payment made well within 180 days.' : 'Bank vouchers must be formally linked to invoice numbers.'
    },
    {
      id: 'sp-6',
      parameterCode: 'P6',
      title: 'Time-Bar for ITC Availment & Retrospective Safe Harbor',
      statutoryProvision: 'Section 16(4) & Section 16(5)/16(6) CGST Act (Finance (No. 2) Act, 2024)',
      statutoryRequirement: 'Section 16(4) prescribes cut-off date for claiming ITC. Section 16(5) retrospectively allows ITC for FY 2017-18 to 2020-21 in any return filed up to 30.11.2021.',
      legalTest: 'Does the claim fall within the retrospective window created by Section 16(5) enacted by Parliament?',
      burdenOfProof: 'Taxpayer via GSTR-3B return filing acknowledgments.',
      requiredEvidence: ['GSTR-3B ARN receipts', 'Circular No. 237/31/2024-GST'],
      availableEvidence: ['Return filing dates on record with ARN'],
      assessment: 'SATISFIED',
      risk: 'LOW',
      reason: 'Section 16(5) has retrospective effect from 01.07.2017, validating ITC claimed up to 30.11.2021.'
    },
    {
      id: 'sp-7',
      parameterCode: 'P7',
      title: 'Conditions for Invoking Extended Period of Limitation & Penalty',
      statutoryProvision: 'Section 74(1) vs Section 73(1) CGST Act, 2017',
      statutoryRequirement: 'Extended period of 5 years and 100% penalty can only be invoked if there is fraud, wilful-misstatement, or suppression of facts with intent to evade tax.',
      legalTest: 'Has Revenue established mens rea and positive act of deliberate deception by the taxpayer?',
      burdenOfProof: 'Heavy burden lies entirely upon the Revenue (Uniworth Textiles / Cosmic Dye Chemical).',
      requiredEvidence: ['Evidence of cash kickbacks', 'Admissions under Section 70', 'Direct evidence of conspiracy'],
      availableEvidence: ['Zero evidence of collusion or cash kickbacks', 'Transactions reflected in regular books and GST returns'],
      assessment: 'NOT SATISFIED',
      risk: 'HIGH',
      reason: 'Department has not discharged burden to prove fraud; invocation of Section 74 is legally unsustainable.'
    },
    {
      id: 'sp-8',
      parameterCode: 'P8',
      title: 'Mandatory Opportunity of Personal Hearing',
      statutoryProvision: 'Section 75(4) CGST Act, 2017',
      statutoryRequirement: 'An opportunity of hearing shall be granted where a request is received in writing or where any adverse decision is contemplated.',
      legalTest: 'Was a personal hearing granted before passing the adverse order?',
      burdenOfProof: 'Statutory obligation on Proper Officer.',
      requiredEvidence: ['Personal Hearing Notices', 'Record of Appearance'],
      availableEvidence: ['Record shows whether hearing was afforded'],
      assessment: 'SATISFIED',
      risk: 'LOW',
      reason: 'Natural justice compliance is a mandatory prerequisite for valid adjudication.'
    }
  ];

  return parameters;
}
"""
write_file("src/service/statutory-engine.ts", statutory_code)

print("Service files 1 & 2 written.")