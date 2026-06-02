---
title: "Stripe Subscriptions — Backdate Subscriptions"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-backdate-2026.md"
tags: [stripe, billing, subscriptions, backdating, backdate-start-date, migration, proration, coupons]
---

## Summary

Guide to backdating subscriptions — billing customers for time that has already elapsed. Common for Stripe migration and record-keeping. Key: billing mode determines how line items are calculated; coupon duration counts from backdate, not API call.

## Key parameter

`backdate_start_date` — Unix timestamp of the backdated start date. Creates invoice for elapsed time.

**Limit**: not supported if invoice would have >250 line items (default limit).

## Billing mode distinction (API 2025-04-30+)

| Mode | Line item behavior |
|---|---|
| `classic` | Single prorated line item (based on "imagined interval" from backdate) |
| `flexible` | Separate line item per natural billing period (mirrors regular billing) |

### Classic proration math

Imagined interval starts from `backdate_start_date`. Month length of that imagined interval determines proration:
- Feb 15 → imagined Feb 15 – Mar 15 (28-day month) → 14/28 = 50% for Feb 15–Mar 1
- Jan 15 → imagined Jan 15 – Feb 15 (31-day month) → 17/31 ≈ 54.8% for Jan 15–Feb 1

## Three usage patterns

### 1. Charge for elapsed time

```js
stripe.subscriptions.create({
  customer: customerId,
  backdate_start_date: pastTimestamp,
  items: [{ price: priceId }]
})
```

### 2. Backdate without charging (migration)

```js
stripe.subscriptions.create({
  customer: customerId,
  backdate_start_date: pastTimestamp,
  proration_behavior: 'none',  // sets start_date but no charge
  items: [{ price: priceId }]
})
```

### 3. Charge + set custom next billing date

```js
stripe.subscriptions.create({
  customer: customerId,
  backdate_start_date: pastTimestamp,   // e.g. Sep 1
  billing_cycle_anchor: futureTimestamp, // e.g. Nov 1
  items: [{ price: priceId }]
})
// → Immediate invoice for Sep 1 – Nov 1; next invoice on Nov 1
```

## Coupon + backdating (critical gotcha)

Coupon duration counts from `backdate_start_date`, NOT from the API call date:

| Coupon duration | Behavior |
|---|---|
| `once` | Applies only to first invoice (backdated period) |
| `repeating` (N months) | Duration consumed from backdate. If N ≤ backdated period, expires before future invoices |
| `forever` | Applies to all invoices including future |

**Rule**: coupon duration must be > backdated period length for it to apply to current/future invoices.

## Backdating an update (`proration_date`)

Normally `proration_date` must be within current period. Exception: during **first period of a backdated subscription**, `proration_date` can go back to `subscription.start_date` (the backdated date).

## Related pages

- [[stripe-subscriptions]] — concept page (updated)
- [[stripe-subscriptions-prorations]] — proration behavior
- [[stripe-subscriptions-coupons]] — coupon behavior
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-backdate-2026]] — verbatim Stripe docs webpage
