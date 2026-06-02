---
title: "Stripe Docs — Querying authentication conversion"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-3ds-sigma-query-2025.md"
tags: [stripe, 3d-secure, sigma, analytics, sca, authentication-rate, deduplication]
---

## Summary

Guide for querying 3DS authentication data via Stripe Sigma. Covers the `authentication_report_attempts` table, key columns, deduplication with `is_final_attempt`, and three example SQL queries.

## Key Table: `authentication_report_attempts`

- **Location**: Analytics Tables in Stripe Sigma schema
- **Granularity**: one row per attempt (PI/SI can have multiple attempts)
- **`is_final_attempt`**: key deduplication column — eventually consistent after a few days

## Key Columns

| Column | Purpose |
| --- | --- |
| `threeds_outcome_result` | Auth result: `authenticated`, `attempt_acknowledged`, `delegated`, `exempted`, `failed` |
| `authentication_flow` | `challenge` or `frictionless` |
| `sca_exemption_requested` | e.g., `low_risk` |
| `sca_exemption_mechanism` | `authorization` = direct to authorization |
| `sca_exemption_status` | `non_sca_decline` = declined for non-SCA reason |
| `charge_outcome` / `charge_outcome_reason` | Payment outcome |
| `is_final_attempt` | Filter to deduped representative transaction |
| `is_threeds_triggered` | Whether 3DS was triggered |

## Auth Success Definition

`threeds_outcome_result` IN `('attempt_acknowledged', 'authenticated', 'delegated', 'exempted')`

## Deduplication Impact

Dedup groups: same `customer_id` + `currency` + `amount` appearing close in time. Example: raw auth rate 59% → deduped rate 80%.

## Three Example Queries

1. Challenge-flow authenticated payments (payment intents)
2. Low-risk SCA exemption direct authorization declined for non-SCA reason
3. Raw vs deduped authentication rate comparison for setup intents

## Related Pages

- [[stripe-3d-secure]] — 3D Secure concept page (Sigma Analytics section)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-3ds-sigma-query-2025]] — verbatim webpage content (109 lines)
