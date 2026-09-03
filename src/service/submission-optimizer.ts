import { ImprovedSubmissionGround, PrecedentAnalysis, StatutoryParameter } from '../types';

export function improveSubmissions(
  primaryIssue: string,
  ingestedPrecedents: PrecedentAnalysis[] = [],
  statutoryParameters: StatutoryParameter[] = [],
  hasTransit: boolean = true,
  hasBank: boolean = true
): ImprovedSubmissionGround[] {
  const grounds: ImprovedSubmissionGround[] = [];

  // Helper to find relevant precedent from live corpus
  const findPrecedent = (keywords: string[]) => {
    return ingestedPrecedents.find(p => 
      keywords.some(kw => 
        p.caseName.toLowerCase().includes(kw.toLowerCase()) || 
        p.relevantProvision.toLowerCase().includes(kw.toLowerCase()) ||
        p.ratioLegalPrinciple.toLowerCase().includes(kw.toLowerCase())
      )
    );
  };

  // 1. Suncraft / Beathel Ground (Exhaustion of Remedies against Supplier)
  const suncraftPrec = findPrecedent(['suncraft', 'beathel', '16(2)(c)', 'supplier default']);
  const suncraftCitation = suncraftPrec 
    ? `${suncraftPrec.caseName} (${suncraftPrec.court}, Auth: ${suncraftPrec.judicialAuthorityStrengthScore || 98}/100 - ${suncraftPrec.article141Status})`
    : 'Suncraft Energy Pvt. Ltd. (Cal HC, affirmed by Honble Supreme Court in SLP 27927/2023) & D.Y. Beathel Enterprises (Madras HC)';

  grounds.push({
    groundNumber: 'Ground 1',
    title: 'Condition Precedent of Exhausting Statutory Remedies Against Selling Dealer (Article 141 Mandate)',
    proposition: 'The Adjudicating Authority erred in law and jurisdiction by demanding tax, interest, and penalty from the Appellant under Section 16(2)(c) without first initiating inquiry or recovery proceedings against the defaulting supplier.',
    supportingFacts: [
      'Appellant purchased goods under genuine tax invoices complying with Rule 46.',
      'Full consideration along with applicable GST was remitted to the supplier via banking RTGS channels within statutory timelines.',
      'The Department has neither issued DRC-01 nor initiated recovery proceedings against the selling dealer under Section 79.',
      'No summons under Section 70 was served on the supplier prior to penalizing the Appellant.'
    ],
    evidence: ['Tax Invoices (Rule 46)', 'Bank Statements with RTGS UTR timestamps', 'Vendor Ledger Reconciliation'],
    statutoryBasis: 'Section 16(2)(c) read with Section 41 & Section 79 CGST Act, 2017',
    precedent: suncraftCitation,
    application: 'Under the binding law declared by the Honble Supreme Court under Article 141 in Suncraft Energy, recovery cannot be made from the purchasing recipient without first exhausting all statutory avenues of recovery against the defaulting seller.',
    likelyRevenueCounterargument: 'Revenue contends that Section 16(2)(c) is a strict condition precedent per ALD Automotive, and credit cannot be allowed if tax was not deposited into the Government treasury.',
    response: 'The Honble Supreme Court in SLP (C) No. 27927/2023 specifically affirmed Suncraft Energy under the CGST Act. The Department cannot bypass statutory recovery against the seller simply because the buyer is easily accessible.',
    residualWeakness: 'Requires verified bank statement showing full invoice consideration paid to registered account.',
    groundStrength: 96
  });

  // 2. Retrospective Supplier Cancellation Ground (LGW Industries)
  const lgwPrec = findPrecedent(['lgw', 'retrospective', 'cancellation ab-initio', 'registration']);
  const lgwCitation = lgwPrec 
    ? `${lgwPrec.caseName} (${lgwPrec.court}, Auth: ${lgwPrec.judicialAuthorityStrengthScore || 88}/100)`
    : 'LGW Industries Ltd. & Ors. v. Union of India (Calcutta High Court, WPA 23512 of 2019)';

  grounds.push({
    groundNumber: 'Ground 2',
    title: 'Post-Facto Retrospective Cancellation of Supplier Registration Cannot Invalidate Past Bona Fide Credit',
    proposition: 'The Proper Officer erred in disallowing ITC on the premise that the supplier registration was subsequently cancelled with retrospective effect, ignoring that the supplier GSTIN was valid and active on the transaction date.',
    supportingFacts: [
      'On the date of supply and tax invoice issuance, the supplier GSTIN was shown as ACTIVE and VALID on the Common GST Portal.',
      'Appellant verified supplier credentials in good faith prior to entering commercial transactions.',
      'Subsequent administrative cancellation by the jurisdictional officer cannot operate retroactively to prejudice a bona fide purchasing dealer.'
    ],
    evidence: ['GST Portal Vendor Master Active Status Screenshot at Transaction Date', 'Purchase Orders', 'Inward Gate Registers'],
    statutoryBasis: 'Section 29 CGST Act read with Article 14 of the Constitution (Doctrine of Legitimate Expectation)',
    precedent: lgwCitation,
    application: 'The Calcutta High Court in LGW Industries held that retrospective cancellation of a selling dealer registration cannot invalidate ITC claimed by a genuine buyer who transacted while the registration was active.',
    likelyRevenueCounterargument: 'Revenue argues that cancellation ab-initio renders all past invoices void ab-initio as issued by a non-existent taxable person.',
    response: 'A retrospective executive act cannot penalize a citizen who acted upon the Governments official public portal representation. Disallowance violates the doctrine of legitimate expectation.',
    residualWeakness: 'Ensure supplier registration was indeed active on the exact invoice date.',
    groundStrength: 93
  });

  // 3. Doctrine of Impossibility under Article 14 (Arise India)
  const arisePrec = findPrecedent(['arise', 'impossibility', 'lex non cogit', 'radha krishan']);
  const ariseCitation = arisePrec 
    ? `${arisePrec.caseName} (${arisePrec.court}, Auth: ${arisePrec.judicialAuthorityStrengthScore || 95}/100 - Supreme Court Affirmed)`
    : 'Arise India Ltd. v. Commissioner of Trade & Taxes (Delhi HC, affirmed by Honble Supreme Court in SLP (C) 36717/2017)';

  grounds.push({
    groundNumber: 'Ground 3',
    title: 'Violation of Doctrine of Impossibility (Lex Non Cogit Ad Impossibilia) & Article 14',
    proposition: 'The Proper Officer erred in demanding compliance with an impossible condition under Section 16(2)(c), compelling the buyer to ensure the third-party supplier deposited tax into the Government exchequer.',
    supportingFacts: [
      'The Appellant has no legal mechanism, statutory power, or investigative machinery to compel the supplier to deposit tax with the Government.',
      'Appellant performed every duty within its control: paid the price, paid the tax, received the goods, and filed statutory returns.',
      'Treating compliant bona fide purchasers on par with defaulting suppliers violates the equality mandate of Article 14.'
    ],
    evidence: ['Bank Payment Records', 'Statutory Returns GSTR-3B', 'Certified Purchase Daybook'],
    statutoryBasis: 'Article 14 of the Constitution of India & Legal Maxim Lex Non Cogit Ad Impossibilia',
    precedent: ariseCitation,
    application: 'The Supreme Court affirmed that the law does not compel a man to do that which he cannot possibly perform. Conditioning credit on third-party deposit without providing investigative machinery is unconstitutional.',
    likelyRevenueCounterargument: 'Article 14 cannot be invoked to override an express statutory condition precedent enacted by Parliament.',
    response: 'Statutory provisions must be read in a manner that avoids manifest arbitrariness. The Supreme Court in Arise India read down identical supplier-default provisions.',
    residualWeakness: 'Requires proof of bona fide commercial diligence.',
    groundStrength: 95
  });

  // 4. Prospective Section 16(2)(aa) & Circular 183 Safe-Harbor (M. Trade Links / Diya Agencies)
  const tradeLinksPrec = findPrecedent(['trade links', 'diya', '16(2)(aa)', 'circular 183', '183/15/2022']);
  const tradeLinksCitation = tradeLinksPrec 
    ? `${tradeLinksPrec.caseName} (${tradeLinksPrec.court}, Auth: ${tradeLinksPrec.judicialAuthorityStrengthScore || 87}/100)`
    : 'M. Trade Links v. Union of India (Kerala HC Division Bench) & Diya Agencies v. State Tax Officer (Kerala HC)';

  grounds.push({
    groundNumber: 'Ground 4',
    title: 'Prospective Applicability of Section 16(2)(aa) & Entitlement to Circular 183 Safe-Harbor',
    proposition: 'The Proper Officer erred in retrospectively applying GSTR-2B matching conditions to periods prior to 01.01.2022 and in refusing to grant safe-harbor relief under binding CBIC Circular No. 183/15/2022-GST.',
    supportingFacts: [
      'The dispute relates to transactions executed prior to 01.01.2022, when Section 16(2)(aa) was not in force.',
      'GSTR-2A during the relevant period was merely a dynamic facilitation view, not a statutory condition precedent.',
      'Taxpayer satisfies all criteria under Circular 183/15/2022-GST for reconciliation of GSTR-2A vs 3B mismatches.'
    ],
    evidence: ['Notification No. 39/2021-CT dated 21.12.2021', 'CBIC Circular No. 183/15/2022-GST Certificate', 'Supplier Ledger Reconciliation'],
    statutoryBasis: 'Section 16(2)(aa) CGST Act (w.e.f. 01.01.2022) & Section 168 CGST Act (Binding effect of Circulars)',
    precedent: tradeLinksCitation,
    application: 'The Division Bench of the Kerala High Court in M. Trade Links held that Section 16(2)(aa) is strictly prospective, and circulars issued by CBIC are binding on adjudicating officers.',
    likelyRevenueCounterargument: 'Circular 183 only applies if the taxpayer produces a formal Chartered Accountant certificate from the supplier.',
    response: 'Appellant has produced the requisite documentary certification and payments through banking channels, fully satisfying paragraph 4 of Circular 183.',
    residualWeakness: 'CA Certificate must be executed and annexed.',
    groundStrength: 92
  });

  // 5. Physical Movement & Delivery Proof (Halder Enterprises / Gheru Lal)
  const halderPrec = findPrecedent(['halder', 'transit', 'e-way', 'gherulal', 'physical']);
  const halderCitation = halderPrec 
    ? `${halderPrec.caseName} (${halderPrec.court}, Auth: ${halderPrec.judicialAuthorityStrengthScore || 86}/100)`
    : 'M/s Halder Enterprises v. State of WB (Cal HC) & Gheru Lal Bal Chand v. State of Haryana (P&H HC DB)';

  grounds.push({
    groundNumber: 'Ground 5',
    title: 'Documentary Disproof of Fake Billing / Circular Trading Allegations through Unbroken Transit Trail',
    proposition: 'The Proper Officer erred in alleging non-genuine supply or paper-only billing without rebutting the contemporaneous physical movement records, E-Way bills, and factory inward gate records.',
    supportingFacts: [
      'Transactions are supported by valid E-Way Bills with Part-A and Part-B vehicle details.',
      'Physical receipt of goods is recorded in the factory inward register and raw material consumption accounts.',
      'Revenue has not examined the transporter or proved that the transport vehicles did not ply on the designated routes.'
    ],
    evidence: ['E-Way Bills (Part A & B)', 'Lorry Receipts (LR)', 'Factory Inward Gate Pass', 'Weighbridge Slips', 'FASTag Toll Records'],
    statutoryBasis: 'Section 16(2)(b) read with Section 155 CGST Act, 2017 & Section 106 Evidence Act',
    precedent: halderCitation,
    application: 'The Calcutta High Court in Halder Enterprises held that where physical carriage is corroborated by E-Way bills and inward toll/delivery records, the transaction cannot be treated as a paper transaction.',
    likelyRevenueCounterargument: 'Department asserts that suppliers premises were found non-existent upon subsequent inspection by DGGI/anti-evasion.',
    response: 'Subsequent closure of premises does not establish that past supplies corroborated by E-Way bills and physical weighment never occurred.',
    residualWeakness: hasTransit ? 'None.' : 'E-Way bill copies must be annexed to substantiate ground.',
    groundStrength: hasTransit ? 94 : 78
  });

  // 6. Section 74 Penalty & Extended Period Rebuttal (Uniworth Textiles / Hindustan Steel)
  const uniworthPrec = findPrecedent(['uniworth', 'hindustan steel', 'mens rea', '74(1)', 'penalty']);
  const uniworthCitation = uniworthPrec 
    ? `${uniworthPrec.caseName} (${uniworthPrec.court}, Auth: ${uniworthPrec.judicialAuthorityStrengthScore || 96}/100 - Supreme Court)`
    : 'Uniworth Textiles Ltd. v. CCE (Supreme Court) & Hindustan Steel Ltd. v. State of Orissa (Supreme Court)';

  grounds.push({
    groundNumber: 'Ground 6',
    title: 'Unlawful Invocation of Section 74 Extended Period & Illegality of Penalty in Absence of Mens Rea',
    proposition: 'The Proper Officer erred in invoking the 5-year extended period of limitation and levying 100% penalty under Section 74 without proving deliberate deception, willful misstatement, or collusion against the Appellant.',
    supportingFacts: [
      'All purchases were recorded in audited books of account and regular GSTR-3B returns.',
      'The SCN contains no specific averment or documentary evidence establishing collusion or cash kickbacks between the Appellant and the supplier.',
      'Mere supplier non-compliance does not satisfy the statutory threshold of deliberate suppression by the recipient.'
    ],
    evidence: ['Audited Financial Statements', 'Statutory GSTR-3B Returns', 'Vendor Ledger Accounts'],
    statutoryBasis: 'Section 74(1) & Section 73(1) CGST Act, 2017',
    precedent: uniworthCitation,
    application: 'The Honble Supreme Court in Uniworth Textiles held that the extended period cannot be invoked without positive evidence of deliberate fraud. Culpable mental state is an indispensable prerequisite for penalty.',
    likelyRevenueCounterargument: 'Under Section 74, availment of credit on fake invoices constitutes fraud per se, justifying extended limitation.',
    response: 'Fraud cannot be presumed; it must be pleaded with precision and proved with tangible evidence against the specific person charged.',
    residualWeakness: 'Ensure no inculpatory statements were recorded during inquiry.',
    groundStrength: 95
  });

  // 7. Dynamic Injection: If any novel or live precedent from Gemini is in the corpus, add it as a specialized ground!
  const standardCases = ['suncraft', 'beathel', 'lgw', 'arise', 'trade links', 'diya', 'halder', 'gherulal', 'uniworth', 'hindustan'];
  const novelPrecedents = ingestedPrecedents.filter(p => 
    !standardCases.some(sc => p.caseName.toLowerCase().includes(sc))
  );

  novelPrecedents.slice(0, 3).forEach((np, idx) => {
    grounds.push({
      groundNumber: `Ground ${grounds.length + 1}`,
      title: `Judicial Mandate under ${np.caseName} (${np.court})`,
      proposition: `The Adjudicating Authority acted contrary to the ratio decidendi laid down in ${np.caseName}, violating established statutory standards governing ${np.relevantProvision}.`,
      supportingFacts: [
        `Appellant transaction facts directly align with the benchmark facts in ${np.caseName}.`,
        `Taxpayer has tendered the physical evidences relied on by the Court: ${(np.evidencesReliedOnByCourt || []).slice(0, 3).join(', ')}.`,
        `Relying on ratio: ${np.ratioLegalPrinciple.slice(0, 180)}...`
      ],
      evidence: np.evidencesReliedOnByCourt || ['Invoices', 'Bank Proof'],
      statutoryBasis: `${np.relevantProvision} (Bench Authority: ${np.judicialAuthorityStrengthScore || 85}/100)`,
      precedent: `${np.caseName} (${np.court}) [${np.article141Status}]`,
      application: `The ratio decidendi of ${np.caseName} squarely governs this matter: ${np.ratioLegalPrinciple}`,
      likelyRevenueCounterargument: 'Revenue may contend that the facts of this matter are distinguishable on evidentiary grounds.',
      response: `The evidentiary matrix of the Appellant matches the threshold recognized by the ${np.court}.`,
      residualWeakness: 'Ensure concordance table matches court evidentiary standards.',
      groundStrength: np.judicialAuthorityStrengthScore || 88
    });
  });

  return grounds;
}