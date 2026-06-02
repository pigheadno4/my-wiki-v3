---
title: "Stripe Trial Offers"
type: concept
category: technology
tags: [stripe, subscriptions, trial-offers, flexible-billing, preview, discounted-trial]
---

## Overview

Trial Offers is a Stripe public preview API (`2026-03-25.preview`) for attaching discounted or free introductory prices to subscription items. It's a separate object — it doesn't replace Products or Prices, but temporarily overlays a different price on a subscription item.

**Requires**: `billing_mode: flexible` + API version header `2026-03-25.preview`.

**Cannot use with**: Checkout (use legacy `trial_end`), `trial_end` parameter simultaneously.

## 4 Use Cases

| Use case | Description |
| --- | --- |
| **Discounted trial** | Reduced introductory price (e.g., $1 for first week) |
| **Free trial** | $0 price on subscription item |
| **Upgrade trial** | Trial at basic rate to access premium features; auto-converts at end |
| **Item-level trial** | Trial for one line item; other items billed at regular price |

## Trial Offer Object

```js
stripe.productCatalog.trialOffers.create({
  price: priceId,
  duration: { type: 'relative', relative: { iterations: 1 } },
  // OR: { type: 'timestamp' }  ← required for subscription schedules
  end_behavior: { transition: { price: regularPriceId } }
})
```

## Attach via `items[].current_trial.trial_offer`

```js
items: [{ current_trial: { trial_offer: 'to_xxx' }, quantity: 1 }]
```

## Status After Trial

- Free ($0 only) → `trialing`
- Paid (>$0) or mixed → `active`/`incomplete`/`past_due`

## Billing Cycle Anchor Post-Trial

Default: `now` (new cycle, no proration). Set `trial_settings.end_behavior.billing_cycle_anchor: 'unchanged'` for prorated continuation.

## Opt-In Renewal

Set `cancel_at` = trial end timestamp to prevent auto-conversion to recurring subscription.

## Limitations

- Recurring items only (no non-recurring)
- Cannot modify trial length after creation
- Trial revenue not in Billing Analytics (paid trials counted as `active` revenue)
- Only `timestamp` duration works with subscription schedules

## Sources

- [[source-stripe-subscriptions-trial-offers]] — full API guide, 4 use cases, status behavior, billing anchor, opt-in pattern
- [[source-stripe-subscriptions-trial-compliance]] — Visa compliance: 7-day reminder emails, statement descriptor 22-char limit + `* TRIAL OVER`, manual path
