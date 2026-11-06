---
title: "Get Capital grant details by grant ID"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/get/grants/(grantId)"
raw_files:
  - "adyen/api-explorer/capital/latest/get/grants/(grantId)/2026-11-07.md"
tags: [adyen, capital, grants, api-explorer]
---

## Overview

Captured Capital API v1 GET reference for details of one grant selected by `grantId`. This is a grant read, separate from a grant offer, grant account and disbursement. See [[adyen]] and [[adyen-capital]].

## Key takeaways

- The required path `grantId` is the unique grant-reference identifier. Captured TEST and LIVE bases are `https://balanceplatform-api-test.adyen.com/capital/v1` and `https://balanceplatform-api-live.adyen.com/capital/v1`.
- A 200 body requires `balances` with currency, fee, principal and total; `total` is fee plus principal. It also requires `grantAccountId`, selected `grantOfferId`, grant `id`, and `status.code`. Optional `counterparty` can identify an account holder, disbursement balance account or transfer instrument, with stated ownership relationships. Optional `status.actions` supplies action codes and resolved flags. Exact schema and status values are in the raw.
- Status codes include Pending, Active, Repaid, WrittenOff, Failed, Revoked, Requested, Reviewing, Approved, Rejected and Cancelled. A readback of these fields is not itself proof of disbursement, bank receipt, repayment booking or current eligibility. The operation documents 404 entity not found and 422 validation errors; it gives no state-transition, idempotency or propagation contract.

## Detail locators

- Purpose, v1 TEST/LIVE servers and required ID: raw lines 5–22.
- 200 grant balances, IDs, optional recipient and status/action fields: raw lines 24–48.
- 404 and 422 error schemas: raw lines 51–86.

## Related

- [[adyen-capital]] — financing product and evidence boundaries.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/2026-11-07|Capital grant detail GET, captured 2026-11-07]]