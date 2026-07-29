# Metronome Campaign 02 Selection Review

Status: `complete`

The user approved this manifest and worker launch on 2026-07-28. All five jobs passed deterministic worker-result validation and serial Sol review on attempt 1, then were promoted to canonical wiki sources.

Post-campaign query-quality audit: [quality-audit.md](quality-audit.md) — 15/15 questions passed after one hard routing repair and one soft completeness repair.

## Proposed jobs

| Order | Job | Page shape | Lines | Selection reason |
| ---: | --- | --- | ---: | --- |
| 1 | `high-volume-ingestion` | Short event guide | 85 | Extends the existing event-ingestion knowledge with a bounded, operational page. |
| 2 | `stripe-marketplace-app` | Stripe setup guide | 154 | Directly documents the Stripe-owned Metronome workflow for managing contracts in Stripe. |
| 3 | `enterprise-commit` | Pricing-model guide | 267 | Covers a core advanced usage-billing model and provides evidence for the planned credits-and-commits concept. |
| 4 | `stripe-invoice-integration` | Long integration guide | 331 | Grounds the operational boundary between Metronome billing and Stripe invoicing. |
| 5 | `create-commit` | Schema-heavy API reference | 605 | Tests structured API extraction while adding the create-side contract for commits. |

## Deterministic checks required before initialization

- Every raw path is one selected English canonical documentation page in `inventory-current.json`.
- Every raw SHA-256 matches the immutable local file.
- Every canonical URL matches the collection inventory.
- No selected raw file is already referenced by a canonical Metronome source page.
- Every source target is unique and does not exist.
- Campaign size is five, worker concurrency is five, and review concurrency remains one.

## Execution result

Workers produced source candidates and shared-file suggestions only. Sol read each complete raw page, audited concepts, repaired and promoted canonical pages serially, and reconciled shared indexes and logs. No worker wrote canonical wiki files; no job failed, retried, or was rejected.
