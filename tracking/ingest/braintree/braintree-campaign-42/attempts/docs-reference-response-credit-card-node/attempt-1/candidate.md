---
title: "Braintree Credit Card Response Reference (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/credit-card/node"
raw_files:
  - "braintree/docs/reference/response/credit-card/node-2026-09-16.md"
tags: [braintree, node-js, credit-cards, response-objects, product-ids]
---

## Overview

This collected Braintree Node.js website response reference is a retrieval page for Credit Card response data. Its substantive captured content is a policy-qualified lookup table for product ID codes returned by the Braintree gateway for credit and debit card payment methods; the codes identify the specific credit product issued to the customer. It is not a card-creation or transaction-operation guide.

## Key takeaways

- The page says a product ID is generally one to three characters and indicates the specific credit product issued to the customer. The full code-to-product-name inventory remains at the raw locator rather than being reproduced here.
- Returned results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. The external policy is not part of this raw, so this entry preserves the limitation without interpreting field availability.
- The captured heading "Returned within the following response objects" is followed by two blank list items. This snapshot therefore does not identify the containing response-object names and is not evidence of a complete Credit Card property schema.
- A returned product ID or other response-field presence is descriptive response metadata; it does not by itself prove payment execution, authorization, capture, settlement or funding.

## Detail locators

- Results-limitation notice: `# Credit Card`, lines 17-18.
- Damaged returned-within list with two blank entries: `# Credit Card`, lines 21-25.
- Product-ID purpose, general length and complete code-to-name table: `## Product ID codes`, lines 28-281.

## Evidence boundaries

> [!warning] Returned metadata is not transaction outcome proof
> This collected Node.js website reference documents a product-ID lookup and a policy limitation. It does not establish current SDK implementation behavior, merchant or card eligibility, field presence in a particular response, or successful authorization, capture, settlement or funding.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/response/credit-card/node-2026-09-16|Braintree Credit Card response reference - Node.js]] - complete collected page containing the policy notice, damaged returned-within list and product-ID lookup table
