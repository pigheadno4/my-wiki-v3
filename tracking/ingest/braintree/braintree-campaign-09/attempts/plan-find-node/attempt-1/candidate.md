---
title: "Braintree Plan Find (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/plan/find/node"
raw_files:
  - "braintree/docs/reference/request/plan/find/node-2026-09-16.md"
tags: [braintree, node-js, plans, recurring-billing, lookup]
---

## Overview

This Braintree Node.js reference documents lookup of a single plan by ID. The prose omits the method name, while the displayed callback and Promise examples identify the invocation as `gateway.plan.find()`.

## Key takeaways

- The callback example passes a plan ID to `gateway.plan.find()` and supplies `(err, result)` to its callback.
- The Promise example passes a plan ID to the same method and uses `.then(result => { })`. Neither example shows fields within `result`; the linked Plan response-object page is the navigation route for that separate detail.
- The page states that a missing plan returns the linked `notFoundError`. It does not document plan listing, creation, update, subscription behavior, or recurring-billing enablement.

## Detail locators

- Single-plan ID lookup purpose, omitted prose method name, and Plan response-object route: `# Plan: Find`, lines 15-16.
- Callback invocation and result-variable form: `### Callback`, lines 17-20.
- Promise invocation and result-variable form: `### Promise`, lines 22-25.
- Missing-plan error route: line 26, immediately after `### Promise`.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/plan/find/node-2026-09-16|Braintree Node.js plan-find request reference]] - complete collected page covering single-plan ID lookup, callback and Promise invocation forms, the Plan response-object route, and the missing-plan error route
