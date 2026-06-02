---
title: "Stripe — Set Up Flat Rate Pricing"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-flat-rate-pricing-2026.md"
tags: [stripe, subscriptions, flat-rate, pricing, products, prices]
---

## Summary

Implementation guide for flat rate subscription pricing: create Product → create Price(s) with monthly/yearly intervals → create Subscription. One product can have multiple prices (monthly + yearly) sharing the same product description.

## Key API Pattern

```js
// 1. Create product
stripe.products.create({ name: 'Basic' })

// 2. Create monthly price
stripe.prices.create({ product: id, unit_amount: 1000, currency: 'usd', recurring: { interval: 'month' } })

// 3. Create yearly price
stripe.prices.create({ product: id, unit_amount: 10000, currency: 'usd', recurring: { interval: 'year' } })

// 4. Create subscription
stripe.subscriptions.create({ customer: id, items: [{ price: priceId }] })
```

**Note**: Products can't be edited after a subscription is created with them.

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-recurring-pricing-models]] — pricing models overview

## Raw Sources

- [[stripe-flat-rate-pricing-2026]] — verbatim flat rate pricing guide (106 lines, 1 image)
