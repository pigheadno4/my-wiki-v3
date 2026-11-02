---
title: "Adyen Balance Control v1: POST /balanceTransfer"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BalanceControlv1/latest/post/balanceTransfer"
raw_files:
  - "adyen/api-explorer/BalanceControlv1/latest/post/balanceTransfer/2026-09-15.md"
tags: [adyen, balance-control, merchant-accounts, balance-transfer, api]
---

## Overview

This 2026-09-15 API Explorer capture documents Balance Control **v1** `POST /balanceTransfer`, which starts a balance-transfer request between merchant accounts. The listed server is the TEST `https://pal-test.adyen.com/pal/servlet/BalanceControl/v1`. The source and destination merchant accounts must share a company account and legal entity, the source must have sufficient funds, and both must share at least one processing currency. This is a merchant-account balance operation, separate from Adyen for Platforms balance-account transfers. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- The request body requires `amount` with required ISO three-character `currency` and integer `value` in minor units, `fromMerchant`, `toMerchant`, and a `type` of `tax`, `fee`, `terminalSale`, `credit`, `debit`, or `adjustment`. The merchant IDs identify the source and destination accounts; the page names no device, session, shopper, or end beneficiary.
- `reference` is optional, up to 80 characters; Adyen generates a unique reference if omitted. The optional human-readable `description` accepts alphanumeric characters and hyphens; the page recommends at most 140 characters because longer text may be truncated. For multiple requests involving the same source/destination merchant pair, send them sequentially: the page warns that parallel requests may not be processed.
- The `200 Success` section says the **request** succeeded. Its response requires `amount`, `createdAt` (date the transfer was **requested**), `fromMerchant`, `toMerchant`, `type`, a 16-character Adyen `pspReference`, and `status`. The status can be `transferred`, `failed`, `error`, or `notEnoughBalance`; therefore HTTP 200 and a PSP reference alone do not establish that funds transferred. `reference` and `description` are optional response fields. The single example shows `status: transferred` and is not a guarantee for other calls.
- The page gives no separate authentication role, idempotency or retry contract, asynchronous webhook or polling lifecycle, timing for completion, transfer reversal, settlement schedule, payout, or bank-receipt evidence. `createdAt` marks request time, not a bank or settlement event. It does not establish capabilities of Balance Control v2 or the Balance Platform Transfers API.

## Detail locators

- Purpose, eligibility conditions and same-pair sequential-request warning: raw lines 5–15.
- TEST Balance Control v1 server: lines 17–18.
- Required request amount, merchant IDs and type; optional reference/description constraints: lines 20–32.
- Illustrative request without a reference: lines 34–48.
- HTTP 200 request wording, required response identifiers and status enum: lines 49–67.
- Illustrative `transferred` response and generated-looking reference: lines 69–89.

## Related

- [[adyen]] — provider route.
- [[adyen-account-structure]] — company and merchant-account identity.
- [[source-adyen-docs-account-manage-your-balances]] — separate merchant-account balance management guide; its permissions and operational paths are distinct evidence.

## Raw Sources

- [[raw/adyen/api-explorer/BalanceControlv1/latest/post/balanceTransfer/2026-09-15|POST /balanceTransfer API Explorer capture]]
