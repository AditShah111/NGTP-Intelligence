import { runComplete13StepEvaluation } from '../src/service/evaluator-agent';
import * as fs from 'fs';

async function verify() {
  const set1Text = fs.readFileSync('public/sample-data/set1-proceed/Set1_Statement_of_Facts_and_Grounds.txt', 'utf-8');
  const set1Docs = [
    { id: 'd1', name: 'Set1_Tax_Invoice_Rule46.pdf', type: 'Invoice' as const, fileSize: '120 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'Tax Invoice DMA/2018-19/0402 Hot Rolled Steel Coils 40 MT Tax 38,40,000 Supplier GSTIN 27AABCD5544E1Z2 active on date' },
    { id: 'd2', name: 'Set1_Bank_RTGS_Statement.pdf', type: 'Bank Statement' as const, fileSize: '110 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'RTGS DEBIT UTR HDFCR52018102400918234 amount 2,51,73,333 paid in 12 days' },
    { id: 'd3', name: 'Set1_EWay_Bill_PartA_B.pdf', type: 'E-Way Bill' as const, fileSize: '95 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'E-Way Bill 241089201945 Vehicle MH-12-RN-7845 valid' },
    { id: 'd4', name: 'Set1_Weighbridge_FASTag_Receipt.pdf', type: 'E-Way Bill' as const, fileSize: '105 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'Weighbridge Slip DWB/18/10492 Net Weight 40040 Kg FASTag Toll Khalapur Kusgaon Talegaon' },
    { id: 'd5', name: 'Set1_Tax_Ledger_GSTR1_Ack.pdf', type: 'Invoice' as const, fileSize: '90 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'GSTR-1 ARN AA2710180918234 filed 10-11-2018' },
    { id: 'd6', name: 'Set1_Impugned_DRC07_Order.pdf', type: 'DRC-07' as const, fileSize: '115 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'DRC-07 Order ZA2703240098412 disallowing ITC due to retrospective cancellation' }
  ];

  const eval1 = await runComplete13StepEvaluation(
    'Apex Precision v. ACST LTU-1 Pune - Retrospective NGTP Cancellation FY 2018-19',
    'Apex Precision Engineering Pvt. Ltd.',
    '27AAACA9876C1Z3',
    '2018-19',
    'INR 38,40,000',
    'Order-in-Original / DRC-07',
    'Section 16(2)(c) ITC denial due to retrospective cancellation of supplier GSTIN even though tax was deposited via RTGS while registration was active',
    set1Text,
    set1Docs
  );

  console.log("=== SET 1 VERIFICATION ===");
  console.log("Verdict:", eval1.finalOutput.executiveVerdict.recommendation, "| Readiness:", eval1.readinessScore.totalScore, "| Viability:", eval1.viabilityScore.totalScore);
  console.log("Top 5 Drivers:");
  eval1.finalOutput.executiveVerdict.top5Reasons.forEach((r, i) => console.log(`  ${i+1}. ${r}`));
  console.log("Statutory Parameters Satisfied:", eval1.statutoryParameters.filter(p => p.assessment === 'SATISFIED').length, "/", eval1.statutoryParameters.length);
  console.log("Draft Defects Count:", eval1.draftAudit.length);
  console.log("Red Team Attacks Surviving:", eval1.redTeamItems.filter(r => r.survivesAttack).length, "/", eval1.redTeamItems.length);
  console.log("Grounds Titles:");
  eval1.improvedSubmissions.forEach(g => console.log(`  - [${g.groundStrength}%] ${g.groundNumber}: ${g.title}`));

  const set2Text = fs.readFileSync('public/sample-data/set2-hold/Set2_Statement_of_Facts_and_Grounds.txt', 'utf-8');
  const set2Docs = [
    { id: 'sd1', name: 'Set2_Tax_Invoice_Deficient.pdf', type: 'Invoice' as const, fileSize: '100 KB', uploadedAt: '2024-04-15', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'Tax Invoice GTS/19-20/0118 building materials lump sum without vehicle or eway bill' },
    { id: 'sd2', name: 'Set2_Bank_Statement_Delayed.pdf', type: 'Bank Statement' as const, fileSize: '100 KB', uploadedAt: '2024-04-15', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'Paid after 216 days delayed beyond 180 days statutory limit under Section 16(2)' },
    { id: 'sd3', name: 'Set2_Impugned_DRC07_Order.pdf', type: 'DRC-07' as const, fileSize: '110 KB', uploadedAt: '2024-04-15', ocrReadability: 'Clearly readable text' as const, extractedTextSnippet: 'DRC-07 Order ZA2701240049182 circular trading without movement of goods under Section 74' }
  ];

  const eval2 = await runComplete13StepEvaluation(
    'Shaurya Infra v. DCST Nodal-7 Thane - Paper-Only Allegation FY 2019-20',
    'Shaurya Infra Projects Ltd.',
    '27AAACS4321D1Z8',
    '2019-20',
    'INR 52,00,000',
    'Order-in-Original / DRC-07',
    'Section 16(2)(c) circular trading allegation - NO e-way bill, NO transit proof, supplier fictitious 100 sq ft room, payment delayed 216 days beyond 180-day limit',
    set2Text,
    set2Docs
  );

  console.log("\n=== SET 2 VERIFICATION ===");
  console.log("Verdict:", eval2.finalOutput.executiveVerdict.recommendation, "| Readiness:", eval2.readinessScore.totalScore, "| Viability:", eval2.viabilityScore.totalScore);
  console.log("Top 5 Drivers:");
  eval2.finalOutput.executiveVerdict.top5Reasons.forEach((r, i) => console.log(`  ${i+1}. ${r}`));
  console.log("Statutory Parameters Satisfied:", eval2.statutoryParameters.filter(p => p.assessment === 'SATISFIED').length, "/", eval2.statutoryParameters.length);
  console.log("Draft Defects Count:", eval2.draftAudit.length);
  console.log("Red Team Attacks Surviving:", eval2.redTeamItems.filter(r => r.survivesAttack).length, "/", eval2.redTeamItems.length);
  console.log("Grounds Titles:");
  eval2.improvedSubmissions.forEach(g => console.log(`  - [${g.groundStrength}%] ${g.groundNumber}: ${g.title}`));
}

verify().catch(e => console.error(e));