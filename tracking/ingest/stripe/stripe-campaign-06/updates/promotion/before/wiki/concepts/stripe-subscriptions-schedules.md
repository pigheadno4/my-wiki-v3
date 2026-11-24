---
title: "Stripe Subscription Schedules"
type: concept
category: framework
tags: [stripe, billing, subscriptions, subscription-schedules, phases, proration, installments, automation]
---

## Overview

Subscription schedules automate changes to subscriptions over time using sequential phases. The November 2026 guide describes Dashboard and API workflows; the May 2026 guide's classic-editor-only statement is dated UI guidance, not a current universal limit. Up to 10 current and future phases per schedule.

## Key behaviors

- **First invoice**: for a schedule-created subscription with `collection_method=charge_automatically`, the guide says the invoice is initially `draft` rather than immediately finalized as in its direct-creation comparison. Its `start_date=now` example allows about an hour to edit; later `open` or `paid` depends on the asynchronous payment outcome.
- **Phase transitions**: automatic on `end_date`; subscription updated to next phase attributes
- **`end_behavior`**: `release` detaches the schedule and preserves an existing subscription; when `not_started`, release creates no subscription. Canceling an active schedule with a subscription cancels that subscription; canceling before start ends the schedule before subscription creation.
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

> [!warning] Contradiction
> This default describes the top-level and per-phase **Subscription Schedule API** settings above. The 2026-05-12 [[source-stripe-subscriptions-migration-toolkit]] capture described its separate CSV `proration_behavior` default as `create_prorations`, while the 2026-11-07 capture says an omitted or blank toolkit CSV value defaults to `none`. Do not use the schedule API default to fill a toolkit CSV value.

## Phase attribute inheritance

Five attributes are settable at both schedule (`default_settings`) and phase level: `automatic_tax`, `billing_thresholds`, `collection_method`, `default_payment_method`, `invoice_settings`. Phase overrides schedule. For a phase using manual `default_tax_rates`, explicitly set `automatic_tax.enabled=false`; enabled automatic tax and manual rates cannot apply together. Directly enabling automatic tax on the attached subscription updates the current phase and schedule default, so future phases without an explicit setting inherit that default. Retained manual rates are not a fallback if automatic tax calculation fails.

## Phase metadata merge rules

- Non-empty value → adds key if absent, updates if present
- Empty string value → unsets that key on subscription
- Updating subscription metadata directly does NOT affect current phase metadata

## Direct sub updates when schedule attached

Direct edits to `items`, `discounts`, `tax_rates`, `trial_end`, `automatic_tax`, `add_invoice_items` and other listed fields **might** create a new phase. In the guide's item-deletion example, the active phase splits into ended and new phases. Direct metadata edits do not propagate to the attached schedule.

**Best practices**:
- Use SubscriptionSchedule API (not Subscriptions API) when a schedule is attached
- Store schedule IDs alongside subscription IDs
- Listen for `subscription_schedule.released` to discard schedule IDs
- Use Dashboard where possible (auto-updates attached schedule)

## Use cases

| Use case | Key parameter |
|---|---|
| Future start | `start_date: future_unix`; subscription created when date arrives |
| Backdate | `start_date: past_unix`; subscription created immediately and elapsed time billed; application controls digital access |
| Add schedule to existing sub | `from_subscription: subId`; one phase from current period/configuration, with no migration proration invoice items |
| Upgrade / downgrade | Multi-phase with different items |
| Reset billing anchor | `billing_cycle_anchor: 'phase_start'` |
| Installment plan | `iterations: N` + `end_behavior: 'cancel'` |
| Coupon for first N months | Phase 1 with coupon, Phase 2 without |
| Change tax rates per period | Different `tax_rates` per phase |

Schedule updates must include every current and future phase and any previously set parameters to keep them; omitted parameters are unset. Past phases are response-only.

## Create from existing subscription

```js
stripe.subscriptionSchedules.create({ from_subscription: subId })
// Creates one phase from current billing period and configuration; migration creates no proration invoice items
```

## Release vs cancel

- **Release (API)**: `subscriptionSchedules.release(scheduleId)` accepts `not_started` or `active`, removes remaining phases, preserves an existing subscription, and creates none before start.
- **Cancel (API or Dashboard)**: `subscriptionSchedules.cancel(scheduleId)` accepts `not_started` or `active`; when active with a subscription, it cancels that subscription immediately. Dashboard deletion before start cancels the schedule before creation. A finite final Dashboard phase end date cancels the subscription; use API `end_behavior=release` for fixed-duration release.

## Limitations

- The May 2026 capture said classic Dashboard editor only and a 30-day persisted editor choice; the November guide describes Dashboard create/edit/preview/cancel without establishing universal account or editor availability. It documents release through the API.
- Dashboard can't set: sub schedule metadata, phase item metadata, currency, Connect params
- Dashboard sets some attrs globally across all phases (not per-phase): billing thresholds, payment methods, invoice settings, description, trial days

## Sources

- [[source-stripe-subscriptions-schedules]] — Stripe docs: full subscription schedules guide (phases, proration, metadata, direct update interactions, 10+ use cases)
