---
title: "Stripe Surcharge"
type: concept
category: technology
tags: [stripe, surcharge, compliance, payment-intent, multicapture, preview, us, canada, australia, new-zealand]
---

## Overview

Stripe surcharging (public preview) lets merchants offset card processing costs. Available in US/CA/AU/NZ. Merchant is **fully responsible** for compliance with laws, regulations, and card network rules.

## Availability

| Country | Payment methods | Max surcharge |
| --- | --- | --- |
| US | Credit cards only | 3% |
| CA | Credit cards only | 2.4% |
| AU | All cards | 4% |
| NZ | All cards | 4% |

Requires API version `2026-03-25.preview`.

## Critical Rule

**Stripe does NOT auto-increment `amount`** — you must set `amount` inclusive of surcharge, then track it in `amount_details[surcharge][amount]`.

## `enforce_validation`

| Value | Effect |
| --- | --- |
| `enabled` | Technical max enforced; `maximum_amount` returned |
| `disabled` | No technical max; no `maximum_amount` |
| `automatic` | Default (same as enabled) |

Cannot change after setting.

## Compliance Obligations

- Disclose surcharge amount before purchase; show separately on receipt
- Notify acquirer/card network of intent to surcharge
- Surcharge consistently across networks
- Allow customer to cancel or choose different PM after disclosure
- Merchant bears full responsibility for fines/penalties

## Refund Rules

- **Full refund**: return entire surcharge
- **Partial refund**: return prorated surcharge (refund % × surcharge)

## Feature Compatibility

- ✓ Payment Line Items
- ✓ Multicapture (per-capture surcharge; sum ≤ confirmed surcharge)
- ✓ Incremental Authorization (can only decrease surcharge at capture)
- ✗ Autocapture with partial authorizations

## Sources

- [[source-stripe-surcharge]] — availability table, enforce_validation, API examples, refund rules, compatibility, migration from private preview
