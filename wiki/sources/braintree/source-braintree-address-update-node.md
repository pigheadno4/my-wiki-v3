---
title: "Braintree Address Update (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/address/update/node"
raw_files:
  - "braintree/docs/reference/request/address/update/node-2026-09-16.md"
tags: [braintree, node-js, address, customer, vault]
---

## Overview

This Braintree Node.js reference documents updating a Vault address through `gateway.address.update()`. The example identifies the customer and address separately, supplies updated address attributes, and receives `err` and `result` through a callback.

## Key takeaways

- The Node example passes a customer ID, an address ID, an address-attribute object, and a callback to `gateway.address.update()`. Its callback exposes `err` and `result`, but the page does not describe result fields or a success condition.
- The page links to the Address response-object reference for response details; this source does not reconstruct that unread response schema.
- In addition to direct address updating, the page says an address can be updated while updating a customer or while updating a payment method. It does not describe the qualifications or field behavior of those linked operations.
- If either the address or customer cannot be found, the page routes the failure to Braintree's Node.js `notFoundError` reference.

## Detail locators

- Address response-object route: `# Address: Update`, line 15.
- Customer ID, address ID, update attributes, and callback result handling: `# Address: Update > ### Node`, lines 17-30.
- Direct-update and alternative customer/payment-method update routes: `# Address: Update > **NOTE**`, lines 33-34.
- Missing-address or missing-customer error route: line 36.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]
- Related operation: [[source-braintree-customer-update-node]]

## Raw Sources

- [[raw/braintree/docs/reference/request/address/update/node-2026-09-16|Braintree Node.js address update reference]] - complete page covering update identifiers, callback shape, alternative update routes, and the missing-address or missing-customer error route
