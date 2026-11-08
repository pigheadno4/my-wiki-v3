---
title: "Stripe — Mixed Interval Subscriptions"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/mixed-interval"
raw_files:
  - "stripe-subscriptions-mixed-interval-2026.md"
tags: [stripe, subscriptions, mixed-interval, flexible-billing, billing-periods, interval-alignment]
---

## Overview

The 2026-05-13 combined Stripe guide describes mixed interval subscriptions: one subscription with items that have different prices and billing periods. Its Dashboard and API variants explain item-level billing, invoice alignment, schedules, dunning, trials, and limits. The 2026-11-07 base capture at the same URL is only an index linking separate Dashboard and API variants. It provides no current operational details, so omission of May content does not establish deprecation or current account eligibility. See [[stripe-subscriptions-mixed-interval]] and [[stripe]].

## Key mechanics from the 2026-05-13 guide

- The May guide requires flexible billing mode and API version `2025-06-30.basil` or later for its Dashboard and API paths. Its API example's `collection_method: send_invoice`, `days_until_due: 5`, and `proration_behavior: none` are sample choices, not general mixed interval requirements.
- When item billing periods align, Stripe describes a combined invoice; when they diverge, separate invoices. The January 2024 monthly/quarterly example bills both items initially, monthly only in February and March, and both in April. That timeline illustrates its particular periods and start date.
- Each item tracks its own `current_period_start` and `current_period_end`. In the May period table, the subscription period follows the latest item start and earliest item end. A future-dated `trial_end` sets the item and subscription end dates to the trial end.
- Canceling the shared subscription or its schedule cancels all its items. **If all retries for a payment fail**, even when the failed invoice concerns one item, the May guide says Stripe cancels the entire subscription and marks it unpaid or past due according to configured dunning settings. A single failure alone does not establish that outcome.
- On resuming after a missing-payment-method trial pause, the May example distinguishes `billing_cycle_anchor: unchanged` with `proration_behavior: none` from `billing_cycle_anchor: now`. Its invoice and active-versus-paused outcomes depend on those settings and whether the resumption invoice is paid.

## Interval alignment and schedules

Every item's price interval must be a multiple of the shortest interval in that subscription, subject to the May guide's listed equivalences and unsupported interval types. It treats one week as seven days and twelve months as one year for validation, but expressly gives no week/month, week/year, day/month, or day/year equivalence. The supported and unsupported combinations at May lines 354–385 are **examples**, not exhaustive lists.

The May guide supports mixed interval subscription schedules. It **recommends** phase `duration` rather than deprecated phase `iterations` because iteration counts cannot accurately model total mixed-interval time. The guide also describes migrating an existing subscription to flexible mode before adding differently timed items.

## Dated limitations and locators

- Dashboard creation and adding mixed interval items: May raw lines 14–32. API creation and its monthly/quarterly invoice example: May lines 34–142.
- Schedule example and `duration` recommendation: May lines 144–274 and 393. The example does not establish a universal `send_invoice` or five-day due setting.
- Shared cancellation and exhausted-retry dunning consequence: May lines 282–286. Item periods, trial, and setting-dependent resume comparison: May lines 290–352.
- Alignment rule, equivalences and combination examples: May lines 354–385. Its `cancel_at_period_end` helper limitation and `cancel_at`, `min_period_end`, `max_period_end` alternatives are at lines 386–392.
- The May guide says a mixed interval subscription cannot use a customer-portal retention coupon or be created through Checkout Sessions (lines 394–395). The November index cannot verify whether those limits remain current.
- The former source's flexible-to-classic migration claim is not in this matched May guide or November index; see [[source-stripe-subscriptions-billing-mode]] for separate billing-mode authority.

## Related

- [[stripe-subscriptions-mixed-interval]] — reciprocal concept
- [[source-stripe-subscriptions-billing-mode]] — separate billing-mode guide
- [[stripe]] — company

## Related raw API references

- [[raw/stripe-billing-subscriptions-mixed-interval-2026-11-07|2026-11-07 Dashboard/API variant index]] — navigation only; linked variant bodies were not captured in this job

## Raw Sources

- [[raw/stripe-subscriptions-mixed-interval-2026|Stripe mixed interval guide, captured 2026-05-13]] — detailed historical Dashboard and API variants
