---
title: "Stripe Subscriptions — Cancel Subscriptions"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-cancel-2026.md"
tags: [stripe, billing, subscriptions, cancellation, prorations, webhooks]
---

## Summary

Comprehensive guide to canceling Stripe subscriptions — immediate, at period end, on a custom date, or via schedule. Key contributions: custom cancel date caveats, invoice item handling on cancel, dispute-triggered cancellation, billing cycle anchor behavior.

## Auto-cancellation

Subscriptions cancel automatically after up to **8 failed billing attempts** (configurable in Dashboard subscription settings).

## Immediate cancellation

```js
stripe.subscriptions.cancel(subscriptionId)
```

Takes effect immediately. No more invoices generated. After cancel, only `metadata` and `cancellation_details` can be updated.

## Cancel at period end

```js
stripe.subscriptions.update(subId, { cancel_at_period_end: true })
```

Subscription continues through the paid period. Reactivate any time before period end by setting `cancel_at_period_end: false`.

## Custom cancel date (`cancel_at`)

```js
stripe.subscriptions.update(subId, { cancel_at: timestamp })
```

- Updates `items.current_period_end` to match the cancel date → creates prorations
- **Cannot provide a refund** with a custom cancel date — credit proration always generated
- To suppress credit proration: set `cancel_at` within current billing period + `proration_behavior=none`
- If >1 period away: subscription cycles normally until the period containing `cancel_at`
- `min_period_end` / `max_period_end` enum helpers available for `billing_mode` subscriptions

## Via subscription schedule

Set `end_behavior=cancel` on schedule. Schedule automatically manages `cancel_at`. Adding a new phase to the last phase **removes** the cancel date.

## Dispute-triggered cancellation

Configurable in Dashboard (Manage disputed payments). Options:
- Cancel immediately without prorating
- Cancel at period end (`cancel_at_period_end=true`)

Limitations: only full-amount credit/debit card disputes; ~1h delay; NOT compatible with test clocks. Subscriptions on schedules are first released from the schedule then canceled.

## Invoice items on cancellation

- Pending invoice items still billed if: final invoice generated, or customer has another active subscription
- Must **manually delete** pending invoice items to avoid billing them
- Metered usage billed at period end unless `clear_usage` is used on update
- If `cancel_at_period_end`, pending prorations are collected at period end
- On cancel, all `open`/`draft` invoices for that subscription get `auto_advance=false` — pauses automatic collection and reminder emails (manual collection still possible)

## Billing cycle anchor on cancel removal/extension

- First period: any anchor originally set is preserved
- After first period (or if no custom anchor): anchor resets to `current_period_start` when cancel date is removed/extended
- Subs created before June 2024 may exhibit legacy behavior (anchor unchanged)
- Moving cancel date closer: shortens billing anchor to match; creates credit proration for removed time

## Webhooks

| Event | Description |
|---|---|
| `customer.subscription.updated` | Any update, including `cancel_at_period_end=true` |
| `customer.subscription.deleted` | Actual cancellation (immediate or period-end) |

## Related pages

- [[stripe-subscriptions-cancel]] — concept page
- [[stripe-subscriptions-prorations]] — proration behavior on cancel
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-cancel-2026]] — verbatim Stripe docs webpage
