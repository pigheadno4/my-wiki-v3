---
title: "Stripe — Fraud Insights"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-fraud-insights-2026.md"
tags: [stripe, radar, fraud-insights, fraud-teams, pivot-chart, analytics, investigation]
---

## Summary

Radar for Fraud Teams Insights tab: explore fraud patterns by filtering, pivoting, and drilling into individual transactions. Default view shows elevated risk (>65) + high velocity (>10 charges/card/hour).

## Default Filters

- Risk score > 65
- Card charges > 10/hour (high velocity)

## Configuration

**Time period**: prior 3 months by default (near real-time); custom range available.

**Payment status filter**:
- All payments (successful + blocked + declined)
- Successful payments only
- All fraud (disputes for fraud + EFWs + refunded as fraud)
- Disputes (any category)
- Early fraud warnings only

**Attribute filters**: Risk score, Card BIN, Card brand, Card country, IP country + more.

## Visualizations

**Pivot chart**: stacked bar chart, group by Day/Week/Month or by attribute dimension (e.g. Risk score stacks into 0-9, 10-19… ranges).

**Transaction list columns**: Risk score, Amount, Status, Customer, Payment method, Created. Click row → payment detail page.

## Actions

- Refund individual high-risk payments (overflow menu → Refund payment)
- Enable Risk controls for discovered patterns
- Write custom Radar rules targeting identified attributes

## Related Pages

- [[stripe-radar]] — concept page (updated with fraud insights)
- [[source-stripe-radar-analytics]] — Radar analytics center
- [[source-stripe-radar-risk-settings]] — risk controls to enable

## Raw Sources

- [[stripe-radar-fraud-insights-2026]] — verbatim fraud insights guide
