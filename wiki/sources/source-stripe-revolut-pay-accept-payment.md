---
title: "Stripe: Accept a Payment with Revolut Pay"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/revolut-pay/accept-a-payment"
raw_files:
  - "stripe-revolut-pay-accept-payment-2025.md"
tags: [stripe, wallets, revolut-pay, checkout, elements, direct-api, ios, android, react-native, redirect, qr-code, manual-capture]
---

## Summary

Revolut Pay is a reusable, redirect-based payment method on [[stripe]]. The 2026-05-07 acceptance guide covers Checkout, Elements, Direct API, iOS, Android, and React Native. The 2026-11-07 capture is a variant selector. It links those surfaces and lists Checkout Sessions API and Payment Intents API separately under Elements. The May capture supplies the implementation details below.

## Key Details

- **May Checkout.** Start with an existing Checkout integration and use the same currency for all line items in each Session. Stripe can present eligible methods dynamically, or the integration can list `revolut_pay` manually. The guide supports recurring subscription plans (lines 12–40).
- **May Elements and Direct API.** The merchant creates a PaymentIntent on the server. The client confirms the payment and the customer authenticates. Direct API requires a supported currency and documents an optional manual redirect from `requires_action` via `next_action.redirect_to_url` (lines 129–176, 394–425, 743–745, 830–925 and 946–953).
- **May Elements web authentication.** The mobile flow describes customer approval or decline in Revolut and a return to the integration. On desktop the customer scans a QR code, which can be refreshed up to 20 times. The authentication section gives a one-hour expiry. The failure section says decline or one hour of inaction after a `requires_action` redirect detaches the PaymentMethod and returns the PaymentIntent to `requires_payment_method` (lines 607–622 and 705–712).
- **May Elements web testing.** Its testing section describes approval and decline controls on the sandbox test page. The same section describes live-mode automatic approval after mobile redirect or desktop QR scan. Keep this testing description scoped to those May passages. The mobile authentication instructions elsewhere in the May guide describe a customer choice (lines 609–622 and 691–701).
- **May payment outcome and fulfillment.** The desktop QR paragraph mentions fulfillment after successful authentication and modal closure. The return page separately retrieves the PaymentIntent and inspects its status for display. Use Stripe's `payment_intent.succeeded` event for fulfillment and other business actions. QR modal closure, app or browser return, or a client callback alone does not establish payment success (lines 490–545, 619 and 671–675).
- **May manual capture.** With `capture_method=manual`, successful authorization moves the PaymentIntent to `requires_capture`. A separate capture request collects the authorized funds. The May Elements authorization section and the general React Native capture section describe a seven-day window and cancellation if the payment remains uncaptured. May native iOS and Android testing also state seven days after successful authorization. May React Native testing specifies ten minutes after successful authorization for an uncaptured test-mode PaymentIntent (lines 623–670, 1248–1254, 1514–1520, 1778–1787 and 1841–1849).
- **May mobile SDKs.** Each uses a backend PaymentIntent and platform-specific client confirmation and result handling. The native iOS guide allows a custom URL scheme or universal link, while the React Native iOS-only return setup specifies a custom scheme and excludes universal links. The Android overview describes a redirect into the Revolut app and the PaymentLauncher instructions describe a webview. The May capture leaves that Android interface distinction unresolved (lines 1054–1183, 1284, 1350–1450, 1618–1776).
- **May errors.** The Elements table lists `payment_intent_invalid_currency`, `missing_required_parameter`, `payment_intent_payment_attempt_failed`, and `payment_intent_redirect_confirmation_without_return_url`. The iOS, Android and React Native tables list the latter three (lines 715–722, 1266–1274, 1532–1540 and 1861–1869).

## Related Pages

- [[stripe-revolut-pay]] — payment method concept
- [[source-stripe-subscriptions-revolut-pay]] — separate Revolut Pay subscriptions guide

## Raw Sources

- [[raw/stripe-revolut-pay-accept-payment-2025|Revolut Pay acceptance guide, captured 2026-05-07]] — 1,869 lines, 15 italic fixes, one CDN image captured (`stripe-revolut-pay-checkout-visible.png`).

## Related raw API references

- [[raw/stripe-payments-revolut-pay-accept-a-payment-2026-11-07|Revolut Pay acceptance variant selector, captured 2026-11-07]] — navigation for Checkout, Elements, Direct API, iOS, Android, and React Native.
