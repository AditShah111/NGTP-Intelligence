# AGENTS.md

Welcome to the **NGTP Litigation Readiness & Viability Engine** repository.

This repository is built following **Codex and Harness Engineering** principles:
1. Strict boundary layering: `Types -> Config -> Repo -> Service -> Runtime -> UI + Providers`.
2. Multi-agent evaluation loops: `Planner -> Generator -> Evaluator (Adversarial Red-Team)`.
3. In-repository knowledge as the system of record.

## System Index & Source of Truth

- [ARCHITECTURE.md](ARCHITECTURE.md) - Layer definitions and permissible dependency directions.
- [DESIGN.md](DESIGN.md) - Design tokens, typography, executive legal theme, and craft rules.
- [QUALITY_SCORE.md](QUALITY_SCORE.md) - Domain benchmarks for Section 16(2)(c), 16C, 73/74, 155 litigation analysis.
- [RELIABILITY.md](RELIABILITY.md) - Validation invariants, fail-safes, and boundary typing with Zod.
- [SECURITY.md](SECURITY.md) - Schema isolation (`ngtp` namespace) and database credential isolation.
- [13-Step Engine Spec](product-specs/13-step-engine.md) - Deep operational definitions of the 13-step analysis.
- [Adversarial Red-Team Spec](product-specs/adversarial-redteam.md) - Opposing counsel attack vectors and resilience matrix.
