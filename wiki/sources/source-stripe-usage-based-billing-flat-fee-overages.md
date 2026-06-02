---
title: "Stripe: Set Up a Flat Fee and Overages Pricing Model"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-flat-fee-overages-2025.md"
tags: [stripe, billing, usage-based, meters, subscriptions, pricing, flat-fee, tiered]
---

## Summary

End-to-end guide for implementing flat fee + overages pricing using two separate products/prices on one subscription. Uses Hypernian (LLM company: $100/user/month license + $0.04/token above 1,000 free tokens) as the example.

## Key Details

### Two-product approach

**Product 1 — metered usage (overages):**
- `billing_scheme: 'tiered'`, `tiers_mode: 'graduated'`, `usage_type: 'metered'`
- Tiers: `[{ up_to: 1000, unit_amount_decimal: '0', flat_amount_decimal: '0' }, { up_to: 'inf', unit_amount_decimal: '4', flat_amount_decimal: '0' }]`
- `Decimal.from()` used for all monetary values in tiers
- References meter via `recurring.meter`

**Product 2 — license fee (flat):**
- `billing_scheme: 'per_unit'`, `usage_type: 'licensed'`
- `unit_amount_decimal: Decimal.from('10000')` (= $100)
- No meter — standard recurring flat price

**Subscription:** `items: [{ price: LICENSE_PRICE_ID }, { price: USAGE_PRICE_ID }]`

### Invoice timing

Second invoice combines: previous month's usage overages + upcoming month's license fee. First invoice charges only the license fee (no prior usage to bill under `billing_mode=flexible`).

### Alternative single-product approach

Set `flat_amount` on the first graduated tier row to $100 to bill the base fee at end-of-month alongside usage — avoids a second product but changes timing (end-of-month vs beginning-of-month for the flat fee).

## Raw Sources

- [[stripe-usage-based-billing-flat-fee-overages-2025]] — verbatim webpage content (351 lines, end-to-end guide with Dashboard + API for every step)
