---
title: "Stripe: Set Up Future Cash App Pay Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
original_format: webpage
canonical_url: https://docs.stripe.com/payments/cash-app-pay/set-up-payment
raw_files:
  - "stripe-cash-app-pay-set-up-payment-2025.md"
tags: [stripe, wallets, cash-app-pay, setup-intent, recurring, off-session, mandate, cashtag, ios, android]
---

## Summary

[[stripe]]'s 2026-05-07 detailed guide describes four Cash App Pay setup variants: Checkout, Direct API, iOS, and Android. The Checkout setup-mode Session and Direct API SetupIntent save a Customer-associated PaymentMethod for later use without an immediate charge. The Direct API PaymentIntent path instead charges at checkout while saving the method with `setup_future_usage`. Any subsequent charge of a saved method uses a new PaymentIntent; customer authorization and a successful setup or payment remain separate outcomes. The 2026-11-07 capture of https://docs.stripe.com/payments/cash-app-pay/set-up-payment is only a four-variant index and does not verify the current bodies of those routes. See [[stripe-wallets]].

## Dated setup details from the May 2026 guide

### Customer identity and Checkout

- The May guide says to create or retrieve a Customer and associate its ID with the merchant's own customer record before saving a Cash App Pay PaymentMethod for reuse. Its opening note conditionally recommends customer-configured Accounts v2 objects for most use cases, while saying Accounts v2 was generally available for Connect users and in preview for others; that dated note does not override the Customer-based examples here.
- The Checkout example creates a server-side Session with `mode: "setup"`, `customer: customer.id`, `success_url`, and `payment_method_types: ["card", "cashapp"]`, then redirects to the returned Session URL for customer authorization. The prior source's one-type list omitted `card` from this example. The example does not prove the list is mandatory for every Checkout configuration.
- The May Checkout testing section distinguishes a sandbox approval/decline page from the live Cash App redirect or QR scan, which it describes as automatically approved. That is a dated description of the authorization experience, not evidence of a successful future charge.

### Direct API: save, authenticate, and charge later

- The Direct API route distinguishes a SetupIntent to save details before the amount or date is known from a PaymentIntent that charges at checkout and saves the method with `setup_future_usage`. The May SetupIntent example uses `payment_method_types: ["cashapp"]`, a Customer ID and `usage: "off_session"` (the prose also allows `on_session`). The PaymentIntent example uses `confirm: true`, `setup_future_usage: "off_session"`, `return_url`, the Customer ID, an amount and USD currency. These are route-specific examples, not proof that every value is universally required.
- A custom form must present written authorization before confirming the SetupIntent or PaymentIntent for future off-session use. The guide says to show it the first time the customer's $Cashtag is saved and gives recommended wording; do not turn the example brand text into a required literal.
- In the **browser Direct API** flow, `stripe.confirmCashappSetup(clientSecret, { payment_method: { type: "cashapp" }, return_url })` confirms the SetupIntent. On mobile, Cash App authorization redirects back to the SetupIntent's `return_url` with setup and redirect parameters. On desktop, the customer scans a QR code. This Stripe.js method is not the Checkout, iOS, or Android confirmation method.
- The May guide says the authentication session expires after 10 minutes; the desktop QR code can be refreshed up to 20 times before the SetupIntent returns to the guide's `require_payment_method` wording and the process restarts. In manual action handling, a `requires_action` SetupIntent exposes `next_action.cashapp_handle_redirect_or_display_qr_code`: mobile `mobile_auth_url`, desktop QR image URLs and expiry, and `hosted_instructions_url`. The mobile URL expires after 30 seconds; if missed, `stripe.retrieveSetupIntent` obtains a new URL. The May manual sample inconsistently checks `result.paymentIntent.status` while reading `result.setupIntent.next_action`; use the prose and object-specific state boundary rather than that mixed-object condition as a recipe.
- After successful in-app authentication, the guide says the SetupIntent moves to `succeeded` and yields a reusable PaymentMethod ID. A later PaymentIntent uses that same PaymentMethod with the Customer and `off_session: true` when the customer is outside checkout. A created intent, `requires_action`, QR display, or redirect is not a successful setup or later payment.

### Mobile SDKs and revocation

- The dated iOS path creates a Customer-linked SetupIntent, constructs `STPPaymentMethodCashAppParams()`, and calls `STPPaymentHandler.shared().confirmSetupIntent` with a return URL. The dated Android path uses `PaymentMethodCreateParams.createCashAppPay()`, `ConfirmSetupIntentParams`, and `PaymentLauncher.confirm`; its Gradle sample specifies Stripe Android `23.7.0`, a historical sample version. Android's captured variant says “Available in: US.”
- For revocation in the May guide, Cash App deactivation sends `mandate.updated`; the merchant subscribes and detaches the PaymentMethod. A merchant UI can also trigger detach. After either detach call, `payment_method.detached` is sent. These event and detach claims are not reverified by the November index.

## November 2026 variant navigation

The 2026-11-07 canonical root capture names Checkout, Direct API, iOS, and Android variants. It has no variant body, request fields, mandate rules, authentication windows, revocation instructions, or success states. Its replacement of the detailed combined guide is a navigation change in this capture, not proof those features were removed or changed. Fetch a specific variant before making a current behavior claim.

## Raw Sources

- [[raw/stripe-cash-app-pay-set-up-payment-2025|stripe-cash-app-pay-set-up-payment-2025]] — detailed combined guide (850 lines; Checkout, Direct API, iOS, Android), fetched 2026-05-07.

## Related raw API references

- [[raw/stripe-payments-cash-app-pay-set-up-payment-2026-11-07|stripe-payments-cash-app-pay-set-up-payment-2026-11-07]] — 2026-11-07 canonical variant index only; navigation reference, not payment-behavior evidence.
