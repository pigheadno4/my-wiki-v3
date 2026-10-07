---
title: "Braintree Apple Pay Card Response (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/apple-pay-card/node"
raw_files:
  - "braintree/docs/reference/response/apple-pay-card/node-2026-09-16.md"
tags: [braintree, node-js, apple-pay, response-objects, product-id-codes]
---

## Overview

This collected Braintree website page is the Node.js Apple Pay Card response reference. Its captured content names the response-object type and provides a product-ID lookup for credit and debit card payment methods; it does not document a native-client API, direct Apple integration, or a complete Apple Pay payment flow.

## Key takeaways

- The page says the Braintree gateway returns product IDs for credit and debit card payment methods.
- It describes a product ID as generally one to three characters and as indicating the specific credit product issued to the customer. The full code-to-name inventory belongs to the raw locator below rather than being reproduced here.
- The captured "Returned within the following response objects" list contains two empty bullets, so this snapshot does not establish which containing response objects expose Apple Pay Card data.
- The table includes repeated codes paired with different product names, including `I` and `MHD`; do not infer from this page that the displayed code alone is a unique product-name key.
- A returned field or code is retrieval metadata, not proof of authentication, card or merchant eligibility, payment acceptance, authorization, settlement, funding, or any later lifecycle outcome.

## Detail locators

- Apple Pay Card response-reference title: `# Apple Pay Card`, line 14.
- Empty containing-response-object list: `##### Returned within the following response objects:`, lines 17-21.
- Gateway product-ID purpose and general one-to-three-character description: `## Product ID codes`, lines 24-28.
- Complete product-ID-code and product-name table, including repeated-code entries: `## Product ID codes`, lines 28-279.

## Evidence boundaries

> [!warning] Snapshot and scope boundary
> This is a collected Node.js website reference, not current product documentation, native Apple SDK authority, direct Apple authority, GitHub implementation evidence, or authority for sibling Braintree SDKs. Its field and token labels do not establish authentication, merchant configuration, acceptance, execution, or lifecycle success.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-apple-pay]]
- Node.js server integration boundary: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/response/apple-pay-card/node-2026-09-16|Braintree Apple Pay Card response reference - Node.js]] - complete collected page containing the response-object heading and product-ID-code table
