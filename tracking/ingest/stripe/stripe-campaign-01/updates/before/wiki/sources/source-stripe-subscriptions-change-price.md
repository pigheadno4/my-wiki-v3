---
title: "Stripe Subscriptions — Change the Price of Existing Subscriptions"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-change-price-2026.md"
tags: [stripe, billing, subscriptions, upgrade, downgrade, price-change, prorations]
---

## Summary

Detailed guide for changing a subscription's price (upgrade/downgrade). Key contributions: the item-ID pitfall, quantity reset behavior, billing period rules per interval match, and zero-amount edge cases.

## Two update methods

### 1. Update the subscription

```js
stripe.subscriptions.update(subId, {
  items: [{ id: subItemId, price: newPriceId }]
})
```

**Critical**: must include the subscription item `id`. Without it, Stripe **adds** the new price as an additional item — both prices become active simultaneously.

Alternative: delete old item + create new item in the same call (set `deleted: true` on old item).

### 2. Update the subscription item directly

```js
stripe.subscriptionItems.update(subItemId, { price: newPriceId })
```

Use when no other subscription-level changes are needed.

## Quantity resets to 1

Changing price automatically resets `quantity` to `1`. Must explicitly pass the existing quantity to preserve it.

## Billing period behavior on price change

| Scenario | Billing date behavior |
|---|---|
| Same `interval` + `interval_count` | Unchanged |
| Different intervals (e.g. monthly → yearly) | Resets to date of change |
| Same interval but adding a trial | Resets to trial conclusion |

Use a **subscription schedule** when changing price at end of billing period to prevent unexpected overwrites.

## Proration

Price changes trigger prorations by default. Options:
- Preview with `stripe.invoices.retrieveUpcoming`
- `proration_behavior=always_invoice` — charge immediately; combine with pending updates so change only applies if invoice pays
- **Billing cycle anchor reset** triggers immediate payment; if payment fails, subscription goes `past_due` (change still applies)

Credit prorations behavior depends on `billing_mode` (classic vs flexible).

## Usage-based edge cases

- **Billing Meter**: `clear_usage` has no effect on Billing Meter prices
- **Legacy usage records**: usage transfers to the new price on update

## Zero-amount edge cases

| Change | Generates invoice? | Resets billing period? |
|---|---|---|
| Zero-amount price → non-zero price | Yes | Yes |
| Non-zero price + zero quantity → non-zero quantity | No | No |

## Related pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-modify]] — billing-related vs non-billing updates overview
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-change-price-2026]] — verbatim Stripe docs webpage
