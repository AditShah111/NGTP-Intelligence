import { EvidenceGapItem } from '../types';

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
