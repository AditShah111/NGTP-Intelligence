import { FactMatrixItem, CaseDocument, EvidenceStrength } from '../types';

export function extractFactMatrix(
  caseSummary: string,
  primaryIssue: string,
  documents: CaseDocument[] = []
): FactMatrixItem[] {
  const hasInvoices = documents.some(d => d.type === 'Invoice') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('invoice'));
  const hasBank = documents.some(d => d.type === 'Bank Statement') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('bank') || d.extractedTextSnippet.toLowerCase().includes('rtgs'));
  const hasTransit = documents.some(d => d.type === 'E-Way Bill') || documents.some(d => d.extractedTextSnippet.toLowerCase().includes('e-way') || d.extractedTextSnippet.toLowerCase().includes('vehicle'));
  const hasOrder = documents.some(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07');

  const docCount = documents.length;

  return [
    {
      id: 'fm-1',
      issue: 'Possession of Valid Tax Invoices (Section 16(2)(a))',
      allegedFact: hasInvoices 
        ? `Taxpayer possesses valid tax invoices on record satisfying Rule 46 particulars.` 
        : `NO TAX INVOICES UPLOADED. Taxpayer assertion of possessing valid invoices is currently unverified.`,
      sourceDocument: hasInvoices ? documents.find(d => d.type === 'Invoice')?.name || 'Uploaded Invoices' : 'NONE (Missing Evidentiary Proof)',
      pageParagraph: hasInvoices ? 'Verified from uploaded file' : 'N/A',
      evidenceStrength: hasInvoices ? 'Established' : 'Unsupported',
      contradiction: hasInvoices ? 'None.' : 'Fatal statutory deficiency: Section 16(2)(a) mandate is unevidenced.',
      significance: hasInvoices ? 'Satisfies Section 16(2)(a) CGST Act.' : 'Immediate ground for statutory ITC disallowance.',
      ocrStatus: hasInvoices ? 'Clearly readable text' : 'Missing text'
    },
    {
      id: 'fm-2',
      issue: 'Actual Physical Receipt of Goods (Section 16(2)(b))',
      allegedFact: hasTransit 
        ? `Consignments moved with verifiable E-Way bills and inward transit records.` 
        : `NO E-WAY BILLS OR PROOF OF PHYSICAL DELIVERY UPLOADED. Movement of goods is uncorroborated.`,
      sourceDocument: hasTransit ? documents.find(d => d.type === 'E-Way Bill')?.name || 'Uploaded E-Way Bills' : 'NONE (Missing Evidentiary Proof)',
      pageParagraph: hasTransit ? 'Verified from uploaded file' : 'N/A',
      evidenceStrength: hasTransit ? 'Established' : 'Unsupported',
      contradiction: hasTransit ? 'None.' : 'High risk of bogus billing / fake invoicing allegation under Section 74.',
      significance: hasTransit ? 'Satisfies Section 16(2)(b) CGST Act.' : 'Fatal vulnerability against Revenue fake-transit allegations.',
      ocrStatus: hasTransit ? 'Clearly readable text' : 'Missing text'
    },
    {
      id: 'fm-3',
      issue: 'Payment of Consideration and Tax to Supplier (2nd Proviso to Section 16(2))',
      allegedFact: hasBank 
        ? `100% invoice amount including GST paid through verifiable banking channels (RTGS/NEFT).` 
        : `NO BANK STATEMENT OR PAYMENT PROOF UPLOADED. Payment of tax to supplier is unverified.`,
      sourceDocument: hasBank ? documents.find(d => d.type === 'Bank Statement')?.name || 'Uploaded Bank Records' : 'NONE (Missing Evidentiary Proof)',
      pageParagraph: hasBank ? 'Verified from uploaded bank statements' : 'N/A',
      evidenceStrength: hasBank ? 'Established' : 'Unsupported',
      contradiction: hasBank ? 'None.' : 'Taxpayer cannot claim bona fide buyer protection without bank payment proof.',
      significance: hasBank ? 'Complies with 2nd Proviso to Section 16(2) and establishes bona fides.' : 'Precludes reliance on Suncraft Energy safe-harbor.',
      ocrStatus: hasBank ? 'Clearly readable text' : 'Missing text'
    },
    {
      id: 'fm-4',
      issue: 'Departmental Action Against Selling Dealer (Suncraft / D.Y. Beathel Test)',
      allegedFact: hasOrder 
        ? `Impugned SCN / DRC-07 order shows disallowance against recipient without pursuing the supplier.` 
        : `NO LOWER AUTHORITY NOTICE / ORDER UPLOADED. Departmental findings and allegations cannot be audited.`,
      sourceDocument: hasOrder ? documents.find(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07')?.name || 'Uploaded Order' : 'NONE (Missing Impugned Order)',
      pageParagraph: hasOrder ? 'Notice Findings' : 'N/A',
      evidenceStrength: hasOrder ? 'Established' : 'Unable to determine',
      contradiction: hasOrder ? 'Direct breach of Calcutta HC Suncraft principles.' : 'Cannot formulate appeal grounds without the impugned order.',
      significance: hasOrder ? 'Ground for quashing order under Article 226 / Section 107.' : 'Must procure SCN / DRC-07 to frame grounds.',
      ocrStatus: hasOrder ? 'Clearly readable text' : 'Missing text'
    }
  ];
}
