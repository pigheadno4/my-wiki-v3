---
title: "Stripe Billing Analytics"
type: concept
category: framework
tags: [stripe, billing, analytics, mrr, churn, subscribers, ltv, arpu, cohort, recurring-revenue]
---

## Overview

Stripe Billing Dashboard analytics tracks recurring-revenue, subscriber, trial, churn, retention, and usage metrics. It offers configurable definitions, scoped drill-downs and filtering, metric-level CSV exports, and three listed prebuilt CSV reports in live mode. See [[source-stripe-billing-analytics]] for the 2026-05-13 and 2026-11-07 variants.

## Key metrics

### MRR (Monthly Recurring Revenue)

Monthly-normalized value of all `active` + `past_due` subscriptions.

**Excluded from ordinary MRR**: taxes, free plans, and metered products. For item-level trial offers, only trialing items are excluded; non-trial items in a mixed subscription still contribute. A legacy `trial_end` free trial excludes the whole subscription during the trial. See [[source-stripe-billing-analytics]] (2026-11-07 lines 111–115); the 2026-05-13 capture used subscription-level trial language.

`canceled` or `unpaid` subscription → churn → removed from MRR.

### MRR growth components

| Component | Description |
|---|---|
| New MRR | Trial → paid, new subscriber |
| Expansion MRR | Upgrade |
| Contraction MRR | Downgrade |
| Reactivation MRR | Churned customer returns |
| Churn MRR | Cancellation |
| FX Adjustment | Foreign currency value change |

### Active subscribers

Customers with ≥1 `active`/`past_due` subscription with **positive MRR**. Multiple subs per customer = 1 subscriber.

**Edge case**: 100% coupon applied + discount subtracted from MRR → counted as churned.

### ARPU

`MRR ÷ active subscribers`

### LTV (Subscriber Lifetime Value)

`ARPU ÷ subscriber churn rate`

### Trial conversion rate

`trials converted ÷ trials ended (last 30 days)` — can exceed 100% if conversions happen after trial end. Item-level trial offers count new trials and conversions per trialing subscription item; legacy `trial_end` counts at the subscription level. See [[source-stripe-billing-analytics]] (2026-11-07 lines 199–209; 2026-05-13 lines 163–172).

### Subscriber churn rate

`churned subscribers ÷ (subscribers 30 days ago + new subscribers in period)`

### Churned revenue

`churned MRR + contraction MRR`

### Retention by cohort

Cohorts assigned by month of first positive MRR. Revenue retention can exceed 100% due to expansion upgrades.

### Usage metrics

- **Aggregate usage**: SUM/COUNT of meter events in period
- **Usage revenue**: price × usage events (excludes taxes and discounts)

Note: Only SUM and COUNT aggregation types displayed; others not shown.

## Configurable settings (24–48h to appear in configuration)

**Discount subtraction from MRR**:
- Recurring discounts: optional subtract
- One-time discounts: optional subtract
- Permanent recurring discounts: always subtracted (not configurable)

**Active subscriber timing**:
- Start of subscription (most common option; no product default established by these captures)
- When first payment received

## CSV exports and prebuilt reports

The 2026-11-07 capture distinguishes individual-metric exports, whose summary tables reflect selected date range, filters, grouping, and comparison, from live-mode prebuilt reports with fixed schemas. Data-result rows are available only for supported metrics. Prebuilt report dates use UTC; charts use the account time zone. See [[source-stripe-billing-analytics]] (new lines 40–65).

| November 2026 prebuilt report | Listed contents |
|---|---|
| MRR per subscriber per month | MRR per subscriber at month end |
| Subscription metrics per month | MRR and subscriber roll-forwards, retention, customer value |
| Customer MRR changes | Customer MRR change log (new/upgrade/downgrade/reactivation/churn) |

The 2026-05-13 capture instead listed **Subscription metrics summary**, with MRR and active-subscriber roll-forwards, trial conversion, and lifetime value. The later page does not establish that the older report is unavailable elsewhere.

## Dashboard features

- **AR aging**: Billing overview > Collections shows current unpaid invoice balances by age as of today. Supported past reporting dates require Revenue Recognition; see [[source-stripe-billing-analytics]] (2026-11-07 lines 36–38).
- **Explore**: drill into chart data points to see underlying events (subset of metrics)
- **Filter/group by Product or Price**: available for subset; not available for multi-currency
- **Benchmark**: compare against similar Stripe businesses

## Sources

- [[source-stripe-billing-analytics]] — Stripe docs: full analytics guide with all metric definitions, configurations, and report descriptions
- [[source-stripe-billing-benchmarks]] — benchmarking: k-NN peer matching, access requirements (≥5 subs), 7 benchmarked metrics, percentile display
