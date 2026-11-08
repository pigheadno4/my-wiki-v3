---
title: "Stripe: Set Up Usage-Based Alerts"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/usage-based/alerts"
raw_files:
  - "stripe-billing-subscriptions-usage-based-alerts-2026-11-07.md"
  - "stripe-usage-based-billing-alerts-setup-2025.md"
tags: [stripe, billing, usage-based, meters, alerts, webhooks, monitoring]
---

## Summary

The November 7, 2026 guide describes **usage alerts** that notify an application when meter usage reaches a configured threshold. It separately mentions **billing thresholds** that can trigger invoices. A meter must exist before an alert is created. The May 2026 capture covers the same core usage-alert flow; the new capture adds invitations to request preview or early access to other features.

## Preview invitations

The November page invites readers to request **Usage Analytics API preview** access for customer-facing analytics dashboards and **early access** to spend and credit balance alerts. Its registration cURL is documentation for requesting access, not proof that any account received access, that these alert types are generally available, or that they use the usage-alert endpoint. No registration was performed in this update. The May capture only mentioned Usage Analytics.

## Create a usage alert

The guide names a `One-time per-customer usage alert`: it fires at most once for each customer that meets its configured usage level. Its example threshold is **100 API calls**, and the API example uses `usage_threshold[gte]=100`; that number and a customer ID are sample values, not universal requirements. The prose alternates between “reaches” and “exceeds,” so the example's explicit `gte` comparator is the precise boundary for that request.

- **Dashboard:** The alert form defaults to **Any customer**; choose **Specific customer** to limit it to one customer. This is a Dashboard setting.
- **API:** The November cURL and May Node examples both create a `usage_threshold` alert with a customer filter, meter ID, `gte=100`, and `recurrence=one_time`. Neither capture shows the all-customer API request shape or establishes that omitting `usage_threshold.filters` produces one.

```js
// May 2026 Node example, abbreviated; customer-filtered only
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

The November cURL renders the same customer-filtered example at `POST /v1/billing/alerts`; its language change does not establish a behavior change.

## Triggering, events, and verification

`billing.alert.triggered` is the usage-alert event. The page directs an application receiving webhooks to verify the event signature. The November Ruby example verifies only when `STRIPE_WEBHOOK_SECRET` is nonempty; its fallback parses unsigned JSON. That fallback is not proof of authenticated delivery and should not be copied as a secure production pattern. The sample's generic comment about checking PaymentIntent status does not define this alert event.

Stripe evaluates an alert when usage is **reported after alert creation**, and that evaluation includes usage reported before creation. The page does not say that historical usage fires an alert immediately at creation. The guide permits at most **25 alerts for each meter and customer combination** and says alerts currently do not work with **test clocks**.

## Related pages

- [[stripe-usage-based-billing]] — usage billing concept
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-alerts-2026-11-07|November 7 usage-alert guide]] — updated full documentation with preview invitations
- [[raw/stripe-usage-based-billing-alerts-setup-2025|May 5 usage-alert guide]] — earlier Node examples and retained alert behavior
