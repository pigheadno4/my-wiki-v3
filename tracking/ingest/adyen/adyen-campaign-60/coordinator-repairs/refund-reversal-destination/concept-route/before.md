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

- [[source-adyen-api-explorer-webhooks-latest-post-refund-failed]] — 2026-09-15-captured refund-failure event; API Explorer's scheme-rejection heading coexists with a BLIK example. See [[source-adyen-docs-online-payments-refund]] for original-payment versus refund-request PSP reference mapping.


- [[source-adyen-api-explorer-webhooks-latest-post-refunded-reversed]] — 2026-09-15-captured reversed-refund notification contract; its “your bank account” destination wording conflicts with the refund guide's Adyen/merchant-account wording, and HTTP receipt is separate from event outcome.


- [[source-adyen-api-explorer-webhooks-latest-post-refund]] — 2026-09-15-captured REFUND webhook reference for refund-request result, item fields and an uncaptured-transaction failure example; HTTP acceptance is distinct from refund completion.


- [[source-adyen-api-explorer-webhooks-latest-post-postponed-refund]] — 2026-09-15-captured `Webhooks/latest` POSTPONED_REFUND event reference: refund postponed until after capture, Support enablement for the notification, and HTTP receiver acceptance separate from refund completion.


- [[source-adyen-api-explorer-payment-latest-post-refund]] — 2026-09-15 inactive Classic Payment API v68 POST /refund reference for captured-payment eligibility, partial-refund qualification, original PSP identity and received-for-processing response.


- [[source-adyen-docs-industries-peak-season-refunds]] — 2026-09-15 seasonal guide to reserve advice, asynchronous ecommerce/POS and always-referenced omnichannel refunds, offline constraints, and direct-merchant versus platform payout timing; request or schedule is not bank-credit proof.


- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-cancel-or-refund]] — inactive Classic `/cancelOrRefund` guide for uncertain capture state, split and multiple-partial-capture exclusions, original payment reference, and webhook outcome boundary (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-refund]] — 2026-09-15 Classic Payment API refund guide for referenced and restricted unreferenced requests, asynchronous refund and failure events, and inactive endpoint scope.


- [[source-adyen-docs-online-payments-reversal]] — 2026-09-15 Adyen webpage guide to cancel-or-refund choice when capture state is uncertain, exclusions for multiple partial captures and split data, and request receipt versus asynchronous webhook and later refund exceptions.


- [[source-adyen-docs-online-payments-refund]] — captured-payment refund routes, request conditions, webhooks, failure/reversal distinctions, and authorization behavior
