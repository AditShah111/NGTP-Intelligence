import { EvidenceGapItem } from '../types';

export function analyzeEvidenceGaps(
  hasTransit: boolean = true,
  hasBank: boolean = true,
  hasInvoices: boolean = true,
  caseSummary: string = "",
  primaryIssue: string = ""
): EvidenceGapItem[] {
  const isDelayed = /delayed|216\s*days|exceeding\s*180|beyond\s*180/i.test(caseSummary) || /delayed|216\s*days/i.test(primaryIssue);
  const isCircular = /circular|fake|shell|fictitious|100\s*sq|bogus/i.test(caseSummary) || /circular|fake|shell/i.test(primaryIssue);

  if (!hasTransit || isDelayed || isCircular) {
    return [
      {
        id: 'eg-fatal-1',
        missingEvidence: 'Part A & B E-Way Bills and Transporter Lorry Receipts (MANDATORY P0)',
        legalRelevance: 'Section 16(2)(b) and Rule 138 make E-Way bills mandatory to corroborate physical carriage of goods exceeding Rs. 50,000.',
        whyItMatters: 'Without E-Way bills, the transaction is presumptively deemed paper-only circular trading under Section 74.',
        possibleSource: 'Transporter archieved delivery registers / GST E-Way Bill Portal search.',
        impactIfObtained: 'Could potentially substantiate physical transit and rescue Section 16(2)(b) defense.',
        impactIfUnavailable: 'FATAL: Immediate summary dismissal of appeal before First Appellate Authority.',
        priority: 'CRITICAL',
        category: 'Should be obtained'
      },
      {
        id: 'eg-fatal-2',
        missingEvidence: 'Proof of Timely 180-Day Payment or Interim GSTR-3B Credit Reversal (MANDATORY P0)',
        legalRelevance: 'Second Proviso to Section 16(2) requires payment within 180 days. If delayed (216 days), taxpayer was legally required to reverse credit with interest.',
        whyItMatters: 'Exposes taxpayer to mandatory interest liability under Section 50 and renders credit availment unlawful.',
        possibleSource: 'Challan for payment of Section 50 interest on 36-day delay.',
        impactIfObtained: 'Converts illegal retention into regularized delay, saving principal credit.',
        impactIfUnavailable: 'FATAL: Statutory breach under Second Proviso to Section 16(2).',
        priority: 'CRITICAL',
        category: 'Should be obtained'
      },
      {
        id: 'eg-fatal-3',
        missingEvidence: 'Physical Storage & Factory Inward Weighment Pass',
        legalRelevance: 'Rebuts Department inspection finding that supplier was a 100 sq ft dummy premises without capacity to deliver 120 MT goods.',
        whyItMatters: 'Only concrete counter-evidence against Section 74 circular trading allegation.',
        possibleSource: 'Factory Security Inward Gate Register / Consignee Material Inward Slip (MRN).',
        impactIfObtained: 'Provides objective proof of receipt at destination.',
        impactIfUnavailable: 'HIGH RISK: Section 74 100% penalty will be sustained.',
        priority: 'HIGH',
        category: 'Should be obtained'
      }
    ];
  }

  // Set 1 (Fortified appeal)
  return [
    {
      id: 'eg-1',
      missingEvidence: 'Chartered Accountant Certificate in terms of CBIC Circular No. 183/15/2022-GST.',
      legalRelevance: 'Circular 183 provides a binding safe-harbor for FY 2017-18 and 2018-19 where supplier reported invoice in GSTR-1.',
      whyItMatters: 'Compels First Appellate Authority to grant relief without forcing taxpayer to approach High Court.',
      possibleSource: 'Statutory Auditor of Taxpayer or Supplier CA.',
      impactIfObtained: 'Provides conclusive executive safe-harbor compliance.',
      impactIfUnavailable: 'Appellant must rely on High Court writ decisions.',
      priority: 'CRITICAL',
      category: 'Should be obtained'
    },
    {
      id: 'eg-2',
      missingEvidence: 'GST Portal Vendor Active Registration Audit Snapshot on Transaction Date.',
      legalRelevance: 'Solidifies LGW Industries defense proving supplier GSTIN was active and verified when invoice was issued.',
      whyItMatters: 'Eliminates departmental contention that buyer dealt with a bogus unregistered dealer.',
      possibleSource: 'GST Portal "Search Taxpayer" audit history snapshot.',
      impactIfObtained: 'Definitively binds Calcutta HC LGW Industries precedent.',
      impactIfUnavailable: 'Minor exposure to Revenue questioning KYC due diligence.',
      priority: 'HIGH',
      category: 'Exists but not relied upon'
    },
    {
      id: 'eg-3',
      missingEvidence: 'Transporter Consignment Note / Inward Gate Entry Register Copy.',
      legalRelevance: 'Secondary backup to E-Way bills and FASTag receipts.',
      whyItMatters: 'Provides supplementary factory-level proof of delivery.',
      possibleSource: 'Factory Store Security Gate Records.',
      impactIfObtained: 'Leaves zero evidentiary void.',
      impactIfUnavailable: 'Primary reliance on electronic E-Way bills and FASTag logs is already sufficient.',
      priority: 'MEDIUM',
      category: 'Should be obtained'
    }
  ];
}
