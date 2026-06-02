---
title: "Accept In-App Purchases on iOS and Android"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-ios-android-purchases-2025.md"
tags: [stripe, mobile, ios, android, digital-goods, in-app-purchases, checkout, payment-links, customer-portal]
---

## Summary

Navigation/overview page covering the platform rules and integration paths for in-app purchases on iOS and Android. Key policy: iOS digital goods must redirect to Stripe Checkout; Android can go fully in-app.

## Platform Rules (US)

| Platform | Digital goods/subscriptions | Physical goods |
| --- | --- | --- |
| **iOS** | Must redirect to Stripe Checkout (external page) | Can use in-app SDK directly |
| **Android** | Can process directly in-app with Stripe | Can use in-app SDK directly |

## Integration Paths

### Accept payments
1. **Prebuilt payment page (Recommended)** — Stripe Checkout hosted page (`mobile/digital-goods/checkout`)
2. **Payment Links (low-code)** — create a Payment Link for the digital good/subscription
3. **Custom in-app flow** — in-app payments SDK directly in Android app

### Manage subscriptions
- **Customer portal** — Stripe-hosted subscription management page

## Key Insight

iOS App Store rules require external payment for digital goods in US apps. Stripe Checkout is the compliant redirect target. Android has no equivalent restriction — Stripe in-app SDK can handle digital goods directly.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-checkout]] — Stripe Checkout (the redirect target for iOS digital goods)

## Raw Sources

- [[stripe-inapp-ios-android-purchases-2025]] — verbatim navigation page (26 lines)
