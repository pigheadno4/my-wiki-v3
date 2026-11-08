---
title: "Stripe Subscription Cancellation"
type: concept
category: framework
tags: [stripe, billing, subscriptions, cancellation, prorations, webhooks]
---

## Overview

Stripe subscriptions can be canceled immediately, at period end, on a custom future date, or automatically via schedule or failed payment policy. Each method has different proration, invoice, and billing cycle anchor implications.

## Auto-cancellation

Subscriptions cancel automatically after up to **8 failed billing attempts** (configurable in Dashboard → subscription settings). Smart Retries and customer email reminders are part of Stripe's revenue recovery tooling.

## Cancellation methods

### Immediate

```js
stripe.subscriptions.cancel(subscriptionId)
```

Takes effect immediately. No more invoices generated. Only `metadata` and `cancellation_details` can be updated after cancel.

### Cancel at period end

```js
stripe.subscriptions.update(subId, { cancel_at_period_end: true })
```

Subscription runs through the paid period. Reactivate any time before period end by setting back to `false`.

### Custom cancel date (`cancel_at`)

```js
stripe.subscriptions.update(subId, { cancel_at: unixTimestamp })
```

Key behaviors:
- Updates `items.current_period_end` to match → creates prorations
- **Cannot provide a refund** — credit proration always generated with a custom cancel date
- To suppress: set `cancel_at` within current billing period + `proration_behavior=none`
- If >1 period away: subscription cycles normally until the period containing the cancel date, then `current_period_end` shortens to match
- `min_period_end` / `max_period_end` enum helpers for `billing_mode` subscriptions

### Via subscription schedule

Set `end_behavior=cancel`. Schedule manages `cancel_at` automatically. Adding a new phase to the last phase **removes** the cancel date.

### Dispute-triggered

Configurable in Dashboard (Manage disputed payments):
- Cancel immediately (no proration)
- Cancel at period end

Limits: full-amount card disputes only; ~1h delay; incompatible with test clocks. Subs on schedules are released from the schedule first.

## Invoice items on cancellation

- Pending invoice items still billed if a final invoice is generated or the customer has another active subscription
- Must manually delete pending items to avoid billing
- Metered usage billed at period end unless `clear_usage` is used
- `cancel_at_period_end`: pending prorations collected at period end
- On cancel: all `open`/`draft` invoices get `auto_advance=false` — pauses automatic collection and emails (manual still possible)

## Billing cycle anchor behavior

- First period: custom anchor preserved
- After first period (or no custom anchor): anchor resets to `current_period_start` when cancel date removed/extended
- Moving cancel date closer: shortens anchor to match; creates credit proration
- Subs created before June 2024 may use legacy behavior (anchor unchanged)

## Webhooks

| Event | Description |
|---|---|
| `customer.subscription.updated` | Any update including `cancel_at_period_end=true` |
| `customer.subscription.deleted` | Actual cancellation (immediate or period-end reached) |

## Sources

- [[source-stripe-subscriptions-cancel]] — Stripe docs: full cancellation guide (all methods, invoice items, dispute config, anchor behavior)
