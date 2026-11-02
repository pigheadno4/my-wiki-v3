---
title: "Balance Control API v2 balance transfer | Adyen API Explorer"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BalanceControl/latest/post/balanceTransfers"
raw_files:
  - "adyen/api-explorer/BalanceControl/latest/post/balanceTransfers/2026-09-15.md"
tags: [adyen, balance-control, balance-transfers, merchant-accounts, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Balance Control API `POST /balanceTransfers` for moving balances between **merchant accounts**. Its Test and Live server bases both end in `/balance-control/api/v2`; the `latest` documentation label does not make this the separate BalanceControlV1 or Balance Platform Transfers API. The request identifies source and destination merchant accounts, not platform balance accounts, payment terminals, devices, or sessions.

## Key takeaways

- A successful transfer requires source and destination merchant accounts under the same company account and legal entity, sufficient funds in the source, and at least one common processing currency. For multiple requests using the same source/destination pair, the page instructs sequential sending: parallel requests may go unprocessed. This is a processing warning, not an idempotency or retry rule.
- The body table requires `amount.currency` (three-character ISO code) and integer `amount.value` in minor units, `fromMerchant`, `toMerchant`, and `type`. Allowed `type` values are `tax`, `fee`, `terminalSale`, `credit`, `debit`, and `adjustment`. Optional `reference` is limited to 80 characters. The EUR 3000-minor-unit `adjustment` request is an example, not a currency or transfer-type default.
- The `200 Success` description says the request succeeded. Its response body requires `createdAt`, described as the date the transfer was performed, and a 16-character `pspReference`; the example caption calls it “balance transfer created.” Preserve that wording distinction: the page supplies no separate status transitions, balance-ledger entries, reconciliation event, payout, or bank-receipt proof.
- `401 Unauthorized` and `422` validation error responses are documented with optional problem fields, including `requestId` and conditional `invalidFields` entries. The page does not specify the authentication mechanism, credential role, retry behavior, reversal endpoint, asynchronous outcome, settlement timing, or deprecation rule. The optional client `reference`, error `requestId`, and success `pspReference` have distinct stated roles.

## Detail locators

- Eligibility, currency overlap, same-pair sequencing, and v2 Test/Live server bases: raw lines 5–22.
- Required body fields, type enum, optional reference length, and illustrative request: raw lines 24–51.
- Success wording, `createdAt` and `pspReference`: raw lines 52–62 and 101–111.
- Unauthorized/validation error schemas, including optional request correlation: raw lines 64–99.

## Related

- [[adyen]] — provider context.
- [[adyen-account-structure]] — merchant/company hierarchy and merchant-balance context.
- [[source-adyen-docs-account-manage-your-balances]] — separately sourced role, allocation, and balance-management guidance; this API Explorer page alone does not establish those rules.
- [[adyen-platform-internal-transfers]] — different balance-account transfer family; do not apply its status model to this merchant-account API.

## Raw Sources

- [[raw/adyen/api-explorer/BalanceControl/latest/post/balanceTransfers/2026-09-15|Adyen API Explorer Balance Control v2 balance transfer (2026-09-15 snapshot)]]
