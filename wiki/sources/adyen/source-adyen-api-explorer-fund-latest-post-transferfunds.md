---
title: "Adyen Fund API v6 POST /transferFunds"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/post/transferFunds"
raw_files:
  - "adyen/api-explorer/Fund/latest/post/transferFunds/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, fund-transfers]
---

## Overview

This captured Classic Fund API v6 `POST /transferFunds` reference initiates a transfer that debits one platform account and credits another **within the same platform**. The accounts may belong to different account holders. It is a Classic account-to-account transfer, not an external bank payout or a newer Balance Platform transfer. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The body requires `amount` with three-character ISO `currency` and integer `value` in minor units, `sourceAccountCode`, `destinationAccountCode`, and `transferCode`; `merchantReference` is optional for linking transactions. The source account holder must be **Active** and allow payouts; the destination holder must be **Active**. The example's `TransferCode_1` and EUR 2000 minor units are illustrative, not universal defaults. See raw lines 14–38.
- The overview says the platform should determine a transfer code in compliance with local regulations; this API table says permitted codes vary by platform account and are defined in its service level agreement. These are captured documentation conditions, not a current regulatory determination or a global code enum. See raw lines 5–7 and 20–23.
- The companion [[source-adyen-docs-classic-platforms-fund-transfer]] adds setup and outcome conditions: Adyen Support enables fund transfers and defines codes, the destination holder must also allow processing, and the asynchronous result comes through `TRANSFER_FUNDS`. Its destination processing condition is **additional to** this operation table's Active-only wording; retain both scoped statements. See that guide's raw lines 30–48 and 68–81.
- `200` is labeled request succeeded. `202` explicitly means accepted for processing but **not completed**. Both response tables mark `invalidFields`, `merchantReference`, `pspReference` and `resultCode` optional; `pspReference` identifies the request. Neither an HTTP receipt nor an optional reference proves the transfer reached the destination account. The companion guide says even `resultCode: Received` is receipt only and directs outcome tracking to the webhook. See raw lines 39–74 and the companion guide's raw lines 68–81.
- `merchantReference` links transactions; this page does not describe it as an idempotency key. Error classes are 400, 401, 403, 422 and 500, with authentication required and insufficient-permission descriptions for 401/403. See raw lines 21, 77–139.

## Detail locators

- Same-platform scope, historical transfer-code wording, TEST v6 server: raw lines 5–10.
- Required request properties, account-holder gates and example: raw lines 14–38.
- 200/202 result boundary and optional fields: raw lines 39–74.
- Error classes and generic error-body schema: raw lines 77–139.

## Related

- [[adyen-classic-platforms]] — Classic account and money-flow context.
- [[source-adyen-docs-classic-platforms-fund-transfer]] — Support setup, destination processing gate, asynchronous webhook result and reversal guide.
- [[adyen-platforms]] — separate newer balance-platform model.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/post/transferFunds/2026-09-15|POST /transferFunds, captured 2026-09-15]]
