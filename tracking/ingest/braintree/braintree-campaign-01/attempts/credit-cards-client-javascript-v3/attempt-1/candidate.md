---
title: "Braintree Credit Cards: JavaScript v3 Client-Side Support Boundary"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/credit-cards/client-side/javascript/v3"
raw_files:
  - "braintree/docs/guides/credit-cards/client-side/javascript/v3-2026-09-16.md"
tags: [braintree, javascript-sdk, credit-cards, hosted-fields, card-fields]
---

## Overview

This short Braintree guide is a retrieval entry for choosing a client-side card-entry surface. It records a version-qualified boundary: the JavaScript v3 SDK supports Hosted Fields, not Card Fields.

## Key takeaways

- Braintree's JavaScript v3 SDK does not support Card Fields. The guide lists client-side Card Fields only for Android v5 and iOS v7; those named native versions are separate from JavaScript v3 and should not be generalized to other SDK versions.
- JavaScript v3 supports Hosted Fields. The page points to Hosted Fields for SAQ A eligibility and checkout-design control, but this brief support statement is not a merchant compliance guarantee; use the linked Hosted Fields documentation when implementation or eligibility detail is required.
- Card Fields and Hosted Fields are distinct client-side surfaces in this guide. Support for one must not be projected onto the other.

## Detail locators

- JavaScript v3 Card Fields exclusion and named native alternatives: `# Standard Client-Side Implementation` > `IMPORTANT`, line 18.
- JavaScript v3 Hosted Fields support and SAQ A eligibility wording: `# Standard Client-Side Implementation` > `IMPORTANT`, line 20.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/credit-cards/client-side/javascript/v3-2026-09-16|Braintree JavaScript v3 standard client-side implementation]] - complete guide and SDK-specific Card Fields/Hosted Fields support boundary
