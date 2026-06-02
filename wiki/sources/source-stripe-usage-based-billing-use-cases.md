---
title: "Stripe: Usage-Based Billing Use Cases"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-use-cases-2025.md"
tags: [stripe, billing, usage-based, meters, pricing]
---

## Summary

Index page listing the three supported usage-based pricing models, each with its own implementation guide.

## Key Details

| Model | Description | API path |
| --- | --- | --- |
| Pay as you go | Pure consumption billing | `usage-based/implementation-guide` (v2 Meter API) |
| Flat fee and overages | Flat base rate + arrears usage charges | `usage-based-v1/use-cases/flat-fee-and-overages` (legacy v1) |
| Credit-based | Pre-purchase credits | `usage-based/use-cases/credits-based-pricing-model` (v2) |

**Note**: Flat fee and overages links to the `usage-based-v1` path — likely only available via the legacy metered billing API, not the new Meter API.

## Raw Sources

- [[stripe-usage-based-billing-use-cases-2025]] — verbatim webpage content (14 lines, 3-model index table)
