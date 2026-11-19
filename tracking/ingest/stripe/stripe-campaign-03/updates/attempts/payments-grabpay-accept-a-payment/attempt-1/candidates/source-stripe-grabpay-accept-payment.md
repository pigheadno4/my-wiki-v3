---
title: "Stripe: Accept a GrabPay Payment"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
original_format: webpage
canonical_url: https://docs.stripe.com/payments/grabpay/accept-a-payment
raw_files:
  - "stripe-grabpay-accept-payment-2025.md"
tags: [stripe, wallets, grabpay, singapore, malaysia, checkout, ios, android, react-native, direct-api, no-minimum]
---

## Summary

[[stripe]]'s archived GrabPay acceptance guide describes five variants: Checkout, Direct API, iOS, Android, and React Native. It describes a single-use wallet redirect in which the customer authorizes at GrabPay, returns to the merchant website or app, and the merchant checks the PaymentIntent result. Its detailed rules and examples are from the 2026-05-07 capture. The 2026-11-07 capture of https://docs.stripe.com/payments/grabpay/accept-a-payment is a variant index only and does not independently establish current payment behavior. See [[stripe-wallets]].

## Dated acceptance details from the May 2026 guide

### Merchant, currency, and Checkout conditions

- The guide says subscriptions and using GrabPay for future payments were not supported at that capture. For Checkout it requires one-time line items and the same currency for every line item; split mixed currencies into separate Checkout Sessions. It pairs Singapore-based businesses and Singapore customers with SGD, and Malaysia-based businesses and Malaysia customers with MYR. These are dated guide conditions, not proof of current account eligibility.
- GrabPay is described as single-use. The Checkout guide offers dynamic payment methods or manual configuration with `grabpay` in `payment_method_types`. Its sample Sessions use `mode: "payment"`; the Stripe-hosted sample has `success_url`, while the embedded-page sample has `ui_mode: "embedded_page"` and `return_url`.
- The iOS, Android, React Native, and Direct API sections say there is no minimum GrabPay charge and the PaymentIntent `amount` value can be as low as `1` with `sgd` or `myr` currency. This is the archived API-amount wording, not a claim that the minimum is one whole SGD or MYR, and it does not establish a Checkout minimum.

### PaymentIntent and mobile clients

- The mobile and Direct API examples create a PaymentIntent on the server with an amount, `sgd` or `myr`, and `payment_method_types: ["grabpay"]`, then give the client its client secret. Intent creation or possession of the secret does not mean the payment succeeded.
- iOS uses `STPPaymentMethodGrabPayParams()` and `STPPaymentHandler.shared().confirmPayment` to present a GrabPay webview. To let the webview dismiss after authentication, the archived guide allows a **custom URL scheme or universal link** with the app delegate forwarding the URL to Stripe; its sample sets a `returnURL`. The earlier source's custom-scheme-only requirement was too narrow.
- Android collects the customer's full name in `PaymentMethod.BillingDetails`, passes that to `PaymentMethodCreateParams.createGrabPay`, and calls `PaymentLauncher.confirm`. The archived Gradle sample pins Stripe Android `23.7.0`; this is a dated sample version.
- React Native collects the customer's full name and calls `confirmPayment(clientSecret, { paymentMethodType: "GrabPay", paymentMethodData: { billingDetails } })`. Its return-flow instructions say to register a custom URL scheme, configure it, and forward URLs with `handleURLCallback`; that section explicitly says universal links are unsupported. Do not transfer that React Native restriction to native iOS.

### Direct API and outcome boundary

- The browser Direct API sample uses `stripe.confirmGrabPayPayment(clientSecret, { return_url })` to start the GrabPay redirect. The return page retrieves the PaymentIntent and displays its status; arriving at `return_url` alone is not success.
- A separate optional manual-redirect path confirms the PaymentIntent on the server with `payment_method_data: { type: "grabpay" }` and `return_url`. Its `requires_action` result contains `next_action.type: "redirect_to_url"`; the merchant then sends the browser to that URL. The redirect is an authorization step, not a succeeded charge.
- The archived test flow uses a Stripe-hosted GrabPay page with authorize or fail choices. For business actions, the guide recommends listening for `payment_intent.succeeded` through an event receiver instead of relying on the client callback. The older guide also links the applicable GrabPay SG and MY transaction limits and branding assets; those linked limits are not restated by the November index.

## November 2026 variant navigation

The canonical root capture lists Checkout, Direct API, and mobile iOS, Android, and React Native destinations. It provides no variant bodies, current merchant or customer eligibility, amount rule, SDK instructions, subscription status, or payment outcome. The root-body replacement in the diff is a navigation change; omission of the archived details is not evidence of deprecation or reversal. Review a specific variant before making a current behavior claim.

## Raw Sources

- [[raw/stripe-grabpay-accept-payment-2025|stripe-grabpay-accept-payment-2025]] — detailed GrabPay guide (1,134 lines; Checkout, iOS, Android, React Native, Direct API), fetched 2026-05-07.

## Related raw API references

- [[raw/stripe-payments-grabpay-accept-a-payment-2026-11-07|stripe-payments-grabpay-accept-a-payment-2026-11-07]] — 2026-11-07 canonical variant index only; navigation reference, not factual payment-behavior evidence.
