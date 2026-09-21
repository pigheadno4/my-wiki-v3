---
title: "Braintree Plan All (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/plan/all/node"
raw_files:
  - "braintree/docs/reference/request/plan/all/node-2026-09-16.md"
tags: [braintree, node-js, plans, recurring-billing, retrieval]
---

## Overview

This Braintree Node.js reference documents `gateway.plan.all()` for retrieving a collection of Plan objects. It shows callback and Promise forms for the collection request; it does not document plan creation, subscription creation or behavior, or merchant enablement.

## Key takeaways

- The operation returns a collection of Plan objects. The linked Plan response-object reference is the route for object details, but that linked page is not factual evidence for this source.
- In callback form, the example calls `gateway.plan.all(function(err, result) { ... })`; the displayed code assigns the call expression to `plans`.
- In Promise form, the example calls `gateway.plan.all()` and resolves to a `result` argument; the displayed code assigns the Promise chain to `plans`.
- The page's See Also section links to recurring billing plans for navigation only. This page does not establish how plans are created, how subscriptions use them, or whether recurring billing is enabled for a merchant.

## Detail locators

- Returned Plan-object collection and response-object route: `# Plan: All`, line 15.
- Callback form and displayed `plans` assignment: `### Callback`, lines 16-20.
- Promise form and displayed `plans` assignment: `### Promise`, lines 22-26.
- Recurring-billing plans navigation route: `## See Also`, lines 28-31.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/plan/all/node-2026-09-16|Braintree Node.js plan-all request reference]] - complete collected page covering Plan-object collection retrieval, callback and Promise forms, and the recurring-billing plans navigation link
