---
title: "Stripe Billing — Analytics"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-billing-analytics-2026.md"
tags: [stripe, billing, analytics, mrr, churn, subscribers, ltv, arpu, cohort, reports]
---

## Summary

Comprehensive definitions and configuration guide for Stripe Billing analytics metrics. Covers MRR, MRR growth components, active subscribers, ARPU, LTV, trial conversion, churn, cohort retention, and 3 downloadable CSV reports.

## Downloadable CSV reports

1. **MRR per subscriber per month** — MRR per subscriber at end of each month
2. **Subscription metrics summary** — MRR roll-forward, subscriber roll-forward, trial conversion, LTV
3. **Customer MRR changes** — log of every MRR change (new, upgrade, downgrade, reactivation, churn)

## Configurable metrics (24-48h to apply)

**Discounts in MRR**:
- Subtract recurring discounts: optional
- Subtract one-time discounts: optional
- Permanent recurring discounts: always subtracted (not configurable)

**Active subscriber timing**:
- At start of subscription (default/most common)
- When first payment received

## Metric definitions

### MRR
Sum of monthly-normalized value of `active` + `past_due` subscriptions.
**Excludes**: trials, taxes, free plans, metered/usage-based products.
`canceled` or `unpaid` → churn → no longer counts.

Example: 100 × $100/month + 50 × ($600/year ÷ 12) = $12,500 MRR

### MRR growth components
- **New MRR**: trial → paid conversion
- **Expansion MRR**: upgrade
- **Contraction MRR**: downgrade
- **Reactivation MRR**: churned customer returns
- **Churn MRR**: cancellation
- **FX Adjustment**: currency value change

### Active subscribers
Customers with ≥1 `active`/`past_due` sub with positive MRR. Multiple subs = 1 subscriber.
100% coupon (when discount subtracted from MRR) → counted as churn.

### ARPU
MRR ÷ active subscribers

### LTV
ARPU ÷ subscriber churn rate

### Trial conversion rate
Trials converted ÷ trials ended (last 30 days). Can exceed 100% (some convert after trial end).

### Subscriber churn rate
Churned subscribers ÷ (subscribers 30 days ago + new subscribers in period)

### Churned revenue
Churned MRR + contraction MRR

### Retention by cohort
Cohort = month of first positive MRR. Revenue retention can exceed 100% (expansion upgrades).

### Usage metrics
- **Aggregate usage**: SUM/COUNT of meter events (SUM and COUNT only; other aggregation types not displayed)
- **Usage revenue**: price × usage events; excludes taxes and discounts

## Dashboard features
- **Explore**: drill down into chart data points (available for subset of metrics)
- **Filter/group**: by Product or Price (not available for multi-currency)
- **Benchmark**: against similar businesses on Stripe

## Related pages

- [[stripe-billing-analytics]] — concept page
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-analytics-2026]] — verbatim Stripe docs webpage (212 lines)
