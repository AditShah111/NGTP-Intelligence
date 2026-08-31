# SECURITY.md

## Security & Database Isolation

- **Supabase Isolation**: All queries execute against the dedicated `ngtp` schema or `ngtp_*` tables.
- **Zero-Touch Invariant**: Under NO circumstances does any code modify, inspect, or drop existing tables (e.g. `users`, `society`, `complaints`, etc.).
- **Data Protection**: Document text uploaded by users is sanitized and stored securely with cryptographic IDs.
