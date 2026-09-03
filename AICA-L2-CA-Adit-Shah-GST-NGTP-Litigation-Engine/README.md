# GST NGTP Litigation Intelligence Engine & Precedent Harmonizer

**ICAI Artificial Intelligence in CA Practice (AICA Level 2) Capstone Project**  
**Author:** CA. Adit Shah  
**Live Production URL:** [https://ngtp-litigation-engine.onrender.com](https://ngtp-litigation-engine.onrender.com)  
**Official YouTube Thumbnail:** [View / Download Thumbnail](04_Media_and_Branding/ICAI_AICA_Level2_YouTube_Thumbnail.jpg)  

---

## 1. Executive Summary & Problem Statement

Across India, thousands of bona fide purchasing taxpayers face severe tax demands, interest under Section 50, and 100% penalties under Section 74 solely because their suppliers were subsequently investigated by the Directorate General of GST Intelligence (DGGI) or State GST authorities and had their GSTINs cancelled with retrospective effect as "Non-Genuine Taxable Persons" (NGTP).

### The Core Problem:
- Tax authorities mechanically issue Form GST DRC-01 and DRC-07 orders against purchasing recipients without pursuing the defaulting suppliers.
- Chartered Accountants spend 8 to 15 billable hours manually compiling invoices, transporter bilties, bank UTRs, and researching conflicting High Court precedents.
- Inadvertent drafting traps and evidentiary gaps (such as missing Part-B E-Way bills or payment delayed beyond 180 days) result in immediate summary dismissal before First Appellate Authorities.

### The Solution:
The **GST NGTP Litigation Intelligence Engine** is a full-stack, deterministic AI platform designed specifically for CA firms. In under 2 seconds, it executes a comprehensive **13-Step Verification Pipeline**, calculates a 7-factor quantitative Litigation Readiness Score (0–100), models appellate win-probability, tests defenses in an adversarial red-team war room, and synthesizes court-ready IRAC appeal grounds anchored on binding Supreme Court precedents.

---

## 2. 13-Step Verification Pipeline Architecture

The engine moves beyond black-box generative AI by implementing a deterministic evidentiary rules-engine coupled with constitutional Article 141 precedent binding:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        13-STEP VERIFICATION PIPELINE                                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE I: FACT & STATUTORY AUDIT                                                        │
│ • Step 1: Fact Matrix Ingestion (Automated reconciliation of invoices, UTRs & bilties) │
│ • Step 2: Statutory Parameter Audit (8 Core Tests: NGTP-P1 to P8)                      │
│                                                                                        │
│ PHASE II: JUDICIAL PRECEDENT SYNTHESIS                                                 │
│ • Step 3: Judicial Precedent Retrieval (Indexed High Court & Supreme Court database)   │
│ • Step 4: Article 141 Judicial Hierarchy Audit (Binds Supreme Court Suncraft Energy)  │
│                                                                                        │
│ PHASE III: DEFENSE FORTIFICATION & ADVERSARIAL STRESS-TEST                             │
│ • Step 5: Lower Authority Error Audit (Detects non-application of mind & Sec 79 bypass)│
│ • Step 6: Submission Optimizer (Drafts structured IRAC Grounds of Appeal)              │
│ • Step 7: Adversarial Red-Team War Room (Simulates Revenue Standing Counsel attacks)  │
│ • Step 8: Evidence Gap Engine (Classifies missing proof into P0 Mandatory vs P1)       │
│                                                                                        │
│ PHASE IV: QUANTITATIVE SCORING & FORWARD ACTION                                        │
│ • Step 9: Quantitative Litigation Readiness Score (0 to 100 Points)                    │
│ • Step 10: Appellate Viability & Win-Probability Modeling                              │
│ • Step 11: Forward Litigation Decision Tree (Remediation Roadmap)                      │
│ • Step 12: Appeal Draft Defect Audit (Scans for statutory traps & fatal admissions)    │
│ • Step 13: Executive Action Verdict & Structured Dossier Compilation                  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Statutory & Judicial Foundation

The system strictly implements the statutory provisions of the CGST Act, 2017:
- **Section 16(2)(a)**: Possession of tax invoices satisfying Rule 46.
- **Section 16(2)(b)**: Actual physical receipt of goods corroborated by Rule 138 E-Way bills and weighbridge records (*Halder Enterprises*).
- **Section 16(2)(c)**: Non-deposit by supplier harmonized with the **Doctrine of Impossibility** (*Arise India Ltd.* affirmed by SC).
- **Second Proviso to Section 16(2)**: Payment within 180 days via banking channels read with Rule 37.
- **Section 79**: Condition precedent of exhausting recovery against the supplier prior to proceeding against the buyer (*Suncraft Energy* Supreme Court SLP 27927/2023).
- **Section 155**: Discharge of initial burden of proof shifting to Revenue under Section 106 of the Evidence Act.

---

## 4. Benchmark Datasets Included

This repository contains two complete benchmark datasets demonstrating the platform's deterministic accuracy:

### 🟢 Dataset 1: Proceed Worthy (Retrospective Supplier Cancellation)
- **Taxpayer:** Apex Precision Engineering Pvt. Ltd.
- **Dispute:** INR 38,40,000 (FY 2018-19).
- **Factual Matrix:** Supplier registration was ACTIVE when invoice was issued and tax paid via RTGS in 12 days. Supplier filed GSTR-1. DGGI cancelled supplier registration ab-initio 5 years later. Full transit records present.
- **Evidence Attached (7 files):** Rule 46 Invoice, RTGS Bank Statement, E-Way Bill (Part A & B), Dharamnath Weighbridge Slip, NHAI FASTag Toll Receipts, GSTR-1 Ack, DRC-07 Impugned Order.
- **Engine Verdict:** **PROCEED (Readiness Score: 100/100 | Viability: 95% HIGH | 8 Grounds Formulation)**.

### 🔴 Dataset 2: Not Worthy of Proceeding / HOLD (Missing Transit & Delayed Payment)
- **Taxpayer:** Shaurya Infra Projects Ltd.
- **Dispute:** INR 52,00,000 (FY 2019-20).
- **Factual Matrix:** Zero E-Way bills, zero transporter consignment notes. Consideration paid after 216 days (exceeding 180-day statutory limit) without interim GSTR-3B credit reversal. Supplier operated from a 100 sq ft dummy room.
- **Evidence Attached (4 files):** Deficient Invoice, Delayed Bank Statement, DRC-07 Impugned Order, Statement of Facts.
- **Engine Verdict:** **HOLD (Readiness Score: 50/100 | Viability: 43% LOW | 5 Deficient Grounds)**.

---

## 5. Submission Package Folder Structure

```
AICA-L2-CA-Adit-Shah-GST-NGTP-Litigation-Engine/
├── 00_READ_ME_FIRST.txt
├── README.md
├── 01_Project_Summary/
│   └── AICA_Level_2_Capstone_Problem_Statement.pdf  (2-Slide Executive Landscape Deck)
├── 02_System_Architecture_and_Prompts/
│   └── NGTP_13_Step_Verification_Pipeline.pdf      (2-Slide Architecture Landscape Deck)
├── 03_Sample_Datasets/
│   ├── Set1_Proceed_Worthy_Retrospective_Cancellation/
│   │   ├── Set1_Tax_Invoice_Rule46.pdf
│   │   ├── Set1_Bank_RTGS_Statement.pdf
│   │   ├── Set1_EWay_Bill_PartA_B.pdf
│   │   ├── Set1_Weighbridge_FASTag_Receipt.pdf
│   │   ├── Set1_Tax_Ledger_GSTR1_Ack.pdf
│   │   ├── Set1_Impugned_DRC07_Order.pdf
│   │   └── Set1_Statement_of_Facts_and_Grounds.txt
│   └── Set2_Not_Worthy_HOLD_Missing_Transit/
│       ├── Set2_Tax_Invoice_Deficient.pdf
│       ├── Set2_Bank_Statement_Delayed.pdf
│       ├── Set2_Impugned_DRC07_Order.pdf
│       └── Set2_Statement_of_Facts_and_Grounds.txt
├── 04_Media_and_Branding/
│   └── ICAI_AICA_Level2_YouTube_Thumbnail.jpg       (Official ICAI AI Branded Thumbnail)
└── 05_Source_Code/                                  (Full-Stack Next.js Application)
```

---

## 6. How to Run the Application Locally

```bash
cd 05_Source_Code
npm install
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 7. Declaration & Intellectual Property

This Capstone Project is submitted as an original work for the **AICA Level 2 Certification** conducted by the **Institute of Chartered Accountants of India (ICAI)**.
