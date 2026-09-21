---
title: "Braintree Subscription Search (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/subscription/search/node"
raw_files:
  - "braintree/docs/reference/request/subscription/search/node-2026-09-16.md"
tags: [braintree, node-js, subscriptions, search]
---

## Overview

This Braintree Node.js reference documents searching subscriptions with `gateway.subscription.search()`. It returns Subscription response objects and shows both callback-based iteration and Node stream consumption; detailed filter examples and linked result schemas remain routed to the raw documentation.

## Key takeaways

- The page supports searching subscriptions with multiple criteria and directs readers to the separate Search fields reference for available operators. Its displayed examples qualify price as a range field, plan ID and status as multiple-value fields, and active-status searches by whether a trial period is present; the complete filter examples remain in the raw page rather than being reproduced here.
- The opening callback example consumes the response with `response.each()`. The Search results section states that the search method returns a Node stream and shows consumption through `pipe()` or `data` and `end` events followed by `resume()`.
- The collected rendering omits the version values from both `All examples assume versionor greater` and the prior-version sentence. This source therefore does not claim a minimum Node SDK version or reconstruct the missing version qualifier.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. Because that external policy was not part of this source, this entry preserves the notice without interpreting which results or fields are limited, or why.
- The sentence about looking up one subscription by ID is incomplete (`useinstead`). It does not establish the missing method; the separately retained subscription-find source is the retrieval route for single-ID lookup.

## Detail locators

- Results-limitation policy notice, Subscription response-object route, and general search-criteria/operator route: `# Subscription: Search`, lines 16-21.
- Callback search and `response.each()` result iteration: `# Subscription: Search > ### Node`, lines 22-31.
- Incomplete single-subscription lookup sentence: `# Subscription: Search`, line 32.
- Node stream statement, `pipe()` form, event/resume form, and missing rendered version qualifiers: `## Search results`, lines 33-61.
- Filter examples and their displayed qualifications: `## Examples`, lines 62-180.
- Linked Search fields, Search results, Subscription object, and payment-method response routes: `## See Also`, lines 182-192.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Distinct single-subscription lookup: [[source-braintree-subscription-find-node]]

## Raw Sources

- [[raw/braintree/docs/reference/request/subscription/search/node-2026-09-16|Braintree Node.js subscription-search request reference]] - complete collected page covering subscription-search criteria, result collection and stream consumption, qualified filter examples, the results-limitation notice, and the damaged version rendering
