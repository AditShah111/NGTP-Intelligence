# ARCHITECTURE.md

## Layer Invariants

The application strictly adheres to forward dependency flow:

```
Types -> Config -> Repo -> Service -> Runtime -> UI
```

Cross-cutting concerns (Database connection, LLM inference provider, Document parser, PDF export) are injected through **Providers**.

### 1. Types Layer (`src/types/`)
- Domain models and Zod schemas.
- Cannot import from any other layer.

### 2. Config Layer (`src/config/`)
- Runtime environment variables, database strings, ports.
- Depends only on Types.

### 3. Repo Layer (`src/repo/`)
- Data access to Supabase PostgreSQL in the `ngtp` schema.
- Enforces strict table isolation: never touches or queries any tables outside the `ngtp` schema.
- Includes pre-seeded landmark benchmark GST cases.

### 4. Service Layer (`src/service/`)
- Pure business logic and legal engines:
  - Fact Matrix Engine (Step 1)
  - Statutory Parameter Engine (Step 2)
  - Precedent Engine & Comparability Scorer (Steps 3 & 4)
  - Lower Authority Error Classifier (Step 5)
  - Submission Optimizer (Step 6)
  - Adversarial Red-Team Stress Tester (Step 7)
  - Evidence Gap Analyzer (Step 8)
  - Dual Scoring Engine: Readiness vs Viability (Steps 9, 10, 11)
  - Draft Auditor (Step 12)
  - Master 13-Step Evaluator Orchestrator (Step 13)

### 5. Runtime / API Layer (`src/app/api/`)
- Next.js Edge / Node Route Handlers.
- Validates request payload using Zod.

### 6. UI Layer (`src/components/`, `src/app/`)
- High-craft, executive-grade legal analytical dashboard.
- Interactive multi-tab 13-step evaluator.
- Red-Team live war-room / simulation.
- PDF & Markdown legal dossier export.
