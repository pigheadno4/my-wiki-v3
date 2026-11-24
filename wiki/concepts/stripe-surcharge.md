---
title: "Stripe Surcharge"
type: concept
category: technology
tags: [stripe, surcharge, compliance, payment-intent, multicapture, preview, us, canada, australia, new-zealand]
---

## Overview

Stripe surcharging (public preview) lets merchants offset card processing costs. The November 7, 2026 table lists US/Canada/New Zealand; the May 11, 2026 table also listed Australia. The omission does not establish current Australian permission or prohibition. Merchant is **fully responsible** for compliance with laws, regulations, and card network rules.

## Availability

| Country | Payment methods | Max surcharge |
| --- | --- | --- |
| US | Credit cards only | 3% |
| CA | Credit cards only | 2.4% |
| AU (May 11, 2026 table only; omitted November 7) | All cards | 4% |
| NZ | All cards | 4% |

Requires API version `2026-03-25.preview`.

## Critical Rule

**Stripe does NOT auto-increment `amount`** — you must set `amount` inclusive of surcharge, then track it in `amount_details[surcharge][amount]`.

## `enforce_validation`

| Value | Effect |
| --- | --- |
| `enabled` | Technical max enforced; `maximum_amount` returned |
| `disabled` | No Stripe technical maximum validation or `maximum_amount`; card-funding, regional, legal, and card-network restrictions still apply |
| `automatic` | Default (same as enabled) |

Cannot change after setting.

## Compliance Obligations

- Disclose surcharge amount before purchase; show separately on receipt
- Notify the acquirer or card network of intent to surcharge if required by the jurisdiction or card network; the page frames its listed duties as obligations that might apply.
- Surcharge consistently across networks
- Allow customer to cancel or choose different PM after disclosure
- Merchant bears full responsibility for fines/penalties

## Refund Rules

- **Full refund**: implement return of the entire surcharge where required by card-network rules or applicable law.
- **Partial refund**: implement a prorated surcharge return where required (refunded order share × surcharge).

## Feature Compatibility

- ✓ Payment Line Items. The [[source-stripe-payment-line-items-flexible|flexible payment scenarios guide]] covers surcharge and line-item tax field placement.
- ✓ Multicapture (per-capture surcharge; sum ≤ confirmed surcharge)
- ✓ Incremental Authorization (can only decrease surcharge at capture)
- ✗ Autocapture with partial authorizations

## Sources

- [[source-stripe-surcharge]] — availability table, enforce_validation, API examples, refund rules, compatibility, migration from private preview
