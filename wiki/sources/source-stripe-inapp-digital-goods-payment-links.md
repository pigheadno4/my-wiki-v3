---
title: "Accept iOS Digital Goods Payments with Payment Links"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-digital-goods-payment-links-2025.md"
tags: [stripe, mobile, ios, digital-goods, payment-links, universal-links, apple-pay, webhooks, client-reference-id]
---

## Summary

No-server guide for selling iOS in-app digital goods using Payment Links (vs Checkout which requires a server). Same Universal Links setup as the Checkout path, but the success URL is configured in the Dashboard rather than via API.

> See also [[source-stripe-inapp-digital-goods-checkout]] for the Checkout (server-required) path.

## When to Use Which

| Approach | Server needed | Dynamic cart | Attach Customer | Best for |
| --- | --- | --- | --- | --- |
| Payment Links | No | No | No | Limited products, simple flow |
| Checkout | Yes | Yes | Yes | Dynamic cart, personalization |
| Elements | Yes | Yes | Yes | Fully custom UI |

## Apple Pay Geography Restriction

- **US + EEA**: Apple Pay works for digital goods/subscriptions
- **Other regions**: Apple Pay cannot be used for digital products/subscriptions on iOS

## Key URL Parameters

| Parameter | Notes |
| --- | --- |
| `prefilled_email` | Pre-fills email; customer can edit |
| `locked_prefilled_email` | Pre-fills email; customer cannot edit; takes precedence over `prefilled_email` |
| `client_reference_id` | Up to 200 chars (alphanumeric/dash/underscore); appears in `checkout.session.completed` webhook; use for reconciliation |

```
https://buy.stripe.com/test_xxx?prefilled_email=jenny%40example.com&client_reference_id=id_123
```

Encode email addresses in URL parameters to avoid pass-through failures.

## Dashboard Setup

1. Create product + price in Dashboard
2. Create Payment Link: Products → After Payment → "Don't show confirmation page" → set Universal Link as success URL
3. Card + Apple Pay enabled by default; enable additional methods from Dashboard settings

## Webhook Fulfillment

`checkout.session.completed` → `client_reference_id` in session payload → identify user/order → grant entitlement

No server endpoint needed to create the Payment Link, but a webhook endpoint is still needed for fulfillment.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-payment-links]] — Stripe Payment Links concept page
- [[source-stripe-inapp-digital-goods-checkout]] — Checkout path (server required, dynamic cart)
- [[source-stripe-inapp-ios-android-purchases]] — platform rules overview

## Raw Sources

- [[stripe-inapp-digital-goods-payment-links-2025]] — verbatim guide (~166 lines)
