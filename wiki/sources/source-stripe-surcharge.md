---
title: "Stripe — Collect Surcharges"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-surcharge-2026.md"
tags: [stripe, surcharge, payment-intent, compliance, refunds, multicapture, preview]
---

## Summary

Surcharging API (public preview) lets merchants offset card processing costs. US/CA/AU/NZ only; compliance is merchant's responsibility.

## Availability

| Country | Payment methods | Max surcharge |
| --- | --- | --- |
| US | Credit cards only | 3% |
| CA | Credit cards only | 2.4% |
| AU | All cards | 4% |
| NZ | All cards | 4% |

Requires API version `2026-03-25.preview`.

## Key API Rule

**Total `amount` must include surcharge** — Stripe does NOT auto-increment. Surcharge tracked separately in `amount_details[surcharge][amount]`.

Example: $10.00 subtotal + $0.20 surcharge → `amount: 1020`, `amount_details.surcharge.amount: 20`.

## `enforce_validation` Values

| Value | Behavior | Returns `maximum_amount`? |
| --- | --- | --- |
| `enabled` | Technical limit enforced | Yes |
| `disabled` | No technical limit | No |
| `automatic` (default) | Same as enabled | Yes |

**Cannot change after setting.**

## Surcharge Fields on PaymentIntent

- `surcharge.status`: `available` or `unavailable`
- `surcharge.maximum_amount`: technical max (not a compliance limit)
- `surcharge.enforce_validation`: current setting
- `surcharge.amount`: applied surcharge

## Compliance Requirements

- Disclose amount before purchase; show separately on receipt
- Notify acquirer/network of intent to surcharge
- Surcharge consistently across networks
- Allow cancellation or different PM choice after disclosure
- **Merchant bears full responsibility for fines/penalties**

## Refund Rules

- Full refund → full surcharge returned
- Partial refund → prorated surcharge (e.g. 60% of order → refund 60% of surcharge)

## Compatibility

- ✓ Payment Line Items
- ✓ Multicapture (per-capture surcharge; sum can't exceed confirmed surcharge)
- ✓ Incremental Authorization (can only decrease surcharge at capture)
- ✗ Autocapture with partial authorizations

## Reporting

`amount_details_surcharge_amount` in Sigma `payment_intents` table.

## Related Pages

- [[stripe-surcharge]] — concept page
- [[stripe-refunds]] — refund proration rules
- [[stripe-payment-intents]] — PaymentIntent lifecycle

## Raw Sources

- [[stripe-surcharge-2026]] — verbatim surcharge guide (272 lines)
