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

- [[source-adyen-docs-industries-peak-season-refunds]] — 2026-09-15 seasonal guide to reserve advice, asynchronous ecommerce/POS and always-referenced omnichannel refunds, offline constraints, and direct-merchant versus platform payout timing; request or schedule is not bank-credit proof.


- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-cancel-or-refund]] — inactive Classic `/cancelOrRefund` guide for uncertain capture state, split and multiple-partial-capture exclusions, original payment reference, and webhook outcome boundary (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-refund]] — 2026-09-15 Classic Payment API refund guide for referenced and restricted unreferenced requests, asynchronous refund and failure events, and inactive endpoint scope.


- [[source-adyen-docs-online-payments-reversal]] — 2026-09-15 Adyen webpage guide to cancel-or-refund choice when capture state is uncertain, exclusions for multiple partial captures and split data, and request receipt versus asynchronous webhook and later refund exceptions.


- [[source-adyen-docs-online-payments-refund]] — captured-payment refund routes, request conditions, webhooks, failure/reversal distinctions, and authorization behavior
