---
title: "Stripe Subscription Schedules"
type: concept
category: framework
tags: [stripe, billing, subscriptions, subscription-schedules, phases, proration, installments, automation]
---

## Overview

Subscription schedules automate changes to subscriptions over time using sequential phases. Available via API and Dashboard (classic editor only). Up to 10 phases per schedule.

## Key behaviors

- **First invoice**: schedule-created subs start with a DRAFT invoice (1h window to edit) — unlike direct subscription creation which finalizes immediately
- **Phase transitions**: automatic on `end_date`; subscription updated to next phase attributes
- **`end_behavior`**: `release` (sub continues, schedule detached) or `cancel` (both terminated)
- **Max phases**: 10 current + future (past phases don't count)

## Phase configuration

```js
phases: [{
  items: [{ price: priceId, quantity: 1 }],
  duration: { interval: 'month', interval_count: 3 },  // recommended over manual start/end_date
  // or: iterations: 6  (for installment plans)
  trial_end: timestamp,  // optional, can be partial (before end_date) or full (= end_date)
  proration_behavior: 'create_prorations',  // per-phase transition behavior
  billing_cycle_anchor: 'phase_start',  // optional reset
  discounts: [{ coupon: couponId }],
  tax_rates: [taxRateId],
  metadata: { key: 'value' }  // see metadata rules below
}]
```

## Two proration settings

| Setting | Scope |
|---|---|
| Top-level `proration_behavior` | When updating a schedule affecting the current phase |
| Per-phase `proration_behavior` | When transitioning INTO that phase |

Both accept: `create_prorations` (default), `none`, `always_invoice`.

## Phase attribute inheritance

4 attributes settable at both schedule (`default_settings`) and phase level: `billing_thresholds`, `collection_method`, `default_payment_method`, `invoice_settings`. Phase overrides schedule.

## Phase metadata merge rules

- Non-empty value → adds key if absent, updates if present
- Empty string value → unsets that key on subscription
- Updating subscription metadata directly does NOT affect current phase metadata

## Direct sub updates when schedule attached

Modifying `items`, `discounts`, `tax_rates`, `trial_end`, `automatic_tax`, `add_invoice_items` etc. directly on the subscription **auto-splits** the active schedule phase into two phases.

**Best practices**:
- Use SubscriptionSchedule API (not Subscriptions API) when a schedule is attached
- Store schedule IDs alongside subscription IDs
- Listen for `subscription_schedule.released` to discard schedule IDs
- Use Dashboard where possible (auto-updates attached schedule)

## Use cases

| Use case | Key parameter |
|---|---|
| Future start | `start_date: future_unix` |
| Backdate | `start_date: past_unix` |
| Add schedule to existing sub | `from_subscription: subId` |
| Upgrade / downgrade | Multi-phase with different items |
| Reset billing anchor | `billing_cycle_anchor: 'phase_start'` |
| Installment plan | `iterations: N` + `end_behavior: 'cancel'` |
| Coupon for first N months | Phase 1 with coupon, Phase 2 without |
| Change tax rates per period | Different `tax_rates` per phase |

## Create from existing subscription

```js
stripe.subscriptionSchedules.create({ from_subscription: subId })
// Creates schedule with 1 phase mirroring current billing period
```

## Release vs cancel

- **Release**: `subscriptionSchedules.release(id)` — removes schedule, subscription continues
- **Cancel**: `subscriptionSchedules.cancel(id)` — cancels both schedule and subscription

## Limitations

- Classic Dashboard editor only (not new subscription editor)
- Dashboard can't set: sub schedule metadata, phase item metadata, currency, Connect params
- Dashboard sets some attrs globally across all phases (not per-phase): billing thresholds, payment methods, invoice settings, description, trial days

## Sources

- [[source-stripe-subscriptions-schedules]] — Stripe docs: full subscription schedules guide (phases, proration, metadata, direct update interactions, 10+ use cases)
