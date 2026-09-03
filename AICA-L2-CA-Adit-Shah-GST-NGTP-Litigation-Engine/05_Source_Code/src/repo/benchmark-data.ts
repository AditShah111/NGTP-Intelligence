import { CaseStudy } from '../types';

export const BENCHMARK_CASES: CaseStudy[] = [
  {
    "id": "case-suncraft-16-2-c",
    "title": "Landmark Section 16(2)(c) Supplier Default vs Beneficiary Recovery",
    "taxpayerName": "Apex Precision Engineering Pvt Ltd",
    "gstin": "19AAACA1234F1Z5",
    "financialYear": "2018-19",
    "disputedAmount": "INR 48,50,000 (ITC) + INR 48,50,000 (Penalty u/s 73) + Interest",
    "noticeType": "Order-in-Original / DRC-07",
    "primaryIssue": "Disallowance of ITC under Section 16(2)(c) due to supplier (M/s Steel Corp) filing GSTR-1 but failing to pay tax in GSTR-3B, without prior investigation against supplier.",
    "summary": "The Proper Officer issued DRC-07 disallowing ITC of Rs. 48.50 Lakhs solely on the ground that tax reflected in GSTR-2A was not remitted in GSTR-3B by the supplier. Taxpayer has genuine tax invoices, proof of banking payment (RTGS), and verified E-way bills.",
    "documents": [
      {
        "id": "doc-1",
        "name": "DRC-07 Order-in-Original No. 89/2023",
        "type": "DRC-07",
        "fileSize": "2.4 MB",
        "uploadedAt": "2026-08-15",
        "ocrReadability": "Clearly readable text",
        "extractedTextSnippet": "It is observed that supplier M/s Steel Corp did not deposit tax in GSTR-3B. Hence condition of Section 16(2)(c) is not satisfied. ITC disallowed with equal penalty."
      },
      {
        "id": "doc-2",
        "name": "Tax Invoices & E-Way Bills (14 Consignments)",
        "type": "Invoice",
        "fileSize": "18.1 MB",
        "uploadedAt": "2026-08-15",
        "ocrReadability": "Clearly readable text",
        "extractedTextSnippet": "Tax Invoice Nos. SC/18-19/0101 to 0114 with valid GSTIN and HSN 7208. Corresponding Part-A & Part-B E-Way bills generated with active vehicle numbers."
      },
      {
        "id": "doc-3",
        "name": "HDFC Bank Payment Statements & RTGS Slips",
        "type": "Bank Statement",
        "fileSize": "4.2 MB",
        "uploadedAt": "2026-08-15",
        "ocrReadability": "Clearly readable text",
        "extractedTextSnippet": "Full invoice amounts including CGST & SGST transferred via RTGS within 30 days of invoice date."
      },
      {
        "id": "doc-4",
        "name": "GSTR-2A & Portal Form GSTR-1 View",
        "type": "GSTR-2A",
        "fileSize": "1.8 MB",
        "uploadedAt": "2026-08-15",
        "ocrReadability": "Clearly readable text",
        "extractedTextSnippet": "Supplier uploaded all 14 invoices in GSTR-1; auto-populated in Appellant GSTR-2A table 3."
      }
    ],
    "factMatrix": [
      {
        "id": "fm-1",
        "issue": "Possession of Valid Tax Invoices",
        "allegedFact": "Taxpayer possesses 14 tax invoices containing all particulars under Rule 46.",
        "sourceDocument": "Tax Invoices SC/18-19/0101-0114",
        "pageParagraph": "Annexure A-1, Pages 1-28",
        "evidenceStrength": "Established",
        "contradiction": "None. Proper Officer admitted invoice validity.",
        "significance": "Satisfies Section 16(2)(a) CGST Act.",
        "ocrStatus": "Clearly readable text"
      },
      {
        "id": "fm-2",
        "issue": "Actual Receipt of Goods & Movement",
        "allegedFact": "Goods moved via designated commercial carriers with active E-Way bills and weighbridge inward slips.",
        "sourceDocument": "E-Way Bills & Inward Material Gate Pass",
        "pageParagraph": "Annexure A-2, Pages 29-58",
        "evidenceStrength": "Established",
        "contradiction": "None in SCN; Revenue made no adverse physical finding.",
        "significance": "Satisfies Section 16(2)(b) CGST Act.",
        "ocrStatus": "Clearly readable text"
      },
      {
        "id": "fm-3",
        "issue": "Payment of Consideration and Tax to Supplier",
        "allegedFact": "100% invoice amount paid through banking channels within 30 days.",
        "sourceDocument": "HDFC Bank Statements & CA Certificate",
        "pageParagraph": "Annexure A-3, Pages 59-64",
        "evidenceStrength": "Established",
        "contradiction": "None.",
        "significance": "Complies with 2nd Proviso to Section 16(2).",
        "ocrStatus": "Clearly readable text"
      },
      {
        "id": "fm-4",
        "issue": "Departmental Action Against Selling Dealer",
        "allegedFact": "Proper officer took NO recovery action or summons against selling dealer before demanding tax from purchasing beneficiary.",
        "sourceDocument": "DRC-07 Order Body",
        "pageParagraph": "Paragraph 4.2, Page 6",
        "evidenceStrength": "Established",
        "contradiction": "Direct breach of Calcutta HC Suncraft & Madras HC D.Y. Beathel principles.",
        "significance": "Fatal flaw in Revenue adjudication.",
        "ocrStatus": "Clearly readable text"
      }
    ],
    "statutoryParameters": [
      {
        "id": "sp-1",
        "parameterCode": "P1",
        "title": "Possession of Tax Invoice",
        "statutoryProvision": "Section 16(2)(a) CGST Act, 2017",
        "statutoryRequirement": "Registered person must be in possession of a tax invoice or debit note issued by a supplier.",
        "legalTest": "Does the document comply with Rule 46 (GSTIN, HSN, Tax rate, Serialized number)?",
        "burdenOfProof": "Initial burden on Taxpayer u/s 155.",
        "requiredEvidence": [
          "Tax Invoices",
          "ERP Purchase Register"
        ],
        "availableEvidence": [
          "14 Tax Invoices on record",
          "Rule 46 compliance audit certificate"
        ],
        "assessment": "SATISFIED",
        "risk": "LOW",
        "reason": "Proper officer has not disputed invoice authenticity."
      },
      {
        "id": "sp-2",
        "parameterCode": "P2",
        "title": "Receipt of Goods / Movement",
        "statutoryProvision": "Section 16(2)(b) CGST Act, 2017",
        "statutoryRequirement": "Registered person must have actually received the goods or services.",
        "legalTest": "Is there contemporaneous proof of physical transit, delivery, and factory receipt?",
        "burdenOfProof": "Taxpayer burden u/s 155.",
        "requiredEvidence": [
          "E-Way Bills",
          "Lorry Receipts (LR)",
          "Gate Inward Registers",
          "Weighbridge Slips"
        ],
        "availableEvidence": [
          "E-Way bills (Part A & B)",
          "Store Inward Vouchers",
          "Stock ledger consumption records"
        ],
        "assessment": "SATISFIED",
        "risk": "LOW",
        "reason": "Full documentary movement trail available."
      },
      {
        "id": "sp-3",
        "parameterCode": "P3",
        "title": "Tax Actually Paid to Government",
        "statutoryProvision": "Section 16(2)(c) CGST Act, 2017",
        "statutoryRequirement": "Subject to Section 41, the tax charged in respect of supply must be actually paid to the Government.",
        "legalTest": "Can ITC be recovered from the buyer when the seller fails to remit tax, without first exhausting recovery against the seller?",
        "burdenOfProof": "Revenue must establish seller default and attempt recovery from seller first (Suncraft / D.Y. Beathel).",
        "requiredEvidence": [
          "DRC-01A / DRC-01 issued to supplier",
          "Attachment proceedings against supplier"
        ],
        "availableEvidence": [
          "Supplier filed GSTR-1 (tax invoiced)",
          "Zero recovery steps taken by Department against supplier"
        ],
        "assessment": "PARTIALLY SATISFIED",
        "risk": "MEDIUM",
        "reason": "Statute requires payment to Govt, but binding High Court precedents hold recovery from buyer is impermissible without exhausting supplier remedy unless collusion is proved."
      },
      {
        "id": "sp-4",
        "parameterCode": "P4",
        "title": "GSTR-2B Mandatory Matching Condition",
        "statutoryProvision": "Section 16(2)(aa) CGST Act, 2017",
        "statutoryRequirement": "Details of invoice communicated in Form GSTR-2B.",
        "legalTest": "Is Section 16(2)(aa) applicable to FY 2018-19?",
        "burdenOfProof": "Legal question.",
        "requiredEvidence": [
          "Notification 39/2021-CT",
          "Finance Act 2021 date of enforcement (01.01.2022)"
        ],
        "availableEvidence": [
          "Section 16(2)(aa) inserted w.e.f 01.01.2022 and is strictly prospective"
        ],
        "assessment": "SATISFIED",
        "risk": "LOW",
        "reason": "Section 16(2)(aa) is prospective and cannot be applied retrospectively to FY 2018-19."
      }
    ],
    "precedents": [
      {
        "id": "prec-1",
        "caseName": "Suncraft Energy Pvt. Ltd. v. Assistant Commissioner",
        "court": "Calcutta High Court (Affirmed by Supreme Court in SLP (C) No. 27927/2023)",
        "citation": "(2023) 9 Centax 48 (Cal.) / 2023-VIL-489-CAL",
        "relevantProvision": "Section 16(2)(c) CGST Act, 2017 & Press Release dt 04.05.2018",
        "materialFacts": "ITC denied to buyer because supplier did not pay tax. Buyer produced invoices, payment proof. Revenue made no inquiry with supplier.",
        "ratioLegalPrinciple": "Before directing the recipient to reverse ITC or paying the tax, the proper officer should first proceed against the selling dealer. Only in exceptional cases of collusion or missing dealer can recipient be directly fastened with liability.",
        "necessaryConditions": [
          "Purchaser must be bona fide",
          "Purchaser has invoice and payment proof",
          "Supplier filed GSTR-1",
          "No inquiry or coercive recovery initiated against supplier"
        ],
        "distinguishingFacts": [
          "None. Facts are on all fours."
        ],
        "favourableApplicability": "HIGH",
        "adverseApplicability": "NONE",
        "parameterExtracted": "Department must exhaust remedies against defaulting supplier prior to demanding tax from bona fide recipient.",
        "presentCaseEvidenceSatisfying": [
          "Invoices",
          "RTGS payment slips",
          "GSTR-1 upload extract",
          "DRC-07 admission of no action on seller"
        ],
        "presentCaseEvidenceFailing": [],
        "litigationUse": "Primary anchor ground in First Appeal under Section 107 and Writ under Article 226.",
        "comparabilityScore": {
          "statutorySimilarity": 20,
          "factualSimilarity": 25,
          "evidentiarySimilarity": 20,
          "proceduralSimilarity": 10,
          "courtAuthorityRelevance": 15,
          "distinguishabilityRisk": 10,
          "totalScore": 100,
          "explanation": "Identical facts, identical FY 2018-19 period, identical Section 16(2)(c) disallowance without supplier inquiry. Supreme Court dismissed Revenue SLP."
        }
      }
    ],
    "lowerAuthorityErrors": [
      {
        "id": "err-1",
        "finding": "ITC rejected solely due to GSTR-2A vs GSTR-3B mismatch.",
        "lowerAuthorityReasoning": "Supplier did not pay tax in GSTR-3B, therefore buyer must reverse ITC under Sec 16(2)(c).",
        "evidenceIgnoredMisread": "Ignored valid invoices, E-way bills, and bank payment statements produced in reply.",
        "legalError": "Failed to apply binding Supreme Court affirmed Calcutta HC ruling in Suncraft Energy and CBIC Circular 183/15/2022-GST.",
        "relevantAuthority": "Suncraft Energy (2023) 9 Centax 48 (Cal.); Circular No. 183/15/2022-GST",
        "strength": "Fundamental"
      }
    ],
    "improvedSubmissions": [
      {
        "groundNumber": "Ground 1",
        "title": "Recovery from Recipient without Exhausting Remedies against Selling Dealer is Illegal",
        "proposition": "The Adjudicating Authority erred in demanding tax from the Appellant under Section 16(2)(c) without first initiating any recovery proceedings against the defaulting supplier M/s Steel Corp.",
        "supportingFacts": [
          "Appellant purchased goods under genuine tax invoices.",
          "Appellant paid full consideration including GST through RTGS.",
          "Supplier reported invoices in GSTR-1 which populated in GSTR-2A.",
          "Department has not issued DRC-01 or attached assets of the supplier."
        ],
        "evidence": [
          "Annexure A-1 (Invoices)",
          "Annexure A-2 (Bank Statements)",
          "Annexure A-3 (GSTR-2A)"
        ],
        "statutoryBasis": "Section 16(2)(c) CGST Act read with Press Release dated 04.05.2018",
        "precedent": "Suncraft Energy Pvt. Ltd. (Cal HC, affirmed by SC in SLP 27927/2023) & D.Y. Beathel Enterprises (Mad HC)",
        "application": "The Appellant is an innocent bona fide purchaser. Under established law, the Department cannot shift the collection burden onto the buyer without exhausting remedies against the supplier.",
        "likelyRevenueCounterargument": "Section 16(2)(c) is a non-negotiable statutory condition precedent; if tax is not deposited in the government treasury, no credit can be allowed regardless of bona fides (citing ALD Automotive / Bharti Telemedia).",
        "response": "The Honble Supreme Court in Suncraft Energy has specifically settled this issue under the CGST Act, 2017. Furthermore, CBIC Circular 183/15/2022-GST provides that for FY 2017-18 and 2018-19, where supplier has filed GSTR-1 and buyer produces CA Certificate / Bank proof, ITC cannot be denied.",
        "residualWeakness": "If the supplier GSTIN is found to be non-existent or cancelled ab-initio.",
        "groundStrength": 94
      }
    ],
    "redTeamItems": [
      {
        "id": "rt-1",
        "category": "Statutory Interpretation",
        "opposingArgument": "Section 16(2) starts with a non-obstante clause ('Notwithstanding anything contained in this section...'). Clause (c) unequivocally mandates that tax must actually be paid to the Government. Equity has no place in fiscal statutes.",
        "strengthOfOpposingArgument": 82,
        "taxpayerResponse": "The non-obstante clause governs the entitlement of the dealer. However, statutory impossibility of performance ('lex non cogit ad impossibilia') prevents punishing a buyer for a third-party seller default over which the buyer has no administrative control (Arise India v. CTT, upheld by SC).",
        "evidenceSupportingResponse": "Bank RTGS receipts, Supplier GSTR-1 extract, and CA certification under Circular 183.",
        "residualRisk": "LOW",
        "survivesAttack": true
      }
    ],
    "evidenceGaps": [
      {
        "id": "eg-1",
        "missingEvidence": "Chartered Accountant Certificate in terms of Circular No. 183/15/2022-GST confirming supplier non-payment was not fraudulent.",
        "legalRelevance": "CBIC Circular 183 provides a statutory safe harbor for FY 2017-18 and 2018-19 mismatches where difference exceeds Rs. 5 Lakhs.",
        "whyItMatters": "Mandatory under CBIC guidelines to compel First Appellate Authority to grant relief without requiring High Court intervention.",
        "possibleSource": "Statutory Auditor of Supplier or Taxpayer CA.",
        "impactIfObtained": "Converts assessment to 100% compliant with CBIC binding circular.",
        "impactIfUnavailable": "Appellant must rely solely on High Court judicial precedents.",
        "priority": "CRITICAL",
        "category": "Should be obtained"
      }
    ],
    "readinessScore": {
      "statutoryPosition": 18,
      "evidence": 19,
      "precedent": 15,
      "lowerAuthorityError": 15,
      "draftingQuality": 9,
      "counterargumentResilience": 9,
      "proceduralPosition": 10,
      "totalScore": 95,
      "interpretation": "85-100: Highly litigation-ready"
    },
    "viabilityScore": {
      "merits": 19,
      "evidenceQuality": 19,
      "precedentSupport": 15,
      "proceduralSoundness": 10,
      "opposingCaseDifficulty": 13,
      "curabilityOfGaps": 9,
      "appellateForumTrend": 9,
      "totalScore": 94,
      "probabilityOfFavourableOutcome": "HIGH",
      "probabilityNote": "Analytical estimate: 90%+ probability of complete relief at First Appellate Authority or High Court based on settled Suncraft & Circular 183 doctrine."
    },
    "forwardDecision": {
      "currentReadinessScore": 95,
      "potentialScoreAfterRemediation": 99,
      "scoreEnhancers": [
        "Obtain and annex Form Circular 183 CA Certificate",
        "Incorporate specific averment on prospective nature of Section 16(2)(aa)"
      ],
      "scoreReducers": [
        "Failure to tender proof of supplier active registration at the time of transaction"
      ],
      "evidenceDependentImprovements": [
        "Supplier VAT/GST active status certificate from GST portal on invoice dates"
      ],
      "nonCurableWeaknesses": [
        "None identified in present case record"
      ],
      "actionRequiredToAchievePotential": [
        "File Section 107 Appeal with CA Certificate under Circular 183",
        "Cite Supreme Court dismissal of Revenue SLP in Suncraft Energy"
      ]
    },
    "draftAudit": [
      {
        "id": "da-1",
        "parameter": "Precedent Citations",
        "issueDetected": "Draft mentions Calcutta HC Suncraft Energy but omits the Supreme Court SLP dismissal order citation.",
        "recommendedCorrection": "Update citation to include Honble Supreme Court SLP (C) No. 27927/2023 Order dated 14.12.2023.",
        "severity": "Medium"
      }
    ],
    "finalOutput": {
      "executiveVerdict": {
        "litigationReadiness": 95,
        "litigationViability": 94,
        "recommendation": "PROCEED AFTER RECTIFICATION",
        "top5Reasons": [
          "Directly covered by Supreme Court affirmed Calcutta HC judgment in Suncraft Energy.",
          "Revenue committed fundamental error by demanding tax from buyer without taking any recovery steps against seller.",
          "Full physical receipt and genuine banking payment proven with unassailable documentary evidence.",
          "Section 16(2)(aa) cannot be applied retrospectively to FY 2018-19.",
          "CBIC Circular 183/15/2022-GST provides an executive safe-harbor once CA certificate is placed on record."
        ]
      },
      "strongestLegalParameters": [
        "Lex non cogit ad impossibilia - Law does not compel a person to perform an impossible act.",
        "Suncraft / D.Y. Beathel condition precedent: Exhaustion of recovery remedies against selling dealer."
      ],
      "weakestParameters": [
        "Section 16(2)(c) literal tax-paid condition if argued strictly before lower departmental officers."
      ],
      "strongestGroundsOfChallenge": [
        {
          "ground": "Recovery from buyer without investigating supplier is illegal (Suncraft)",
          "rank": 1,
          "strength": 95
        }
      ],
      "strongestOpposingArguments": [
        "Section 16(2)(c) strict condition precedent regarding receipt of tax in government exchequer."
      ],
      "evidenceGapReport": [
        "Attach CA Certificate as per Circular 183/15/2022 Annexure A."
      ],
      "precedentMatrix": [
        {
          "precedent": "Suncraft Energy (Cal HC / SC)",
          "applicability": "Controlling / Direct Ratio",
          "score": 100
        }
      ],
      "lowerAuthorityErrorMatrix": [
        {
          "error": "Disallowance solely based on GSTR-2A mismatch without examining seller",
          "significance": "Fundamental jurisdictional defect"
        }
      ],
      "draftDefects": [
        {
          "defect": "Missing Supreme Court SLP citation for Suncraft Energy",
          "severity": "Medium"
        }
      ],
      "litigationImprovementPlan": {
        "p0MustFixBeforeFiling": [
          "Obtain CA certificate in format prescribed in Circular 183/15/2022 and annex to Appeal memo."
        ],
        "p1StronglyRecommended": [
          "Plead the prospective effect of Section 16(2)(aa) inserted via Finance Act 2021."
        ],
        "p2AdditionalStrengthening": [
          "Include vehicle toll data / FASTag transit logs to reinforce Section 16(2)(b) receipt."
        ]
      },
      "finalLitigationAssessment": {
        "shouldProceed": true,
        "proceedExplanation": "The case has exceptional legal merits. The lower authority order is in direct contravention of binding judicial precedents and CBIC circulars.",
        "singleBiggestRisk": "Departmental bias at First Appellate stage; may require statutory pre-deposit (10%) and pursuit up to Tribunal / High Court.",
        "singleStrongestAdvantage": "Unbroken chain of tax invoices, E-way bills, RTGS bank receipts, and Supreme Court affirmation of Suncraft.",
        "evidenceMostNeeded": "Circular 183 Chartered Accountant Certificate.",
        "propositionRequiringCarefulDrafting": "Framing Section 16(2)(c) through the lens of impossibility of performance and mandatory seller recovery without conceding non-remittance."
      }
    }
  }
];
