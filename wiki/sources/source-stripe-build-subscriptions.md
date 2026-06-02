---
title: "Stripe — Build a Subscriptions Integration"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-build-subscriptions-2026.md"
tags: [stripe, subscriptions, billing, checkout, elements, customer-portal, billing-mode, webhooks]
---

## Summary

Full step-by-step integration guide for subscriptions across three UI paths: Stripe-hosted Checkout, Embedded Checkout, and Custom Elements form. 10,049 lines; 10 CDN images not downloaded.

## Three Integration Paths

| Path | Key API |
| --- | --- |
| Stripe-hosted page | `checkout.sessions.create({ mode: 'subscription', line_items, success_url })` |
| Embedded page | `checkout.sessions.create({ ui_mode: 'embedded_page', return_url })` → `stripe.createEmbeddedCheckoutPage({ fetchClientSecret })` |
| Custom Elements | SetupIntent → PaymentElement → `stripe.preparePaymentMethod()` → `subscriptions.create()` |

## Key Implementation Notes

**`billing_mode: { type: 'flexible' }`** in `subscription_data`: more predictable subscription behavior; requires Stripe API version `2025-06-30.basil`.

**Provision access**: listen to `customer.subscription.created/updated/deleted`; check `subscription.status`; store `product.id` + `subscription.id` + `customer.id` in DB. Use entitlements to gate features.

**Minimum webhook events**:
- `checkout.session.completed` — new subscription created
- `invoice.paid` — recurring payment succeeded
- `invoice.payment_failed` — payment failed; notify customer

**Customer portal**: `stripe.billingPortal.sessions.create({ customer_account: acct_xxx })` (v2) OR `{ customer: cus_xxx }` (v1); pass `return_url`.

**Test payment methods**: BECS (900123456 / BSB 000000), Credit cards (4242/3155/9995), SEPA (AT321904300235473204).

## Related Pages

- [[stripe-subscriptions]] — concept page (updated with billing_mode, provision access pattern)
- [[source-stripe-checkout-subscriptions-quickstart]] — simpler Checkout quickstart

## Raw Sources

- [[stripe-build-subscriptions-2026]] — verbatim full integration guide (10,049 lines, 3 paths, 10 CDN images not downloaded)
