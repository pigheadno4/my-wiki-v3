---
title: "Braintree Transactions Guide (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/transactions/node"
raw_files:
  - "braintree/docs/guides/transactions/node-2026-09-16.md"
tags: [braintree, node-js, transactions, authorization, settlement, validation-errors, disputes]
---

## Overview

This Braintree Node.js guide organizes transaction operations around attempts to transfer money between a merchant and its customers. It distinguishes authorization through a sale, submission of an authorized sale for settlement, voiding before settlement, refunding previously collected money, validation-error routes, and account-qualified dispute retrieval. Exact request fields, status meanings, processor responses, and test values remain in the linked dedicated references.

## Key takeaways

- Creating a sale gets authorization to collect money; submitting the authorized sale transaction for settlement is the separate step the guide identifies for collecting the money. A transaction can instead be voided before it settles, while a refund returns previously collected money. These are distinct actions rather than interchangeable transaction outcomes.
- Settlement submission can be requested while creating the sale with `options.submit_for_settlement`, or afterward through `gateway.transaction.submitForSettlement()` using the transaction ID. The transaction must be authorized before the latter submission. A successful request result exposes `result.transaction`, but the guide does not state that `result.success` proves final settlement.
- A transaction's `status` indicates its current lifecycle stage. The collected page routes exact status explanations to a separate reference and includes a diagram; it does not define the complete status set in text.
- Invalid or malformed transaction details produce validation errors on the transaction, and additional information such as the payment method, customer, or address can produce its own validation errors. Because billing and shipping addresses may return the same error code, the guide says errors are scoped by parameter and the affected address must be identified.
- For certain account setups, Braintree recommends collecting and passing billing-address information when storing payment methods or creating transactions; it says at least the postal code can help increase the likelihood of successful authorization. This is account-qualified guidance, not a universal required-field rule or an authorization guarantee.
- Depending on account setup, disputes filed through a customer's bank or card network can be retrieved from the transaction response object's `disputes` array, which contains zero or more disputes. The guide also routes disputed-transaction search by dispute date and says handling after location depends on the merchant's banking partner.

## Detail locators

- Transaction purpose and sale, settlement, void, refund, search/find, and advanced-action routes: `# Transactions`, lines 20-28.
- Lifecycle-status purpose, diagram, and external status reference: `## Status`, lines 31-35.
- Settlement purpose and sale-time `options.submit_for_settlement` callback/Promise examples: `## Settlement`, lines 36-78.
- Separate `gateway.transaction.submitForSettlement()` callback/Promise examples, missing-transaction route, and authorization prerequisite: `## Settlement`, lines 80-106.
- Transaction and associated-information validation errors, account-qualified billing-address recommendation, and parameter-scoped duplicate error codes: `## Validations`, lines 107-115.
- Account-qualified dispute retrieval, zero-or-more response-array scope, dispute-date search, and banking-partner handling boundary: `## Disputes`, lines 116-122.
- Processor-response, gateway-rejection, currency, refund/void/credit, 3D Secure, and sandbox-testing navigation: `## Learn more`, lines 123-134.

## Evidence limitations

> [!warning] Submission, validation, and dispute boundaries
> This guide distinguishes authorization from settlement submission but does not establish final settlement from the example's success branch or variable name. Its billing-address recommendation applies only to certain account setups, and its dispute route depends on account setup and the banking partner. Dedicated status, request, response, validation, processor-response, and dispute authorities listed below are unread navigation only in this source.

## Related

- Company: [[braintree]]
- Concepts: [[braintree-server-sdk]], [[disputes]]
- Existing operation routes: [[source-braintree-transaction-sale-node]], [[source-braintree-transaction-submit-for-settlement-node]], [[source-braintree-transaction-void-node]], [[source-braintree-transaction-refund-node]], [[source-braintree-transaction-search-node]]

## Raw Sources

- [[raw/braintree/docs/guides/transactions/node-2026-09-16|Braintree Transactions guide for Node.js]] - complete collected guide covering authorization, settlement submission, validation and dispute navigation

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Transaction Sale (Node.js)]] - unread navigation-only sale request reference
- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Transaction Submit for Settlement (Node.js)]] - unread navigation-only settlement-submission request reference
- [[raw/braintree/docs/reference/request/transaction/void/node-2026-09-16|Transaction Void (Node.js)]] - unread navigation-only void request reference
- [[raw/braintree/docs/reference/request/transaction/refund/node-2026-09-16|Transaction Refund (Node.js)]] - unread navigation-only refund request reference
- [[raw/braintree/docs/reference/general/statuses-2026-09-16|Transaction statuses]] - unread navigation-only lifecycle-status reference
- [[raw/braintree/docs/reference/general/validation-errors/all/node-2026-09-16|Validation errors (Node.js)]] - unread navigation-only transaction and associated-information validation reference
- [[raw/braintree/docs/reference/response/transaction/node-2026-09-16|Transaction response object (Node.js)]] - unread navigation-only response and disputes-property reference
- [[raw/braintree/docs/reference/request/transaction/search/node-2026-09-16|Transaction Search (Node.js)]] - unread navigation-only disputed-transaction search reference
