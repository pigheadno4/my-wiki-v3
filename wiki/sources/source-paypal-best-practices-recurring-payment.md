---
title: "Pay with PayPal for Recurring Payments: Best Practices"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-best-practices-recurring-payment.md"
tags: [paypal, checkout, best-practices, recurring-payments, subscriptions, vault, webhooks, shipping-module, saas]
---

## Pay with PayPal for Recurring Payments: Best Practices

Official PayPal guide on best practices for recurring payment flows — integration patterns, review page setup, physical goods handling, and webhook-based subscription lifecycle management.

Source URL: <https://developer.paypal.com/docs/checkout/standard/best-practices/recurring/>

Last updated: 2025-08-12

## Key Takeaways

### Two integration patterns

| Pattern | Description | When to use |
| ------- | ----------- | ----------- |
| **Setup without purchase** | Save payment method before any charge | Free trials, postpaid services, no immediate payment needed |
| **Save during purchase** | Process payment + save method in one step via Orders v2 API | Subscriptions where first charge happens at sign-up |

> **Important**: Do NOT use standalone Payment Method or Token APIs for the "save during purchase" pattern — use Orders v2 API only.

### Two customer flows (both patterns support both)

- **Pay Now** — collect payment and save method in one step
- **Setup Now** — save method for future use, no immediate charge

### PayPal review page best practices

- Show **plan information and a recurring indicator** on the order card — transparency before the buyer accepts terms reduces disputes
- Pass the buyer's email in the Create Order call (Pass buyer identifier) to prefill the PayPal login page

### Physical goods recurring payments

- Integrate **Shipping module** to capture shipping address at first purchase
- Show **delivery estimates upfront**

### Digital goods recurring payments

- Pass the correct address and delivery context to match your fulfilment process (even for digital goods)

### Subscription lifecycle (server-side)

- Set up **server-side webhooks or callbacks** for real-time subscription status updates:
  - Failed payments
  - Expired payment methods
  - Cancellations
- Sync billing events with your system to manage: access control, fulfilment, customer communication
- Use automated retries or grace periods for failed payments

## Comparison to one-time payment best practices

The recurring flow omits upstream button placement (cart/PDP shortcuts) — the guide targets digital service providers where buyers typically have an existing account. The focus shifts from button placement to review page transparency and post-purchase lifecycle management.

## Images

- `raw/assets/paypal-best-practices-recurring-subscription.png` — 3-screen end-to-end subscription sign-up flow (shared with overview page)
- `raw/assets/paypal-best-practices-recurring-implementation.png` — example recurring payments review page implementation

## Raw Sources

- [[paypal-best-practices-recurring-payment]] — verbatim webpage content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[paypal-vault]] — PayPal Vault / Payment Method Tokens concept
- [[recurring-payments]] — Recurring payments concept
- [[source-paypal-best-practices-pay-with-paypal]] — parent best practices overview page
- [[source-paypal-checkout-recurring-payment]] — technical integration guide for recurring payments
