---
title: "Stripe Payment Methods API"
type: source
date_ingested: 2026-04-19
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/payment-methods
raw_files:
  - "stripe-payments-payment-methods-2026-11-07.md"
  - "stripe-payment-methods-api-2025.md"
tags: [stripe, payment-methods, webhooks, ach, sepa, bank-debit, customer-actions]
---

## Summary

The April 19 and November 7, 2026 [[stripe]] Payment Methods API guides describe instrument details, customer actions, immediate and delayed outcomes, reusable and single-use methods, and server-side status tracking. Use a PaymentMethod with a PaymentIntent to take payment, or with a SetupIntent and Customer to save payment details for later.

## PaymentMethod and customer actions

A PaymentMethod contains instrument and billing details, including the `type` and matching type-specific hash. The payment amount and currency belong to the payment. Stripe recommends creating PaymentMethods with Stripe.js to handle sensitive payment data and customer actions. The Dashboard enables methods available to the account. Both captures say activation is generally immediate without additional contracts and point to a separate guide for geographic availability.

When the PaymentIntent requires a customer action, its `next_action` specifies the action. Card payments without 3D Secure illustrate a flow without extra authentication beyond collecting card details.

| Action | Example |
| --- | --- |
| Redirect to bank | Customer approves and authenticates in the bank's online service |
| One-time code | Customer supplies a code to verify account ownership, and the merchant sends it to the Stripe API |
| Push funds | Customer sends a transfer through the bank's online service |

## Immediate and delayed notification

| Notification | Example | PaymentIntent outcome |
| --- | --- | --- |
| Immediate | Card payment without additional authentication | `succeeded` on success or `requires_payment_method` after a failed attempt |
| Delayed | ACH Direct Debit | `processing` until a result, then `succeeded` on success or `requires_payment_method` after a failed attempt that can be retried |

While the PaymentIntent is `processing`, November recommends keeping the merchant order pending and waiting for verified success before fulfillment.

The April capture described `succeeded` as guaranteeing receipt of funds. November defines it as successful completion under the method's processing flow and says funds remain subject to refund, dispute, return, or reversal. The separate November [lifecycle guide](../../raw/stripe-payments-paymentintents-lifecycle-2026-11-07.md#L33-L34) uses funds-in-account and fulfillment language. The November [verifying-status guide](../../raw/stripe-payments-payment-intents-verifying-status-2026-11-07.md#L30-L34) places later refunds, disputes, and outcomes on the Charge even when the PaymentIntent remains `succeeded`. Verified success supports fulfillment. Balance detail and payout timing are separate, and some Charge balance data can be deferred under asynchronous capture.

## Single-use and reusable methods

Set up a reusable method, such as a card or bank debit, during a payment or in a separate setup without charging. This reduces later payment friction, including authentication and declines. Some bank transfers are single-use, are consumed after an attempt, and cannot be attached to a Customer.

## PaymentMethod object structure

This abbreviated SEPA example illustrates the type and matching hash.

```json
{
  "id": "pm_123",
  "type": "sepa_debit",
  "billing_details": { "email": "...", "name": "..." },
  "sepa_debit": { "bank_code": "...", "last4": "3000", "country": "FR" }
}
```

## Webhook events

For methods that require customer action or report the outcome later, configure an event destination. The November Payment Methods API guide explicitly directs merchants to verify webhook signatures to authenticate Stripe as the sender. The companion Intent lifecycle documentation already covers verified webhooks.

| Event | Meaning | Merchant action |
| --- | --- | --- |
| `payment_intent.processing` | Submitted for a method with delayed notification | Keep the order pending and wait for the outcome |
| `payment_intent.succeeded` | Payment completed successfully | Fulfill on verified success |
| `payment_intent.payment_failed` | Payment attempt failed | Ask the customer for another payment method |

Other tracking options include the Dashboard for low-volume delayed payments, rate-limited API polling with lower reliability at scale, and a partner application.

## Related Pages

- [[stripe]] — Stripe company page
- [[source-stripe-payment-intents]] — PaymentIntents and SetupIntents lifecycle, verified webhooks, and asynchronous capture
- [[stripe-payment-methods]] — payment-method selection, regional availability, and integration routes
- [[stripe-payment-intents]] — PaymentIntent states and verification

## Raw Sources

- [[raw/stripe-payments-payment-methods-2026-11-07|November 7, 2026 Payment Methods API overview]]
- [[raw/stripe-payment-methods-api-2025|April 19, 2026 Payment Methods API overview]] — instrument roles, customer actions, notification timing, reuse, and webhooks
