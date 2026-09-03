import { CaseDocument } from '../types/index';

export interface NGTPGatekeeperResult {
  isNGTP: boolean;
  detectedDomain: string;
  confidenceScore: number;
  rejectionReason?: string;
  matchedKeywords: string[];
  allowedTopics: string[];
}

// Explicit Non-NGTP / Out of Scope markers
const OUT_OF_SCOPE_DOMAINS = [
  {
    domain: 'Customs Duty & Import Tariff Dispute',
    keywords: ['customs act', 'bill of entry', 'customs tariff', 'anti-dumping duty', 'import duty dispute', 'safeguard duty', 'customs act 1962', 'icd port clearance', 'bonded warehouse customs']
  },
  {
    domain: 'Direct Tax / Income Tax / Transfer Pricing',
    keywords: ['income tax act', 'section 148', 'section 147', 'reassessment notice', 'transfer pricing', 'form 3cd', 'section 143(3)', 'direct tax', 'capital gains tax']
  },
  {
    domain: 'HSN Classification & Tax Rate Dispute',
    keywords: ['classification dispute', 'hsn classification dispute', 'rate of tax dispute', 'whether taxable at 12% or 18%', 'whether taxable at 5% or 18%', 'tariff classification dispute', 'rate notification interpretation']
  },
  {
    domain: 'Place of Supply / Inter-State vs Intra-State Dispute',
    keywords: ['place of supply dispute', 'section 10 of igst', 'section 12 of igst', 'section 13 of igst', 'intermediary services dispute', 'wrong head payment section 77']
  },
  {
    domain: 'Export Refund & Inverted Duty Structure Claim',
    keywords: ['export refund dispute', 'inverted duty structure refund', 'rule 89(5) refund', 'rule 89(4) refund', 'unutilized itc refund dispute', 'rfid-06 refund rejection']
  },
  {
    domain: 'Valuation & Related Party Supply',
    keywords: ['valuation dispute under section 15', 'rule 28 valuation', 'open market value valuation', 'corporate guarantee valuation']
  }
];

export function validateNGTPScope(
  title: string,
  primaryIssue: string,
  caseSummary: string,
  noticeType: string,
  documents: CaseDocument[] = []
): NGTPGatekeeperResult {
  const allowedTopics = [
    'Section 16(2)(c) Supplier Tax Non-Deposit & Recovery',
    'Non-Genuine Taxpayer (NGTP) & Fake Billing Allegations',
    'GSTR-2A / 2B vs GSTR-3B Mismatch Disallowance',
    'Retrospectively Cancelled or Non-Existent Supplier GSTINs',
    'Rule 86A Electronic Credit Ledger Blocking for Supplier Default',
    'Circular No. 183/15/2022-GST Safe-Harbor Verification'
  ];

  const fullTextCorpus = [
    title,
    primaryIssue,
    caseSummary,
    noticeType,
    ...documents.map(d => `${d.name} ${d.type} ${d.extractedTextSnippet || ''}`)
  ].join(' ').toLowerCase();

  // Check for explicit Out-of-Scope non-NGTP domains
  for (const oos of OUT_OF_SCOPE_DOMAINS) {
    let matchCount = 0;
    const matchedTerms: string[] = [];
    for (const kw of oos.keywords) {
      if (fullTextCorpus.includes(kw)) {
        matchCount++;
        matchedTerms.push(kw);
      }
    }

    // If it clearly belongs to an out-of-scope domain (e.g. customs, income tax, refund)
    if (matchCount >= 1) {
      return {
        isNGTP: false,
        detectedDomain: oos.domain,
        confidenceScore: 98,
        rejectionReason: `This Legal Intelligence Engine is strictly calibrated exclusively for Non-Genuine Taxpayer (NGTP) and Section 16(2)(c) supplier disputes. The submitted matter pertains to "${oos.domain}", which is not applicable and not allowed to run through the NGTP engine.`,
        matchedKeywords: matchedTerms,
        allowedTopics
      };
    }
  }

  // Permitted NGTP project (engine defaults to treating uploaded matters under NGTP statutory rules)
  return {
    isNGTP: true,
    detectedDomain: 'Non-Genuine Taxpayer (NGTP) & Section 16(2)(c) Supplier Default',
    confidenceScore: 100,
    matchedKeywords: ['NGTP Core Scope'],
    allowedTopics
  };
}
