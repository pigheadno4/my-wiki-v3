---
title: "Braintree Discount All (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/discount/all/node"
raw_files:
  - "braintree/docs/reference/request/discount/all/node-2026-09-16.md"
tags: [braintree, node-js, discounts, recurring-billing, retrieval]
---

## Overview

This Braintree Node.js reference documents retrieving the collection of Discount objects with `gateway.discount.all()` in callback form. The displayed code accesses the returned collection through `result.discounts`.

## Key takeaways

- The Node example invokes `gateway.discount.all((err, result) => { ... })` and assigns `result.discounts` to a local `discounts` variable.
- The page states that a missing discount returns a `notFoundError`; the linked Node exception reference is the route for further error detail.
- The linked Discount response-object reference is navigation-only for this source, and the recurring-billing add-ons-and-discounts See Also link points to Ruby documentation. Neither link supplies additional Node.js facts without a separate full read.
- This collection-listing page does not document creating discounts or applying them to plans or subscriptions.

## Detail locators

- Collection purpose and Discount response-object route: `# Discount: All`, line 15.
- Node callback invocation and `result.discounts` access: `### Node`, lines 18-23.
- Missing-discount error route: line 24.
- Ruby recurring-billing add-ons-and-discounts navigation route: `## See also`, lines 27-30.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/discount/all/node-2026-09-16|Braintree Node.js discount-all request reference]] - complete collected page covering collection retrieval, callback result access, the not-found route, and navigation links
