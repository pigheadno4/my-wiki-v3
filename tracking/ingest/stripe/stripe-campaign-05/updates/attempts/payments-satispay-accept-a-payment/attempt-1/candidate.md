---
title: "Stripe: Accept a Payment with Satispay"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/satispay/accept-a-payment"
raw_files:
  - "stripe-satispay-accept-payment-2025.md"
tags: [stripe, wallets, satispay, integration, checkout, elements, direct-api, ios, android, manual-capture, accounts-v2]
---

## Summary

Stripe’s May 8, 2026 guide documents six ways to accept Satispay. The customer leaves the merchant site or app to authorize a single-use EUR payment with Satispay and then returns. Stripe describes immediate success or failure notification. The November 7, 2026 base page is a directory of integration variants.

## Key Details

**Checkout compatibility.** The May hosted Checkout and Elements with Checkout Sessions guides list European business locations, EUR presentment, payment mode, and same-currency line items. Use separate Sessions for different currencies. Setup and subscription Checkout modes are unsupported in those two paths. The May [[source-stripe-satispay|method overview]] lists Subscriptions among Dashboard products that can add Satispay and separately marks recurring payments unsupported. The Dashboard listing supplies no evidence of recurring Satispay charges.

1. **Hosted Checkout.** Stripe recommends configuring payment methods in the Dashboard. For existing manual configuration, include `satispay` in the Checkout Session’s `payment_method_types`.
2. **Elements with Checkout Sessions API.** The merchant server creates a payment-mode Checkout Session (`ui_mode: 'elements'`) and returns its client secret. The client confirms the Session through the Checkout integration.
3. **Elements with Payment Intents API.** The merchant server creates a PaymentIntent. Stripe.js confirms it on the client with the Payment Element and a `return_url`.
4. **Direct API.** Create the PaymentIntent on the server. The client calls Stripe.js `stripe.confirmPayment` with the Intent client secret, `payment_method_data.type` set to `satispay`, and a `return_url`. For the optional manual redirect, confirm on the server with `stripe.paymentIntents.confirm`, check `requires_action` and `next_action.type=redirect_to_url`, and send the customer to the supplied URL.
5. **iOS.** The Swift sample uses `STPPaymentMethodSatispayParams` and `STPPaymentHandler.confirmPayment()`. Pass the return URL at confirmation. A custom URL scheme or universal link, forwarded by the app delegate to the SDK, enables automatic WebView dismissal.
6. **Android.** The Kotlin sample uses `PaymentMethodCreateParams.createSatispay()` and `PaymentLauncher.confirm()` without specifying a custom URL scheme. The surrounding prose uses different API names. The sample’s generic future-use comment supplies no Satispay recurring support.

**Payment result and fulfillment.** On return, check the PaymentIntent status. For fulfillment, the May guide recommends listening for `payment_intent.succeeded` instead of relying on the browser or app callback.

**Customer association.** The May Elements/Payment Intents examples use `customer_account` for an Accounts v2 customer-configured Account and `customer` for a Customers v1 Customer. The Direct API and mobile sections list the country-to-EUR mappings in the raw guide.

**Manual capture.** Set `capture_method: 'manual'` on the PaymentIntent to authorize only. Successful authorization leads to `requires_capture`. A capture request captures the total by default or a lower `amount_to_capture`. Cancel intentionally if you will not capture. Stripe cancels the Intent and sends `payment_intent.canceled` if it remains uncaptured after seven days.

**Testing.** The May Elements variants describe a sandbox page for approving or declining a test payment. Live mode redirects to Satispay without the sandbox choices.

## Error Codes

| Error code | Action |
| --- | --- |
| `payment_intent_invalid_currency` | Enter a supported currency |
| `missing_required_parameter` | Check the error message for details |
| `payment_intent_payment_attempt_failed` | Inspect `last_payment_error.code` and the error message |
| `payment_intent_authentication_failure` | Inspect `last_payment_error.code`. The guide shows this for a manually triggered test failure |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming the PaymentIntent |

## Detail locators

- May guide lines 12–49 and 95–160 cover Checkout compatibility and configuration. Lines 799–934 cover PaymentIntent creation, customer association and client confirmation.
- May guide lines 1076–1158 cover fulfillment events, authorization and capture, testing and errors. Lines 1179–1195 and 1268–1378 cover Direct API actors, return flow and country mapping.
- May guide lines 1565–1642 and 1804–1857 cover iOS return handling, Android sample confirmation and mobile country mappings.

## Related

- [[stripe|Stripe]]
- [[stripe-wallets|Stripe Wallets]]
- [[source-stripe-satispay|Satispay method overview]]

## Raw Sources

- [[raw/stripe-satispay-accept-payment-2025|May 8, 2026 Satispay acceptance guide]] — full six-variant capture (1,887 lines, 16 italic fixes, one CDN image downloaded).

## Related raw API references

- [[raw/stripe-payments-satispay-accept-a-payment-2026-11-07|November 7, 2026 Satispay acceptance variant index]] — navigation to Checkout, Elements with Checkout Sessions or Payment Intents, Direct API, iOS and Android.
