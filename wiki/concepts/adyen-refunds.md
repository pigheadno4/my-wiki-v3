---
title: "Adyen Online Payment Refunds"
type: concept
category: technology
tags: [adyen, online-payments, refunds, webhooks]
---

## Definition

Adyen online-payment refunds return funds to a shopper after the payment has been captured. A merchant can use the Customer Area or submit a referenced Checkout API refund; unreferenced refunds require Adyen approval. Before capture, use cancellation, or use reversal when capture status is unknown.

## Lifecycle boundary

Refund processing is asynchronous. A `REFUND` webhook reports validation success or failure; `success: true` means Adyen sent the request onward but does not guarantee final completion. A later `REFUND_FAILED` event can report payment-method rejection, while `REFUNDED_REVERSED` means funds from a previously refunded payment returned to Adyen and the merchant account.

## Sources

- [[source-adyen-docs-online-payments-refund]] — captured-payment refund routes, request conditions, webhooks, failure/reversal distinctions, and authorization behavior
