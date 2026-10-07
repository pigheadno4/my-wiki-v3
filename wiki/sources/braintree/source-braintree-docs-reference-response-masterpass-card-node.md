---
title: "Braintree Masterpass Card Response Reference (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/masterpass-card/node"
raw_files:
  - "braintree/docs/reference/response/masterpass-card/node-2026-09-16.md"
tags: [braintree, node-js, masterpass, response-objects, product-ids]
---

## Overview

This collected Braintree Node.js website response reference is a retrieval page for Masterpass Card response data. Its substantive captured content is a generic lookup table for product ID codes returned by the Braintree gateway for credit and debit card payment methods; the codes indicate the specific credit product issued to the customer. It is not an integration, card-creation or transaction-operation guide.

## Key takeaways

- The page says a product ID is generally one to three characters and indicates the specific credit product issued to the customer. However, the captured table maps `I` to both Visa Infinite and Visa Infinite Privilege, and maps `MHD` to MasterCard HELOC Debit Standard, Gold, Platninum and Premium. This snapshot does not resolve which row applies, so it does not establish a one-code-to-one-product mapping. The complete code-to-product-name inventory remains at the raw locator rather than being reproduced here.
- The captured heading "Returned within the following response objects" is followed by two blank list items. This snapshot therefore does not identify the containing response-object names and is not evidence of a complete Masterpass Card property schema.
- Although the page title and URL identify Masterpass Card, the table's description is generic to credit and debit card payment methods. The snapshot does not establish current Masterpass availability or that every listed product necessarily occurs in a Masterpass Card response.
- A returned product ID or response object is descriptive response data; it does not by itself prove payment execution, authorization, capture, settlement or funding.

## Detail locators

- Page identity: `# Masterpass Card`, line 14.
- Damaged returned-within list with two blank entries: `# Masterpass Card`, lines 17-21.
- Product-ID purpose, general length and complete code-to-product-name table: `## Product ID codes`, lines 24-280.
- Repeated code mappings: `I` at lines 66-67; `MHD` at lines 129 and 132-134.

## Evidence boundaries

> [!warning] Title and captured body do not prove wallet availability or payment outcome
> This collected Node.js website reference supplies a product-ID lookup under a Masterpass Card route. It does not establish current wallet availability, merchant or buyer eligibility, exact Node SDK implementation behavior, field presence in a particular response, or successful authorization, capture, settlement or funding.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/response/masterpass-card/node-2026-09-16|Braintree Masterpass Card response reference - Node.js]] - complete collected page containing the damaged returned-within list and product-ID lookup table
