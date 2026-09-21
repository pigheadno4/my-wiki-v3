---
title: "Braintree Transaction Line Item Find All (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction-line-item/find-all/node"
raw_files:
  - "braintree/docs/reference/request/transaction-line-item/find-all/node-2026-09-16.md"
tags: [braintree, node-js, transactions, line-items, retrieval]
---

## Overview

This Braintree Node.js reference documents retrieving a collection of Transaction Line Item objects for a transaction. Its code shows `gateway.transactionLineItem.findAll()` with a transaction ID in callback and Promise forms; a damaged explanatory sentence is preserved as an evidence limitation rather than reconstructed.

## Key takeaways

- The page states that the operation returns a collection of Transaction Line Item objects and links to a separate response-object reference for their details. That unread response reference, not this source, owns individual item fields.
- The callback example passes `theTransactionId` and receives `transactionLineItems`; the Promise example passes the same displayed ID and resolves `transactionLineItems`. Neither empty handler establishes item properties, ordering, count, pagination, completeness, or failure behavior.
- The prose immediately before the examples is incomplete: `To retrieve a list of transaction line items that were provided when a transaction was created with, use.` The missing creation qualifier and method text must not be reconstructed. The displayed code independently establishes the Node.js invocation used in this source.
- Braintree says results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. Because that external policy was not read as part of this source, this entry preserves the notice without interpreting which results or fields are limited or why.

> [!warning] Damaged prose and result boundary
> Do not reconstruct the missing words in the explanatory sentence or infer a transaction-creation feature from it. The code establishes the displayed `findAll()` call and collection variable only; detailed result semantics remain with the dedicated response reference and policy authority.

## Detail locators

- Results-limitation policy notice: `# Transaction Line Item: Find All > **NOTE**`, lines 16-17.
- Collection and Transaction Line Item response-object route: line 19.
- Damaged explanatory sentence with missing creation qualifier and method text: line 21.
- Callback invocation and collection variable: `### Callback`, lines 22-30.
- Promise invocation and collection variable: `### Promise`, lines 32-38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/response/transaction-line-item/node-2026-09-16|Braintree Node.js Transaction Line Item response reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction-line-item/find-all/node-2026-09-16|Braintree Node.js transaction-line-item find-all request reference]] - complete collected page covering the policy notice, collection statement, damaged explanatory prose, and callback and Promise invocation forms
