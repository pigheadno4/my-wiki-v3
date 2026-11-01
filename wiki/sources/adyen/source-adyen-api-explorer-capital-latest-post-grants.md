---
title: "Adyen Capital API v1 grant request"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/post/grants"
raw_files:
  - "adyen/api-explorer/capital/latest/post/grants/2026-09-15.md"
tags: [adyen, capital, grants, api]
---

## Overview

This captured Capital API v1 `POST /grants` reference lets a platform request a grant on behalf of an account holder using a selected offer and a grant account. It lists separate TEST and LIVE `/capital/v1` bases. This is grant-request and response documentation, not evidence that a specific offer was accepted, a grant was disbursed, or funds reached a recipient. See [[adyen]] and [[adyen-capital]].

## Key takeaways

- The request requires `grantAccountId` (the account that tracks the grant) and `grantOfferId` (the selected offer). The `counterparty` object is optional. If used, its optional `balanceAccountId` must belong to the specified account holder; its optional `transferInstrumentId` must belong to that account holder's legal entity.
- The 200 response schema requires `balances` (`currency`, `fee`, `principal`, `total`), `grantAccountId`, `grantOfferId`, grant reference `id`, and `status`. `total` is fee plus principal. The status object's `code` is required and can include `Requested`, `Reviewing`, `Approved`, `Rejected`, `Pending`, `Active`, `Repaid`, `WrittenOff`, `Failed`, `Revoked` or `Cancelled`; optional actions carry required `actionCode` and `resolved` fields when present. A successful HTTP response does not itself identify which grant status was returned.
- A 422 response is a request validation error. Its problem fields are optional at top level; within an `invalidFields` item, `message`, `name`, and `value` are marked required. The page provides no request/response example or authorization/disbursement timing.

## Detail locators

- Operation and TEST/LIVE servers: pinned raw lines 5–15.
- Request body and destination ownership conditions: lines 17–26.
- 200 grant response and status schema: lines 28–52.
- 422 validation-error schema: lines 55–71.

## Related

- [[adyen-capital]]
- [[source-adyen-api-explorer-capital-webhooks-latest-post-balanceplatform-grants-created]]
- [[source-adyen-api-explorer-capital-webhooks-latest-post-balanceplatform-grants-updated]]

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/post/grants/2026-09-15|Capital POST grants API Explorer capture]]
