---
title: "Stripe: How Usage-Based Billing Works"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-how-it-works-2025.md"
tags: [stripe, billing, usage-based, meters, subscriptions, pricing]
---

## Summary

Overview of Stripe's usage-based billing model — how the lifecycle works and definitions of the six core concepts. Oriented around the Meter API (new v2 approach), distinct from the legacy metered billing via `aggregate_usage` on prices.

## Key Details

### Four-component lifecycle

1. **Ingestion** — send usage data to Stripe as meter events
2. **Product catalog** — create usage-based and recurring prices linked to meters
3. **Billing** — subscribe customer to prices; Stripe invoices at end of billing period
4. **Monitoring** — alerts for usage thresholds; analytics for trends

### Core concepts

| Term | Definition |
| --- | --- |
| **Customer / Account** | `Customer` object or Accounts v2 `customer_account` — stores billing details, links to subscriptions |
| **Subscription** | Recurring billing relationship; generates invoices at end of each billing cycle |
| **Price** | Attached to a product; defines how much and how often to charge; can be usage-based |
| **Meter** | Tracks usage data; specifies aggregation formula (sum, count, etc.) over billing period |
| **Meter event** | Unit of usage reported: event name + customer ID + numerical value; optional timestamp, idempotency ID, dimensions |
| **Meter event summary** | Aggregated usage for a custom time period; updates asynchronously |

## Raw Sources

- [[stripe-usage-based-billing-how-it-works-2025]] — verbatim webpage content (42 lines, lifecycle overview + concept table)
