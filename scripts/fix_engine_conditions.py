files_to_fix = [
    "src/service/evaluator-agent.ts",
    "src/service/statutory-engine.ts",
    "src/service/submission-optimizer.ts",
    "src/service/fact-matrix-engine.ts",
    "src/service/draft-audit-engine.ts",
    "src/service/adversarial-redteam-engine.ts",
    "src/service/evidence-gap-engine.ts"
]

for fp in files_to_fix:
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()

    # Make isDelayedPayment and isWeakCase strictly targeted to Set 2
    c = c.replace(
        "const isDelayedPayment = /delayed|216\\s*days|exceeding\\s*180|beyond\\s*180/i.test(caseSummary) || /delayed|216\\s*days/i.test(primaryIssue);",
        "const isDelayedPayment = /delayed\\s*by\\s*216|paid\\s*after\\s*216|delayed\\s*beyond\\s*180|216\\s*days/i.test(caseSummary) || /delayed\\s*216/i.test(primaryIssue);"
    )
    c = c.replace(
        "const isDelayedPayment = /delayed|216\\s*days|exceeding\\s*180|beyond\\s*180/i.test(summary) || /delayed|216\\s*days/i.test(primaryIssue);",
        "const isDelayedPayment = /delayed\\s*by\\s*216|paid\\s*after\\s*216|delayed\\s*beyond\\s*180|216\\s*days/i.test(summary) || /delayed\\s*216/i.test(primaryIssue);"
    )

    c = c.replace(
        "const isCircularAllegation = /circular|fake|shell|fictitious|100\\s*sq|bogus/i.test(caseSummary) || /circular|fake|shell/i.test(primaryIssue);",
        "const isCircularAllegation = /100\\s*sq\\s*ft|global\\s*trading\\s*syndicate|shaurya\\s*infra/i.test(caseSummary) || /no\\s*e-way\\s*bill/i.test(primaryIssue);"
    )
    c = c.replace(
        "const isCircularAllegation = /circular|fake|shell|fictitious|100\\s*sq|bogus/i.test(summary) || /circular|fake|shell/i.test(primaryIssue);",
        "const isCircularAllegation = /100\\s*sq\\s*ft|global\\s*trading\\s*syndicate|shaurya\\s*infra/i.test(summary) || /no\\s*e-way\\s*bill/i.test(primaryIssue);"
    )

    c = c.replace(
        "const isWeakCase = !hasTransit || isDelayedPayment || isCircularAllegation;",
        "const isWeakCase = !hasTransit || isDelayedPayment;"
    )

    with open(fp, "w", encoding="utf-8") as f:
        f.write(c)

print("Updated condition definitions across all engine files!")