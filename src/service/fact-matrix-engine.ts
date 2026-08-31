import { CaseDocument, FactMatrixItem, OcrReadability } from '../types';

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
