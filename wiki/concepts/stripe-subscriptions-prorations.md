---
title: "Stripe Subscription Prorations"
type: concept
category: framework
tags: [stripe, billing, subscriptions, prorations, credit-prorations, billing-mode]
---

## Overview

Stripe can create proration invoice items when a subscription changes, with credits or debits depending on the operation. The November guide classifies items by the generating operation, using Invoice item `proration` or Invoice line item `parent.subscription_item_details.proration`; partial duration alone does not decide classification. A single operation can create proration and non-proration items. The familiar unused-time credit plus remaining-time debit is one price-change example, not every proration.

> [!warning] Contradiction
> This page's former definition treated every mid-period change as a paired credit and debit. The November classification includes credit-only, debit-only and mixed-item operations; see [[source-stripe-subscriptions-prorations]] for the dated same-URL evidence.

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
| `create_prorations` (default) | Creates applicable proration items; immediate invoicing occurs only under certain conditions, without a guaranteed period-end outcome from this setting alone |
| `always_invoice` | Calculates prorations and immediately generates an invoice; payment success is not established |
| `none` | Disables prorations on that request, but regular renewal or full-period non-proration items can still be created; the guide says the full new price is billed when the next invoice is generated |

For cancellation, the November guide permits disabling proration only when `cancel_at` falls within the current billing period. `none` must be passed on each relevant request to suppress future prorations.

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
| Classic | Current (new, unbilled) price | May credit based on a price that was not billed |
| Flexible | Last **billed** price | Example credits based on the prior billed price; payment is not established |

For `amount_off` coupons across multiple items:

| Mode | Logic |
|---|---|
| Classic | Distributes coupon evenly across items |
| Flexible | Uses proportional actual `discount_amounts` from original invoice |

The flexible example uses proportional `discount_amounts` from the original invoice and shows a different credit total. These sample totals do not establish actual customer payment or a refund. See [[source-stripe-subscriptions-prorations]].

## Manual prorations

To calculate an adjustment outside Stripe, pass `add_invoice_items` with a negative `unit_amount` to CreateSubscription, UpdateSubscription, CreateSubscriptionSchedule, or UpdateSubscriptionSchedule. A manually created negative invoice item is not automatically classified as a Stripe proration; see [[source-stripe-subscriptions-prorations]].

## Sources

- [[source-stripe-subscriptions-prorations]] — May and November 2026 Stripe guide captures: item classification, behavior controls, credit attribution, classic/flexible examples, preview and unpaid-invoice handling
