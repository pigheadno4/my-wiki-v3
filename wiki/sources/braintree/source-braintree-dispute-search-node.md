---
title: "Braintree Dispute Search (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/dispute/search/node"
raw_files:
  - "braintree/docs/reference/request/dispute/search/node-2026-09-16.md"
tags: [braintree, node-js, disputes, search]
---

## Overview

This Braintree Node.js reference documents searching disputes with `gateway.dispute.search()`. It returns a collection of Dispute response objects and shows callback result access through `response.forEach()`; routine criteria, operators, and response fields remain routed to the raw and linked references.

## Key takeaways

- The opening example filters by dispute ID and iterates returned disputes with `response.forEach()`.
- The page routes operator details to the separate Search fields reference. Its examples demonstrate searches across multiple dispute kinds and a disputed-amount range; use the raw locators below for the exact criteria, enum constants, sample values, and operators rather than treating this entry as an exhaustive search specification.
- Managing disputes through the API is available only to merchants who can access disputes in the Braintree Control Panel.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products. Because that external policy was not part of this source, this entry preserves the notice without interpreting which results or fields are limited, or why.

## Detail locators

- Results-limitation policy notice: `# Dispute: Search > NOTE`, lines 16-17.
- Dispute collection identity, response-object route, and Control Panel access restriction: `# Dispute: Search`, lines 19-21.
- Search fields operator route, ID-filter example, and `response.forEach()` result iteration: `# Dispute: Search > ### Node`, lines 23-33.
- Multiple-kind search example: `## Examples > ### Multiple kinds`, lines 38-50.
- Disputed-amount range example: `## Examples > ### Amount disputed range`, lines 52-61.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/reference/general/searching/search-fields/node-2026-09-16|Braintree Node.js Search fields reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/response/dispute/node-2026-09-16|Braintree Node.js Dispute response reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/dispute/search/node-2026-09-16|Braintree Node.js dispute-search request reference]] - complete collected page covering dispute-search identity, callback result iteration, criteria examples, access availability, and the results-limitation notice
