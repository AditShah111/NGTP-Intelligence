# 13-Step Legal Evaluation Pipeline Specification

The engine strictly implements the 13-step Indian Tax Litigation framework:
1. **Case Fact Matrix**: Traceability, OCR confidence, Fact Strength.
2. **Statutory Parameter Engine**: Section 16(2)(c), 16(2)(aa), 16(4), 17(5), 73/74, 155 tests.
3. **Precedent Parameter Engine**: Ratio, Necessary Conditions, Distinguishing factors.
4. **Precedent Comparability Scoring (0-100)**: Statutory (20), Factual (25), Evidentiary (20), Procedural (10), Forum (15), Distinguishability (10).
5. **Lower Authority Error Analysis**: Jurisdiction, Natural Justice, Perverse Findings, Evidence Misread.
6. **Submission Improvement Engine**: Fact -> Evidence -> Statute -> Precedent -> Counterargument -> Rebuttal.
7. **Adversarial Red-Team Stress Test**: Revenue attack simulation, Burden of proof challenges.
8. **Evidence Gap Analysis**: Critical, High, Medium, Low missing evidence prioritization.
9. **Litigation Readiness Score (0-100)**: Weighted A-G readiness calculation.
10. **Litigation Viability Score (0-100)**: Substantive merits, judicial trend, probability of outcome.
11. **Base Score -> Forward Decision**: Enhancers, Reducers, Remediation targets.
12. **Draft Audit**: Checklist of defects, limitation, prayer validity.
13. **Final Evaluator Output**: 11 Structured sections with executive recommendation.
