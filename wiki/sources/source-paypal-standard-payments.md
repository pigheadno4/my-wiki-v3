---
title: "PayPal Standard Payments Overview"
type: source
date_ingested: 2026-04-17
original_format: webpage
raw_files:
  - "paypal-standard-payments.md"
tags: [paypal, payments, checkout, authorization, capture, refunds]
---

## Summary

Overview page for accepting PayPal payments on a website. Customers pay with any funding source linked to their PayPal account. Part of the new `docs.paypal.ai` documentation site, referencing the **PayPal JavaScript SDK v6** and **Orders v2 API**.

## Key takeaways

- Two capture flows determine the available feature set:
  - **Immediate capture** — auth + capture in one step; use when shipping within 3 days. Supports: refunds, shipping/tax, split shipments.
  - **Authorize then capture** — auth first, capture later; use when shipping after 3+ days or requiring order verification. Supports: void, delayed capture, reauthorization, BOPIS.
- Authorization holds funds without transferring money; capture triggers the actual transfer.
- All features are implementable programmatically via API; merchants can also manage tracking, shipments, and refunds via the PayPal business dashboard.

## Use case categories

| Category | Features |
| --- | --- |
| Retail / ecommerce | Refunds, split shipments |
| Services / hospitality | Delayed capture, void authorization, buy online pick up in store (BOPIS) |
| Recurring / extended | Save payment methods (recurring), reauthorize beyond 3 days |

## Sub-pages referenced

- Refund a payment
- Split shipments
- Delay capture
- Void an authorization
- Buy online, pick up in store (BOPIS)
- Recurring payments / save payment method
- Reauthorize an authorization

## Raw Sources

- [[paypal-standard-payments]] — verbatim webpage content
