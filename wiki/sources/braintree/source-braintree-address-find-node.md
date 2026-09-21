---
title: "Braintree Address Find (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/address/find/node"
raw_files:
  - "braintree/docs/reference/request/address/find/node-2026-09-16.md"
tags: [braintree, node-js, address, customer, vault]
---

## Overview

This Braintree Node.js reference documents looking up one customer address through `gateway.address.find()`. The displayed call identifies the lookup with both a customer ID and an address ID and returns callback arguments named `err` and `address`.

## Key takeaways

- The Node example passes `"aCustomerId"` first and `"anAddressId"` second to `gateway.address.find()`. Keep the customer identity and address identity distinct; the page does not show an address-only lookup.
- The callback exposes `(err, address)`. The page does not display fields on `address`, a success flag, a Promise form, or any other response shape; it instead links to the separate Address response-object reference.
- If either the address or the customer cannot be found, the page routes the failure to Braintree's linked Node.js `notFoundError`. It does not show different errors for the two missing identities or define the error object's fields.

## Detail locators

- Separate Address response-object route: `# Address: Find`, line 15.
- Customer ID, address ID, and callback argument names: `# Address: Find > ### Node`, lines 16-20.
- Missing-address or missing-customer error route: line 21.

## Evidence limitations

> [!warning] Response details are not supplied here
> This page shows only the two lookup identifiers and the callback names. Do not infer Address fields, success semantics, Promise behavior, customer/address uniqueness rules, or distinct not-found outcomes from the example.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/address/find/node-2026-09-16|Braintree Node.js address-find reference]] - complete page covering the customer/address identifiers, callback names, response-object route, and shared not-found condition
