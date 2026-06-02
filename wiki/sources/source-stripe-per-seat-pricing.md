---
title: "Stripe — Set Up Per-Seat Pricing"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-per-seat-pricing-2026.md"
tags: [stripe, subscriptions, per-seat, pricing, quantity]
---

## Summary

Per-seat pricing implementation: same flat rate API pattern but pass `quantity` (number of seats/users) when creating the subscription. Each unit = one user/license.

## Key API Difference from Flat Rate

```js
stripe.subscriptions.create({
  customer: id,
  items: [{ price: per_seat_price_id, quantity: 12 }]  // ← quantity = number of seats
})
```

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-flat-rate-pricing]] — flat rate (same API, no quantity)

## Raw Sources

- [[stripe-per-seat-pricing-2026]] — verbatim per-seat pricing guide (87 lines, 1 image)
