---
title: "Stripe: Set Up Future PayPal Payments"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/paypal/set-up-future-payments"
raw_files:
  - "stripe-paypal-set-up-future-payments-2025.md"
tags: [stripe, wallets, paypal, recurring, setup-intent, off-session, mandate, billing-agreement, fraudnet, accounts-v2]
---

## Summary

The 2026-05-07 [[stripe]] guide explains how to save PayPal payment details for future charges using Checkout, Direct API, iOS or Android. The 2026-11-07 capture links the same four implementation variants. The details below describe the May guide.

## Enable recurring payments and authorize setup

- **Enablement.** May says Stripe automatically enables recurring payments at PayPal activation for most users. PayPal policies, regional restrictions or an account configured before automatic enablement can require manual enablement under **Payment methods → PayPal → Recurring payments**. The Dashboard then shows pending and access usually takes up to five business days. Recurring payments are enabled by default in testing environments (lines 18–29).
- **Checkout.** Create a Checkout Session in `mode: 'setup'` for a Customer, with PayPal in the sample's `payment_method_types`. Use `checkout.session.completed` or verified server-side Session retrieval on return to read `setup_intent` and retrieve its `payment_method` ID. The Session example uses `success_url`. Returning to that URL alone does not verify authorization or payment (lines 49–183).
- **Direct API.** Create a PayPal SetupIntent on the server and pass its client secret to the client. The May examples identify an Accounts v2 customer-configured Account with `customer_account` or a Customers v1 Customer with `customer`. The guide describes Accounts v2 as generally available to Connect users and in public preview for other users, with a preview version required for participants. Stripe.js `confirmPayPalSetup` uses `return_url` and shows online acceptance with `infer_from_client: true`. The buyer approves the PayPal billing agreement (lines 8–14 and 285–375).
- **Direct API manual redirect.** Create and confirm the SetupIntent with `confirm: true`, `mandate_data` and a required `return_url`. The example uses the customer's IP address and user agent for online acceptance. From a SetupIntent in `requires_action` with `next_action.type = redirect_to_url`, redirect to its `next_action.redirect_to_url.url`. The dated example repeats `next_action` and names its redirect variable `paymentIntent`; the surrounding instructions identify the object as a SetupIntent (lines 505–586).
- **Mobile SDKs.** The May iOS sample uses `STPPaymentHandler.confirmSetupIntent` with PayPal method parameters and a return URL. The Android sample uses `PaymentLauncher.confirm` with `ConfirmSetupIntentParams`. Both use a backend SetupIntent (lines 652–733 and 929–1018).
- **Verify the outcome.** Successful billing agreement authorization produces `setup_intent.succeeded`. Failed authorization produces `setup_intent.setup_failed` and returns the SetupIntent to `requires_payment_method`. Use the setup events to verify the billing agreement rather than relying on the buyer returning. Setup and the later PaymentIntent are distinct (lines 181–189, 384–386, 731–733 and 1016–1018).

## PaymentMethod, Mandate and later charges

- **Field locations.** The May Direct API prose locates `payer_id` and `billing_agreement_id` (BAID) in the resulting Mandate's PayPal `payment_method_details`. It locates buyer `payer_email` and `payer_id` on `PaymentMethod.paypal`. The nearby field table defines the labels without assigning them all to the Mandate (lines 376–382).
- **Off-session.** The May examples create a separate PaymentIntent with the saved PaymentMethod ID, Customer ID, `off_session: true` and `confirm: true`. The request errors if authentication is required. The separate save-while-charging option uses `setup_future_usage: 'off_session'` on a PaymentIntent (lines 192–228, 388–425 and 487–503).
- **On-session.** The May Direct API client flow uses `confirmPayPalPayment`. It allows omission of `return_url` when the PayPal PaymentMethod was previously set up via a SetupIntent or a PaymentIntent with `setup_future_usage`. A return URL is required in other cases, including a newly created PayPal PaymentMethod (lines 427–480).
- **Risk libraries.** Stripe.js includes Fraudnet for on-session use. For manual server-side confirmation with a saved PayPal method, the May guide uses Fraudnet on web or Magnes on mobile and passes the Client Metadata ID in `payment_method_options.paypal.risk_correlation_id`. Without it the guide describes `paypal_risk_correlation_id_missing` (lines 588–616, 797–825 and 1082–1110).
- **Revocation and detach.** Customer cancellation of the billing agreement in PayPal produces `mandate.updated`. Later PaymentIntents using the saved method fail until it is replaced by a method with an active mandate. For subscription collection, the resulting status follows the configured automatic collection settings. Merchant detachment revokes the Stripe mandate and calls PayPal to cancel the agreement (lines 230–237, 482–484 and 618–630).

## Related Pages

- [[stripe-wallets]] — Stripe wallet integrations
- [[stripe-paypal]] — PayPal integration and separate subscription guidance

## Raw Sources

- [[raw/stripe-paypal-set-up-future-payments-2025|Set up future PayPal payments, captured 2026-05-07]] — full 1,124-line guide with 18 italic formatting fixes.

## Related raw API references

- [[raw/stripe-payments-paypal-set-up-future-payments-2026-11-07|Future PayPal payments variant selector, captured 2026-11-07]] — navigation for Checkout, Direct API, iOS, and Android.
