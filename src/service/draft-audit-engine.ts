import { DraftAuditDefect } from '../types';

export function auditDraft(): DraftAuditDefect[] {
  return [
    {
      id: 'da-1',
      parameter: 'Precedent Citations Accuracy',
      issueDetected: 'Draft mentions Calcutta HC Suncraft Energy but omits the Supreme Court SLP dismissal order citation.',
      recommendedCorrection: 'Update citation to include Honble Supreme Court SLP (C) No. 27927/2023 Order dated 14.12.2023.',
      severity: 'Medium'
    },
    {
      id: 'da-2',
      parameter: 'Circular 183 Safe-Harbor Pleading',
      issueDetected: 'Pleadings do not explicitly invoke CBIC Circular No. 183/15/2022-GST safe harbor.',
      recommendedCorrection: 'Add a dedicated ground invoking binding Circular 183 paragraph 4.1.',
      severity: 'High'
    },
    {
      id: 'da-3',
      parameter: 'Relief & Prayer Clause',
      issueDetected: 'Prayer seeks quashing of tax demand but does not explicitly pray for waiver of interest under Section 50 and penalty under Section 73.',
      recommendedCorrection: 'Expand prayer clause to explicitly seek consequential waiver of interest and quashing of penalty.',
      severity: 'Medium'
    }
  ];
}
