with open("src/service/fact-matrix-engine.ts", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("evidenceStrength: 'Partially Corroborated'", "evidenceStrength: 'Disputed'")
c = c.replace("evidenceStrength: 'Established (Adverse to Taxpayer)'", "evidenceStrength: 'Contradicted'")

with open("src/service/fact-matrix-engine.ts", "w", encoding="utf-8") as f:
    f.write(c)

print("Fixed EvidenceStrength in fact-matrix-engine.ts!")