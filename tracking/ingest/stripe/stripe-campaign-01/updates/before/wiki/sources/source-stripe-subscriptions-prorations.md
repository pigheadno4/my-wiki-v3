---
title: "Stripe Subscriptions — Prorations"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-prorations-2026.md"
tags: [stripe, billing, subscriptions, prorations, credit-prorations, billing-mode]
---

## Summary

Comprehensive guide to how Stripe calculates and manages prorations when subscriptions change mid-period. Key contributions: the exhaustive trigger/non-trigger tables, classic vs flexible credit proration difference, preview-locking pattern, and unpaid invoice handling.

## How prorations work

When a subscription changes mid-period, Stripe creates proration invoice items for the unused time at the old price (credit) and the remaining time at the new price (debit). Example: upgrading $10→$20 halfway through → net +$5.

- **Negative prorations** (credits) are NOT automatically refunded
- **Positive prorations** (debits) are NOT immediately billed by default
- Both can be done manually

## Prorations and discounts

- All proration invoice items are `discountable=false` — discounts on an invoice don't apply to proration items
- Discounts already affecting the subscription are baked into the proration amount itself
- Non-proration items show discount adjustments in `discount_amounts`

### Discount-change interaction

Discount-only changes don't trigger prorations. But when combined with a proration trigger in the same API call, the proration is calculated using the **modified discount state** (the new discount is used in the proration math).

## What triggers prorations

| Update | Description |
|---|---|
| Add/remove items | Adding a new item or removing an existing item |
| Change price | Price with different base cost or billing period |
| Change quantity | Increasing or decreasing quantity on a subscription item |
| Add `trial_end` / `trial_from_plan` | Adding a trial period to an active subscription |
| Change `billing_cycle_anchor` | Resetting the billing period to a new date |
| Set `cancel_at` | Canceling mid-period (not `cancel_at_period_end`) |

## What doesn't trigger prorations

Configuration and settings: `automatic_tax`, `default_payment_method`, `default_source`, `payment_behavior`, `collection_method`, `days_until_due`, `tax_filing_currency`, `retry_settings`, `trial_settings`, `pay_immediately`, `pending_invoice_item_interval`, `pause_collection`, `proration_date` alone.

Metadata: `metadata`, `items.metadata`, `cancellation_details`.

Future billing settings: `discounts`, `items.discounts`, `billing_thresholds`, `items.billing_thresholds`, `cancel_at_period_end`, `add_invoice_items`.

## Unpaid invoices

Stripe credits for unused time even if prior invoice is unpaid. To avoid crediting for unpaid time:
1. Set `proration_behavior=none` on the update
2. Then either: manually create a one-off invoice (preserves billing period), or set `billing_cycle_anchor=now` (resets billing period)
3. Void the old invoice to prevent double-payment if the customer eventually pays

## proration_behavior options

| Value | Behavior |
|---|---|
| `create_prorations` (default) | Creates proration items; invoiced at period end or on anchor reset |
| `always_invoice` | Creates prorations and immediately generates an invoice |
| `none` | No prorations created; customer billed full new price at next invoice |

## Preview a proration

```js
stripe.invoices.createPreview({
  customer: customerId,
  subscription: subId,
  subscription_details: { items, proration_date }
})
```

Doesn't modify the subscription. Because Stripe prorates to the second, amounts can drift — lock with `proration_date` and pass the **same value** when making the actual update.

## Credit prorations: classic vs flexible billing_mode

When downgrading after a mid-period upgrade that used `proration_behavior=none` (so upgrade was never billed):

| Mode | Credit logic | Example result |
|---|---|---|
| Classic | Credits based on **current** price, even if never billed | -$6.67 credit + $3.33 debit = -$3.34 net |
| Flexible | Credits based on **last actually-billed** price | $0 net (credit and debit cancel out) |

### Multi-item coupon credit prorations

For `amount_off` coupons spread across multiple items:

| Mode | Logic | Example |
|---|---|---|
| Classic | Distributes coupon evenly across items | -$2.50 |
| Flexible | Uses proportional actual `discount_amounts` from original invoice | -$4.17 |

Flexible is more accurate to what the customer actually paid.

## Manual prorations

To calculate prorations outside Stripe and add them manually, pass `add_invoice_items` with a negative `unit_amount` to: CreateSubscription, UpdateSubscription, CreateSubscriptionSchedule, UpdateSubscriptionSchedule.

## Related pages

- [[stripe-subscriptions-prorations]] — concept page
- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-change-price]] — price change guide (triggers prorations)
- [[source-stripe-subscriptions-modify]] — billing-related vs non-billing updates overview
- [[source-stripe-subscriptions-billing-mode-compare]] — classic vs flexible billing mode comparison
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-prorations-2026]] — verbatim Stripe docs webpage
