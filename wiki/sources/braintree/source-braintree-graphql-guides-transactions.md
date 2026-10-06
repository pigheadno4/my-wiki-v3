---
title: "Braintree GraphQL Transactions Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/transactions"
raw_files:
  - "braintree/graphql/guides/transactions-2026-09-16.md"
tags: [braintree, graphql, transactions, authorization, capture, refunds]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes GraphQL operations for creating, advancing, reversing, refunding and finding transaction records. It covers immediate charge, separate authorization and capture, partial capture, state-dependent reversal, direct refund, void, refund reversal, detached refund, search and node lookup. It is a documentation snapshot, not a language-SDK implementation or an exact-schema baseline, and it does not establish current production deployment, merchant eligibility, payment-method support, transaction success, settlement or funding.

## Key takeaways

- `chargePaymentMethod` creates a transaction and captures immediately, while `authorizePaymentMethod` followed by `captureTransaction` separates the authorization hold from capture. The capture request uses the authorized transaction ID, and the guide says an authorization has only a limited number of days in which it can be captured.
- The guide describes partial capture as child transactions against a parent authorization. Its own payment-method scope is inconsistent: the opening says the flow is available for PayPal and Venmo, while the dedicated partial-capture subsection says it is available for PayPal transactions. Treat support as unresolved in this snapshot. The subsection describes successful child states as `SETTLING`, `SUBMITTED_FOR_SETTLEMENT`, or `SETTLED`, with the parent at `SETTLEMENT_PENDING`.
- A mutation returning no errors is not proof that a transaction was created successfully. Declines or fraud settings can instead produce a transaction with a failure status, and other errors can return no transaction object or only a partial object. Successful transaction status also changes over time; authorization, settlement submission, settling and settlement remain distinct events.
- `reverseTransaction` attempts a full reversal whose result depends on settlement state: either the existing transaction becomes `VOIDED` or a new linked refund is returned. `refundTransaction` is the direct route for a known settled transaction, a partial refund or a separate refund order ID; the guide limits refundable transactions to `SETTLING` or `SETTLED` and not already fully refunded. `voidTransaction` is the pre-settlement cancellation route. The guide also covers `reverseRefund` and detached card or US-bank-account refund routes, with a displayed detached credit-card example.
- Transactions can be searched through a `TransactionSearchInput` example or retrieved by global ID through a node query. The displayed selection sets and filters are examples, not a complete or guaranteed schema.

> [!warning] Consequential and snapshot boundaries
> Charging a single-use payment method consumes it so it can no longer be looked up, charged or vaulted. Capture is time-limited after authorization, and reverse, refund, void, refund-reversal and detached-refund mutations change transaction or monetary state; callers must use the applicable current status and operation prerequisites. The curl sample targets the sandbox endpoint, uses placeholder Basic credentials and sends `Braintree-Version: 2019-01-01`; it is an example from this collected page, not production-deployment evidence, a current-version recommendation or proof of API compatibility.

## Detail locators

- Creation modes and the opening PayPal/Venmo partial-capture statement: `## Creating Transactions`, lines 17-33.
- Charge prerequisite, single-use consumption, mutation/variables/curl examples and displayed successful statuses: `### Charging a Payment Method`, lines 36-103.
- Separate authorization/capture examples, object identity, displayed states and limited capture window: `### Using Separate Authorization and Capture`, lines 105-187.
- Dedicated PayPal-only partial-capture statement, parent/child object and status behavior, and example blocks: `### Using Multiple Partial Capture`, lines 189-240.
- Transaction state evolution, failure statuses and missing-or-partial-object error handling: `### Transaction Statuses` and `### Error Handling`, lines 245-290.
- State-dependent full reversal, refund criteria and examples: `## Reversing or Refunding a Transaction` through `### Refunding a Transaction`, lines 293-516.
- Pre-settlement void examples and displayed error scenarios: `### Voiding a Transaction`, lines 518-672.
- Refund reversal, operation-selection table and detached-refund routes/example: `### Reversing Refunds` through `### Detached Refunds`, lines 674-813.
- Search and node-query example shapes: `## Searching For Transactions`, lines 815-939.
- Exact commit-qualified GraphQL operation shapes, nullability, enums and documented constraints are separately retained in `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql` via [[source-github-graphql-api]]; they must not be inferred from these website examples.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Exact commit-qualified schema: [[source-github-graphql-api]]
- Provider lifecycle stages: [[source-braintree-transaction-lifecycle]]

## Raw Sources

- [[raw/braintree/graphql/guides/transactions-2026-09-16|Braintree GraphQL Transactions guide]] - complete collected website page for GraphQL transaction creation, lifecycle actions, reversal/refund operations, errors and lookup examples
