---
title: "Braintree UnionPay Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/unionpay/server-side/node"
raw_files:
  - "braintree/docs/guides/unionpay/server-side/node-2026-09-16.md"
tags: [braintree, unionpay, nodejs, server-side, transactions, deprecated]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] Node.js-routed server-side guide documents the deprecated dedicated UnionPay flow: after the client successfully tokenizes payment information, the server receives the payment-method nonce and client-collected device data and uses them to create a transaction. The page directs UnionPay processing to the credit-card path through Discover, while its retained examples still describe the deprecated flow. It identifies no exact Node SDK package or version, environment, processing time, or Vault behavior, and does not establish current merchant or card eligibility or a successful transaction. See [[braintree-payment-methods]] for the provider-wide route.

> [!warning] Deprecated dedicated integration
> The page says this dedicated UnionPay integration is deprecated because UnionPay can now be processed as a credit card through Discover. Treat the transaction examples as historical route documentation, not proof that the dedicated path remains available or that the replacement has executed successfully.

## Key takeaways

- Under **Creating transactions**, the page places tokenization on the client and transaction creation on the server: send the client-produced nonce to the server, collect device data on the client and include both in the transaction request.
- The callback and Promise examples call `gateway.transaction.sale()` with an amount, `paymentMethodNonce`, `deviceData` and `submitForSettlement: true`. The examples branch on `result.success`; they are request-shape evidence, not a transaction-result guarantee.
- Delayed settlement is presented only when the UnionPay card is not a debit card. In that condition, the page says submission for settlement may occur separately, including for delayed fulfillment.

## Detail locators

- Dedicated UnionPay deprecation and Discover credit-card replacement: opening `**AVAILABILITY**`, raw lines 17-18.
- Client tokenization, nonce handoff, device-data collection and server transaction instruction: `## Creating transactions`, raw lines 21-25.
- Callback `gateway.transaction.sale()` example: `### Callbacks`, raw lines 26-42.
- Promise `gateway.transaction.sale()` example: `### Promises`, raw lines 44-60.
- Non-debit condition and separate settlement for delayed fulfillment: `### Delayed settlement`, raw lines 62-67.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- UnionPay product and processing scope: [[source-braintree-payment-methods-unionpay]]
- Replacement credit-card route: [[source-braintree-credit-cards-server-side-node]]

## Raw Sources

- [[raw/braintree/docs/guides/unionpay/server-side/node-2026-09-16|Braintree UnionPay server-side Node.js guide (captured 2026-09-16)]] - fully read pinned website snapshot covering deprecation, client-to-server nonce and device-data handoff, transaction examples and the non-debit delayed-settlement condition
