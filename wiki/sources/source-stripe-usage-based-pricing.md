---
title: "Stripe — Set Up Usage-Based Pricing Models"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-usage-based-pricing-2026.md"
tags: [stripe, subscriptions, usage-based, metered, billing-credits, credit-burndown, graduated, tiered]
---

## Summary

Implementation guide for the three usage-based pricing models: fixed fee + overage, pay as you go, and credit burndown. Covers API patterns for licensed vs metered prices, graduated tiers, and billing credit grants.

## Fixed Fee + Overage API Pattern

Two prices on one product — both required in subscription `items[]`:

```js
// Price 1: flat licensed rate
stripe.prices.create({ product, currency: 'usd', unit_amount: 20000,
  billing_scheme: 'per_unit', recurring: { usage_type: 'licensed', interval: 'month' } })

// Price 2: metered graduated tiers (with meter ID)
stripe.prices.create({ product, currency: 'usd', billing_scheme: 'tiered',
  recurring: { usage_type: 'metered', interval: 'month', meter: METER_ID },
  tiers_mode: 'graduated', tiers: [{ up_to: 100000, unit_amount_decimal: '0' }, { up_to: 'inf', unit_amount_decimal: '0.1' }] })

// Subscription with both prices
stripe.subscriptions.create({ customer, items: [
  { price: FLAT_PRICE_ID, quantity: 1 },
  { price: METERED_PRICE_ID }   // no quantity for metered
]})
```

## Pay As You Go

In-arrears billing. Strategies: per unit, per package, volume-based, graduated. No implementation code in this guide — see usage-based billing implementation guide.

## Credit Burndown API

1. Create invoice + add line item (prepayment amount)
2. Finalize invoice (`auto_advance: true`)
3. After payment: `stripe.billing.creditGrants.create({ customer, category: 'paid', amount: { type: 'monetary', monetary: { value, currency } }, applicability_config: { scope: { price_type: 'metered' } }, expires_at })`

## Related Pages

- [[stripe-subscriptions]] — concept page (updated with usage-based API patterns)
- [[stripe-usage-based-billing]] — usage-based billing concept page

## Raw Sources

- [[stripe-usage-based-pricing-2026]] — verbatim usage-based pricing guide (250 lines)
