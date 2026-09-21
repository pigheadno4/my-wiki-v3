---
title: "Braintree Add-On All (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/add-on/all/node"
raw_files:
  - "braintree/docs/reference/request/add-on/all/node-2026-09-16.md"
tags: [braintree, node-js, add-ons, recurring-billing, retrieval]
---

## Overview

This Braintree Node.js reference documents retrieving the collection of Add-On objects with `gateway.addOn.all()`. Its callback and Promise examples both access the returned collection through `result.addOns`.

## Key takeaways

- The callback example invokes `gateway.addOn.all((err, result) => { ... })` and assigns `result.addOns` to a local `addOns` variable.
- The Promise example invokes `gateway.addOn.all()` and likewise reads the collection from `result.addOns`.
- The page states that a missing add-on returns a `notFoundError`; the linked exception route is the location for further error detail.
- The linked Add-On response-object reference and recurring-billing add-ons-and-discounts guide both point to Ruby documentation. They are navigation routes, not Node.js response or behavior evidence for this source.
- This retrieval page does not document creating add-ons or applying them to plans or subscriptions.

## Detail locators

- Collection purpose and Ruby response-object link: `# Add On: All`, line 16.
- Node callback invocation and `result.addOns` access: `### Callback`, lines 17-22.
- Node Promise invocation and `result.addOns` access: `### Promise`, lines 24-29.
- Missing-add-on error route: line 30.
- Ruby recurring-billing add-ons-and-discounts navigation route: `## See also`, lines 31-34.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/add-on/all/node-2026-09-16|Braintree Node.js add-on-all request reference]] - complete collected page covering collection retrieval, callback and Promise result access, the not-found route, and Ruby-language navigation links
