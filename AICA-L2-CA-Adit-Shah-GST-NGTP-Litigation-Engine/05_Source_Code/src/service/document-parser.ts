export interface ExtractedDocumentData {
  name: string;
  type: string;
  textSnippet: string;
  hasInvoices: boolean;
  hasBankPayment: boolean;
  hasEWayBills: boolean;
  hasScnOrOrder: boolean;
  hasCaCert: boolean;
  detectedGstins: string[];
  detectedAmounts: string[];
}

export function parseDocumentContent(name: string, content: string, typeHint?: string): ExtractedDocumentData {
  const lower = (content + ' ' + name).toLowerCase();

  // Pattern detection
  const hasInvoices = lower.includes('invoice') || lower.includes('bill no') || lower.includes('hsn') || lower.includes('taxable value');
  const hasBankPayment = lower.includes('bank') || lower.includes('rtgs') || lower.includes('neft') || lower.includes('utr') || lower.includes('cheque') || lower.includes('debit');
  const hasEWayBills = lower.includes('e-way') || lower.includes('eway') || lower.includes('vehicle') || lower.includes('transporter') || lower.includes('lr no');
  const hasScnOrOrder = lower.includes('scn') || lower.includes('drc-01') || lower.includes('drc-07') || lower.includes('show cause') || lower.includes('adjudication') || lower.includes('order-in-original');
  const hasCaCert = lower.includes('chartered accountant') || lower.includes('circular 183') || lower.includes('udina') || lower.includes('certificate');

  // Detect GSTINs (2 digits + 5 alpha + 4 digits + 1 alpha + 1 alpha/digit + Z + 1 alpha/digit)
  const gstinRegex = /[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}/g;
  const detectedGstins = Array.from(new Set(content.match(gstinRegex) || []));

  // Detect Amounts
  const amountRegex = /(?:rs\.?|inr|₹)\s*([\d,]+(?:\.\d{2})?)/gi;
  const detectedAmounts: string[] = [];
  let m;
  while ((m = amountRegex.exec(content)) !== null) {
    if (detectedAmounts.length < 5) detectedAmounts.push(m[0]);
  }

  let determinedType = typeHint || 'Other';
  if (hasScnOrOrder) determinedType = lower.includes('drc-07') ? 'DRC-07' : (lower.includes('drc-01') ? 'DRC-01' : 'SCN');
  else if (hasInvoices) determinedType = 'Invoice';
  else if (hasBankPayment) determinedType = 'Bank Statement';
  else if (hasEWayBills) determinedType = 'E-Way Bill';
  else if (hasCaCert) determinedType = 'CA Certificate';

  return {
    name,
    type: determinedType,
    textSnippet: content.slice(0, 500) + (content.length > 500 ? '...' : ''),
    hasInvoices,
    hasBankPayment,
    hasEWayBills,
    hasScnOrOrder,
    hasCaCert,
    detectedGstins,
    detectedAmounts
  };
}
