---
title: "Braintree Amex Direct Industry-Specific Fields (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-direct-industry-specific/node"
raw_files:
  - "braintree/docs/guides/amex-direct-industry-specific/node-2026-09-16.md"
tags: [braintree, node-js, amex-direct, transactions, industry-data, lodging, travel]
---

## Overview

This captured [[braintree]] Node.js website guide describes optional industry-specific data that may be sent on transactions when the gateway uses an American Express Direct processor connection. Its scope is the American Express-defined Lodging and Travel/Cruise industry types, and it limits a transaction to data for one industry type. The snapshot does not establish current merchant eligibility or enablement, an exact Node package or runtime contract, interchange treatment, or successful authorization, settlement or funding.

## Key takeaways

- For Travel/Cruise, the page labels `travelPackage` as required and identifies flight, car, both, or neither as the four represented choices. Departure date, lodging check-in/check-out dates and lodging name are labeled optional; exact captured formats and the lodging-name length limit remain at the raw locator.
- For Lodging, the page labels folio number, check-in date and check-out date as required and room rate as optional. Its captured prose gives a 12-character alphanumeric limit for the folio number and date/amount formatting descriptions; use the raw locator for those routine constraints.
- Callback and Promise examples call `gateway.transaction.sale()` with `industry.industryType` set to `Transaction.IndustryData.TravelAndCruise` or `Transaction.IndustryData.Lodging`, and place the corresponding fields under `industry.data`. They are examples, not evidence of current package-qualified SDK behavior or a successful payment.

> [!warning] Snapshot and execution boundary
> The page does not identify a Node SDK package version or runtime version, say how the Amex Direct processor connection is enabled, establish merchant or transaction eligibility, promise interchange treatment, or prove that any example request was accepted or completed.

## Detail locators

- Optional industry-data purpose, Amex Direct processor-connection condition, Lodging and Travel/Cruise scope, and one-industry-type-per-transaction limit: introductory prose, raw lines 16-19.
- Travel/Cruise field requiredness, permitted travel-package values, date formats and lodging-name limit: `## Travel/cruise industry parameters`, raw line 22.
- Travel/Cruise callback and Promise sale examples: raw lines 27-68.
- Lodging field requiredness, folio constraint, date formats and room-rate description: `## Lodging industry parameters`, raw line 72.
- Lodging callback and Promise sale examples: raw lines 77-116.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-direct-industry-specific/node-2026-09-16|Braintree Amex Direct industry-specific fields (Node.js)]] — fully read 2026-09-16 website snapshot
