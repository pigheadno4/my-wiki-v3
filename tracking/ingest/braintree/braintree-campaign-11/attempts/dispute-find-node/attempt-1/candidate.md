---
title: "Braintree Dispute Find (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/dispute/find/node"
raw_files:
  - "braintree/docs/reference/request/dispute/find/node-2026-09-16.md"
tags: [braintree, node-js, disputes, lookup]
---

## Overview

This Braintree Node.js reference documents looking up one dispute by its ID with `gateway.dispute.find()`. The page qualifies API access and result availability while routing the full Dispute response shape to separate documentation.

## Key takeaways

- Use the find method with a dispute ID to look up a single dispute. The Promise example passes `"a_dispute_id"` to `gateway.dispute.find()` and handles the resolved `dispute` value.
- Managing disputes through the API is available only to merchants who can access disputes in the Braintree Control Panel.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products. Because that external policy was not part of this source, this entry preserves the notice without interpreting which results or fields are limited, or why.
- The linked Dispute response page owns the response-field details; this lookup page does not provide or support an exhaustive result schema.

## Detail locators

- Results-limitation policy notice: `# Dispute: Find > NOTE`, lines 16-17.
- Dispute response-object route and Control Panel access restriction: `# Dispute: Find`, lines 19-21.
- Single-dispute ID lookup instruction: `# Dispute: Find`, line 23.
- `gateway.dispute.find()` Promise example and resolved dispute value: `# Dispute: Find > ### Node`, lines 24-29.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/reference/response/dispute/node-2026-09-16|Braintree Node.js Dispute response reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/dispute/find/node-2026-09-16|Braintree Node.js dispute-find request reference]] - complete collected page covering single-dispute ID lookup, access availability, the results-limitation notice, and Promise result handling
