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
- A custom `cancel_at` does not provide a refund. Shortening the current billing period updates `items.current_period_end` and creates prorations unless disabled where allowed.
- A credit proration can be prevented only when `cancel_at` is within the current billing period; the May 2026 capture names `proration_behavior=none` for that path. Being within the period alone does not suppress it. Beyond the current period, the November 2026 guide says prorations cannot be disabled.
- Disabling prorations when `cancel_at` shortens the current period has billing-mode-dependent invoice-line effects; this guide does not enumerate each mode's result.
- If more than one period away, the current cycle continues until renewal into the period containing the cancel date; then `current_period_end` shortens.
- `min_period_end` / `max_period_end` enum helpers are available for `billing_mode` subscriptions.

> [!warning] Contradiction
> The May 2026 capture calls custom-date credit prorations “always generated” but also gives a within-period prevention path in the same passage. The November 2026 guide clarifies that prevention is bounded to a date in the current period and unavailable outside it. See [[source-stripe-subscriptions-cancel]].

### Via subscription schedule

Set `end_behavior=cancel`. Schedule manages `cancel_at` automatically. Adding a new phase to the last phase **removes** the cancel date.

### Dispute-triggered

Configurable in Dashboard (Manage disputed payments):
- Cancel immediately (no proration)
- Cancel at period end

Limits: full-amount card disputes only; ~1h delay; incompatible with test clocks. Subs on schedules are released from the schedule first.

## Invoice items on cancellation

- Pending invoice items still billed if a final invoice is generated or the customer has another active subscription
- To avoid billing pending items, delete them manually, or use the optional November 2026 Workflows template: it runs when the subscription ends and deletes only that subscription's pending invoice items. The template does not erase existing invoices or prove execution for an account.
- Metered usage billed at period end unless `clear_usage` is used
- `cancel_at_period_end`: pending prorations collected at period end
- On cancel: all `open`/`draft` invoices get `auto_advance=false` — pauses automatic collection and emails (manual still possible)

## Billing cycle anchor behavior

- First period: custom anchor preserved
- After first period (or no custom anchor): anchor resets to `current_period_start` when cancel date removed/extended
- Adding `cancel_at` or moving an existing cancel date earlier can move the billing-cycle anchor to the new cancel date, subject to the original-anchor and creation-date qualifications in this section. The November guide illustrates a credit proration when it is not suppressed; for `cancel_at` within the current billing period, the May capture names `proration_behavior=none` to prevent that credit. Outside the current period, the November guide says prorations cannot be disabled.
- Subs created before June 2024 may use legacy behavior (anchor unchanged)

## Webhooks

| Event | Description |
|---|---|
| `customer.subscription.updated` | Any update including `cancel_at_period_end=true` |
| `customer.subscription.deleted` | Actual cancellation (immediate or period-end reached) |

## Sources

- [[source-stripe-subscriptions-cancel]] — May and November 2026 cancellation guide: methods, bounded custom-date prorations, pending-item deletion routes, dispute limits and anchor behavior
