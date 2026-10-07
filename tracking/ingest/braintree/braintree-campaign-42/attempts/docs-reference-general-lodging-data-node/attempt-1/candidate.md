---
title: "Braintree Lodging Industry Data (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/lodging-data/node"
raw_files:
  - "braintree/docs/reference/general/lodging-data/node-2026-09-16.md"
tags: [braintree, node-js, lodging, industry-data, interchange, transactions]
---

## Overview

This captured [[braintree]] Node.js website reference describes optional lodging-specific industry data for transactions and displays callback and Promise examples that pass an `industry` object through `gateway.transaction.sale()`. It says a transaction that qualifies for the lodging-industry format under card-network standards may obtain a discounted interchange rate, but limits the captured capability statement to US merchants with Visa and Mastercard transactions and directs merchants to Customer Success to determine whether their merchant account is eligible. This snapshot is not current eligibility, a guaranteed rate, or evidence that a transaction qualified or succeeded.

## Key takeaways

- The displayed examples set `industry.industryType` to `Transaction.IndustryData.Lodging` and place lodging values under `industry.data`. The damaged prose immediately before the parameter table says only that fields can be included "inthecall" and does not identify an operation; therefore the examples support the shown `gateway.transaction.sale()` route, not an inferred broader operation set.
- The table says only one industry type may be sent per transaction. It labels check-in date, check-out date, folio number and property phone as required **to qualify for reduced interchange**; that qualification condition is not presented as unconditional request-body requiredness. The date formats, folio length, phone shape and optional room-rate/tax constraints remain at the raw locators below.
- The table uses snake_case labels such as `industry_type`, `data.check_in_date` and `data.additional_charge`, while the Node examples use camelCase names such as `industryType`, `checkInDate` and `additionalCharges`. Treat the table spellings as captured documentation labels, not as proof that those snake_case names are executable Node request properties; use the displayed Node examples as the page evidence for Node request-key spelling. The snapshot does not resolve whether the table describes an underlying wire representation.
- Multiple additional charges may be supplied, but each charge kind may appear only once and each specified charge requires a kind and amount. The allowed kinds, positive-amount and formatting rules, nine-digit limit, and currency-without-decimals qualification are routed to the raw tables.
- The validation catalog separately requires check-out after check-in and records errors for invalid or unknown lodging fields, dates, boolean indicators, property phone, charge kinds and charge amounts. These cataloged errors do not establish current SDK implementation behavior or successful authorization, settlement, funding, or reduced-interchange assessment.

## Detail locators

- Optional lodging-data purpose, possible discounted-interchange outcome, US merchant and Visa/Mastercard scope, and merchant-account eligibility contact: introductory prose, raw lines 16-23.
- `industry_type` and one-industry-type limit: `## Parameters`, raw lines 26-34.
- Check-in/check-out formats, reduced-interchange qualification fields, folio and property-phone limits, and room-rate/tax constraints: `## Parameters`, raw lines 35-64.
- No-show, advance-deposit and fire-safety indicators: `## Parameters`, raw lines 65-91.
- Additional-charge multiplicity, uniqueness, allowed kinds and required amount: `## Parameters`, raw lines 92-118.
- Callback `gateway.transaction.sale()` example and camelCase Node request keys: `## Example > ### callback`, raw lines 121-155.
- Promise `gateway.transaction.sale()` example: `## Example > ### Promise`, raw lines 157-189.
- Lodging validation codes, including date order, amount, format, size, boolean and phone checks: `## Validation errors > ### Lodging data`, raw lines 191-215.
- Additional-charge kind, uniqueness, amount, format, size, required-attribute and type errors: `## Validation errors > ### Lodging data additional charges`, raw lines 217-262.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/lodging-data/node-2026-09-16|Braintree Lodging Industry Data (Node.js)]] — fully read 2026-09-16 website snapshot
