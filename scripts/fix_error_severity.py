with open("src/service/error-analysis-engine.ts", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("strength: 'Moderate'", "strength: 'Material'")
c = c.replace("strength: 'Substantial'", "strength: 'Serious'")

with open("src/service/error-analysis-engine.ts", "w", encoding="utf-8") as f:
    f.write(c)

print("Fixed ErrorSeverity in error-analysis-engine.ts!")