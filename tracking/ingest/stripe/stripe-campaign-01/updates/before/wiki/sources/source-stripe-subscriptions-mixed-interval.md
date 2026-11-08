---
title: "Stripe — Mixed Interval Subscriptions"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-mixed-interval-2026.md"
tags: [stripe, subscriptions, mixed-interval, flexible-billing, billing-periods, interval-alignment]
---

## Summary

Mixed interval subscriptions allow different billing periods (e.g., monthly + quarterly) on a single subscription. Requires flexible billing mode + API 2025-06-30.basil+. Stripe generates combined invoices when periods align, separate invoices otherwise.

## Key Mechanics

- Each subscription item has its own `current_period_start`/`current_period_end`
- Subscription-level period = latest `current_period_start` + earliest `current_period_end` across all items
- Combined invoice when periods align; separate invoices when they diverge

## Interval Alignment Rules

Every interval must be a multiple of the shortest. Equivalences: 1 week = 7 days, 12 months = 1 year.

**Supported**: 1mo + 3mo, 1mo + 1yr, 1day + 1wk, 2wk + 4wk, 2mo + 4mo + 6mo

**Not supported**: week+month, week+year, day+month, day+year, 2mo+3mo, 4mo+6mo

## Cancellation

Cancels all items regardless of interval. Dunning failure cancels entire subscription. `cancel_at_period_end` defaults to `min_period_end` (use `cancel_at` instead).

## Subscription Schedules

Use `duration` not `iterations` (iterations deprecated for mixed intervals).

## Limitations

- Cannot use with Checkout Sessions
- No retention coupon via customer portal
- Cannot migrate from flexible back to classic
- `min_period_end`/`max_period_end` helpers for determining cancellation date

## Related Pages

- [[stripe-subscriptions-mixed-interval]] — concept page
- [[source-stripe-subscriptions-billing-mode]] — flexible billing mode prerequisite

## Raw Sources

- [[stripe-subscriptions-mixed-interval-2026]] — verbatim mixed interval guide (395 lines, Dashboard + API sections)
