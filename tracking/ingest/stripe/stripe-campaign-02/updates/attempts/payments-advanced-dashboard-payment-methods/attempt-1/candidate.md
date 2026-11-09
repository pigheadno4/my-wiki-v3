---
title: "Migrate Payment Methods to the Dashboard"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/payments/advanced/dashboard-payment-methods
raw_files:
  - "stripe-migrate-payment-methods-dashboard-2025.md"
tags: [stripe, payment-methods, dashboard, dynamic-payment-methods, payment-intents, checkout-sessions, delayed-notification, apple-pay, google-pay, webhooks, testing]
---

## Summary

The April 21, 2026 capture contains separate Checkout Sessions (embedded-components) and Payment Intents (Elements) migration guides under this URL. Both describe moving existing integrations from explicit `payment_method_types` to Dashboard-managed payment-method preferences, with distinct webhook event families. The November 7, 2026 capture is a variant index linking those two paths; it does not contain their current instructions. The older guide below is retained as dated guidance, not verified November behavior or evidence of deprecation.

> See also [[source-stripe-checkout-dashboard-payment-methods]] for the separately captured Checkout Sessions guide.

## Migration in the April 21 Guide

- **Checkout Sessions path**: remove `payment_method_types` from existing Checkout Session creation to use Dashboard preferences. The guide says currency, customer location, and payment-method restrictions affect which compatible methods appear; non-default methods such as bank redirects are initially disabled on upgrade and must be enabled in Dashboard if previously added to the integration.
- **Payment Intents path**: separately remove `payment_method_types` from existing PaymentIntent creation for Dashboard preferences with Elements. Its guide likewise says non-default methods are initially disabled on upgrade and need Dashboard re-enablement. Currency and method restrictions influence the compatible methods shown.
- Dashboard settings allow enabling or disabling individual methods; some require **Set up** or **Review terms** rather than simply **Turn on**. The April examples describe popular methods shown prominently and others in an overflow menu. These are descriptions of those captured variants, not claims that every method is available for every integration.

## Wallet Examples in the April 21 Guide

The captured examples say Apple Pay is enabled and Google Pay is disabled by default in the described setup. They also say Google Pay might be hidden even when enabled, including when automatic tax is enabled without collecting a shipping address. Treat these as dated examples subject to the integration and payment-method conditions in the guide.

## Delayed Notification and Fulfillment

The April Checkout Sessions variant marks its delayed-notification step as required **only if the integration plans to use** one of these listed methods: Bacs Direct Debit, bank transfers, Boleto, Canadian pre-authorized debits, Konbini, OXXO, Pay by Bank, SEPA Direct Debit, or ACH Direct Debit. It says an integration using webhooks to fulfill orders automatically **might need** an update when adding its first method with delayed notifications. This is not a blanket webhook migration requirement for every integration.

For delayed methods, the older guide notes funds are not immediately available and recommends waiting before fulfillment. Payment authorization, payment success, and funds becoming available in an account are distinct states; the event table describes payment success, not settlement or balance availability. Its sample checks `session.payment_status === "paid"` before fulfilling on `checkout.session.completed`; a delayed payment can be `unpaid` at completion and later produce an async success or failure event.

### Checkout Sessions events in the April guide

| Event | Described meaning | Guide's example action |
| --- | --- | --- |
| `checkout.session.completed` | Customer submitted the form and authorized a debit; delayed payment may still be unpaid | Create the order; fulfill at this point only when `payment_status === "paid"` |
| `checkout.session.async_payment_succeeded` | Customer payment succeeded | Fulfill the purchase |
| `checkout.session.async_payment_failed` | Payment declined or otherwise failed | Handle failure; the sample emails the customer to place a new order |

### Payment Intents events in the April guide

The separate Payment Intents variant recommends listening for `payment_intent.succeeded` to handle successful payments. For methods with delayed notifications, it also recommends `payment_intent.payment_failed` to handle failure after initial confirmation. Its sample fulfills on success and handles failure separately. These are PaymentIntent events, not Checkout Session events.

## Test Examples in the April Guide

These values and outcomes are **test-mode scenarios from the captured guide**, not production guarantees.

| Test value | Captured scenario |
| --- | --- |
| Card `4242424242424242` | Successful payment without authentication |
| Card `4000002500003155` | Authentication required |
| Card `4000000000009995` | Decline such as `insufficient_funds` |
| Card `6205500000000000004` | UnionPay variable-length card-number example |
| BECS `900123456`, BSB `000000` | Sample success after `processing`; `111111113` is a failure example |
| SEPA `AT321904300235473204` | Sample success after `processing`; `AT861904300235473202` is a failure example |

The captured table also describes redirect test-page success and failure choices for Alipay, Bancontact, EPS, iDEAL, Przelewy24, and Pay by Bank; BLIK email patterns for failure simulation; and Boleto/OXXO voucher flows. The example delay of about three minutes for BECS and SEPA is a test scenario, not a production timing promise.

## Related Pages

- [[source-stripe-checkout-dashboard-payment-methods]] — separately captured Checkout Sessions path
- [[stripe-checkout]] — Checkout concept
- [[stripe-payment-intents]] — Payment Intents concept

## Related raw API references

- [[stripe-payments-advanced-dashboard-payment-methods-2026-11-07]] — November 7 variant index with Checkout Sessions and Payment Intents links; the linked variant bodies were not captured in this update

## Raw Sources

- [[stripe-migrate-payment-methods-dashboard-2025]] — April 21 capture of the two detailed variant bodies
