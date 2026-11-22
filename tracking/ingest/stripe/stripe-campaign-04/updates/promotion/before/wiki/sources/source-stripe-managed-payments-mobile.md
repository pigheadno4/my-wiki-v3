---
title: "iOS Digital Products with Managed Payments (MoR)"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-managed-payments-mobile-2025.md"
tags: [stripe, managed-payments, merchant-of-record, mobile, ios, digital-goods, checkout, universal-links, origin-context]
---

## Summary

iOS app-to-web digital goods integration using **both** Managed Payments (Stripe as MoR) **and** `origin_context: 'mobile_app'`. This is the MoR-compliant alternative to [[source-stripe-inapp-digital-goods-checkout]] (which uses regular Checkout without MoR). Available only in countries that allow iOS external payment links.

## Key Checkout Session Params

```javascript
stripe.checkout.sessions.create({
    line_items: [{ price: priceId, quantity: 1 }],
    managed_payments: { enabled: true },    // Stripe as MoR
    origin_context: 'mobile_app',           // mobile-optimized UI
    mode: 'payment',                        // or 'subscription'
    customer: customerId,
    success_url: 'https://example.com/checkout_redirect/success',
})
```

Both params required together for this use case.

## Decision Tree: Which iOS digital goods guide to use?

| Situation | Guide |
| --- | --- |
| Managed Payments eligible product + supported country | This source (MoR, Stripe handles tax/fraud/disputes) |
| Digital goods, but not Managed Payments eligible | [[source-stripe-inapp-digital-goods-checkout]] (non-MoR, origin_context only) |
| Physical goods | In-app payments SDK (no web redirect) |

## Flow (Same as Non-MoR App-to-Web)

1. `SKPaymentQueue.canMakePayments()` check
2. App calls server → server creates Checkout Session with `managed_payments.enabled + origin_context: mobile_app`
3. App opens session URL in Safari: `UIApplication.shared.open(url)`
4. Customer pays via Managed Payments Checkout (Link as MoR)
5. Universal Link redirects back to app
6. Server receives `checkout.session.completed` → grant entitlement

## Tax Example

Dashboard product creation example uses `txcd_10201000` (Video Games - downloaded - non subscription - with permanent rights) as the tax code.

## Universal Links + Testing

Same setup as other iOS guides: `apple-app-site-association`, Associated Domains, fallback page, sysdiagnose debugging.
Link test passcode: `000000`.

## Related Pages

- [[stripe-managed-payments]] — Managed Payments concept page
- [[stripe-inapp-payments]] — In-App Payments concept page
- [[source-stripe-inapp-digital-goods-checkout]] — same iOS app-to-web flow without Managed Payments
- [[source-stripe-managed-payments-setup]] — full Managed Payments Checkout setup guide

## Raw Sources

- [[stripe-managed-payments-mobile-2025]] — verbatim guide (~581 lines, 2 images)
