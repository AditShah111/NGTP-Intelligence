const { runComplete13StepEvaluation } = require('./src/service/evaluator-agent');

async function test() {
  console.log('--- TEST 1: EMPTY CASE (ONLY NAME, NO DOCUMENTS) ---');
  const emptyCase = await runComplete13StepEvaluation(
    'Empty Case Test',
    'ABC Corp',
    '27AAAAA0000A1Z5',
    '2018-19',
    'INR 50,00,000',
    'Order-in-Original / DRC-07',
    'Section 16(2)(c) recovery',
    'Taxpayer received an SCN.',
    [] // NO DOCUMENTS
  );

  console.log('Empty Case Readiness Score:', emptyCase.readinessScore.totalScore, '/ 100');
  console.log('Empty Case Viability Score:', emptyCase.viabilityScore.totalScore, '/ 100');
  console.log('Empty Case Verdict:', emptyCase.finalOutput.executiveVerdict.recommendation);
  console.log('Empty Case Fact Matrix:', emptyCase.factMatrix.map(f => `${f.issue}: [${f.evidenceStrength}]`));

  console.log('\n--- TEST 2: DOCUMENTED CASE (WITH INVOICES, BANK RTGS & SCN) ---');
  const fullCase = await runComplete13StepEvaluation(
    'Full Case Test',
    'ABC Corp',
    '27AAAAA0000A1Z5',
    '2018-19',
    'INR 50,00,000',
    'Order-in-Original / DRC-07',
    'Section 16(2)(c) recovery',
    'Taxpayer purchased goods under tax invoices and paid 100% via RTGS.',
    [
      { id: '1', name: 'Tax Invoices.pdf', type: 'Invoice', fileSize: '2 MB', uploadedAt: '2026-08-31', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'Tax Invoice 101 to 114 HSN 7208 with GSTIN' },
      { id: '2', name: 'HDFC Bank Statement.pdf', type: 'Bank Statement', fileSize: '1 MB', uploadedAt: '2026-08-31', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'RTGS UTR HDFC000123 paid full invoice amount' },
      { id: '3', name: 'E-Way Bills.pdf', type: 'E-Way Bill', fileSize: '3 MB', uploadedAt: '2026-08-31', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'E-Way Bill with vehicle transit logs' },
      { id: '4', name: 'DRC-07 Order.pdf', type: 'DRC-07', fileSize: '1.5 MB', uploadedAt: '2026-08-31', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'DRC-07 disallowing ITC without inquiry on seller' }
    ]
  );

  console.log('Full Case Readiness Score:', fullCase.readinessScore.totalScore, '/ 100');
  console.log('Full Case Viability Score:', fullCase.viabilityScore.totalScore, '/ 100');
  console.log('Full Case Verdict:', fullCase.finalOutput.executiveVerdict.recommendation);
}

test().catch(console.error);