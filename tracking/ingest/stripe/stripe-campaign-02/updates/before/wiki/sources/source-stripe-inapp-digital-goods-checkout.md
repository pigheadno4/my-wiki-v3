---
title: "Accept iOS Digital Goods Payments with Stripe Checkout"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-digital-goods-checkout-2025.md"
tags: [stripe, mobile, ios, digital-goods, checkout, universal-links, storekit, webhooks, app-to-web]
---

## Summary

Full integration guide for iOS in-app digital goods using Stripe Checkout as the redirect target (app-to-web flow). Covers server setup, Products/Prices/Customers, Universal Links, opening Checkout in Safari, and webhook fulfillment.

> See also [[source-stripe-inapp-ios-android-purchases]] for the platform overview page.

## Key Integration Facts

- **`origin_context: 'mobile_app'`** on Checkout Session — opts into UI optimized for app-to-web purchases
- **Checkout opened in Safari**: `UIApplication.shared.open(url)` — not a web view or in-app browser
- **StoreKit gate**: check `SKPaymentQueue.canMakePayments()` before showing buy button (respects Parental Controls)
- **Webhook**: `checkout.session.completed` → update customer balance; Checkout auto-redirects to `success_url` 10s after successful payment if webhook not acknowledged
- **Managed Payments alternative**: Stripe's merchant-of-record solution (handles tax/disputes) — linked but separate guide

## Flow Overview

1. Customer taps "Buy" → app calls server `/create-checkout-session`
2. Server creates Customer (if not exists) + Checkout Session with `origin_context: 'mobile_app'`
3. App opens session URL in Safari via `UIApplication.shared.open(url)`
4. Customer pays in Stripe Checkout
5. Checkout redirects to `success_url` (Universal Link → deep links back to app)
6. Server receives `checkout.session.completed` webhook → grants entitlement

## Universal Links Setup

Required for redirect back into app:

1. Serve `/.well-known/apple-app-site-association` with `application/json` MIME type
2. Add Associated Domains entitlement: `applinks:example.com`
3. Create fallback page at `success_url` (in case universal link fails)
4. Handle incoming URL in app: `.onOpenURL { url in ... }`

```json
{
  "applinks": {
    "details": [{
      "appIDs": ["TEAMID.com.example.MyApp"],
      "components": [{ "/": "/checkout_redirect*" }]
    }]
  }
}
```

## Checkout Session (Node.js)

```javascript
const session = await stripe.checkout.sessions.create({
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'payment',              // or 'subscription'
  origin_context: 'mobile_app', // KEY: optimizes UI for app-to-web
  customer: customerId,
  success_url: 'https://example.com/checkout_redirect/success',
});
res.json({ url: session.url });
```

## Swift Client

```swift
Button {
    myBackend.createCheckoutSession { url in
        UIApplication.shared.open(url, options: [:], completionHandler: nil)
    }
} label: { Text("Buy 100 coins") }
.onOpenURL { url in
    if url.absoluteString.contains("success") {
        paymentComplete = true
    }
}
```

## Webhook Fulfillment

```javascript
case 'checkout.session.completed':
    const user = myUserDB.userForStripeCustomerID(session.customer);
    user.addCoinsTransaction(100, session.id);
```

## Out of Scope

- User auth (suggest Sign in with Apple / Firebase)
- Native StoreKit in-app purchases

## Test Cards

| Number | Description |
| --- | --- |
| 4242 4242 4242 4242 | Success |
| 4000 0000 0000 3220 | 3DS2 auth required |
| 4000 0000 0000 9995 | Decline (insufficient funds) |

## Universal Link Debugging

Add `?mode=developer` to Associated Domains entry → enable Associated Domains Development in Settings → check `swcutil_show.txt` in sysdiagnose for errors.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-inapp-ios-android-purchases]] — platform rules overview

## Raw Sources

- [[stripe-inapp-digital-goods-checkout-2025]] — verbatim guide (~566 lines, 2 images)
