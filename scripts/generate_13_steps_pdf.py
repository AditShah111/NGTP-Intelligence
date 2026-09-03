import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, A4[1] - 36, "NGTP Litigation Intelligence Engine | 13-Step Verification Pipeline Technical Whitepaper")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, A4[1] - 42, A4[0] - 54, A4[1] - 42)
            
        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(A4[0] - 54, 30, footer_text)
        self.drawString(54, 30, "CONFIDENTIAL & PRIVILEGED | Automated Statutory & Evidentiary Audit")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 42, A4[0] - 54, 42)
        self.restoreState()

def build_13_step_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#B45309'),
        spaceAfter=14
    )
    
    meta_style = ParagraphStyle(
        'MetaText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#475569')
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=12,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#B45309'),
        spaceBefore=8,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155'),
        leftIndent=12,
        spaceAfter=3
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#1E293B')
    )

    story = []

    # Title Banner
    story.append(Paragraph("NGTP LITIGATION INTELLIGENCE ENGINE", title_style))
    story.append(Paragraph("Comprehensive 13-Step Automated Verification Pipeline & Evidentiary Audit Architecture", subtitle_style))
    
    # Metadata Box
    meta_table_data = [
        [
            Paragraph("<b>Document Classification:</b> Technical Specification & Legal Whitepaper", meta_style),
            Paragraph("<b>Target Domain:</b> GST SCNs, DRC-01/07 & Section 16(2)(c) Appeals", meta_style)
        ],
        [
            Paragraph("<b>Engine Version:</b> v1.0 Production Architecture", meta_style),
            Paragraph("<b>Constitutional Framework:</b> Article 141 Supreme Court Precedence", meta_style)
        ]
    ]
    t_meta = Table(meta_table_data, colWidths=[240, 247])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 12))

    # Executive Overview
    story.append(Paragraph("1. Executive Overview & System Philosophy", h1_style))
    story.append(Paragraph(
        "The NGTP Litigation Intelligence Engine is an autonomous multi-agent system designed to eliminate subjective guesswork, human oversight, and fatal procedural drafting omissions in Indian Goods and Services Tax (GST) litigation. Built specifically for disputes arising under Section 16(2)(c) (supplier tax payment condition) and Section 74 (fraudulent ITC / Non-Genuine Taxpayers), the engine executes a deterministic, 13-step sequential verification pipeline in the background before rendering an actionable verdict (PROCEED vs. HOLD) and synthesizing court-ready IRAC appeal briefs.",
        body_style
    ))
    story.append(Paragraph(
        "Rather than relying on unconstrained LLM text generation, the engine pairs strict statutory rule mathematics with deep dynamic case law calibration under Article 141 of the Constitution of India. The complete 13-step methodology is documented below.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # Detailed 13 Steps Breakdown
    steps_data = [
        (
            1, "Fact Matrix & Transaction Timeline Extraction",
            "src/service/fact-matrix-engine.ts",
            "Section 155 CGST Act & Section 106 Indian Evidence Act",
            "Extracts raw factual assertions from Show Cause Notices (DRC-01), Order-in-Original (DRC-07), and taxpayer written submissions. Builds an immutable chronological timeline of the underlying supply.",
            "Cross-references alleged facts against documentary evidence (invoices, bank statements, transport receipts). Flags internal contradictions such as payment dates preceding invoice dates, or supplier GSTIN cancellation predating transaction dates. Categorizes evidentiary strength: Established, Probable, Disputed, or Unsupported."
        ),
        (
            2, "Statutory Parameters Audit (P1 to P8 Calibration)",
            "src/service/statutory-engine.ts",
            "Sections 16(2)(a), 16(2)(b), 16(2)(c), 16(2)(d), 16(2)(aa), 2nd Proviso, 16(4)/(5), and 74(1)",
            "Tests whether the transaction satisfies each of the 8 mandatory statutory conditions governing input tax credit entitlement.",
            "Evaluates: P1 (Tax Invoice under Rule 46); P2 (Actual receipt of goods via E-Way Bills, FASTag, Weighbridge slips); P3 (Tax paid to Government / Suncraft exception); P4 (GSTR-3B return filing); P5 (Prospective GSTR-2B condition w.e.f. 01.01.2022); P6 (Payment within 180 days via bank RTGS); P7 (Section 16(5) retrospective validation up to 30.11.2021); P8 (Extended period of limitation & mens rea test under Section 74)."
        ),
        (
            3, "Judicial Precedent Retrieval & Real-Time Precedent Sync",
            "src/service/precedent-engine.ts & Gemini API Client",
            "Article 141 of the Constitution of India (Law declared by Supreme Court binding on all courts)",
            "Retrieves relevant High Court and Supreme Court authorities governing Section 16(2)(c) recovery from bona fide purchasing recipients.",
            "Continuously queries Google Gemini 1.5 Pro/Flash to identify recently pronounced rulings across all 25 Indian High Courts. Extracts the ratio decidendi, the court's physical evidentiary standard (what documents the judge relied on), and identifies adverse or distinguishable rulings."
        ),
        (
            4, "6-Axis Precedent Evidentiary Comparability & Conflict Resolution",
            "src/service/hierarchy-engine.ts",
            "Judicial discipline & binding precedent doctrine (Union of India v. Raghubir Singh)",
            "Ranks ingested precedents by authority and resolves competing judicial rulings under Article 141.",
            "Computes a Judicial Authority Strength Score (0 to 100) based on bench composition (Supreme Court = 98-100, Division Bench = 86, Single Judge = 74). Applies 6-axis comparability scoring: statutory similarity, factual similarity, evidentiary similarity, procedural similarity, court authority relevance, and distinguishing risk. Automatically resolves conflicts (e.g. Suncraft affirmed by SC overrides adverse rulings like Aastha Enterprises where bank proof was lacking)."
        ),
        (
            5, "Lower Authority Error & Jurisdictional Defect Audit",
            "src/service/error-analysis-engine.ts",
            "Section 73/74, Section 75(4) Natural Justice, & CBIC Circulars",
            "Scans the impugned SCN or Order for fatal procedural, evidentiary, and jurisdictional errors committed by the Proper Officer.",
            "Detects recurring administrative flaws: (1) Disallowance of ITC solely on GSTR-2A mismatch in violation of Circular 183; (2) Mechanical recovery from buyer without initiating proceedings against defaulting supplier (violating D.Y. Beathel); (3) Invoking Section 74 extended limitation without establishing fraud or mens rea; (4) Adjudication without mandatory personal hearing under Section 75(4)."
        ),
        (
            6, "Grounds of Appeal Optimizer (IRAC Formulation)",
            "src/service/submission-optimizer.ts",
            "Rule 108 CGST Rules, 2017 & Appellate Tribunal practice",
            "Converts raw factual contentions into structured, court-ready legal grounds of appeal.",
            "Restructures every argument into the formal IRAC legal paradigm: Issue (exact legal error), Rule (statutory section & binding circular), Application (taxpayer's documented facts), and Conclusion (prayer for quashing). Fortifies each ground with Supreme Court SLP order citations and calculates ground strength percentage."
        ),
        (
            7, "Adversarial Red-Team Defense War Room",
            "src/service/adversarial-redteam-engine.ts",
            "Revenue Department Standing Counsel adversarial modeling",
            "Simulates the toughest counter-arguments the Revenue will advance during oral hearings before the Appellate Authority or High Court.",
            "Subject the taxpayer's case to aggressive challenges: (1) Condition precedent strictly construed under ALD Automotive; (2) Inability to verify supplier existence; (3) Circular 183 inapplicable due to lack of supplier CA certification; (4) Collusion allegation. Tests whether the defense survives and provides pre-formulated rebuttals."
        ),
        (
            8, "Evidence Gap Prioritization & Action Plan (P0 / P1 / P2)",
            "src/service/evidence-gap-engine.ts",
            "Evidentiary threshold management",
            "Identifies missing or corroborative documents needed to elevate case viability before filing.",
            "Classifies missing items into three strict operational tiers: P0 Fatal (Must fix before filing, e.g. bank RTGS proof); P1 Strongly Recommended (Substantially enhances survival probability, e.g. E-Way Bills & FASTag records); P2 Corroborative (Additional strengthening, e.g. CA Certificate under Circular 183)."
        ),
        (
            9, "Quantitative Litigation Readiness Scoring (0 to 100)",
            "src/service/scoring-engine.ts",
            "Strict evidentiary mathematical weighting",
            "Calculates the objective litigation readiness score from first principles without artificial inflation.",
            "Computes score via weighted matrix: Rule 46 Tax Invoice (15 pts), Bank Payment & 180-Day RTGS Clearance (25 pts), Physical Transit & E-Way Bills (20 pts), Return Filing Reconciliation (15 pts), Retrospective Safe Harbor / Limitation (15 pts), Absence of Fraud / Section 74 Defence (10 pts). Penalizes unverified or missing documents."
        ),
        (
            10, "Litigation Viability Scoring & Forum Outcome Probability",
            "src/service/scoring-engine.ts",
            "Probabilistic appellate modeling",
            "Estimates the statistical probability of a favorable outcome across Appellate Authority (Section 107), GSTAT (Section 112), and High Court (Article 226).",
            "Synthesizes statutory readiness, precedent authority strength, lower authority error vulnerability, and judicial trend into a viability score (0 to 100) and probability band: HIGH (>75%), MODERATE (50-75%), or LOW (<50%)."
        ),
        (
            11, "Forward Litigation Decision Matrix",
            "src/service/scoring-engine.ts",
            "Risk-adjusted commercial decision theory",
            "Formulates the definitive actionable recommendation for senior tax executives and legal counsels.",
            "Outputs one of four unambiguous decisions: PROCEED (dossier is fully fortified), PROCEED AFTER RECTIFICATION (proceed only after procuring P0/P1 documents), HOLD (untenable in present form; high risk of bank attachment or adverse precedent), or DO NOT PROCEED (fatal defects / fraudulent supply trail)."
        ),
        (
            12, "Drafting Trap & Defect Audit",
            "src/service/draft-audit-engine.ts",
            "Pleading verification & procedural compliance",
            "Audits taxpayer's written submission, reply, or memo of appeal for catastrophic drafting errors.",
            "Flags fatal drafting traps: (1) Inadvertently conceding that the supplier failed to pay tax; (2) Failing to plead the doctrine of impossibility (lex non cogit ad impossibilia under Arise India); (3) Failing to invoke binding Circular 183; (4) Omitting express prayer for waiver of Section 50 interest and Section 73 penalty."
        ),
        (
            13, "Executive Verdict & Appeal Dossier Assembly",
            "src/service/evaluator-agent.ts",
            "Comprehensive litigation dossier compilation",
            "Synthesizes the outputs of all preceding 12 steps into a unified, 1-page executive summary view and exportable court-ready litigation brief.",
            "Generates downloadable legal dossiers formatted for statutory filings (Form GST APL-01) or High Court Writ Petitions, complete with Article 141 case index, IRAC grounds, evidentiary concordance tables, and oral argument notes."
        )
    ]

    for num, name, code_file, legal_basis, purpose, logic in steps_data:
        step_box = [
            [
                Paragraph(f"<b>STEP {num}: {name.upper()}</b>", table_header),
                Paragraph(f"<b>Engine:</b> {code_file}", table_header)
            ],
            [
                Paragraph(f"<b>Statutory & Legal Basis:</b> {legal_basis}", table_cell),
                Paragraph(f"<b>Primary Function:</b> {purpose}", table_cell)
            ],
            [
                Paragraph(f"<b>Methodology & Execution Logic:</b> {logic}", table_cell),
                Paragraph(f"<b>Status:</b> 100% Background Autonomous", table_cell)
            ]
        ]
        t_step = Table(step_box, colWidths=[240, 247])
        t_step.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E293B')),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8FAFC')),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(t_step)
        story.append(Spacer(1, 6))

    # Summary Architecture Table
    story.append(Spacer(1, 8))
    story.append(Paragraph("2. Summary Architecture & Decision Matrix", h1_style))
    
    summary_headers = [
        Paragraph("<b>Step #</b>", table_header),
        Paragraph("<b>Verification Phase</b>", table_header),
        Paragraph("<b>Core Law / Section</b>", table_header),
        Paragraph("<b>Output Metric</b>", table_header)
    ]
    summary_rows = [
        summary_headers,
        [Paragraph("1", table_cell), Paragraph("Fact Matrix & Timeline", table_cell), Paragraph("Sec 155 CGST / Evidence Act", table_cell), Paragraph("Reconciled Timeline & Contradiction Report", table_cell)],
        [Paragraph("2", table_cell), Paragraph("Statutory Parameters", table_cell), Paragraph("Sec 16(2)(a)-(d), 16(5)", table_cell), Paragraph("P1 to P8 Compliance Matrix", table_cell)],
        [Paragraph("3", table_cell), Paragraph("Precedent Retrieval", table_cell), Paragraph("Article 141 Constitution", table_cell), Paragraph("Supreme Court & HC Authorities", table_cell)],
        [Paragraph("4", table_cell), Paragraph("Comparability & Hierarchy", table_cell), Paragraph("Bench Strength Doctrine", table_cell), Paragraph("0-100 Authority Score & Conflict Resolution", table_cell)],
        [Paragraph("5", table_cell), Paragraph("Lower Authority Errors", table_cell), Paragraph("Sec 73/74, Sec 75(4)", table_cell), Paragraph("Jurisdictional Error Dossier", table_cell)],
        [Paragraph("6", table_cell), Paragraph("Grounds Optimizer", table_cell), Paragraph("IRAC Formulation", table_cell), Paragraph("Court-Ready Grounds of Appeal", table_cell)],
        [Paragraph("7", table_cell), Paragraph("Adversarial Red-Team", table_cell), Paragraph("Revenue Counsel Simulation", table_cell), Paragraph("Counter-Party Vulnerability Test", table_cell)],
        [Paragraph("8", table_cell), Paragraph("Evidence Gaps", table_cell), Paragraph("Evidentiary Thresholds", table_cell), Paragraph("P0 / P1 / P2 Actionable Gaps", table_cell)],
        [Paragraph("9", table_cell), Paragraph("Litigation Readiness", table_cell), Paragraph("Evidentiary Mathematical Math", table_cell), Paragraph("0-100 Readiness Score", table_cell)],
        [Paragraph("10", table_cell), Paragraph("Litigation Viability", table_cell), Paragraph("Appellate Probability Model", table_cell), Paragraph("0-100 Viability & Outcome Probability", table_cell)],
        [Paragraph("11", table_cell), Paragraph("Forward Decision", table_cell), Paragraph("Risk-Adjusted Decision Matrix", table_cell), Paragraph("PROCEED / HOLD / RECTIFY Verdict", table_cell)],
        [Paragraph("12", table_cell), Paragraph("Drafting Audit", table_cell), Paragraph("Pleading Defect Detection", table_cell), Paragraph("Fatal Trap Warnings & Corrections", table_cell)],
        [Paragraph("13", table_cell), Paragraph("Executive Dossier", table_cell), Paragraph("APL-01 / Writ Brief Assembly", table_cell), Paragraph("Complete Downloadable Legal Brief", table_cell)]
    ]
    t_sum = Table(summary_rows, colWidths=[35, 145, 137, 170])
    t_sum.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0F172A')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_sum)

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated 13-Step Verification PDF at: {output_path}")

if __name__ == '__main__':
    out_dir = r"C:\Users\ajay_\.gemini\antigravity\brain\b21d6f25-c48e-4a17-9d27-1f8b3d49fcc8"
    pub_dir = r"C:\Users\ajay_\.gemini\antigravity\scratch\ngtp-litigation-engine\public"
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(pub_dir, exist_ok=True)

    pdf_path_1 = os.path.join(out_dir, "NGTP_13_Step_Verification_Pipeline.pdf")
    pdf_path_pub = os.path.join(pub_dir, "NGTP_13_Step_Verification_Pipeline.pdf")
    
    build_13_step_pdf(pdf_path_1)
    build_13_step_pdf(pdf_path_pub)