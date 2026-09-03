with open("scripts/generate_capstone_problem_statement.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the title subtitle and description to highlight retrospective cancellation
content = content.replace(
    'Paragraph("Automated Legal Intelligence & Precedent Recalibration Engine for GST Section 16(2)(c) & NGTP Disputes", subtitle_style)',
    'Paragraph("Automated Legal Intelligence Engine for GST Section 16(2)(c), NGTP & Retrospective Cancellation Disputes", subtitle_style)'
)

content = content.replace(
    'Paragraph("M/s Apex Precision Engineering (₹38.4L SCN)", table_cell)',
    'Paragraph("M/s Apex Precision Engineering (₹38.4L - Retrospective Cancellation of Supplier GSTIN)", table_cell)'
)

content = content.replace(
    'Paragraph("M/s Shaurya Infra Projects (₹52.0L SCN)", table_cell)',
    'Paragraph("M/s Shaurya Infra Projects (₹52.0L - Paper Supply / No E-Way Bill)", table_cell)'
)

content = content.replace(
    'Paragraph("<b>85–95 / 100 (HIGH Probability)</b>", table_cell)',
    'Paragraph("<b>100 / 100 (HIGH Viability 95%)</b>", table_cell)'
)

content = content.replace(
    'Paragraph("<b>40–55 / 100 (LOW / CRITICAL Risk)</b>", table_cell)',
    'Paragraph("<b>50 / 100 (LOW Viability 43%)</b>", table_cell)'
)

content = content.replace(
    'Paragraph("<b>HOLD / RECTIFY (Fatal Transit Defect)</b>", table_cell)',
    'Paragraph("<b>HOLD (NOT WORTHY / Fatal Transit Defect)</b>", table_cell)'
)

with open("scripts/generate_capstone_problem_statement.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generate_capstone_problem_statement.py!")