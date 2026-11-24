---
title: "Stripe Payment Records API"
type: source
date_ingested: 2026-04-19
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/payment-records"
raw_files:
  - "stripe-payments-payment-records-2026-11-07.md"
  - "stripe-payment-records-api-2025.md"
tags: [stripe, payment-records, orchestration, multi-processor, off-stripe, reconciliation]
---

## Summary

The April 19 and November 7, 2026 guides describe a unified ledger for on-Stripe and external payments. The combined [[stripe-orchestration|Orchestration]] example says Stripe automatically creates a PaymentRecord for each on-Stripe PaymentIntent and the merchant reports external payments. Orchestration is the condition for that automation example. The guide separately describes Checkout entries for Stripe's custom PayPal adapter.

Payment Records support tracking multi-capture and third-party and partner-initiated payments, including Stripe-instructed card transactions. The guide names Subscriptions smart retries, out-of-band Invoice payments and Radar as related uses.

## Three-level history

- **PaymentRecord** tracks a payment across attempts and outcomes. `latest_payment_attempt_record` points to the most recent attempt.
- **PaymentAttemptRecord** represents an individual processing attempt. One PaymentRecord may have several.
- **PaymentAttemptRecordEntry** records an individual event in an append-only attempt log. Entries are limited to preview users in both captures. April illustrates `initiated`, `authenticated`, `authorized` and `guaranteed`. The November diagram illustrates declined attempts and a subsequent successful retry. These are examples of event histories, with ordering depending on the attempt. A guaranteed outcome or amount records the reported payment state.

## Report payment activity

| Operation | Documented use |
| --- | --- |
| `reportPayment` | Record an external payment with amount, method, processor and timestamps. Stripe creates the first associated attempt. The examples use `outcome=guaranteed` and `processor_details.type=custom`. |
| `reportPaymentAttemptFailed` | Report the failure time against the existing PaymentRecord ID. |
| `reportPaymentAttempt` | Report a new attempt on the same PaymentRecord with the same or a different method or processor. |
| `reportRefund` | Record a previously processed full or partial refund. Omit `amount` to report the entire guaranteed amount. Report multiple partial refunds until the full amount has been reported. |

The refund operation updates the payment history. The separate November Orchestration overview says third-party processors administer refunds for payments routed to them. Record outcomes and guaranteed amounts do not establish settlement.

## Retrieve records, attempts and entries

- Retrieve a PaymentRecord by its own ID, which is returned in the orchestrated PaymentIntent response. For historical payments, the guide also documents lookup by PaymentIntent ID.
- Retrieve the latest PaymentAttemptRecord using the ID under `latest_payment_attempt_record`. For historical payments using the Charges API, use the Charge ID to retrieve the PaymentAttemptRecord. To list all attempts, filter by PaymentRecord ID.
- For preview access, list PaymentAttemptRecordEntries by PaymentAttemptRecord ID. Stripe describes a webhook with the entry object each time an entry is created, for example `payment_attempt_record_entry.initiated`. The Dashboard is another viewing route.

## November custom PayPal Checkout entry outcomes

This preview entry guidance applies to Checkout Sessions using a custom payment method through Stripe's merchant-hosted PayPal adapter. Find the entries through the Checkout Session's `payment_record`.

| Customer or processor action | Entry outcome |
| --- | --- |
| Customer abandons Checkout before entering PayPal or leaves the Session until it expires | `canceled`. Stripe waits for an open Session to expire before treating it as abandoned. |
| Customer enters PayPal and returns to Checkout without approving | `failed` with `failure_details.code=payment_method_customer_decline`. |
| Customer attempts payment and PayPal declines | `failed` with `failure_details.code=payment_method_provider_decline`, regardless of the PayPal reason. |

The [custom PayPal adapter guide](https://docs.stripe.com/payments/payment-methods/custom-payment-methods/paypal) separately describes access during its preview and the merchant-hosted adapter. The above entry classifications describe that integration.

## Detail locators

| Topic | April raw lines | November raw lines |
| --- | --- | --- |
| PaymentIntent relationship, hierarchy and examples | 16–46 | 17–133 |
| Report payment, attempt, retry and refund | 48–143 | 135–187 |
| Retrieve PaymentRecord and attempts | 145–195 | 189–230 |
| Entry preview and list examples | 216–265 | 251–310 |
| Custom PayPal Checkout outcomes | — | 255–263 |

## Related Pages

- [[stripe]] — Stripe company page
- [[stripe-orchestration]] — Stripe Orchestration concept and Payment Records routes
- [[source-stripe-orchestration]] — Separate overview and processor responsibilities
- [[source-stripe-payment-intents]] — PaymentIntents lifecycle
- [[source-stripe-paypal]] — Standard Stripe PayPal payment method
- [[payment-reconciliation-reporting]] — Generic reconciliation concept

## Raw Sources

- [[raw/stripe-payments-payment-records-2026-11-07|November 7, 2026 full Payment Records guide]]
- [[raw/stripe-payment-records-api-2025|April 19, 2026 full Payment Records guide]]
