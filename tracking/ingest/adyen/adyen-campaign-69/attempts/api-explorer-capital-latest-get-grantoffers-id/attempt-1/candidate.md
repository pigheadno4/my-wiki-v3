---
title: "Capital API v1: get a static grant offer"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/get/grantOffers/(id)"
raw_files:
  - "adyen/api-explorer/capital/latest/get/grantOffers/(id)/2026-11-07.md"
tags: [adyen, capital, grant-offer, api-reference]
---

## Overview

This captured Capital API v1 `GET /grantOffers/{id}` reference returns details of one static offer identified by required path `id`. The page lists both TEST and live Balance Platform Capital API hosts. An offer lookup is separate from grant creation, acceptance, disbursement, or repayment. See [[adyen]] and [[adyen-capital]].

## Key takeaways

- The 200 response requires `accountHolderId`, identifying the account holder to whom the grant is offered. The response's `id`, `amount`, `contractType`, validity timestamps, `fee`, and `repayment` are optional in the table; optional parents do not guarantee their nested fields appear.
- If present, `amount` and fee amount values use minor units. `contractType` can be `loan` or `cashAdvance`. `repayment.basisPoints` describes the share of incoming net volume deducted for repayment; `maximumDays` applies only when the contract type is `loan`.
- The listed errors are 404 entity not found and 422 request validation error. This read contract states no offer selection, guarantee of eligibility, funding state, or payment outcome.

## Detail locators

- Identity, TEST/live hosts, and required path ID: raw lines 5–22.
- 200 response fields, conditional nesting and units: raw lines 24–51.
- 404 and 422 error schemas: raw lines 54–89.

## Related

- [[adyen-capital]] — Capital offer and grant context.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/get/grantOffers/(id)/2026-11-07|Capital API v1 static grant-offer lookup (2026-11-07)]]
