---
title: "Handle Uncaptured Payments (APM Reference)"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-handle-uncaptured-payments.md"
tags: [paypal, apm, webhooks, uncaptured-payments, reference]
---

## Overview

Reference guide for handling the `CHECKOUT.PAYMENT-APPROVAL.REVERSED` webhook — fired when a buyer-approved APM payment isn't captured within the configured window.

Source URL: <https://developer.paypal.com/docs/checkout/apm/reference/handle-uncaptured-payments/>

Last updated: 2025-04-24

## Key Detail

**Default capture window: 3 hours** after buyer approval. Merchant-configurable. After expiry:

1. PayPal fires `CHECKOUT.PAYMENT-APPROVAL.REVERSED`
2. Order cancelled
3. Buyer account refunded

Webhook payload includes `order_id`, `purchase_units` (with `custom_id`/`invoice_id`), and `payment_source`.

### Required actions on receiving webhook

1. Notify buyer of cancellation (branded notification with next steps)
2. Update internal records to show order cancelled

## Raw Sources

- [[paypal-apm-handle-uncaptured-payments]] — verbatim reference page with webhook payload sample

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview
- [[source-paypal-apm-subscribe-webhooks]] — Webhook subscription reference (includes `CHECKOUT.PAYMENT-APPROVAL.REVERSED` in the 5 core events)
