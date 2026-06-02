---
title: "Stripe — Configure Trial Offers on Subscriptions"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-trial-offers-2026.md"
tags: [stripe, subscriptions, trial-offers, flexible-billing, preview, discounted-trial, item-level-trial]
---

## Summary

Trial Offer API (public preview, `2026-03-25.preview`). A separate object that attaches a discounted/free price to a subscription item temporarily. Requires `billing_mode: flexible`. Four use cases: discounted, free, upgrade, and item-level trials.

## Prerequisites

- API version `2026-03-25.preview` in request header
- Subscription must use `billing_mode: flexible`
- Cannot use with Checkout (use legacy `trial_end` instead)
- Cannot combine with `trial_end` parameter

## Create a Trial Offer

```js
stripe.productCatalog.trialOffers.create({
  price: priceId,                          // $0 for free, >$0 for paid
  duration: { type: 'relative', relative: { iterations: 1 } },
  // OR: { type: 'timestamp' }  (required for subscription schedules)
  end_behavior: { transition: { price: regularPriceId } }
})
```

## Attach to Subscription

```js
// Create
stripe.subscriptions.create({ customer, billing_mode: { type: 'flexible' },
  items: [{ current_trial: { trial_offer: 'to_xxx' }, quantity: 1 }] })

// Update existing
stripe.subscriptions.update(id, { items: [{ id: itemId, current_trial: { trial_offer: 'to_xxx' } }] })
```

## Subscription Schedules

Only `timestamp` duration trials work with subscription schedules. Use `phases.items.trial_offer: 'to_xxx'`.

## Status After Trial

- Free ($0) → `trialing`
- Paid (>$0) → `active`/`incomplete`/`past_due`

## Billing Cycle Anchor After Trial

Default: `now` (fresh cycle, no proration). Set `trial_settings.end_behavior.billing_cycle_anchor: 'unchanged'` to prorate instead.

## Cancel at Trial End (Opt-In Pattern)

Set `cancel_at` = trial end timestamp so customers aren't auto-renewed.

## Related Pages

- [[stripe-subscriptions-trial-offers]] — concept page
- [[stripe-subscriptions]] — subscriptions context

## Raw Sources

- [[stripe-subscriptions-trial-offers-2026]] — verbatim trial offers guide (505 lines, 1 image)
