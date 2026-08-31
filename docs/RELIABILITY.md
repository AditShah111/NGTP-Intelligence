# RELIABILITY.md

## Reliability Invariants

- All incoming documents and JSON payloads are validated with Zod before processing.
- Database connection to Supabase uses SSL with auto-reconnect and schema health checks.
- If database is unreachable or offline, the engine falls back to deterministic local state caching with zero crash.
- Every score calculation is fully deterministic and mathematical, broken down by explicit weighted sub-components.
