---
title: "Stripe: Set Up Usage-Based Alerts"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-usage-based-billing-alerts-setup-2025.md"
tags: [stripe, billing, usage-based, meters, alerts, webhooks, monitoring]
---

## Summary

Implementation guide for usage-based alerts: creating alerts via Dashboard or API, listening for the `billing.alert.triggered` webhook event, and limitations including test clock incompatibility.

## Key Details

**Prerequisites**: meter must exist before creating an alert.

**Alert type**: `One-time per-customer usage alert` — triggers once when a customer first exceeds the threshold. Does not re-trigger regardless of future usage.

**Create alert API**:

```js
stripe.billing.alerts.create({
  title: 'Sample alert',
  alert_type: 'usage_threshold',
  usage_threshold: {
    filters: [{ type: 'customer', customer: CUSTOMER_ID }],
    meter: METER_ID,
    gte: 100,
    recurrence: 'one_time',
  },
})
```

- `filters` scopes to a specific customer; omit for all customers
- `gte` sets the usage threshold value
- `recurrence: 'one_time'` = one-time per-customer

**Webhook event**: `billing.alert.triggered` — fires when meter exceeds threshold for a customer. Handle via `stripe.webhooks.constructEvent` with signature verification.

**Additional limitation**: alerts don't work with **test clocks**.

**Usage Analytics API** mentioned (not detailed here) — for building analytics dashboards for end users.

## Raw Sources

- [[stripe-usage-based-billing-alerts-setup-2025]] — verbatim webpage content (129 lines)
