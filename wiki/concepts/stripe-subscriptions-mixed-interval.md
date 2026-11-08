---
title: "Stripe Mixed Interval Subscriptions"
type: concept
category: technology
tags: [stripe, subscriptions, mixed-interval, flexible-billing, billing-periods]
---

## Overview

The 2026-05-13 combined guide describes one subscription with items on different billing periods; its annual flat-rate plus monthly usage fee is an example. It requires flexible billing mode and API version `2025-06-30.basil` or later for the described Dashboard and API paths. The 2026-11-07 base capture is only a Dashboard/API variant index and does not reverify current prerequisites.

## Invoice Generation

- **Periods align** → single combined invoice
- **Periods diverge** → separate invoices per item

## Billing Period Tracking

Each subscription item has its own `current_period_start`/`current_period_end`. The subscription-level period = latest item `current_period_start` + earliest item `current_period_end`.

## Interval Alignment Rules

Every interval must be a multiple of the shortest interval in the subscription.

**May guide examples of supported combinations**: 1mo + 3mo, 1mo + 1yr, 1day + 1wk, 2wk + 4wk, 2mo + 4mo + 6mo. The guide treats 1 week as 7 days and 12 months as 1 year for validation.

**May guide examples of unsupported combinations**: week+month, week+year, day+month, day+year, 2mo+3mo, 4mo+6mo. These lists are not exhaustive; the guide says there is no week/month or day/month type equivalence.

## Key Constraints

- Canceling cancels all items regardless of interval
- In the May guide, if **all retries** for a payment on even one item's invoice fail, the shared subscription is affected; Stripe says it cancels the subscription and marks it unpaid or past due according to configured dunning settings.
- The May 2026 guide says deprecated `cancel_at_period_end` defaults to `min_period_end` for mixed intervals because it cannot choose an item's end date; it offers `cancel_at`, `min_period_end`, or `max_period_end` as date controls. The November index does not reverify this limit.
- For mixed interval schedules, the May guide recommends phase `duration`; phase `iterations` is deprecated and cannot calculate total iterations accurately for mixed intervals.
- The May 2026 guide said mixed interval subscriptions could not be created through Checkout Sessions.
- The May 2026 guide said a customer-portal retention coupon could not be applied to mixed interval subscriptions.
- The 2026-11-07 base capture is only a Dashboard/API variant index; the current status of these limits is unverified without the variant bodies.

## Sources

- [[source-stripe-subscriptions-mixed-interval]] — 2026-05-13 full Dashboard/API guide for item periods, interval alignment and limits; 2026-11-07 base capture is a variant index only
