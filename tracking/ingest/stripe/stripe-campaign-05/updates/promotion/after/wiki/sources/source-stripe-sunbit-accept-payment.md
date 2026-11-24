---
title: "Stripe: Accept a Payment with Sunbit"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/sunbit/accept-a-payment"
raw_files:
  - "stripe-sunbit-accept-payment-2025.md"
tags: [stripe, bnpl, sunbit, buy-now-pay-later, consumer, us, checkout, payment-intents]
---

## Summary

The 2026-05-06 full guide documents Sunbit (`sunbit`) as a single-use payment method for US businesses and USD presentment. Customers choose 3, 6, 12, or 18 installments, authorize with Sunbit, and return to the merchant’s site or app. The guide describes immediate notification of success or failure. Use the relevant Stripe event or independently verified status for fulfillment. A browser return or SDK callback serves the client flow.

## Dated integration guidance

- **Checkout.** The May guide assumes an existing Checkout integration. Checkout supports payment mode only for Sunbit, with a single currency across line items and a total of $60.00–$19,999.99 USD. This is a compatibility condition. The example uses `success_url`. The separate November [Sunbit profile](https://docs.stripe.com/payments/sunbit) retains the US/USD and amount scope.
- **Checkout Sessions API with Elements.** The May examples create a Session on the server with `ui_mode: 'elements'` and `return_url`, then use its Session-specific client secret. The guide gives separate Stripe.js and React confirmation examples.
- **Payment Intents API with Elements and Direct API.** The May guides use a server-created PaymentIntent, its client secret, and a confirmation `return_url`. Direct API also shows the optional server-driven redirect when the Intent is `requires_action` and `next_action.type` is `redirect_to_url`. The merchant can retrieve the Intent to display the outcome after return. Stripe documents `payment_intent.succeeded` for successful completion.
- **iOS and Android.** The May iOS example configures an app return URL and forwards its callback to the SDK for automatic webview dismissal. The May Android Kotlin example uses `PaymentLauncher` and a payment-result callback without an explicit `return_url` argument. Its surrounding text uses iOS-style terminology, so consult the dated sample for the Android path.
- **Test and live redirects.** The May web examples let a tester choose approval or decline on the sandbox page. The live path redirects to Sunbit.

### API version and manual capture

The May PaymentIntent REST samples use a writable `payment_method_types` array. The separate [2026-08-26.preview changelog](https://docs.stripe.com/changelog/dahlia/2026-08-26/removes-payment-method-types-parameter-from-payment-intents-setup-intents) documents removal of this input on affected PaymentIntent and SetupIntent endpoints. Checkout Session and Stripe.js Elements options have separate API scopes.

The acceptance captures supply no manual-capture rule. The May Sunbit profile says manual capture is unsupported. The 2026-11-07 Sunbit profile marks it supported, and the same-date [BNPL API matrix](https://docs.stripe.com/payments/buy-now-pay-later#api-support) marks Sunbit manual capture unsupported. Capture behavior by route, API version, and account remains unresolved. See [[source-stripe-sunbit]] for the method profile.

## Detail locators

- May raw lines 8–85 cover Checkout, eligibility and fulfillment. Lines 87–568 cover Checkout Sessions API with Elements and sandbox versus live.
- May raw lines 570–1110 cover Payment Intents API with Elements, and lines 1112–1342 cover Direct API. The dated PaymentIntent error locators include `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, and `payment_intent_redirect_confirmation_without_return_url`.
- May raw lines 1344–1613 cover iOS, and lines 1614–1839 cover Android. These preserve the dated SDK setup and confirmation examples.

## Related Pages

- [[stripe]] — Stripe company page
- [[stripe-bnpl#Sunbit Details|Stripe BNPL and Sunbit]]
- [[source-stripe-sunbit]] — Sunbit method profile

## Raw Sources

- [[raw/stripe-sunbit-accept-payment-2025|2026-05-06 full Sunbit acceptance guide]] — Checkout, Elements, Direct API, iOS and Android

## Related raw API references

- [[raw/stripe-payments-sunbit-accept-a-payment-2026-11-07|2026-11-07 Sunbit acceptance variant index]] — Checkout, Checkout Sessions API and Payment Intents API with Elements, Direct API, iOS, and Android
