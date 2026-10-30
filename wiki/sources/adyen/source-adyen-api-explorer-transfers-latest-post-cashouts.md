---
title: "Adyen Transfers API v4: initiate a cashout"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/post/cashouts"
raw_files:
  - "adyen/api-explorer/transfers/latest/post/cashouts/2026-09-15.md"
tags: [adyen, platforms, cashout, transfers-api, payouts]
---

## Overview

This captured Transfers API v4 test-server reference documents `POST /cashouts`, which initiates a cashout request from an instructing balance account. It is a request/response contract, not proof that funds have settled or reached a bank. See [[adyen]], [[adyen-platforms]], and the separate [[source-adyen-docs-platforms-cash-out-instantly-cashout-request]] guide for enablement, capability, route, balance, and asynchronous outcome conditions.

## Key takeaways

- The request schema requires `instructingBalanceAccountId` and `amount` with currency and value in minor units. The optional `counterparty.transferInstrumentId` identifies a payout destination; without it, cashout funds remain in the instructing balance account after the cashout transfer settles. The top-level `transferInstrumentId` is present but marked to use `counterparty.transferInstrumentId` instead.
- `fee` is optional; its nested `amount` and currency/value are required when that object is supplied. `description` and `referenceForBeneficiary` are allowed and returned only with `counterparty.transferInstrumentId`; the page specifies supported characters and automatic-generation behavior at the request table.
- A 200 marks the request successful. Its response has a cashout `id` and a `transfers` array. The listed transfer types are `cashoutRepayment` and `cashoutFee`; their presence and amounts in the example are illustrative, not evidence of completed repayment, fee debit, bank credit, or settlement.
- Errors listed are 400, 401, 403, 404, 422, 429 and 500. This reference says 401 is an invalid API credential and 403 is insufficient permission, but names no particular roles, capability grants, bank routes, or live-account eligibility. The captured server is `https://balanceplatform-api-test.adyen.com/btl/v4`; `latest` does not identify a fixed current release.

## Detail locators

- Purpose and test server: pinned raw lines 5–10.
- Required and conditional request fields, plus example: pinned raw lines 14–53.
- 200 response fields, transfer types and example: pinned raw lines 54–81, 216–259.
- Error statuses and schemas: pinned raw lines 84–214.

## Related

- [[adyen-platforms]] — principal platform concept.
- [[source-adyen-docs-platforms-cash-out-instantly-cashout-request]] — separate Platforms prerequisites, checks, constraints, webhooks and failure route.
- [[source-adyen-docs-platforms-cash-out-instantly-cashout-webhooks]] — separate asynchronous leg tracking.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/post/cashouts/2026-09-15|Captured POST /cashouts API Explorer page]]
