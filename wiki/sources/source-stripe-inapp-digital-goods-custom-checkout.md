---
title: "Accept iOS Digital Goods Payments with Custom Checkout (Elements)"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-digital-goods-custom-checkout-2025.md"
tags: [stripe, mobile, ios, digital-goods, payment-element, elements, subscriptions, universal-links, webhooks, default-incomplete]
---

## Summary

Most custom iOS digital goods path — own checkout page using Payment Element. Server-required. Focused on subscriptions (vs Checkout guide which covers one-time + subscriptions). Open own web URL in Safari; Universal Links redirect back to app.

> See also [[source-stripe-inapp-digital-goods-checkout]] (Checkout hosted page) and [[source-stripe-inapp-digital-goods-payment-links]] (no-server Payment Links path).

## Three iOS Digital Goods Paths

| Path | Server | Dynamic | Attach Customer | Notes |
| --- | --- | --- | --- | --- |
| Payment Links | No | No | No | Limited products only |
| Checkout | Yes | Yes | Yes | `origin_context: mobile_app` |
| Elements (this) | Yes | Yes | Yes | Own checkout UI; subscription-focused |

## Apple Pay Geography

US + EEA only for digital goods. Appears automatically in Payment Element when customer has a saved card in Wallet.

## Key Server Patterns

```javascript
// 1. Create Customer (if not exists) — store stripeCustomerID mapping

// 2. Create Subscription with default_incomplete
const subscription = await stripe.subscriptions.create({
  customer: customerId,
  items: [{ price: priceId }],
  payment_behavior: 'default_incomplete',   // KEY: creates in incomplete status
  expand: ['latest_invoice.payment_intent'], // KEY: get client_secret
});

// Store subscription.id in DB for future cancellation/upgrade/downgrade
const clientSecret = subscription.latest_invoice.payment_intent.client_secret;
res.json({ subscriptionId: subscription.id, clientSecret });
```

## Key Client Pattern (Swift)

```swift
// Open own checkout URL in Safari (not Stripe-hosted)
UIApplication.shared.open("https://example.com/checkout")

// Handle universal link return
.onOpenURL { url in
    if url.absoluteString.contains("success") { paymentComplete = true }
}
```

## Payment Element confirm (web side)

```javascript
stripe.confirmPayment({
  elements,
  confirmParams: {
    return_url: 'https://example.com/checkout_redirect/success', // universal link
  },
})
```

## Webhook Events (Subscription)

Different from one-time Checkout path (`checkout.session.completed`):

- `invoice.payment_succeeded` → grant/renew subscription
- `invoice.payment_failed` → notify user to update payment method
- `customer.subscription.updated` → handle pause/cancel/upgrade

## Accounts v2 Note

If using customer-configured Accounts (Accounts v2), replace `Customer` object references and event references with Accounts v2 API equivalents.

## Universal Links Setup

Same as other iOS digital goods paths:
1. Serve `/.well-known/apple-app-site-association` with `application/json` MIME type
2. Add Associated Domains entitlement: `applinks:example.com`
3. Fallback pages at both `success` and `cancel` URLs (both needed for Elements path)

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-subscriptions]] — Stripe subscriptions concept page
- [[source-stripe-inapp-digital-goods-checkout]] — Checkout (hosted) path
- [[source-stripe-inapp-digital-goods-payment-links]] — Payment Links (no-server) path

## Raw Sources

- [[stripe-inapp-digital-goods-custom-checkout-2025]] — verbatim guide (~402 lines)
