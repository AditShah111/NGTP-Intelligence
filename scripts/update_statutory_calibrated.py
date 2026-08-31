code_statutory_calibrated = """import { StatutoryParameter, CaseDocument, PrecedentAnalysis } from '../types';

export function evaluateStatutoryParameters(
  financialYear: string,
  primaryIssue: string,
  hasInvoices: boolean,
  hasTransit: boolean,
  hasBank: boolean,
  hasScn: boolean = false,
  hasCaCert: boolean = false,
  ingestedPrecedents: PrecedentAnalysis[] = []
): StatutoryParameter[] {
  const isPre2022 = ['2017-18', '2018-19', '2019-20', '2020-21'].includes(financialYear) || financialYear.includes('2017') || financialYear.includes('2018') || financialYear.includes('2019') || financialYear.includes('2020');

  // Compute dynamic precedent modifiers
  const p3Precedents = ingestedPrecedents.filter(p => p.relevantProvision.includes('16(2)(c)') || p.caseName.includes('Suncraft') || p.caseName.includes('Beathel'));
  const p2Precedents = ingestedPrecedents.filter(p => p.relevantProvision.includes('16(2)(b)') || p.evidencesReliedOnByCourt?.some(e => e.toLowerCase().includes('way') || e.toLowerCase().includes('transit')));
  const p5Precedents = ingestedPrecedents.filter(p => p.relevantProvision.includes('16(2)(aa)') || p.caseName.includes('Trade Links') || p.caseName.includes('Diya'));

  return [
    {
      id: 'sp-1',
      parameterCode: 'P1',
      title: 'Possession of Valid Tax Invoice',
      statutoryProvision: 'Section 16(2)(a) CGST Act, 2017',
      statutoryRequirement: 'Registered person must be in possession of a valid tax invoice or debit note issued by a supplier complying with Rule 46.',
      legalTest: 'Is a physical or digitally signed tax invoice with all Rule 46 particulars (GSTIN, HSN, Place of Supply) available on record?',
      burdenOfProof: 'Initial burden on Taxpayer under Section 155.',
      requiredEvidence: ['Tax Invoices', 'ERP Purchase Register', 'Vendor Master GSTIN Verification'],
      availableEvidence: hasInvoices ? ['Tax Invoices on record satisfying Rule 46'] : ['NONE SUBMITTED (Fatal deficiency)'],
      assessment: hasInvoices ? 'SATISFIED' : 'NOT SATISFIED',
      risk: hasInvoices ? 'LOW' : 'CRITICAL',
      reason: hasInvoices 
        ? 'Valid tax invoices complying with Rule 46 particulars are attached.' 
        : 'No tax invoices provided. Non-negotiable mandatory condition under Section 16(2)(a) is unmet.',
      dynamicWeightModifier: 1.0,
      courtEvidentiaryPrecedent: 'Arise India Ltd. v. CTT (Del HC / SC)'
    },
    {
      id: 'sp-2',
      parameterCode: 'P2',
      title: 'Actual Physical Receipt of Goods / Services',
      statutoryProvision: 'Section 16(2)(b) CGST Act, 2017',
      statutoryRequirement: 'Registered person must have actually received the goods or services.',
      legalTest: 'Is there contemporaneous documentary proof of physical movement, transportation, and delivery?',
      burdenOfProof: 'Taxpayer burden under Section 155.',
      requiredEvidence: ['E-Way Bills (Part A & B)', 'Lorry Receipts (LR)', 'Factory Inward Gate Pass', 'Weighbridge Slips', 'FASTag Toll Records'],
      availableEvidence: hasTransit ? ['E-Way bills (Part A & B) and inward delivery gate records'] : ['NO TRANSIT RECORDS SUBMITTED'],
      assessment: hasTransit ? 'SATISFIED' : (hasInvoices ? 'PARTIALLY SATISFIED' : 'NOT SATISFIED'),
      risk: hasTransit ? 'LOW' : 'HIGH',
      reason: hasTransit 
        ? 'Documentary transit trail (E-Way bills / LR) confirms physical movement.' 
        : 'Absence of E-Way bills creates serious exposure to Revenue allegations of paper transactions / fake billing under Section 74.',
      dynamicWeightModifier: p2Precedents.length > 0 ? 1.2 : 1.0,
      courtEvidentiaryPrecedent: p2Precedents[0]?.caseName || 'Halder Enterprises v. State of WB (Cal HC)'
    },
    {
      id: 'sp-3',
      parameterCode: 'P3',
      title: 'Tax Actually Paid to Government (Suncraft / D.Y. Beathel Test)',
      statutoryProvision: 'Section 16(2)(c) CGST Act, 2017',
      statutoryRequirement: 'Subject to Section 41, the tax charged in respect of supply must be actually paid to the Government.',
      legalTest: 'Has the recipient paid full tax to the registered supplier, and has the Department exhausted recovery remedies against the supplier first?',
      burdenOfProof: 'Initial payment proof on Taxpayer; recovery proceedings on Revenue (Suncraft Energy).',
      requiredEvidence: ['Bank RTGS payment advice', 'Supplier GSTR-1 acknowledgement', 'Evidence of no recovery action against supplier'],
      availableEvidence: hasBank 
        ? ['Bank RTGS payment advice proving 100% payment to registered supplier', 'Supreme Court affirmed Suncraft precedent'] 
        : ['NO BANK STATEMENT OR PAYMENT PROOF SUBMITTED'],
      assessment: hasBank ? 'SATISFIED' : 'NOT SATISFIED',
      risk: hasBank ? 'LOW' : 'CRITICAL',
      reason: hasBank 
        ? 'Bona fide payment proven through banking channels. Covered by Calcutta HC / Supreme Court Suncraft Energy ratio.' 
        : 'Without bank statement / RTGS payment advice, buyer cannot establish bona fides or invoke Suncraft Energy protections.',
      dynamicWeightModifier: p3Precedents.length > 0 ? 1.3 : 1.0,
      courtEvidentiaryPrecedent: p3Precedents[0]?.caseName || 'Suncraft Energy Pvt. Ltd. (SC SLP 27927/2023)'
    },
    {
      id: 'sp-4',
      parameterCode: 'P4',
      title: 'Filing of Valid Return under Section 39 (Form GSTR-3B)',
      statutoryProvision: 'Section 16(2)(d) CGST Act, 2017',
      statutoryRequirement: 'Registered person must have furnished the return under Section 39.',
      legalTest: 'Was ITC availed and reported in monthly Form GSTR-3B filed for the relevant tax period?',
      burdenOfProof: 'Taxpayer under Section 155.',
      requiredEvidence: ['Form GSTR-3B filed ARN Receipts', 'ITC Ledger Tables'],
      availableEvidence: hasInvoices ? ['Form GSTR-3B return filed within statutory timelines'] : ['Return filing unverified'],
      assessment: hasInvoices ? 'SATISFIED' : 'UNCERTAIN',
      risk: 'LOW',
      reason: 'GSTR-3B returns filed regularly; credit availed in accordance with Section 39.',
      dynamicWeightModifier: 1.0,
      courtEvidentiaryPrecedent: 'Bharti Airtel Ltd. (Supreme Court)'
    },
    {
      id: 'sp-5',
      parameterCode: 'P5',
      title: 'GSTR-2B Matching & Prospective Enforcement',
      statutoryProvision: 'Section 16(2)(aa) CGST Act, 2017 (Inserted via Finance Act, 2021)',
      statutoryRequirement: 'The details of the invoice or debit note must be communicated to the recipient in Form GSTR-2B.',
      legalTest: 'Is Section 16(2)(aa) applicable to the dispute period (enforced w.e.f. 01.01.2022)?',
      burdenOfProof: 'Question of Law (Constitutional Non-Retrospectivity).',
      requiredEvidence: ['Notification No. 39/2021-CT dated 21.12.2021', 'CBIC Circular No. 183/15/2022-GST'],
      availableEvidence: isPre2022 
        ? ['Transaction pertains to period prior to 01.01.2022; Section 16(2)(aa) operates prospectively only'] 
        : ['Post-2022 transaction subject to GSTR-2B matching'],
      assessment: isPre2022 ? 'SATISFIED' : (hasInvoices ? 'PARTIALLY SATISFIED' : 'NOT SATISFIED'),
      risk: isPre2022 ? 'LOW' : 'MEDIUM',
      reason: isPre2022 
        ? 'Section 16(2)(aa) was brought into force only from 01.01.2022 and cannot be applied retrospectively to earlier financial years.' 
        : 'Post-2022 period requires verification of GSTR-2B communication.',
      dynamicWeightModifier: p5Precedents.length > 0 ? 1.25 : 1.0,
      courtEvidentiaryPrecedent: p5Precedents[0]?.caseName || 'M. Trade Links v. UOI (Kerala HC)'
    },
    {
      id: 'sp-6',
      parameterCode: 'P6',
      title: 'Payment within 180 Days (2nd Proviso to Section 16(2))',
      statutoryProvision: 'Second Proviso to Section 16(2) CGST Act read with Rule 37',
      statutoryRequirement: 'Recipient must pay the supplier the value of supply along with tax within 180 days from the invoice date.',
      legalTest: 'Do banking records prove that full invoice amount including GST was cleared within 180 days?',
      burdenOfProof: 'Taxpayer burden under Section 155.',
      requiredEvidence: ['Bank Statement / RTGS Ledger', 'Vendor Ledger Reconciliation', 'CA Payment Certificate'],
      availableEvidence: hasBank ? ['Bank RTGS payment proof within statutory 180-day window'] : ['NO PAYMENT PROOF SUBMITTED'],
      assessment: hasBank ? 'SATISFIED' : 'NOT SATISFIED',
      risk: hasBank ? 'LOW' : 'CRITICAL',
      reason: hasBank 
        ? 'Consideration and full GST cleared through banking channels within 180 days.' 
        : 'Payment within 180 days unproven. Attracts mandatory reversal under Rule 37.',
      dynamicWeightModifier: 1.1,
      courtEvidentiaryPrecedent: 'Second Proviso to Section 16(2) read with Rule 37'
    },
    {
      id: 'sp-7',
      parameterCode: 'P7',
      title: 'Statutory Time-Limit for ITC Availment & Section 16(5) Retrospective Relief',
      statutoryProvision: 'Section 16(4) read with Section 16(5) (Finance Act, 2024)',
      statutoryRequirement: 'ITC must be availed prior to the due date of September/November return following the financial year.',
      legalTest: 'Is ITC protected under retrospective insertion of Section 16(5) (Finance Act, 2024) for FY 17-18 to 20-21?',
      burdenOfProof: 'Statutory interpretation.',
      requiredEvidence: ['Finance (No. 2) Act, 2024 Section 16(5) & 16(6)', 'GSTR-3B filing dates up to 30.11.2021'],
      availableEvidence: isPre2022 
        ? ['Fully protected by retrospective insertion of Section 16(5) in CGST Act'] 
        : ['Availment within Section 16(4) statutory time-limit'],
      assessment: 'SATISFIED',
      risk: 'LOW',
      reason: 'Section 16(5) inserted retrospectively via Finance Act, 2024 validates ITC availed up to 30th November 2021 for FY 2017-18 through 2020-21.',
      dynamicWeightModifier: 1.0,
      courtEvidentiaryPrecedent: 'Section 16(5) CGST Act (Finance Act, 2024)'
    },
    {
      id: 'sp-8',
      parameterCode: 'P8',
      title: 'Evidentiary Burden of Proof Discharge',
      statutoryProvision: 'Section 155 CGST Act, 2017',
      statutoryRequirement: 'The burden of proof that ITC has been lawfully claimed lies on the person claiming such credit.',
      legalTest: 'Has the taxpayer tendered an unbroken evidentiary chain of invoices, payment, transit, and accounting records?',
      burdenOfProof: 'Taxpayer initial burden; shifts to Revenue on production of primary proof (Section 106 Evidence Act).',
      requiredEvidence: ['Invoices', 'Bank Statements', 'E-Way Bills', 'Books of Account', 'Impugned Order'],
      availableEvidence: (hasInvoices && hasBank && hasTransit)
        ? ['Complete documentary chain (Invoices + RTGS Bank Statements + E-Way Bills + Ledger) fully discharges Section 155 burden']
        : (hasInvoices && hasBank 
            ? ['Invoices and bank proof submitted; physical transit documents recommended'] 
            : ['FATAL DEFICIENCY: Section 155 burden is completely undischarged']),
      assessment: (hasInvoices && hasBank && hasTransit) ? 'SATISFIED' : ((hasInvoices && hasBank) ? 'PARTIALLY SATISFIED' : 'NOT SATISFIED'),
      risk: (hasInvoices && hasBank && hasTransit) ? 'LOW' : ((hasInvoices && hasBank) ? 'MEDIUM' : 'CRITICAL'),
      reason: (hasInvoices && hasBank && hasTransit)
        ? 'Section 155 initial evidentiary burden is affirmatively discharged on the record.'
        : ((hasInvoices && hasBank)
            ? 'Substantial burden discharged via payment and invoices; furnish E-way bills to eliminate transit risk.'
            : 'Taxpayer has entirely failed to discharge Section 155 burden due to missing invoices and bank records.'),
      dynamicWeightModifier: 1.3,
      courtEvidentiaryPrecedent: 'Section 155 CGST Act read with Section 106 Evidence Act'
    }
  ];
}
"""

with open("src/service/statutory-engine.ts", "w", encoding="utf-8") as f:
    f.write(code_statutory_calibrated)

print("Updated statutory-engine.ts with dynamic precedent weight calibration!")