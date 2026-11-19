---
title: "Stripe Docs — Payments optimization"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payments-optimization-2025.md"
tags: [stripe, authorization-boost, adaptive-acceptance, card-account-updater, network-tokens, ic-plus, payment-optimization, cnp]
---

## Summary

Overview of Stripe Authorization Boost — three AI-driven features for improving CNP payment success rates and reducing network costs for IC+ customers.

## Three Authorization Boost Features

| Feature | Recovery | Cost Savings (IC+) |
| --- | --- | --- |
| Adaptive Acceptance | Retry declined payments; PINless network retries (US) | Excessive retry prevention, decline prevention, Data Only 3DS |
| Card account updater | Updated card info (PAN/expiry) | None |
| Network tokens | Higher approval with current credentials | Visa interchange discounts, Mastercard CCP fee prevention |

## Probabilistic Calculation Methodology

Stripe assigns likelihood estimates per optimization → recovered volume = payments × amount × probability. Multi-feature payments attributed to most responsible feature. Cost savings estimated using network fee rules (not reconciled with actual account fees).

**Cost savings shown**: IC+ only; only if ≥ $100 USD equivalent in last 12 months.

## CDN Assets

- `raw/assets/stripe-authorization-boost.png` — Authorization Boost overview (228 KB)
- `raw/assets/stripe-payment-success-rate.png` — Success rate chart with optimization baseline (75 KB)

## Related Pages

- [[stripe-authorization-boost]] — concept page
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payments-optimization-2025]] — verbatim webpage content (136 lines; Adaptive Acceptance table reformatted by linter)
