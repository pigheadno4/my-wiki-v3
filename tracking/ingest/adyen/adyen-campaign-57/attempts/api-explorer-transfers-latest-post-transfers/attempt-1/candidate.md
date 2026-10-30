---
title: "Adyen Transfers API v4: initiate a funds transfer"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/post/transfers"
raw_files:
  - "adyen/api-explorer/transfers/latest/post/transfers/2026-09-15.md"
tags: [adyen, transfers, balance-platform, payouts, api-reference]
---

## Overview

Captured Transfers API reference for `POST /transfers` on the listed test `btl/v4` server. It starts a request to move funds to a balance account, transfer instrument, third-party bank account, or third-party card; Adyen reports the outcome by webhooks. The page says Transfers API versions 1 and 2 are deprecated and directs new implementations to the latest version. The `latest` URL here shows a v4 test endpoint, not proof of current live availability. See [[adyen]], [[adyen-platforms]], [[adyen-platform-internal-transfers]], [[adyen-business-accounts]], and [[adyen-payouts]].

## Key takeaways

- Use requires the **TransferService Webservice Initiate** API-credential role and required account-holder capabilities; the page says to contact Adyen to set up the permissions (raw lines 21–30). An optional `WWW-Authenticate` header is for SCA and an optional `Idempotency-Key` is limited to 64 characters (lines 34–38); the page gives no retry or deduplication outcome guarantee.
- The request-property table marks `amount` (currency and minor-unit value), `category`, and `counterparty` required. The counterparty must identify a balance account, bank account, card, or transfer instrument; nested bank/card details and country/currency-dependent bank fields have their own conditions (lines 41–58). The page does not separately state request-body requiredness. `balanceAccountId` is an optional source balance-account ID; a virtual `bankAccount` source requires its `paymentInstrumentId`, whereas supplying only a balance-account ID selects the assigned default physical `bankAccount` instrument (lines 47, 63). These source IDs are distinct from the counterparty transfer-instrument ID.
- For bank-category transfers, both `priorities` and `priority` rows say they are required, although each row is marked `No` and the bank request examples supply only singular `priority`. Treat their exact combined requirement as unresolved; `priorities` documents ordered fallback attempts and `priority` a single route (lines 64–65, 94–204, 295–312). `executionDate`, if supplied, must be within 30 days; until then status stays `received` and reason `pending`; the timezone defaults to `Europe/Amsterdam` (lines 60–62). Optional review settings specify approval count and Business Account-only SCA on approval (lines 68–70).
- Both documented `200` and `202` success responses say the request was **accepted for processing, not completed** (lines 313–316, 399–400). The response status descriptions distinguish `received`, `refused`, `authorised` (reserved), `booked` (source-balance deduction), `failed`, and `returned` (lines 374, 458). A `booked` source deduction is not beneficiary-bank receipt; use subsequent transfer webhooks to assess outcome.
- Errors listed are `401` authentication required, `403` insufficient permissions, `422` request validation, and `500` server failure (lines 483–568). The request schema also has optional `type` values for bank push, internal push, and internal pull transfers, and optional `ultimateParty` details with card/bank conditions; see the raw for exact combinations (lines 71–92). Example request and response records are illustrations, not live route, fee, timing, or payment guarantees.

## Detail locators

- Full request schema and conditional fields: raw lines 41–92. Request examples (bank, internal, card): lines 94–312. `200` and `202` response schemas: lines 313–480; error schemas: lines 483–568; response examples: lines 570–930.

## Related

- [[adyen-platforms]] — platform and user model.
- [[adyen-platform-internal-transfers]] — internal balance-account transfer flow.
- [[adyen-business-accounts]] — conditional Business Account review/SCA route.
- [[adyen-payouts]] — separate payout product routes and lifecycle.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/post/transfers/2026-09-15|POST /transfers API reference, captured 2026-09-15]]
