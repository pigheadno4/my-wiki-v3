---
title: "Braintree Address Create (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/address/create/node"
raw_files:
  - "braintree/docs/reference/request/address/create/node-2026-09-16.md"
tags: [braintree, node-js, addresses, customers, vault]
---

## Overview

This Braintree Node.js reference documents `gateway.address.create()` for creating a Vault address associated with a customer. It provides the customer-scoped address-ID rules, the per-customer storage limit, a callback-form example, and the page's not-found error route.

## Key takeaways

- `customer_id` is the only attribute the page requires for address creation, because a Vault address must be associated with a customer.
- A caller cannot specify the address ID. The gateway generates a two-character alphanumeric ID, and that ID is unique only within its customer; different customers can have the same address ID.
- A customer can have at most 50 saved addresses. The page also routes readers to address creation with a payment method or together with a customer and payment method.
- The Node example calls `gateway.address.create()` with customer and address attributes in callback form. The page directs cases where the address or customer cannot be found to its Node `notFoundError` reference.

## Detail locators

- Address response-object route: `# Address: Create`, line 15.
- Required customer association, generated address-ID format, and customer-scoped uniqueness: `# Address: Create`, line 17.
- Per-customer limit and alternative creation routes: `# Address: Create`, line 19.
- Node callback-form invocation and example attributes: `### Node`, lines 22-36.
- Not-found error route: `### Node`, line 38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/request/payment-method/create/node-2026-09-16|Braintree Node.js payment-method-create request reference]] - navigation-only alternative address-creation route linked by this page; not used as factual evidence here
- [[raw/braintree/docs/reference/request/customer/create/node-2026-09-16|Braintree Node.js customer-create request reference]] - navigation-only customer-and-payment-method creation route linked by this page; not used as factual evidence here
- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Node.js exceptions reference]] - navigation-only destination for the linked `notFoundError`; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/address/create/node-2026-09-16|Braintree Node.js address-create request reference]] - complete collected page covering customer association, customer-scoped address IDs, the 50-address limit, the Node callback example, and the linked not-found error route
