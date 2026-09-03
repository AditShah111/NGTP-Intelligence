========================================================================================
ICAI / AICA LEVEL 2 CAPSTONE PROJECT SUBMISSION
PROJECT TITLE: GST NGTP LITIGATION INTELLIGENCE ENGINE & PRECEDENT HARMONIZER
PARTICIPANT:   CA. ADIT SHAH
TARGET DOMAIN: GST NON-GENUINE TAXABLE PERSON (NGTP) & SECTION 16(2)(c) LITIGATION
LIVE DEMO URL: https://ngtp-litigation-engine.onrender.com
========================================================================================

QUICK ORIENTATION FOR EXAMINERS:
----------------------------------------------------------------------------------------
This project addresses the widespread litigation arising from retrospective cancellation of 
supplier GST registrations (NGTP) and disallowance of Input Tax Credit under Section 16(2)(c).

The engine operates on a 13-Step Verification Pipeline that combines statutory logic with 
Article 141 Supreme Court precedents (Suncraft Energy SLP 27927/2023, Arise India, LGW Industries)
to conduct an automated evidentiary audit and generate court-ready appeal dossiers.

FOLDER CONTENTS:
----------------------------------------------------------------------------------------
01_Project_Summary/
   - AICA_Level_2_Capstone_Problem_Statement.pdf (2-Slide Landscape Presentation Deck)

02_System_Architecture_and_Prompts/
   - NGTP_13_Step_Verification_Pipeline.pdf (2-Slide Landscape Verification Deck)
   - Master prompt engineering specifications & Article 141 legal authority graphs.

03_Sample_Datasets/
   - Set1_Proceed_Worthy_Retrospective_Cancellation/
     * 7 complete authentic evidence files: Rule 46 Invoice, RTGS Bank Statement, E-Way Bill 
       Part A & B, Dharamnath Weighbridge Slip, NHAI FASTag Toll Receipts, GSTR-1 Ack, DRC-07.
     * Outcome: PROCEED (Score: 100/100, 95% Viability, 8 Strong Grounds).
   - Set2_Not_Worthy_HOLD_Missing_Transit/
     * 4 deficient evidence files: Deficient Invoice, Delayed Bank Statement (216 Days), DRC-07.
     * Outcome: HOLD (Score: 50/100, 43% Viability, 5 Deficient Grounds).

04_Media_and_Branding/
   - ICAI_AICA_Level2_YouTube_Thumbnail.jpg (Official ICAI AI Hackathon Branded Thumbnail 
     with CA. Adit Shah's portrait).

05_Source_Code/
   - Complete production Next.js 14 + TypeScript full-stack litigation engine.

HOW TO TEST THE SYSTEM:
----------------------------------------------------------------------------------------
1. Live Cloud Version: Open https://ngtp-litigation-engine.onrender.com
2. Local Version: Inside 05_Source_Code, run:
      npm install
      npm run dev
   Open http://localhost:3000 in your browser.
========================================================================================
