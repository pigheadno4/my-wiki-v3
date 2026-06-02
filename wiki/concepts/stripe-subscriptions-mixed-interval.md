---
title: "Stripe Mixed Interval Subscriptions"
type: concept
category: technology
tags: [stripe, subscriptions, mixed-interval, flexible-billing, billing-periods]
---

## Overview

Mixed interval subscriptions allow a single subscription to contain items with different billing periods (e.g., monthly flat fee + quarterly usage fee). Requires `billing_mode: flexible` + API `2025-06-30.basil`+.

## Invoice Generation

- **Periods align** → single combined invoice
- **Periods diverge** → separate invoices per item

## Billing Period Tracking

Each subscription item has its own `current_period_start`/`current_period_end`. The subscription-level period = latest item `current_period_start` + earliest item `current_period_end`.

## Interval Alignment Rules

Every interval must be a multiple of the shortest interval in the subscription.

**Supported combinations**: 1mo + 3mo, 1mo + 1yr, 1day + 7days, 2wk + 4wk, 2mo + 4mo + 6mo

**Not supported**: week+month, week+year, day+month, day+year, 2mo+3mo, 4mo+6mo

## Key Constraints

- Canceling cancels all items regardless of interval
- Dunning failure → entire subscription canceled
- `cancel_at_period_end` defaults to `min_period_end` → use `cancel_at` instead
- Use `duration` (not `iterations`) in subscription schedules
- Cannot create via Checkout Sessions
- No retention coupon via customer portal

## Sources

- [[source-stripe-subscriptions-mixed-interval]] — full guide: API, billing period tables, interval alignment rules, limitations
