---
title: "Subscribe to Checkout Webhooks (APM Reference)"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-subscribe-webhooks.md"
tags: [paypal, apm, webhooks, orders-api, reference]
---

## Overview

Shared reference page for subscribing to the 5 core webhook events required by all APM integrations. Uses `POST /v1/notifications/webhooks`.

Source URL: <https://developer.paypal.com/docs/checkout/apm/reference/subscribe-to-webhooks/>

Last updated: 2025-05-13

## Standard APM Webhooks

| Webhook | Action |
| --- | --- |
| `CHECKOUT.ORDER.APPROVED` | Capture the payment |
| `CHECKOUT.PAYMENT-APPROVAL.REVERSED` | Problem after approval/before capture — notify buyer, handle reversed order |
| `PAYMENT.CAPTURE.PENDING` | Payment initiated, not yet completed — do not fulfill yet |
| `PAYMENT.CAPTURE.COMPLETED` | Fulfill the order |
| `PAYMENT.CAPTURE.DENIED` | Cancel fulfillment |

### Registration

`POST /v1/notifications/webhooks` — pass `url` and `event_types` array. Response includes `id` (webhook ID) and HATEOAS links (self/update/delete).

## Raw Sources

- [[paypal-apm-subscribe-webhooks]] — verbatim reference page

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview
