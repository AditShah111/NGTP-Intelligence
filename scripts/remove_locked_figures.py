with open("scripts/generate_landscape_deck.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Card 1
content = content.replace(
    'Paragraph("THE LITIGATION CRISIS", m_label),',
    'Paragraph("STATUTORY CONFLICT", m_label),'
)

content = content.replace(
    'Paragraph("Rs. 75,000+ Crores", m_val_amber),',
    'Paragraph("Section 16(2)(c)", m_val_amber),'
)

content = content.replace(
    'Paragraph("Locked in disputed tax demands against compliant buyers whose suppliers defaulted in cash or were retrospectively cancelled.", m_desc),',
    'Paragraph("Widespread disallowance of ITC against compliant buyers whose suppliers defaulted in cash or faced retrospective cancellation.", m_desc),'
)

# Replace script mention of 75,000
content = content.replace(
    '"\\\"<b>Respected Examiners:</b> This platform solves the Rs. 75,000 Crore Section 16(2)(c) crisis for Indian Chartered Accountants.<br/>"',
    '"\\\"<b>Respected Examiners:</b> This platform resolves the pervasive Section 16(2)(c) and retrospective NGTP dispute crisis for Indian Chartered Accountants.<br/>"'
)

with open("scripts/generate_landscape_deck.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generate_landscape_deck.py without locked-in figures!")