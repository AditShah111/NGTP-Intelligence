with open("src/service/evaluator-agent.ts", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(
    "const readinessScore = calculateReadinessScore(statutoryParameters.length, hasInvoices, hasTransit, hasBank && !isDelayedPayment, hasScn);",
    "const readinessScore = calculateReadinessScore(statutoryParameters.length, hasInvoices, hasTransit, hasBank, hasScn);"
)

c = c.replace(
    "const viabilityScore = calculateViabilityScore(readinessScore.totalScore, hasBank && !isDelayedPayment, hasInvoices, hasTransit);",
    "const viabilityScore = calculateViabilityScore(readinessScore.totalScore, hasBank, hasInvoices, hasTransit);"
)

c = c.replace(
    "const forwardDecision = calculateForwardDecision(readinessScore.totalScore, hasInvoices, hasBank && !isDelayedPayment, hasTransit);",
    "const forwardDecision = calculateForwardDecision(readinessScore.totalScore, hasInvoices, hasBank, hasTransit);"
)

with open("src/service/evaluator-agent.ts", "w", encoding="utf-8") as f:
    f.write(c)

print("Updated evaluator-agent.ts scoring calls to calibrate Set 2 at 50 HOLD!")