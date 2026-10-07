---
title: "Braintree Payment Method Nonce Response Reference (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/payment-method-nonce/node"
raw_files:
  - "braintree/docs/reference/response/payment-method-nonce/node-2026-09-16.md"
tags: [braintree, node-js, payment-method-nonce, response-object, product-ids]
---

## Overview

This collected 2026-09-16 Braintree website page is the exact Node.js response-reference route titled "Payment Method Nonce." Its substantive captured content is limited to a product-ID reference: the Braintree gateway returns product IDs for credit and debit card payment methods, and the generally one-to-three-character ID indicates the specific credit product issued to the customer. The table is not a one-code-to-one-product mapping: `I` appears for both Visa Infinite and Visa Infinite Privilege, while `MHD` appears for MasterCard HELOC Debit Standard, Gold, Platninum, and Premium; this snapshot does not determine which repeated row applies. It does not document nonce creation, lookup, lifespan, consumption, or a payment outcome.

## Key takeaways

- This is a collected website response-object reference for the exact Node.js route, not current SDK-package or GitHub implementation evidence.
- The product-ID code/name table is a lookup inventory for credit and debit card payment methods, but its repeated `I` and `MHD` mappings prevent treating every code as uniquely identifying one listed product. Use the raw locators for exact entries rather than reproducing selected rows.
- The page qualifies the product ID as generally one to three characters long. Its title alone does not establish which nonce fields are present in a particular response or how a nonce was created or used.
- Returned descriptive metadata is not proof that a nonce was consumed or that a payment was authorized, captured, settled, or funded.

## Detail locators

- Exact page identity: frontmatter title at lines 5-10 and `# Payment Method Nonce` at line 14.
- Product-ID purpose and general length qualification: `## Product ID codes`, lines 17-21.
- Repeated code mappings: `I` at lines 59-60; `MHD` at line 122 and lines 125-127.
- Complete product-ID code/name inventory: table header at lines 21-22 and rows at lines 23-272.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/response/payment-method-nonce/node-2026-09-16|Braintree Payment Method Nonce response reference - Node.js]] - complete collected page containing the product-ID explanation and code/name table
