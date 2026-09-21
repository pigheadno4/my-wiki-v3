---
title: "Braintree Transaction Find (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/find/node"
raw_files:
  - "braintree/docs/reference/request/transaction/find/node-2026-09-16.md"
tags: [braintree, node-js, transactions, lookup, marketplace, escrow]
---

## Overview

This Braintree Node.js reference documents lookup of a transaction by its ID through `gateway.transaction.find()`. It shows callback and Promise invocation forms and a separate Braintree Marketplace example for reading the found transaction's escrow status.

## Key takeaways

- Both Node.js examples pass a transaction ID to `gateway.transaction.find()` and receive a transaction through either a callback or a Promise. If the transaction cannot be found, the page routes the outcome to Braintree's Node.js `notFoundError` reference.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. Because that external policy was not part of this source, this entry preserves the limitation notice without inferring which result data is limited or why.
- The escrow-status example is explicitly scoped to Braintree Marketplace transactions. It uses the transaction's ID to find the transaction and reads `escrowStatus`; its shown `"held"` value is an example, not a claim that every Marketplace transaction has that status.
- The page links to the Transaction response-object reference for result details; this source does not reconstruct that unread response schema or the linked escrow-status definitions.

## Detail locators

- Results-limitation notice and Transaction response-object route: `# Transaction: Find`, lines 16-19.
- Transaction lookup callback and Promise forms: `# Transaction: Find > ### Callback`, lines 20-23, and `### Promise`, lines 25-28.
- Missing-transaction `notFoundError` route: `# Transaction: Find`, line 29.
- Marketplace-specific escrow-status purpose and callback/Promise examples: `### Escrow status on Braintree Marketplace transactions`, lines 30-45.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]
- Distinct transaction creation operation: [[source-braintree-transaction-sale-node]]

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/find/node-2026-09-16|Braintree Node.js transaction find reference]] - complete page covering transaction-ID lookup, the results-limitation notice, the missing-transaction route, and the Marketplace escrow-status example
