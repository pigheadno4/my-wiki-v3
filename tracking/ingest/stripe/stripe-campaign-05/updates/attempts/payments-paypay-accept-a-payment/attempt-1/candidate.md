---
title: "Stripe: Accept a Payment with PayPay"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/paypay/accept-a-payment"
raw_files:
  - "stripe-paypay-accept-payment-2025.md"
tags: [stripe, wallets, paypay, japan, jpy, checkout, elements, direct-api, ios, android, redirect]
---

## Summary

The May 7, 2026 guide describes PayPay as single-use. The customer authorizes with PayPay after a website or app redirect and then returns to the merchant's website or app. Hosted Checkout and Elements with the Checkout Sessions API list Japan businesses and JPY presentment, require `payment` mode with one currency per Session and exclude `setup` and `subscription` modes. The May Direct API, iOS and Android branches also map JPY to Japan.

## Integration paths in the May guide

| Surface | Documented flow and return handling | May raw lines |
| --- | --- | --- |
| Hosted Checkout | Build on an existing Checkout integration. The guide recommends Dashboard payment-method management and illustrates manual PayPay selection and `success_url` on a Checkout Session. | 8–84 |
| Elements with Checkout Sessions API | The merchant server creates a Checkout Session and supplies its client secret. Dashboard and manual methods are illustrated. Checkout Elements confirms on the client, and the examples set the Session's `return_url`. | 86–567 |
| Elements with Payment Intents API | The merchant server sets the amount and currency on a PaymentIntent and supplies its client secret. The client calls `stripe.confirmPayment` with `return_url`. The server examples attach an Accounts v2 `customer_account` or a Customers v1 `customer` as applicable. | 569–1109 |
| Direct API | The merchant server creates a PaymentIntent. Stripe.js can handle confirmation with `return_url`. For manual server confirmation, look for `requires_action` and redirect the customer to `next_action.redirect_to_url.url`, then verify the PaymentIntent status after return. | 1111–1341 |
| iOS | The server provides a PaymentIntent client secret. The iOS SDK presents a PayPay webview. For automatic dismissal, configure a custom URL scheme or universal link, forward it to Stripe and set the return URL on `STPPaymentHandler.confirmPayment`. | 1343–1611 |
| Android | The Kotlin example creates PayPay parameters and uses `ConfirmPaymentIntentParams` and `PaymentLauncher.confirm` with a result callback. It shows no explicit return URL. The prose names `STPPaymentIntentParams` and `PaymentHandler.confirmPayment`, which conflict with the Kotlin example. | 1613–1838 |

Generic customer-attachment and Android mandate comments do not establish PayPay reuse. Browser return and client callbacks are separate from the verified payment outcome. The May PaymentIntent branches recommend using Stripe's `payment_intent.succeeded` event for fulfillment and other completion-driven actions.

## Testing and common errors

The two web Elements branches describe an approve/decline test page in a sandbox. The live redirect goes to PayPay without those simulation controls. The May hosted Checkout test instructions say to select PayPay and click Pay.

The May Payment Intents Elements, Direct API and Android branches list these common PaymentIntent errors (May raw 1099–1109, 1331–1341 and 1828–1838).

| Error code | Issue |
| --- | --- |
| `payment_intent_invalid_currency` | Unsupported currency |
| `missing_required_parameter` | Required parameter missing |
| `payment_intent_payment_attempt_failed` | See error message for failure details |
| `payment_intent_authentication_failure` | Authentication failure, including a manually triggered test failure |
| `payment_intent_redirect_confirmation_without_return_url` | Supply `return_url` when confirming the PaymentIntent |

## Related

- [[stripe-wallets]] — PayPay acceptance and wallet context
- [[source-stripe-paypay]] — Separate PayPay product overview
- [[stripe]] — Stripe company page

## Related raw API references

- [[raw/stripe-payments-paypay-accept-a-payment-2026-11-07|November 7, 2026 variant selector]] — Navigation for Checkout, both Elements APIs, Direct API, iOS and Android. Implementation detail above comes from the May full guide.

## Raw Sources

- [[raw/stripe-paypay-accept-payment-2025|May 7, 2026 full acceptance guide]] — 1,838 lines across the six integration surfaces.
