---
title: "Braintree Android Pay Card Response (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/android-pay-card/node"
raw_files:
  - "braintree/docs/reference/response/android-pay-card/node-2026-09-16.md"
tags: [braintree, node-js, response-objects, android-pay, google-pay, product-ids]
---

## Overview

This collected Braintree Node.js website response reference documents the legacy-named Android Pay Card response surface and its product-ID lookup. The page explicitly says that Braintree represents Google Pay cards as Android Pay cards in its API to avoid breaking changes. This is naming and returned-data reference evidence, not a current Google Pay capability, merchant or buyer eligibility, direct-provider behavior, or package-qualified SDK implementation statement.

## Key takeaways

- The page preserves the `Android Pay Card` response name while explaining that Google Pay cards use that representation in the Braintree API for compatibility. The statement explains API naming; it does not establish which platforms, accounts, cards, regions, SDK releases, or transactions currently support Google Pay.
- The Braintree gateway is described as returning product IDs for credit- and debit-card payment methods. A product ID is generally one to three characters and indicates the specific credit product issued to the customer.
- The detailed product-ID code/name inventory, including repeated codes and network- or region-qualified labels, remains in the raw table rather than being restated here. Treat the table as a captured lookup, not as an exhaustive current card-support matrix or a guarantee that a field is populated on every returned object.

## Detail locators

- Legacy Google Pay-to-Android Pay API representation note: `# Android Pay Card`, raw lines 24-25.
- Gateway-returned credit/debit product-ID scope and the generally one-to-three-character description: `## Product ID codes`, raw lines 28-32.
- Exact product-ID code/name inventory and examples: `## Product ID codes`, raw lines 33-283.

## Evidence boundaries

> [!warning] Returned data is not payment-lifecycle proof
> A returned response object or product identifier does not by itself prove request success, authorization, capture, settlement, funding, current availability, or merchant/customer eligibility. The captured `Returned within the following response objects` section contains blank list items, so this entry does not infer or name containing response-object types.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/response/android-pay-card/node-2026-09-16|Braintree Android Pay Card response reference - Node.js]] - complete collected page containing the compatibility naming note and the credit/debit product-ID code table
