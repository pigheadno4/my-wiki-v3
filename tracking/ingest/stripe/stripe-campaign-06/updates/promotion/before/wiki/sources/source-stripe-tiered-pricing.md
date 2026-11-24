---
title: "Stripe — Set Up Tiered Pricing"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-tiered-pricing-2026.md"
tags: [stripe, subscriptions, tiered, volume, graduated, pricing, tiers]
---

## Summary

Tiered pricing implementation guide. Two modes: volume (entire qty × one tier rate; can decrease at higher qty) and graduated (sum across tiers; always increases). Both use `billing_scheme: 'tiered'` + `tiers_mode`.

## Volume vs Graduated Math (key difference)

| qty=6, 3 tiers ($7/5, $6.50/10, $6/∞) | Volume | Graduated |
| --- | --- | --- |
| Formula | 6 × $6.50 | 5×$7 + 1×$6.50 |
| Total | $39 | $41.50 |

## API Pattern

```js
stripe.prices.create({
  billing_scheme: 'tiered',
  tiers_mode: 'volume' | 'graduated',
  tiers: [
    { unit_amount: 700, up_to: 5 },
    { unit_amount: 650, up_to: 10 },
    { unit_amount: 600, up_to: 'inf' }
  ],
  recurring: { interval: 'month', usage_type: 'metered' },
  expand: ['tiers']
})
```

## Flat Amount per Tier

Each tier can have `flat_amount` (fixed fee) alongside `unit_amount`. Works for both volume and graduated.

## `quantity=0` Edge Case

Stripe always bills the first-tier flat rate when `quantity=0`. To bill $0 with no usage: set `up_to=1` tier with `unit_amount = flat_rate` and omit `flat_amount`.

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-usage-based-pricing]] — usage-based pricing (combines tiered + flat rates)

## Raw Sources

- [[stripe-tiered-pricing-2026]] — verbatim tiered pricing guide (186 lines)
