---
title: "Braintree Transaction Search (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/transaction/search/node"
raw_files:
  - "braintree/docs/reference/request/transaction/search/node-2026-09-16.md"
tags: [braintree, node-js, transactions, search]
---

## Overview

This Braintree Node.js request reference documents transaction search through `gateway.transaction.search()`. It returns a collection of Transaction response objects, demonstrates callback-based `response.each()` consumption, and routes detailed criteria, operator behavior, and general result handling to exact documentation locations.

## Key takeaways

- The opening example filters by customer ID and iterates the returned transaction collection through `response.each()`, displaying each transaction's amount in the example.
- The examples cover criteria involving card, customer, billing and shipping details; Vault and creation associations; merchant account, card type, status, source, transaction type, amount, status-change time, and dispute date. These examples are retrieval routes rather than an exhaustive field or operator inventory; the separate Search fields reference is the authority linked by the page for available operators.
- For transaction type, the page distinguishes sales from credits and qualifies refunds as a special kind of credit. A credit-only search includes both refunds and standalone credits; the raw examples show how the additional refund criterion narrows those groups.
- Status-change criteria can select transactions that entered a listed status at a given date and time. For time values in transaction search, supplied time zones are respected; without one, the gateway account's time zone is used, while returned time values are always UTC.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products. Because that external policy is not part of this raw, this entry preserves the notice without inferring a numeric limit, affected fields, or rationale.

## Detail locators

- Policy-based result-limitation notice, Transaction response-object route, and Search fields operator route: `# Transaction: Search`, lines 16-19.
- `gateway.transaction.search()`, customer-ID criterion, callback and `response.each()` result consumption: `# Transaction: Search > ### Node`, lines 20-29.
- Card, customer, billing, shipping and top-level-attribute examples: `## Examples`, lines 31-112.
- Vault association, creation mode, customer location, merchant-account, card-type, status and source criteria: `## Examples`, lines 114-221.
- Sale, credit, refund and standalone-credit distinctions: `## Examples > ### Transaction type`, lines 223-254.
- Amount range examples: `## Examples > ### Amount`, lines 256-272.
- Status-change criteria and displayed status list: `## Examples > ### Status changes`, lines 274-316.
- Dispute-date example and timezone/default/UTC qualifications: `## Examples > ### Dispute date range`, lines 318-332.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Search operator reference: [[source-braintree-search-fields-node]]
- General result-consumption reference: [[source-braintree-search-results-node]]

## Related raw API references

- [[raw/braintree/docs/reference/general/searching/search-fields/node-2026-09-16|Braintree Node.js Search fields reference]] - navigation-only route for available operators; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/searching/search-results/node-2026-09-16|Braintree Node.js Search results reference]] - navigation-only route for general result-consumption behavior and limits; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/transaction/search/node-2026-09-16|Braintree Node.js transaction-search request reference]] - complete collected page covering transaction criteria, callback result iteration, transaction-type scope, status-change searches, timezone behavior, and the policy limitation notice
