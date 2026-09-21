---
title: "Braintree Credit Card Verification Search (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/credit-card-verification/search/node"
raw_files:
  - "braintree/docs/reference/request/credit-card-verification/search/node-2026-09-16.md"
tags: [braintree, node-js, credit-card-verification, search]
---

## Overview

This Braintree Node.js request reference documents searching credit-card verifications through `gateway.creditCardVerification.search()`. It routes readers to verification-specific criteria examples, callback-based result iteration, a result-limitation policy notice, and exact timezone behavior for created-at searches without treating the page as transaction or customer search documentation.

## Key takeaways

- The opening example filters by verification ID and iterates returned verifications through `response.each()` in the search callback, exposing each verification's status in the example.
- The page demonstrates verification-specific criteria across customer details, credit-card details, an associated payment-method token, billing-address postal code, and creation time. The separate Search fields page is the route for the available operators; this source does not promote its examples into an exhaustive operator or field inventory.
- For created-at searches, a supplied timezone is respected. When no timezone is supplied, the gateway account's timezone is used, while returned time values are always UTC.
- The page says results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products. That external policy is not part of this raw, so this entry does not infer a numeric limit, affected fields, or a reason for the restriction.

## Detail locators

- Result-limitation policy notice and Search fields operator route: `# Credit Card Verification: Search`, lines 16-19.
- Verification-ID criterion, `gateway.creditCardVerification.search()`, callback response iteration and displayed status access: `# Credit Card Verification: Search > ### Node`, lines 22-33.
- Customer email and customer ID examples, including `endsWith`: `## Examples > ### Customer Details`, lines 38-60.
- Cardholder name, expiration date, card-number prefix/suffix and card-type examples: `## Examples > ### Credit Card Details`, lines 62-77.
- Associated payment-method-token criterion: `## Examples > ### Payment Methods`, lines 79-91.
- Billing postal-code criterion: `## Examples > ### Billing Address`, lines 93-103.
- Created-at range and timezone/default/UTC qualifications: `## Examples > ### Created At`, lines 105-118.
- Navigation-only general Search fields and Search results routes: `## See also`, lines 123-127.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/general/searching/search-fields/node-2026-09-16|Braintree Node.js Search fields reference]] - navigation-only route for available search-field operators; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/searching/search-results/node-2026-09-16|Braintree Node.js Search results reference]] - navigation-only route for general result-consumption details; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/credit-card-verification/search/node-2026-09-16|Braintree Node.js credit-card-verification search reference]] - complete collected page covering verification-specific criteria, callback result iteration, the policy limitation notice, and created-at timezone behavior
