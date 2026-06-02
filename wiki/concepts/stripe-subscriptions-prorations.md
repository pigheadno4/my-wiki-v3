---
title: "Stripe Subscription Prorations"
type: concept
category: framework
tags: [stripe, billing, subscriptions, prorations, credit-prorations, billing-mode]
---

## Overview

When a Stripe subscription changes mid-period, Stripe creates proration invoice items to charge customers accurately for partial use. A proration consists of a credit for unused time at the old price and a debit for remaining time at the new price.

- **Negative prorations** (credits) are NOT automatically refunded
- **Positive prorations** (debits) are NOT immediately billed by default
- Both can be done manually

## What triggers prorations

| Update | Notes |
|---|---|
| Add/remove subscription items | Any item add or remove |
| Change price | Different base cost or billing period |
| Change quantity | Any quantity change on a subscription item |
| Add trial to active subscription | `trial_end` or `trial_from_plan` |
| Reset `billing_cycle_anchor` | Moves billing date to a new anchor |
| Set `cancel_at` mid-period | NOT `cancel_at_period_end` |

## What doesn't trigger prorations

- **Configuration**: `automatic_tax`, `default_payment_method`, `default_source`, `payment_behavior`, `collection_method`, `days_until_due`, `retry_settings`, `trial_settings`, `pay_immediately`, `pause_collection`, `proration_date` alone
- **Metadata**: `metadata`, `items.metadata`, `cancellation_details`
- **Future billing settings**: `discounts`, `items.discounts`, `billing_thresholds`, `cancel_at_period_end`, `add_invoice_items`

These don't generate proration invoice items even with `proration_behavior=create_prorations` or `always_invoice`.

## proration_behavior

| Value | Behavior |
|---|---|
| `create_prorations` (default) | Creates proration items; invoiced at period end or on anchor reset |
| `always_invoice` | Creates prorations and immediately generates an invoice |
| `none` | No prorations; customer billed full new price at next invoice |

## Prorations and discounts

- Proration items are always `discountable=false` — invoice discounts don't apply to them
- Discounts already on the subscription are baked into the proration amount
- **Mixed-call rule**: if a discount change and a proration trigger happen in the same API call, the proration is calculated using the **modified discount state**

## Preview

```js
stripe.invoices.createPreview({
  customer: customerId,
  subscription: subId,
  subscription_details: { items, proration_date }
})
```

Doesn't modify the subscription. Stripe prorates to the second — lock with `proration_date` and pass the **same value** when making the actual update to prevent drift.

## Unpaid invoice edge case

Stripe credits for unused time even if the prior invoice is unpaid. To avoid crediting for time not yet paid:

1. Set `proration_behavior=none` on the update
2. Either create a one-off invoice manually (keeps billing period) or set `billing_cycle_anchor=now` (resets period)
3. Void the old invoice to prevent double-payment if customer later pays

## Credit prorations: classic vs flexible billing_mode

When downgrading after a mid-period upgrade that wasn't billed (`proration_behavior=none`):

| Mode | Credits based on | Result |
|---|---|---|
| Classic | Current (new, unbilled) price | May credit more than customer paid |
| Flexible | Last **actually-billed** price | Accurate to what customer paid |

For `amount_off` coupons across multiple items:

| Mode | Logic |
|---|---|
| Classic | Distributes coupon evenly across items |
| Flexible | Uses proportional actual `discount_amounts` from original invoice |

Flexible is more accurate to actual customer payment.

## Manual prorations

To calculate prorations outside Stripe, pass `add_invoice_items` with a negative `unit_amount` to: CreateSubscription, UpdateSubscription, CreateSubscriptionSchedule, UpdateSubscriptionSchedule.

## Sources

- [[source-stripe-subscriptions-prorations]] — Stripe docs: full prorations guide (triggers, non-triggers, classic vs flexible, preview, unpaid invoice handling)
