---
title: "Braintree Countries Reference (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/countries/node"
raw_files:
  - "braintree/docs/reference/general/countries/node-2026-09-16.md"
tags: [braintree, node-js, server-sdk, countries, billing-address]
---

## Overview

This captured [[braintree]] Node.js-routed website reference states that a country can be specified by name, alpha-2 code, alpha-3 code or numeric code. It illustrates those representations as billing-country inputs in callback and Promise examples of `gateway.transaction.sale()`, and separately notes an `Unknown` value when the card's country of issuance cannot immediately be determined from its bank identification number (BIN).

## Key takeaways

- The displayed billing fields are `countryCodeAlpha2`, `countryCodeAlpha3`, `countryCodeNumeric` and `countryName`; the examples use `US`, `USA`, `840` and `United States of America`, respectively. These are examples of the page's stated input representations, not a complete validation or country-coverage matrix.
- Every representation is shown in both callback and Promise forms of `gateway.transaction.sale()`. The page does not state that the four fields should be sent together or establish their behavior for other objects or operations.
- `## List of countries` contains no country entries in the captured raw. The following note concerns a returned card country of issuance inferred from the BIN, which is distinct from the merchant-supplied billing-country inputs above.

## Detail locators

- Stated country input representations: introductory sentence, raw line 16.
- Alpha-2 callback and Promise examples using `billing.countryCodeAlpha2`: `## Alpha-2 code`, raw lines 19-46.
- Alpha-3 callback and Promise examples using `billing.countryCodeAlpha3`: `## Alpha-3 code`, raw lines 48-75.
- Numeric callback and Promise examples using `billing.countryCodeNumeric`: `## Numeric code`, raw lines 77-104.
- Country-name callback and Promise examples using `billing.countryName`: `## Country name`, raw lines 106-133.
- Empty country-list section and the BIN-derived issuance-country `Unknown` note: `## List of countries`, raw lines 135-140.

## Evidence limitations

> [!warning] Scope of this snapshot
> The URL is routed to the Node.js SDK family, but this unversioned website snapshot names no package version, Node runtime, environment or effective-time guarantee. Its country inputs do not establish merchant-country eligibility, payment-method or card coverage, current gateway acceptance, authorization or settlement success, and the empty country-list section supplies no supported-country inventory.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/countries/node-2026-09-16|Braintree Countries Reference (Node.js)]] — fully read 2026-09-16 website snapshot
