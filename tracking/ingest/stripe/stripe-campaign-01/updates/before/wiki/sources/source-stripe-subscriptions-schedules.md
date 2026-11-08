---
title: "Stripe Subscription Schedules"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-schedules-2026.md"
tags: [stripe, billing, subscriptions, subscription-schedules, phases, proration, installments]
---

## Summary

Comprehensive guide to subscription schedules — automate subscription changes over time using phases. Classic Dashboard editor only. Covers phases, proration behavior, metadata, phase inheritance, direct subscription update interactions, and 10+ use cases.

## Core concepts

- Up to **10 sequential phases** per schedule; only one active at a time
- `end_behavior`: `release` (sub continues, schedule removed) or `cancel` (both canceled)
- First invoice on schedule-created sub: **DRAFT** (1h window) — unlike direct subscription creation which finalizes immediately

## Phase attributes

- `duration.interval` + `duration.interval_count` (recommended over manual `start_date`/`end_date`)
- `iterations` — number of billing periods (useful for installment plans)
- `trial_end` — trial within a phase; can be partial (before `end_date`) or full (= `end_date`)

## Two proration behavior settings

| Setting | Scope | Values |
|---|---|---|
| Top-level `proration_behavior` | Schedule update affecting current phase | `create_prorations` (default), `none`, `always_invoice` |
| Per-phase `proration_behavior` | Phase transition prorations | Same 3 values |

## Phase attribute inheritance

4 attributes settable at both schedule and phase level: `billing_thresholds`, `collection_method`, `default_payment_method`, `invoice_settings`. Phase overrides schedule.

## Phase metadata rules

- Non-empty value → add if key absent, update if key present
- Empty value → unset that key on subscription
- Updating subscription metadata directly does NOT affect current phase metadata

## Updating schedules

Must pass ALL current + future phases (past omitted). Up to 10 total. Updating active phase also updates underlying subscription.

## Direct subscription updates on schedule-attached subs

Modifying `items`, `discounts`, `tax_rates`, `trial_end`, `automatic_tax`, `add_invoice_items`, etc. directly on subscription **auto-splits** the active phase into two. Best practices:
- Use SubscriptionSchedule API (not Subscriptions API) when schedule is attached
- Store schedule IDs alongside sub IDs
- Discard schedule IDs after `subscription_schedule.released` webhook

## Use cases (9 examples)

1. **Future start** — `start_date: future_timestamp`
2. **Backdate** — `start_date: past_timestamp`
3. **Add schedule to existing sub** — `from_subscription: subId`
4. **Upgrade** — phase 1 = basic, phase 2 = basic + add-on
5. **Downgrade** — phase 1 = full, phase 2 = reduced
6. **Change price** — phase 1 = current, phase 2 = new price
7. **Increase quantity** — phase 1 qty=1, phase 2 qty=2
8. **Coupons** — phase 1 with coupon, phase 2 without
9. **Reset billing cycle anchor** — `billing_cycle_anchor: 'phase_start'`
10. **Installment plans** — `iterations: N`, `end_behavior: 'cancel'`; supports `price_data` for one-off amounts

## Preview

`invoices.createPreview({ schedule: id })` or `schedule_details.phases` for new/update preview.

## Related pages

- [[stripe-subscriptions-schedules]] — concept page
- [[stripe-subscriptions]] — concept page
- [[stripe-subscriptions-prorations]] — proration behavior
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-schedules-2026]] — verbatim Stripe docs webpage (1170 lines)
