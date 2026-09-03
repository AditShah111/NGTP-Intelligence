import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.pdfgen import canvas

def draw_footer(c, doc):
    c.saveState()
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor("#64748B"))
    c.drawString(40, 22, "ICAI / AICA LEVEL 2 CAPSTONE PROJECT | Executive Presentation Brief")
    c.drawRightString(A4[0] - 40, 22, f"Slide {doc.page} of 2")
    c.setStrokeColor(colors.HexColor("#E2E8F0"))
    c.setLineWidth(0.5)
    c.line(40, 32, A4[0] - 40, 32)
    c.restoreState()

def build_executive_deck(pdf_path):
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=36,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()

    # Presentation Typography
    title_style = ParagraphStyle(
        'DeckTitle',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DeckSubtitle',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#B45309'),
        spaceAfter=10
    )

    h2_style = ParagraphStyle(
        'DeckH2',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=8,
        spaceAfter=6
    )

    card_title = ParagraphStyle(
        'CardTitle',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#0F172A')
    )

    card_metric = ParagraphStyle(
        'CardMetric',
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=19,
        textColor=colors.HexColor('#0284C7')
    )

    card_body = ParagraphStyle(
        'CardBody',
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#334155')
    )

    bullet_lead = ParagraphStyle(
        'BulletLead',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor('#1E293B'),
        leftIndent=10,
        spaceAfter=4
    )

    th_style = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.white)
    tc_style = ParagraphStyle('TC', fontName='Helvetica', fontSize=7.5, leading=10, textColor=colors.HexColor('#0F172A'))
    tc_bold = ParagraphStyle('TCB', fontName='Helvetica-Bold', fontSize=7.5, leading=10, textColor=colors.HexColor('#0F172A'))

    story = []

    # =========================================================================
    # SLIDE 1: THE CRISIS & THE PROBLEM STATEMENT
    # =========================================================================
    story.append(Paragraph("ICAI / AICA LEVEL 2 CAPSTONE PROJECT", title_style))
    story.append(Paragraph("Autonomous Legal Intelligence & Precedent Synthesis Engine for GST Section 16(2)(c) & NGTP Disputes", subtitle_style))

    # 3 High-Impact Stat Cards
    stat_cards = [
        [
            Paragraph("<b>THE MACRO CRISIS</b><br/><font color='#B45309' size='15'><b>Rs. 75,000+ Cr</b></font><br/>Locked in Section 16(2)(c) & NGTP demands against compliant buyers across India.", card_body),
            Paragraph("<b>MANUAL TIME SINK</b><br/><font color='#0284C7' size='15'><b>15 - 20 Hours</b></font><br/>Spent by a CA/Advocate auditing invoices, bank UTRs, FASTag, and E-Way bills per SCN.", card_body),
            Paragraph("<b>LITIGATION RISK</b><br/><font color='#DC2626' size='15'><b>65%+ Failure Rate</b></font><br/>Due to inadvertent drafting concessions & failure to invoke binding Supreme Court ratio.", card_body)
        ]
    ]
    t_stats = Table(stat_cards, colWidths=[170, 172, 173])
    t_stats.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#FEF3C7')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#F0F9FF')),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#FEF2F2')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_stats)
    story.append(Spacer(1, 8))

    # The 3 Core Legal Contradictions (Read-Aloud for Examiners)
    story.append(Paragraph("1. The Core Legal Dilemma: The 'Impossible' Condition", h2_style))
    
    story.append(Paragraph(
        "<b>• The Impossible Condition (Section 16(2)(c)):</b> Tax law conditions buyer's credit on the supplier's actual deposit of tax into the Government Treasury. A purchasing recipient can prove payment of consideration & GST via RTGS, but possesses zero legal machinery to compel a third-party seller to deposit tax.",
        bullet_lead
    ))
    story.append(Paragraph(
        "<b>• Retrospective Cancellation Injustice:</b> Tax authorities cancel supplier GSTINs retrospectively (ab-initio 5 years later) and mechanically deny credit to innocent buyers who transacted when the registration was active and valid on the GST portal (violating <i>LGW Industries</i> & <i>D.Y. Beathel</i>).",
        bullet_lead
    ))
    story.append(Paragraph(
        "<b>• Supreme Court Suncraft Ratio (Article 141):</b> The Calcutta High Court ruled—and the Supreme Court affirmed (SLP 27927/2023)—that Revenue cannot recover tax from the buyer without first exhausting all statutory avenues against the defaulting supplier. Yet lower authorities routinely violate this binding rule.",
        bullet_lead
    ))
    story.append(Paragraph(
        "<b>• Absence of Scientific Viability Scoring:</b> Tax leaders lack an objective tool to evaluate whether an appeal is viable (Proceed) or doomed (Hold), relying on subjective guesswork rather than evidentiary mathematics.",
        bullet_lead
    ))
    story.append(Spacer(1, 6))

    # The Engineering Solution
    story.append(Paragraph("2. The Capstone Engineering Solution: NGTP Intelligence Engine", h2_style))
    
    pillars = [
        [
            Paragraph("<b>1. Instant Audit (2 Secs)</b><br/>Replaces 20 hours of manual audit. Validates Rule 46 invoices, 180-day bank RTGS proof, and E-Way bills.", card_body),
            Paragraph("<b>2. Article 141 Synthesis</b><br/>Dynamically binds 8+ Supreme Court & High Court rulings (<i>Suncraft</i>, <i>Beathel</i>, <i>LGW</i>) into court-ready IRAC grounds.", card_body),
            Paragraph("<b>3. Decision Verdict</b><br/>Computes first-principles Readiness (0-100) & Viability scores: Definitive <b>PROCEED</b> vs <b>HOLD</b>.", card_body)
        ]
    ]
    t_pil = Table(pillars, colWidths=[170, 172, 173])
    t_pil.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_pil)

    # =========================================================================
    # SLIDE 2: THE DEMONSTRATION & EXAMINER TEST MATRIX
    # =========================================================================
    story.append(PageBreak())

    story.append(Paragraph("CAPSTONE DEMONSTRATION: PROCEED VS HOLD MATRIX", title_style))
    story.append(Paragraph("Empirical Proof: Testing Genuine Retrospective Cancellation vs Deficient Paper Supply", subtitle_style))

    demo_headers = [
        Paragraph("<b>Dimension</b>", th_style),
        Paragraph("<b>Dataset 1: Proceed Worthy (Retrospective Cancellation)</b>", th_style),
        Paragraph("<b>Dataset 2: Not Worthy (HOLD / Paper Supply)</b>", th_style)
    ]
    demo_rows = [
        demo_headers,
        [
            Paragraph("<b>Taxpayer Matter</b>", tc_bold),
            Paragraph("<b>M/s Apex Precision Engineering</b> (FY 2018-19)<br/>Disputed ITC: <b>INR 38,40,000</b>", tc_style),
            Paragraph("<b>M/s Shaurya Infra Projects</b> (FY 2019-20)<br/>Disputed ITC: <b>INR 52,00,000</b>", tc_style)
        ],
        [
            Paragraph("<b>Core Fact Pattern</b>", tc_bold),
            Paragraph("Supplier registration was <b>ACTIVE</b> at supply date. Tax paid via RTGS in 12 days. Registration cancelled retrospectively 5 years later.", tc_style),
            Paragraph("Allegation of circular trading under Sec 74. <b>NO E-Way bill, NO transit proof</b>. Payment delayed by 216 days (>180 days).", tc_style)
        ],
        [
            Paragraph("<b>Documentary Evidence</b>", tc_bold),
            Paragraph("Rule 46 Invoices + RTGS Bank Statement + E-Way Bill + Weighbridge Slip + FASTag Toll Logs + GSTR-1 Ack + DRC-07", tc_style),
            Paragraph("Deficient Invoices + Delayed Bank Statement + DRC-07<br/><b>[ZERO E-Way Bill & ZERO Transit Records]</b>", tc_style)
        ],
        [
            Paragraph("<b>Engine Statutory Audit</b>", tc_bold),
            Paragraph("<b>All 8 Parameters Satisfied (NGTP-P1 to P8)</b><br/>Protected by <i>LGW Industries</i> and <i>D.Y. Beathel</i>.", tc_style),
            Paragraph("<b>NGTP-P2 Failed</b> (Section 16(2)(b) Transit)<br/><b>High Section 74 Vulnerability</b> (Circular Trading)", tc_style)
        ],
        [
            Paragraph("<b>Litigation Readiness Score</b>", tc_bold),
            Paragraph("<font color='#047857' size='11'><b>100 / 100</b></font> (Optimal Litigation Standard)", tc_style),
            Paragraph("<font color='#DC2626' size='11'><b>50 / 100</b></font> (High Litigation Risk)", tc_style)
        ],
        [
            Paragraph("<b>Viability Assessment</b>", tc_bold),
            Paragraph("<font color='#047857' size='11'><b>95 / 100</b></font> (HIGH Probability of Success)", tc_style),
            Paragraph("<font color='#DC2626' size='11'><b>43 / 100</b></font> (LOW Probability of Success)", tc_style)
        ],
        [
            Paragraph("<b>Actionable Decision</b>", tc_bold),
            Paragraph("<font color='#047857'><b>PROCEED</b></font> &bull; File Form GST APL-01 Appeal", tc_bold),
            Paragraph("<font color='#DC2626'><b>HOLD</b></font> &bull; Do NOT proceed without transit proof", tc_bold)
        ]
    ]
    t_demo = Table(demo_rows, colWidths=[105, 205, 205])
    t_demo.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0F172A')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('BACKGROUND', (1, 5), (1, -1), colors.HexColor('#ECFDF5')), # light green for set 1 score
        ('BACKGROUND', (2, 5), (2, -1), colors.HexColor('#FEF2F2')), # light red for set 2 score
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_demo)
    story.append(Spacer(1, 8))

    # Candidate 30-Second Examiner Presentation Script
    story.append(Paragraph("3. 30-Second Pitch for Examiners (Candidate Script)", h2_style))
    script_box = [
        [Paragraph(
            "<b>\"Respected Examiners:</b> This engine solves the ₹75,000 Crore Section 16(2)(c) crisis for Indian CAs. "
            "In <b>Case 1</b>, when a supplier is retrospectively cancelled but the buyer paid via RTGS and has unbroken transit records, "
            "the engine scores it <b>100/100 PROCEED</b> based on Supreme Court <i>Suncraft</i> and Calcutta HC <i>LGW Industries</i>. "
            "In <b>Case 2</b>, when transit records are missing, it does not hallucinate; it immediately halts the case with <b>50/100 HOLD</b>, "
            "protecting the client from disastrous litigation. That is the power of deterministic legal AI.\"",
            card_body
        )]
    ]
    t_sc = Table(script_box, colWidths=[515])
    t_sc.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_sc)

    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
    print(f"Generated clean 2-slide executive deck at: {pdf_path}")

if __name__ == '__main__':
    out_brain = r"C:\Users\ajay_\.gemini\antigravity\brain\b21d6f25-c48e-4a17-9d27-1f8b3d49fcc8\AICA_Level_2_Capstone_Problem_Statement.pdf"
    out_pub = r"C:\Users\ajay_\.gemini\antigravity\scratch\ngtp-litigation-engine\public\AICA_Level_2_Capstone_Problem_Statement.pdf"
    build_executive_deck(out_brain)
    build_executive_deck(out_pub)