---
title: "Braintree Address Delete (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/address/delete/node"
raw_files:
  - "braintree/docs/reference/request/address/delete/node-2026-09-16.md"
tags: [braintree, node-js, addresses, customers, vault, payment-method]
---

## Overview

This Braintree Node.js reference documents `gateway.address.delete()` for deleting a customer address identified by both customer ID and address ID. It preserves the operation's effect on Vault payment methods that reference the address and routes missing-address or missing-customer cases to the page's not-found error reference.

## Key takeaways

- Both the customer ID and address ID are needed to identify and delete an address.
- The Node example passes the customer ID and address ID to `gateway.address.delete()` and receives an error-only callback.
- Deleting an address from a customer also removes that address from any Vault payment methods that reference it for billing or shipping. The page does not state that those payment methods, the customer, or subscriptions are deleted.
- If the address or customer cannot be found, the page directs readers to its Node `notFoundError` reference.

## Detail locators

- Required customer-ID and address-ID identity: `# Address: Delete`, lines 15-16.
- Node deletion invocation and callback form: `### Node`, lines 17-21.
- Effect on billing or shipping references from Vault payment methods: `**NOTE**`, lines 23-24.
- Not-found error route: line 26.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Node.js exceptions reference]] - navigation-only destination for the linked `notFoundError`; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/address/delete/node-2026-09-16|Braintree Node.js address-delete request reference]] - complete collected page covering two-part address identity, the Node deletion call, removal of billing or shipping address references from Vault payment methods, and the linked not-found error route
