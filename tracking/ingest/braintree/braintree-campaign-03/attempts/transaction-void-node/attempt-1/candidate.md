---
title: "Braintree Transaction Void (Node.js)"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/void/node"
raw_files:
  - "braintree/docs/reference/request/transaction/void/node-2026-09-16.md"
tags: [braintree, node-js, transactions, voids, authorization-reversal]
---

## Overview

This Braintree reference page documents the Node.js server SDK's `gateway.transaction.void()` operation. It identifies the eligible transaction states, the transaction-ID input, the qualified authorization-reversal effect, and the success-versus-validation-error route.

## Key takeaways

- Braintree says a transaction can be voided when its status is `authorized` or `submitted for settlement`; `settlement pending` is eligible only for PayPal transactions. The transaction ID is the only required information identified by this page.
- When the transaction is voided, Braintree says it will perform an authorization reversal, if possible, to remove the pending charge from the customer's card. The reversal is conditional, not guaranteed.
- The Node example calls `gateway.transaction.void()` with the transaction ID. The result is successful when the transaction is successfully voided; otherwise, the page directs the reader to validation errors.

## Scope boundary

This page documents transaction voiding, not refund behavior. It does not state eligibility or effects for other transaction statuses.

## Detail locators

- Eligible states, PayPal-only `settlement pending` qualification, transaction-ID requirement, and conditional authorization reversal: `# Transaction: Void`, first paragraph, line 15.
- Node.js invocation: `# Transaction: Void > ### Node`, lines 18-22.
- Success result and validation-error route: `# Transaction: Void`, line 23, with the result-check example at lines 24-31.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]
- Related source: [[source-braintree-transaction-refund-node]]

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/void/node-2026-09-16|Braintree Node.js transaction-void reference]] - complete page covering eligibility, invocation, qualified authorization reversal, and result handling
