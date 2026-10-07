---
title: "Braintree Visa Checkout Card Response (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/visa-checkout-card/node"
raw_files:
  - "braintree/docs/reference/response/visa-checkout-card/node-2026-09-16.md"
tags: [braintree, node-js, response-object, visa-checkout-card, product-id]
---

## Overview

This collected Braintree website page is the Node.js response-reference variant titled `Visa Checkout Card`. Its captured body does not document a request or client integration: the only substantive section defines gateway-returned product ID codes for credit and debit card payment methods. The capture does not establish which response objects contain this object or expose an object-property table, so it is a narrow retrieval route rather than a complete response contract.

## Key takeaways

- The page title and URL identify the Node.js `Visa Checkout Card` response-reference variant, but the `Returned within the following response objects` section contains only two empty list markers in the captured raw. Do not infer a containing response or lifecycle position from that section.
- The product-ID section says the gateway returns product IDs for credit and debit card payment methods and describes the ID as generally one to three characters indicating the specific credit product issued to the customer. The full code-to-label table remains in the raw source rather than being reproduced here.
- The captured table is not a one-code-to-one-label mapping: code `I` appears for both `Visa Infinite` and `Visa Infinite Privilege`, and code `MHD` appears for four different Mastercard product labels. Preserve those captured conflicts when interpreting a returned code.
- This response-reference snapshot does not establish current Visa Checkout or Secure Remote Commerce support, merchant or buyer eligibility, client-side integration behavior, package-qualified Node SDK behavior, or successful authorization, settlement, funding, or other payment execution.

## Detail locators

- Exact source URL, captured date, page title, and Node-routed slug: metadata and frontmatter, lines 1-10.
- Response-object title: `# Visa Checkout Card`, line 14.
- Empty containing-response list: `##### Returned within the following response objects:`, lines 17-22.
- Product-ID purpose, stated one-to-three-character general form, and the malformed table-header join in the capture: `## Product ID codes`, lines 24-29.
- Full product ID code-to-label table: lines 30-279.
- Duplicate `I` labels: lines 66-67; duplicate `MHD` labels: lines 129-134.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/response/visa-checkout-card/node-2026-09-16|Braintree Node.js Visa Checkout Card response reference]] - complete collected page containing the response-reference identity, empty containing-response list, product-ID explanation, and full captured code table
