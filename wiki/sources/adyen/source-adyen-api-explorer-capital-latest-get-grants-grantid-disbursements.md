---
title: "Adyen Capital API v1: list a grant's disbursements"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/get/grants/(grantId)/disbursements"
raw_files:
  - "adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/2026-11-07.md"
tags: [adyen, capital, grants, disbursements]
---

## Overview

This 2026-11-07-captured Capital API `latest` `/capital/v1` GET reference lists disbursements related to one grant. The page lists both Test and Live server bases. This is a lookup of grant-disbursement records, not a request to create a grant or disburse funds. See [[adyen]] and [[adyen-capital]].

## Key takeaways

- The only documented input is required string path `grantId`, the grant-reference identifier. No query parameters or request body are shown. The `200` response marks `disbursements` required as an array of related records; the page gives no pagination, default, or count limit.
- Each listed record's required fields include account-holder recipient ID, balance-account recipient ID, disbursement `id`, `grantId`, `amount`, `balances`, `fee`, and `repayment`. `amount.value` is an integer in minor units with a three-character currency; `balances` includes currency, fee, principal, and total repayable, where total is fee plus principal. `repayment.basisPoints` represents the configured share of incoming net volume deducted for repayment. The full nested schema is in the pinned raw.
- `fundsCollections` is optional and describes accounts Adyen uses to collect repayment-related funds, with optional `accountIdentification` and `fundsCollectionType` (`UnscheduledRepayment` or `Revocation`). Its absence does not establish the absence of repayment obligations.
- The listed errors are 404 entity not found and 422 validation error. A `200` readback documents the returned disbursement records and repayment configuration; it does not independently prove transfer booking, external bank receipt, current grant eligibility, or repayment completion. This endpoint page does not specify an authentication role or idempotency contract.

## Detail locators

- Pinned raw, lines 5–22: lookup purpose, Test/Live `/capital/v1` servers, and path input.
- Pinned raw, lines 24–52: `200` response, recipient/grant/disbursement identities, minor-unit amounts, balances, fee, optional collection accounts, and repayment basis points.
- Pinned raw, lines 55–90: 404 and 422 responses, with optional problem fields and nested validation-error fields. There are no JSON examples in this capture.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/2026-11-07|Capital grant-disbursements GET reference, captured 2026-11-07]]
