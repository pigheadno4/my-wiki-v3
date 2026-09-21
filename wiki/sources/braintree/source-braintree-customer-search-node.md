---
title: "Braintree Customer Search (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/customer/search/node"
raw_files:
  - "braintree/docs/reference/request/customer/search/node-2026-09-16.md"
tags: [braintree, node-js, customers, search]
---

## Overview

This Braintree Node.js reference documents searching customers with `gateway.customer.search()`. It returns a collection of Customer response objects and shows callback-based result iteration; detailed filters, operators, and examples remain routed to the raw documentation.

## Key takeaways

- The opening Node example filters by customer ID and consumes the callback response with `response.each()`, where each item is a customer object.
- The page groups examples for customer, address, credit-card, creation-time, duplicate-payment-method-token, and all-customer searches. Credit-card-number and expiration-date searches have explicit operator restrictions; use the raw locators below for the exact filters, operators, and qualifications rather than treating this entry as an exhaustive search specification.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products. Because that external policy was not part of this source, this entry preserves the notice without interpreting which results or fields are limited, or why.
- The all-customers section separately warns that search results are currently capped and says that the displayed all-customers call is not implemented in Node. Do not use that example as evidence that Node can enumerate every Vault customer.

## Detail locators

- Customer-search identity, Customer response-object route, results-limitation policy notice, and Search fields operator route: `# Customer: Search`, lines 13-21.
- `gateway.customer.search()` callback example and `response.each()` result iteration: `# Customer: Search > ### Node`, lines 23-34.
- Customer, address, and credit-card filter examples: `## Examples`, lines 37-88.
- Credit-card-number and expiration-date operator restrictions and examples: `## Examples > ### Credit card number` through `### Expiration date`, lines 91-134.
- Created-at and duplicate-payment-method-token examples: `## Examples > ### Created at` through `### Payment method token with duplicates`, lines 137-170.
- All-customers resource-collection route, current-cap warning, and Node non-implementation notice: `## Examples > ### All customers`, lines 173-182.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/general/searching/search-fields/node-2026-09-16|Braintree Node.js Search fields reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/searching/search-results/node-2026-09-16|Braintree Node.js Search results reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/response/customer/node-2026-09-16|Braintree Node.js Customer response reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/customer/search/node-2026-09-16|Braintree Node.js customer-search request reference]] - complete collected page covering customer-search identity, result iteration, filter examples, search restrictions, result limitations, and the unavailable all-customers Node call
