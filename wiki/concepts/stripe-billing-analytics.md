---
title: "Stripe Billing Analytics"
type: concept
category: framework
tags: [stripe, billing, analytics, mrr, churn, subscribers, ltv, arpu, cohort, recurring-revenue]
---

## Overview

Stripe Billing Dashboard analytics tracks recurring revenue metrics. Configurable definitions, drill-down exploration, product/price filtering, and 3 downloadable CSV reports. Benchmarking against similar businesses available.

## Key metrics

### MRR (Monthly Recurring Revenue)

Monthly-normalized value of all `active` + `past_due` subscriptions.

**Excluded from MRR**: trials, taxes, free plans, metered/usage-based products.

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

`trials converted ÷ trials ended (last 30 days)` — can exceed 100% if conversions happen after trial end.

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

## Configurable settings (24-48h to apply)

**Discount subtraction from MRR**:
- Recurring discounts: optional subtract
- One-time discounts: optional subtract
- Permanent recurring discounts: always subtracted (not configurable)

**Active subscriber timing**:
- Start of subscription (most common / default)
- When first payment received

## Downloadable CSV reports

| Report | Contents |
|---|---|
| MRR per subscriber per month | MRR per subscriber at month end |
| Subscription metrics summary | MRR roll-forward, subscriber roll-forward, trial conversion, LTV |
| Customer MRR changes | Log of every MRR change (new/upgrade/downgrade/reactivation/churn) |

## Dashboard features

- **Explore**: drill into chart data points to see underlying events (subset of metrics)
- **Filter/group by Product or Price**: available for subset; not available for multi-currency
- **Benchmark**: compare against similar Stripe businesses

## Sources

- [[source-stripe-billing-analytics]] — Stripe docs: full analytics guide with all metric definitions, configurations, and report descriptions
- [[source-stripe-billing-benchmarks]] — benchmarking: k-NN peer matching, access requirements (≥5 subs), 7 benchmarked metrics, percentile display
