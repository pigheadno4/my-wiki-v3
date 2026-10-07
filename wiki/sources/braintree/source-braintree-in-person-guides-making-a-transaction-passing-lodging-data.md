---
title: "Braintree In-Person Passing Lodging Data"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/making-a-transaction/passing-lodging-data"
raw_files:
  - "braintree/in-person/guides/making-a-transaction/passing-lodging-data-2026-09-16.md"
tags: [braintree, in-person, card-present, lodging, graphql]
---

## Overview

This collected Braintree website guide covers passing lodging data on card-present Auth and Charge requests for hotels and hospitality merchants. The page is an unversioned website snapshot with body metadata updated 2025-01-03 and raw fetched 2026-09-16; it is not current account-eligibility, exact deployed-schema, network-acceptance or payment-outcome evidence.

## Key takeaways

- The page permits lodging data on the `requestAuthorize` and `requestCharge` mutations and on a `captureTransaction` request. Its example uses `requestAuthorize`; that example does not establish current field acceptance, authorization, capture, settlement or funding.
- Eligibility is limited on this page to hotel or other eligible merchant types under MCC 7011. Merchants outside the listed MCC are not eligible to pass lodging data to Braintree.
- The Braintree gateway must be enabled to pass lodging-data fields; the page directs merchants to a Solutions Engineer or Integration Engineer for account enablement. Supplying fields alone does not prove enablement or eligibility.
- The page says the data may help lower card-network interchange fees and describes forwarding passed lodging data to card networks. This is a qualified purpose statement, not proof of current network acceptance or a guaranteed interchange result.
- Lodging data is not supported for offline transactions; passing these fields on an offline transaction produces an API error.

> [!warning] Scope and outcome boundaries
> This source concerns card-present Braintree In-Person operations only. It does not establish card-not-present behavior, current merchant or account eligibility, gateway enablement, exact current GraphQL validation, network acceptance, a lower interchange rate, or any authorization, capture, settlement or funding outcome.

## Detail locators

- Card-present Auth/Charge scope and hospitality context: introduction, line 16.
- Qualified interchange purpose and merchant-type eligibility: `## Feature Overview`, lines 19-31; the sole listed eligible MCC is 7011 at lines 24-31.
- Supported request operations and the `requestAuthorize` example boundary: `## Passing Lodging Data`, line 36.
- Required Braintree gateway enablement and engineering contact route: `## Passing Lodging Data`, lines 38-39.
- Exact sample lodging input names and values, including folio, dates, rates, flags, property phone and additional-charge entries: `## Passing Lodging Data`, line 44. Treat the sample as illustrative rather than a complete current schema or required-field specification.
- Control Panel viewing route and the page's card-network forwarding statement: `## Viewing Lodging Data in the control panel`, lines 45-47.
- Offline exclusion and API-error consequence, plus the authorize/charge/separate-capture operation summary: `## Important Tips for passing Lodging Data`, lines 50-56.

## Related raw API references

The captured page links to the card-present authorization and capture guide, the main transaction guide's reader-charge section, the GraphQL `IndustryLodgingInput` reference, the offline-transactions guide, the Level 2/Level 3 processing guide and the vaulting/customers guide. Except for the separately ingested sources discoverable elsewhere in the wiki, those link targets were not read as evidence for this entry; they are navigation only here.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Raw Sources

- [[raw/braintree/in-person/guides/making-a-transaction/passing-lodging-data-2026-09-16|Braintree In-Person Passing Lodging Data guide]] - complete collected page covering eligible card-present operations, MCC and account-enablement conditions, illustrative lodging fields, Control Panel navigation and the offline exclusion
