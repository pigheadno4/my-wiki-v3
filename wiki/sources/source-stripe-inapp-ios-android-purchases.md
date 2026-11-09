---
title: "Accept In-App Purchases on iOS and Android"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/mobile/digital-goods"
raw_files:
  - "stripe-inapp-ios-android-purchases-2025.md"
tags: [stripe, mobile, ios, android, digital-goods, in-app-purchases, checkout, payment-links, customer-portal]
---

## Summary

Stripe's April 22, 2026 mobile digital-goods overview is a short **US-scoped navigation page**. It says an iOS app selling digital goods, content, or subscriptions in the US **can** redirect to an external page using Stripe Checkout; it separately lists a Payment Links route. It says a US Android app **can** process directly in-app using a third-party processor such as Stripe. These are examples and links, not a rule that iOS must use Stripe-hosted Checkout, proof that Android has no restrictions, or a current app-store compliance or merchant-eligibility determination. The November 7 capture has the same substantive text; its diff changes only trailing heading whitespace. See [[stripe-inapp-payments]]. [April overview](../../raw/stripe-inapp-ios-android-purchases-2025.md#L8-L26).

## Dated US platform examples

| Platform and goods | Statement actually made by this overview | Boundary |
| --- | --- | --- |
| US iOS, digital goods/content/subscriptions | Can redirect to an external page using Stripe Checkout | Checkout is an example, not an exclusive redirect target or independently verified policy rule |
| US iOS, physical goods | Can use in-app payments | The overview links the native iOS guide; it gives no full integration steps |
| US Android, direct in-app payment | Can use a third-party processor such as Stripe | The overview does not establish the absence of other Android restrictions or the eligibility of a particular app |

The captures do not state an app-store rule version, policy jurisdiction beyond their US labels, or approval for a specific developer. [April iOS/Android statements](../../raw/stripe-inapp-ios-android-purchases-2025.md#L10-L12).

## Navigation paths

Under **Accept payments**, the overview lists three distinct routes: (1) a recommended Stripe-hosted Checkout payment page, (2) a low-code Payment Link for an in-app digital good or subscription, and (3) a custom **Android** in-app payment form. The third route is explicitly Android, so it is not evidence of a native iOS digital-goods form. Under **Manage subscriptions**, it separately links the Stripe-hosted customer portal; that route is management, not payment acceptance. The link titles alone do not specify each path's setup, wallet, fulfillment, or policy conditions. [April routes](../../raw/stripe-inapp-ios-android-purchases-2025.md#L14-L26).

The separately reviewed [[source-stripe-inapp-digital-goods-payment-links]] and [[source-stripe-inapp-digital-goods-custom-checkout]] are distinct iOS guides. Their own captured pages provide route-specific details; this overview neither specifies those details nor excludes them by listing a Checkout example. The current source previously described Checkout as the sole compliant redirect target, which exceeds its captured overview wording. [April overview routes](../../raw/stripe-inapp-ios-android-purchases-2025.md#L10-L22).

## Related Pages

- [[stripe-inapp-payments]] — main in-app payments concept
- [[stripe-checkout]] — hosted Checkout, one external iOS example in this overview
- [[source-stripe-inapp-digital-goods-checkout]] — separate Checkout implementation guide
- [[source-stripe-inapp-digital-goods-payment-links]] — separate Payment Links guide
- [[source-stripe-inapp-digital-goods-custom-checkout]] — separate merchant-owned Elements web checkout guide
- [[source-stripe-inapp-digital-goods-customer-portal]] — separate subscription management guide
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-mobile-digital-goods-2026-11-07|November 7, 2026 overview navigation capture]] — same substantive overview text; heading-whitespace change only; navigation, not additional factual provenance

## Raw Sources

- [[raw/stripe-inapp-ios-android-purchases-2025|April 22, 2026 overview capture]] — historical factual webpage content (26 lines)
