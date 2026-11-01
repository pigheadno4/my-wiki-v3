---
title: "Adyen Capital API v1: list an account holder's grants"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/get/grants"
raw_files:
  - "adyen/api-explorer/capital/latest/get/grants/2026-09-15.md"
tags: [adyen, capital, grants, api]
---

## Overview

This 2026-09-15-captured Capital API Explorer reference documents `GET /grants` on the Capital API v1 test and live servers. It returns a list of grants for the account holder identified by the required `counterpartyAccountHolderId` query parameter. This is grant readback, not an offer-selection or funding request.

## Key takeaways

- A 200 response requires a `grants` array. Each listed grant requires `balances`, `grantAccountId`, `grantOfferId`, `id`, and `status`. Within `balances`, `currency`, `fee`, `principal`, and `total` are required; `total` is described as fee plus principal, the amount the user must repay. These are schema fields for each returned grant, not proof of a current payout or repayment.
- The optional `counterparty` object can identify the recipient account holder, balance account for disbursement, or transfer instrument for disbursement. The balance account must belong to the specified holder; a transfer instrument must belong to that holder's legal entity. The required grant `status.code` includes `Pending`, `Active`, `Repaid`, `WrittenOff`, `Failed`, `Revoked`, `Requested`, `Reviewing`, `Approved`, `Rejected`, and `Cancelled`; optional `status.actions` lists steps to proceed. A listed status is readback at the request time, not a guarantee of later transition.
- The page specifies 404 for an entity not found and 422 for request validation. Their optional problem fields include `invalidFields`, whose individual `message`, `name`, and `value` are required when an invalid-field entry appears. No request/response example, response header or authorization-specific rule is shown in this captured page.

## Detail locators

- Purpose and Capital v1 test/live server URLs: raw lines 5–15.
- Required query parameter: raw lines 17–22.
- 200 grant list, identities, balances, recipient and status schema: raw lines 24–47.
- 404 and 422 error schemas: raw lines 50–85.

## Related

- [[adyen]] — provider.
- [[adyen-capital]] — Capital grant lifecycle and funding context.
- [[source-adyen-api-explorer-transfers-latest-get-grants]] — separate Transfers API v4 grant-list contract with a different query shape.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/get/grants/2026-09-15|Capital API v1 GET /grants (captured 2026-09-15)]]
