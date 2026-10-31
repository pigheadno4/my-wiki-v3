---
title: "Adyen Fund API v6: Get account-holder balances"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/post/accountHolderBalance"
raw_files:
  - "adyen/api-explorer/Fund/latest/post/accountHolderBalance/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, account-holders, balances]
---

## Overview

This Fund API Explorer snapshot, captured 2026-09-15 under `Fund/latest`, documents POST `/accountHolderBalance` on the displayed Fund v6 test server. It retrieves balances for a Classic Platforms account holder, with accounts and their currency-specific balances distinguished from a holder-level total. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The request-body table requires `accountHolderCode`; the example supplies only that holder code. This is a balance lookup, with no transfer or payout request field (raw lines 12–26).
- The response schema separates optional `balancePerAccount`, a list of accounts identified by `accountCode` with `detailBalance`, from optional `totalBalance` for the holder. Both describe `balance`, `onHoldBalance` and `pendingBalance` lists; the holder-total list entries specify three-character currency and integer minor-unit value (raw lines 32–59, 65–92). Do not merge accounts or currencies into one fungible amount, or treat `onHoldBalance` or `pendingBalance` as an available-to-transfer figure.
- The page lists 200 for a succeeded request and 202 for acceptance before processing completes; both have the same optional field schema. Neither heading provides an actual balance example or demonstrates that money moved, a payout was initiated, or funds became transferable (raw lines 27–92).
- The listed errors are 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing. The page names no specific permission or eligibility rule (raw lines 95–157).

## Detail locators

- Purpose, displayed test server, required request property and JSON request example: raw lines 5–26.
- 200 and 202 descriptions and full balance schemas: raw lines 27–92. The nested `currency` and `value` properties are marked required within the holder-total balance list entries; that does not make their parent `totalBalance` object required.
- Error categories and optional error-body fields: raw lines 95–157. The generic error body's `pspReference` description mentions a payment; this endpoint is a balance lookup, and that wording does not establish a payment.

## Related

- [[adyen-classic-platforms]] — Classic holder/account model and reciprocal source route.
- [[adyen-platforms]] — separate newer balance-platform resource model.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/post/accountHolderBalance/2026-09-15|Fund API Explorer POST accountHolderBalance, captured 2026-09-15]]
