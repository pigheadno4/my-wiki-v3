---
title: "Braintree Transaction Refund (Node.js)"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/refund/node"
raw_files:
  - "braintree/docs/reference/request/transaction/refund/node-2026-09-16.md"
tags: [braintree, node-js, transactions, refunds, settlement]
---

## Overview

This Braintree reference page documents the Node.js server SDK's `gateway.transaction.refund()` operation. It explains which transaction states are eligible, how an omitted refund amount is handled, and where to distinguish validation, lookup, processor-decline, and settlement-failure outcomes.

## Key takeaways

- A transaction must be `settled` or `settling` to be refunded. The refund cannot exceed the original transaction's remaining non-refunded amount, a completely refunded transaction cannot be refunded again, and an escrow-held transaction can only be refunded in full.
- When no amount is specified, the page says the entire transaction amount is refunded; after an earlier partial refund, it says a subsequent refund without specifying the balance refunds the remaining non-refunded amount. Multiple partial refunds are supported while their sum remains below the initial transaction amount.
- A transaction lookup failure returns a `notFoundError`. Other unsuccessful refunds include validation errors for invalid parameters or a processor settlement response code for the settlement failure type.
- The page qualifies processor-decline reporting by SDK recency: the most current SDK exposes `processor_response_code`, while an older SDK may return a validation error instead. A processor-declined capture for the refund transaction exposes `processor_settlement_response_code` on the transaction object.
- Partial-refund calls for the same transaction should complete before another is created. The page strongly recommends waiting 5–10 seconds between attempts because too many simultaneous refund requests are likely to fail with a gateway error.

## Important documentation gap

> [!warning] Incomplete source text
> The introduction says that if a transaction has not begun settlement, `useinstead`, but the action name is missing. This source does not reconstruct or infer the omitted action.

## Detail locators

- `# Transaction: Refund > Node` contains the callback invocation plus the not-found and unsuccessful-result behavior.
- `## Requirements` contains the status, remaining-amount, completed-refund, and escrow constraints.
- `## Examples > Partial refunds` contains callback and Promise examples, multiple-partial-refund behavior, omitted-balance behavior, and the concurrency warning.
- `## Examples > Refund processor declines` distinguishes most-current-SDK and older-SDK decline reporting.
- `## Examples > Settlement failures` identifies the settlement response field and links to the settlement-declined status details.
- `## Examples > Issuing a credit` is a separate operation whose security warning and parameters remain in the raw source; it does not repair the introduction's missing action.

## Related

- Companies: [[braintree]]
- Concepts: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/refund/node-2026-09-16]] — fully read Braintree Node.js Transaction: Refund reference page
