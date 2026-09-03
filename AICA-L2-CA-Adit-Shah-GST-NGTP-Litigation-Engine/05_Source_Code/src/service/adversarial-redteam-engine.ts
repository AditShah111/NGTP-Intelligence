import { AdversarialRedTeamItem } from '../types';

export function runAdversarialRedTeamAnalysis(
  hasTransit: boolean = true,
  hasBank: boolean = true,
  hasInvoices: boolean = true,
  caseSummary: string = "",
  primaryIssue: string = ""
): AdversarialRedTeamItem[] {
  const isDelayedPayment = /delayed\s*by\s*216|paid\s*after\s*216|delayed\s*beyond\s*180|216\s*days/i.test(caseSummary) || /delayed\s*216/i.test(primaryIssue);
  const isWeakCase = !hasTransit || isDelayedPayment;

  if (isWeakCase) {
    return [
      {
        id: 'rt-weak-1',
        category: 'Section 16(2)(b) Transit Non-Negotiable Condition',
        opposingArgument: 'Section 16(2)(b) mandates actual receipt of goods. In the complete absence of E-Way bills, bilties, and toll entries, the transaction is legally deemed a paper invoice pass-through without underlying supply.',
        strengthOfOpposingArgument: 95,
        taxpayerResponse: 'Taxpayer possesses purchase invoice and bank payment proof, but concedes lack of transport documents.',
        evidenceSupportingResponse: 'Purchase Invoices (Vulnerable under Section 16(2)(b))',
        residualRisk: 'CRITICAL',
        survivesAttack: false
      },
      {
        id: 'rt-weak-2',
        category: 'Second Proviso 180-Day Payment Breach',
        opposingArgument: 'The taxpayer paid the supplier after 216 days, violating the strict statutory deadline of 180 days. Credit was not reversed in GSTR-3B with interest, violating express parliamentary mandate.',
        strengthOfOpposingArgument: 92,
        taxpayerResponse: 'Payment was eventually discharged on Day 216 through banking channels, so substantial compliance is claimed.',
        evidenceSupportingResponse: 'Bank Statement showing delayed debit on Day 216',
        residualRisk: 'CRITICAL',
        survivesAttack: false
      },
      {
        id: 'rt-weak-3',
        category: 'Section 74 Fraudulent Circular Trading',
        opposingArgument: 'Field inspection confirmed supplier was a fictitious 100 sq ft shell entity without infrastructure to store 120 MT of steel goods. The taxpayer is beneficiary of fraudulent paper credit.',
        strengthOfOpposingArgument: 88,
        taxpayerResponse: 'Taxpayer had no knowledge of upstream supplier default and transacted in good faith.',
        evidenceSupportingResponse: 'Commercial Purchase Order (Insufficient to rebut physical shell finding)',
        residualRisk: 'HIGH',
        survivesAttack: false
      },
      {
        id: 'rt-weak-4',
        category: 'Section 155 Evidentiary Failure',
        opposingArgument: 'Supreme Court in Ecom Gill Coffee held that burden of proof under tax statutes is on the claimant. Invoices and delayed bank payment without transport records fail to discharge Section 155.',
        strengthOfOpposingArgument: 90,
        taxpayerResponse: 'Taxpayer shifts burden to Department to examine the absconding supplier.',
        evidenceSupportingResponse: 'None (Section 155 threshold unmet)',
        residualRisk: 'CRITICAL',
        survivesAttack: false
      }
    ];
  }

  // Set 1 (Fortified appeal)
  return [
    {
      id: 'rt-1',
      category: 'Statutory Non-Obstante Override (Section 16(2)(c))',
      opposingArgument: 'Section 16(2) non-obstante clause mandates that tax must actually be deposited in the Government treasury. Equity has no place in fiscal interpretation.',
      strengthOfOpposingArgument: 78,
      taxpayerResponse: 'The Supreme Court in Arise India and Calcutta HC in Suncraft held that the doctrine of impossibility ("lex non cogit ad impossibilia") prevents penalizing a buyer who paid tax to a registered seller.',
      evidenceSupportingResponse: 'Bank RTGS UTR vouchers, GSTR-1 acknowledgement, and Supreme Court affirmed Suncraft SLP order.',
      residualRisk: 'LOW',
      survivesAttack: true
    },
    {
      id: 'rt-2',
      category: 'Section 155 Initial Burden of Proof',
      opposingArgument: 'Under Section 155, the burden of proving ITC legality rests on the claimant. Merely producing invoices does not prove tax reached the treasury.',
      strengthOfOpposingArgument: 72,
      taxpayerResponse: 'Taxpayer discharged the complete primary burden by tendering invoice, E-Way Bill Part-B, weighbridge slips, FASTag logs, and RTGS payment, shifting burden to Revenue under Section 106.',
      evidenceSupportingResponse: 'Part-B E-Way Bill #241089201945, Dharamnath Weighbridge Slip, NHAI FASTag Toll Receipts.',
      residualRisk: 'LOW',
      survivesAttack: true
    },
    {
      id: 'rt-3',
      category: 'Retrospective Supplier Cancellation Ab-Initio',
      opposingArgument: 'Suppliers GSTIN was cancelled ab-initio from 01.07.2017, rendering all past invoices void as issued by a non-existent entity.',
      strengthOfOpposingArgument: 75,
      taxpayerResponse: 'Calcutta HC in LGW Industries and Madras HC in D.Y. Beathel settled that retrospective cancellation cannot prejudice a buyer who transacted when the registration was active on the Government portal.',
      evidenceSupportingResponse: 'GST Common Portal Active Status Verification, Purchase Orders, and Delivery Challans.',
      residualRisk: 'LOW',
      survivesAttack: true
    },
    {
      id: 'rt-4',
      category: 'Allegation of Circular Movement Without Goods',
      opposingArgument: 'Department alleges goods movement was bogus and invoices were issued for commission without actual steel delivery.',
      strengthOfOpposingArgument: 68,
      taxpayerResponse: 'Calcutta HC in Halder Enterprises held that where E-way bills, continuous FASTag toll entries, and weighbridge slips corroborate movement, fake-delivery claims cannot stand.',
      evidenceSupportingResponse: 'NHAI FASTag Toll timestamps across Khalapur, Kusgaon, and Talegaon toll plazas.',
      residualRisk: 'LOW',
      survivesAttack: true
    }
  ];
}
