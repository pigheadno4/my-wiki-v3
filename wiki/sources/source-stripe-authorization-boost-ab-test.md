---
title: "Stripe Docs — Set up an A/B test for Authorization Boost"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-authorization-boost-ab-test-2025.md"
tags: [stripe, authorization-boost, a-b-testing, adaptive-acceptance, network-tokens, card-account-updater, payment-optimization]
---

## Summary

Guide for running a 30-day A/B test before purchasing Authorization Boost. Free to run (only billed for features already enabled).

## Test Design

- **50/50 split**: Control = current config + CAU; Treatment = current config + all Authorization Boost features not yet enabled
- **CAU exception**: CAU runs on both groups (100% coverage) — card credential updates cannot be applied selectively
- **Adaptive Acceptance / Network tokens**: only in Treatment group if not already enabled (50% coverage)

## Key Rules

| Rule | Detail |
| --- | --- |
| Duration | 30 days |
| Cancel | Admin/Developer roles; Dashboard only |
| After cancel | Reverts to prior config; **12-month cooldown** before re-testing |
| Results available | **37 days** after start (30 test + 7 days for retries) |
| Significance threshold | p < 5% |

## Impact Calculation

- **Adaptive Acceptance + Network tokens**: (treatment rate − control rate) × total attempted volume
- **CAU**: probabilistic recovery estimate (same methodology as optimization page)
- **Without CAU in current config**: total impact = A/B impact + CAU recovery estimate

**Example (without CAU)**: $100K × 2.5% success rate diff = $2,500 + $1K CAU recovery = $3,500

## After the Test

Authorization Boost is a **paid add-on** — purchase via "Enable Authorization Boost" on results page. Pre-existing enabled optimizations remain active post-test. Custom pricing available via Stripe account team.

## Related Pages

- [[stripe-authorization-boost]] — Authorization Boost concept page
- [[source-stripe-payments-optimization]] — Authorization Boost features overview
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-authorization-boost-ab-test-2025]] — verbatim webpage content (98 lines; "Request early access" section is a stub)
