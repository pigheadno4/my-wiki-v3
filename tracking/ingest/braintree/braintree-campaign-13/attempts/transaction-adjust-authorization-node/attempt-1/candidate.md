---
title: "Braintree Transaction Adjust Authorization (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/adjust-authorization/node"
raw_files:
  - "braintree/docs/reference/request/transaction/adjust-authorization/node-2026-09-16.md"
tags: [braintree, node-js, transactions, authorization-adjustments]
---

## Overview

This Braintree Node.js request reference documents `gateway.transaction.adjustAuthorization()` for changing a transaction's authorized amount after the transaction has been created. It identifies the eligible transaction status, required inputs, lower-versus-higher adjustment attempts, and callback result handling without treating the operation as capture or settlement submission.

## Key takeaways

- Authorization adjustment is limited by this page to transactions whose status is `authorized`. The required information is the transaction ID and amount; the page does not state broader payment-method, merchant, or processor availability.
- When the new authorized amount is lower than the original amount, Braintree says it attempts a partial reversal of the difference back to the cardholder. When the new amount is higher, it attempts an incremental authorization. Both effects are attempts, not guaranteed outcomes.
- The Node example passes a transaction ID and an amount to `gateway.transaction.adjustAuthorization()`. On success it reads the adjusted transaction from `result.transaction`; otherwise it displays `result.errors`.
- The page warns that authorization and capture can incur merchant fees in some markets and points readers to the Braintree User Agreement. It does not identify the markets, assign a fee to every adjustment, or say that this operation captures the transaction.

## Scope boundary

This page changes an authorized amount. It does not document capture, settlement submission, or a transaction-status transition caused by a successful adjustment; use [[source-braintree-transaction-submit-for-settlement-node]] for the distinct settlement-submission route.

## Detail locators

- Some-market merchant-fee qualification and Braintree User Agreement route: `# Transaction: Adjust Authorization > **NOTE**`, lines 16-17.
- Post-creation adjustment purpose, `authorized`-status restriction, and required transaction ID plus amount: `# Transaction: Adjust Authorization`, lines 21-23.
- Lower-amount partial-reversal attempt and higher-amount incremental-authorization attempt: `# Transaction: Adjust Authorization`, line 25.
- Node method, inputs, success transaction, and error branch: `# Transaction: Adjust Authorization > ### Node`, lines 26-40.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Distinct settlement-submission operation: [[source-braintree-transaction-submit-for-settlement-node]]

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/adjust-authorization/node-2026-09-16|Braintree Node.js adjust-authorization reference]] - complete collected page covering authorized-status scope, amount-adjustment attempts, fee qualification, and callback result handling
