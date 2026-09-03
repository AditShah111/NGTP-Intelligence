import { DraftAuditDefect } from '../types';

export function auditDraft(
  hasTransit: boolean = true,
  hasBank: boolean = true,
  hasInvoices: boolean = true,
  caseSummary: string = "",
  primaryIssue: string = ""
): DraftAuditDefect[] {
  const isDelayed = /delayed|216\s*days|exceeding\s*180|beyond\s*180/i.test(caseSummary) || /delayed|216\s*days/i.test(primaryIssue);
  const isCircular = /circular|fake|shell|fictitious|100\s*sq|bogus/i.test(caseSummary) || /circular|fake|shell/i.test(primaryIssue);

  if (!hasTransit || isDelayed || isCircular) {
    return [
      {
        id: 'da-fatal-1',
        parameter: 'Second Proviso to Section 16(2) Compliance',
        issueDetected: 'FATAL STATUTORY DEFECT: Pleadings concede consideration was paid after 216 days (exceeding 180 days limit) without showing mandatory interim credit reversal in Form GSTR-3B.',
        recommendedCorrection: 'Discharge Section 50 interest immediately for 36 delayed days; amend pleadings to avoid conceding unconditional entitlement during non-payment period.',
        severity: 'Critical'
      },
      {
        id: 'da-fatal-2',
        parameter: 'Section 16(2)(b) Transit Corroboration',
        issueDetected: 'FATAL EVIDENTIARY VOID: Reply to SCN admits absence of Part-B E-Way bills and transporter consignment notes, triggering irrebuttable presumption of paper-only supply.',
        recommendedCorrection: 'Search factory gate records or transporter registers for delivery confirmation; without transit proof, do not file appeal under Section 16(2)(b).',
        severity: 'Critical'
      },
      {
        id: 'da-fatal-3',
        parameter: 'Circular Trading & Shell Entity Rebuttal',
        issueDetected: 'HIGH RISK: Draft fails to rebut Proper Officers physical field inspection finding that supplier operated out of a fictitious 100 sq ft residential room.',
        recommendedCorrection: 'Demand cross-examination of inspecting officer under Section 70; challenge authenticity of adverse report.',
        severity: 'High'
      },
      {
        id: 'da-fatal-4',
        parameter: 'Precedent Invocability (Suncraft Energy)',
        issueDetected: 'INAPPROPRIATE PRECEDENT CITATION: Draft cites Supreme Court Suncraft Energy ratio without establishing the foundational prerequisite of physical receipt of goods.',
        recommendedCorrection: 'Withdraw direct reliance on Suncraft on merits; argue procedural denial of natural justice instead.',
        severity: 'High'
      }
    ];
  }

  // Set 1 (Fortified appeal)
  return [
    {
      id: 'da-1',
      parameter: 'Precedent Citations Precision',
      issueDetected: 'Draft cites Calcutta High Court Suncraft Energy but omits the Honble Supreme Court SLP dismissal order citation.',
      recommendedCorrection: 'Update citation to include Honble Supreme Court SLP (C) No. 27927/2023 Order dated 14.12.2023 to establish binding Article 141 precedence.',
      severity: 'Medium'
    },
    {
      id: 'da-2',
      parameter: 'Circular 183 Safe-Harbor Pleading',
      issueDetected: 'Pleadings do not explicitly cite paragraph 4.1 of CBIC Circular No. 183/15/2022-GST.',
      recommendedCorrection: 'Add a dedicated sub-ground invoking binding safe-harbor under Circular 183 and attach CA certificate.',
      severity: 'High'
    },
    {
      id: 'da-3',
      parameter: 'Retrospective Cancellation Defense (LGW Industries)',
      issueDetected: 'Pleadings should emphasize that supplier GSTIN was verified on Common Portal and active on invoice date.',
      recommendedCorrection: 'Attach GST Portal vendor history screenshot to lock in LGW Industries doctrine.',
      severity: 'Medium'
    },
    {
      id: 'da-4',
      parameter: 'Relief & Prayer Clause',
      issueDetected: 'Prayer seeks quashing of tax demand but does not explicitly pray for consequential waiver of interest under Section 50 and penalty under Section 74.',
      recommendedCorrection: 'Expand prayer clause to explicitly seek quashing of interest and penalty under Section 74.',
      severity: 'Medium'
    }
  ];
}
