import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfgen import canvas

def draw_header_footer(c, doc):
    c.saveState()
    width, height = landscape(A4)
    
    # Top Accent Bar (Navy + Amber stripe)
    c.setFillColor(colors.HexColor("#0F172A"))
    c.rect(0, height - 7, width, 7, fill=True, stroke=False)
    c.setFillColor(colors.HexColor("#D97706"))
    c.rect(0, height - 10, 200, 3, fill=True, stroke=False)
    
    # Bottom Footer
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor("#64748B"))
    c.drawString(40, 18, "ICAI / AICA LEVEL 2 CAPSTONE PROJECT  |  13-Step Legal Intelligence & Precedent Verification Pipeline")
    c.drawRightString(width - 40, 18, f"Slide {doc.page} of 2")
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setLineWidth(0.5)
    c.line(40, 28, width - 40, 28)
    c.restoreState()

def build_13_step_deck(pdf_path):
    width, height = landscape(A4) # 841.89 x 595.28
    usable_width = width - 80     # 761.89 pt

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A4),
        leftMargin=40,
        rightMargin=40,
        topMargin=22,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()

    # Typography
    title_style = ParagraphStyle(
        'MainTitle',
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=23,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=2
    )

    sub_style = ParagraphStyle(
        'SubTitle',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#D97706'),
        spaceAfter=12
    )

    phase_hdr = ParagraphStyle(
        'PhaseHdr',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.white
    )

    step_num = ParagraphStyle(
        'StepNum',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#B45309')
    )

    step_title = ParagraphStyle(
        'StepTitle',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )

    step_desc = ParagraphStyle(
        'StepDesc',
        fontName='Helvetica',
        fontSize=7.6,
        leading=10.5,
        textColor=colors.HexColor('#334155')
    )

    story = []

    # =========================================================================
    # SLIDE 1: STEPS 1 TO 7 (EVIDENTIARY AUDIT, PRECEDENTS & RED TEAM)
    # =========================================================================
    story.append(Paragraph("13-STEP LEGAL INTELLIGENCE & VERIFICATION PIPELINE", title_style))
    story.append(Paragraph("Phase I to Phase III: Evidentiary Ingestion, Statutory Audit, Article 141 Synthesis & Adversarial Red-Team", sub_style))

    # 4 Column Pipeline Grid for Steps 1 - 7
    col_w = usable_width / 4.0 # ~190.5 pt each

    p1_cells = [
        Paragraph("<b>PHASE I: FACT & STATUTORY AUDIT</b>", phase_hdr),
        Paragraph("<b>PHASE II: JUDICIAL SYNTHESIS</b>", phase_hdr),
        Paragraph("<b>PHASE III: DEFENSE STRENGTHENING</b>", phase_hdr),
        Paragraph("<b>PHASE III: COUNTER-ATTACK AUDIT</b>", phase_hdr)
    ]

    p1_content = [
        [
            Paragraph("<b>STEP 1: Fact Matrix Ingestion</b>", step_title),
            Paragraph("<b>STEP 3: Precedent Retrieval</b>", step_title),
            Paragraph("<b>STEP 5: Lower Authority Errors</b>", step_title),
            Paragraph("<b>STEP 7: Adversarial Red-Team</b>", step_title)
        ],
        [
            Paragraph("Parses SCN, DRC-07, invoices, bank records, and bilties. Extracts dates, UTRs, HSN codes, and supplier GSTIN history automatically.", step_desc),
            Paragraph("Retrieves applicable High Court & Supreme Court rulings indexed by legal issue, financial year, and factual matrix alignment.", step_desc),
            Paragraph("Audits notice for non-application of mind, jurisdictional overreach, mechanical Section 74 invocation, and denial of natural justice.", step_desc),
            Paragraph("Simulates aggressive Revenue counterarguments (e.g. non-obstante Sec 16(2), Section 155 burden) to test defense resilience.", step_desc)
        ],
        [
            Paragraph("<b>STEP 2: Statutory Parameter Audit</b>", step_title),
            Paragraph("<b>STEP 4: Article 141 Hierarchy</b>", step_title),
            Paragraph("<b>STEP 6: Submission Optimizer</b>", step_title),
            Paragraph("<b>STEP 8: Evidence Gap Engine</b>", step_title)
        ],
        [
            Paragraph("Evaluates 8 core statutory tests (NGTP-P1 to P8): Rule 46 particulars, physical transit (16(2)(b)), 180-day bank remittance, and GSTR-2B prospective rules.", step_desc),
            Paragraph("Audits precedent bindingness under Art. 141. Binds Supreme Court <i>Suncraft Energy</i> ratio requiring Revenue to first pursue defaulting seller.", step_desc),
            Paragraph("Drafts court-ready, fortified appeal submissions structured in classical IRAC format (Issue, Rule, Application, Conclusion) with statutory citations.", step_desc),
            Paragraph("Identifies missing transit records, absent bank statements, or lack of Circular 183 CA certificates, categorizing them as P0 (Mandatory) or P1.", step_desc)
        ]
    ]

    table_data_s1 = [p1_cells] + p1_content
    t_s1 = Table(table_data_s1, colWidths=[col_w, col_w, col_w, col_w])
    t_s1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#FFFBEB')),
        ('BACKGROUND', (1,1), (1,-1), colors.HexColor('#F0F9FF')),
        ('BACKGROUND', (2,1), (2,-1), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (3,1), (3,-1), colors.HexColor('#FEF2F2')),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_s1)

    # =========================================================================
    # SLIDE 2: STEPS 9 TO 13 (QUANTITATIVE SCORING & FINAL VERDICT)
    # =========================================================================
    story.append(PageBreak())

    story.append(Paragraph("13-STEP LEGAL INTELLIGENCE & VERIFICATION PIPELINE", title_style))
    story.append(Paragraph("Phase IV & V: Mathematical Readiness Scoring, Appellate Viability & Autonomous Decision Engine", sub_style))

    # Grid for Steps 9 - 13
    col2_w = usable_width / 3.0 # ~254 pt each

    p2_cells = [
        Paragraph("<b>PHASE IV: QUANTITATIVE SCORING</b>", phase_hdr),
        Paragraph("<b>PHASE V: FORWARD LITIGATION TREE</b>", phase_hdr),
        Paragraph("<b>PHASE VI: FINAL ACTION VERDICT</b>", phase_hdr)
    ]

    p2_content = [
        [
            Paragraph("<b>STEP 9: Litigation Readiness Score (0-100)</b>", step_title),
            Paragraph("<b>STEP 11: Forward Litigation Decision</b>", step_title),
            Paragraph("<b>STEP 13: Executive Verdict & Export</b>", step_title)
        ],
        [
            Paragraph("Deterministic 7-factor evidentiary scoring:<br/>"
                      "&bull; Statutory Position (Max 20)<br/>"
                      "&bull; Evidence Quality & Transit (Max 20)<br/>"
                      "&bull; Precedent Binding Weight (Max 15)<br/>"
                      "&bull; Lower Authority Error Audit (Max 15)<br/>"
                      "&bull; Counterargument Resilience (Max 10)<br/>"
                      "&bull; Procedural Soundness (Max 10)<br/>"
                      "&bull; Drafting Quality (Max 10)", step_desc),
            Paragraph("Builds dynamic remediation roadmap:<br/>"
                      "&bull; <b>Potential Score Post-Remediation:</b> Quantifies expected score increase after attaching missing records.<br/>"
                      "&bull; <b>P0 Remediation:</b> Must attach bank RTGS statement before filing appeal.<br/>"
                      "&bull; <b>P1 Remediation:</b> Secure E-Way bills & Circular 183 CA Certificate.", step_desc),
            Paragraph("Delivers definitive, unambiguous decision:<br/>"
                      "&bull; <font color='#047857'><b>PROCEED (80 - 100):</b></font> Fully fortified appeal; high probability of complete relief.<br/>"
                      "&bull; <font color='#D97706'><b>PROCEED AFTER RECTIFICATION (60-79):</b></font> Cure evidence gaps before filing.<br/>"
                      "&bull; <font color='#DC2626'><b>HOLD (40 - 59):</b></font> High litigation risk (missing transit/payment).<br/>"
                      "&bull; <font color='#7F1D1D'><b>DO NOT PROCEED (<40):</b></font> Fatal evidentiary void.<br/>"
                      "&bull; <b>Export:</b> Generates court-ready legal dossier.", step_desc)
        ],
        [
            Paragraph("<b>STEP 10: Appellate Viability Modeling</b>", step_title),
            Paragraph("<b>STEP 12: Draft Defect & Trap Audit</b>", step_title),
            Paragraph("<b>SYSTEM ARCHITECTURE SUMMARY</b>", step_title)
        ],
        [
            Paragraph("Calculates statistical win-probability across appellate forums (First Appellate Authority, High Court Writ) calibrated against historical precedent trends and evidentiary burden under Section 155.", step_desc),
            Paragraph("Scans draft grounds for fatal legal traps, inadvertent concessions of supplier non-payment, incorrect section citations, and ensures compliance with Rule 46 Rule 138 mandatory particulars.", step_desc),
            Paragraph("<b>Deterministic & Non-Hallucinatory:</b> The engine uses rules-based statutory logic and Article 141 judicial graphs to guarantee that scores reflect hard evidentiary law rather than AI guesswork.", step_desc)
        ]
    ]

    table_data_s2 = [p2_cells] + p2_content
    t_s2 = Table(table_data_s2, colWidths=[col2_w, col2_w, col2_w])
    t_s2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#FFFBEB')),
        ('BACKGROUND', (1,1), (1,-1), colors.HexColor('#F0F9FF')),
        ('BACKGROUND', (2,1), (2,-1), colors.HexColor('#F0FDF4')),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_s2)

    doc.build(story, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)
    print(f"Successfully generated 13-Step Landscape Deck at: {pdf_path}")

if __name__ == '__main__':
    out_brain = r"C:\Users\ajay_\.gemini\antigravity\brain\b21d6f25-c48e-4a17-9d27-1f8b3d49fcc8\NGTP_13_Step_Verification_Pipeline.pdf"
    out_pub = r"C:\Users\ajay_\.gemini\antigravity\scratch\ngtp-litigation-engine\public\NGTP_13_Step_Verification_Pipeline.pdf"
    build_13_step_deck(out_brain)
    build_13_step_deck(out_pub)