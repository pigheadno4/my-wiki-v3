---
title: "Adyen Management API v3: Add a merchant payout setting"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/payoutSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/payoutSettings/2026-11-03.md"
tags: [adyen, management-api, merchant-accounts, payout-settings]
---

## Overview

This captured Management API reference describes `POST /merchants/{merchantId}/payoutSettings`, a request to add a payout setting for the path's merchant account. The setting links that merchant account to a Legal Entity API transfer instrument containing payout-bank details. Adyen verifies the bank account before allowing and enabling the setting; multiple settings may be added when payments are accepted in multiple currencies. This endpoint is for integrations that require it, such as Adyen for Platforms Manage; an Adyen contact sets up access. The documented server is `https://management-test.adyen.com/v3`, and the calling API credential needs **Management API—Payout account settings read and write**. See [[adyen]], [[adyen-account-structure]], and [[adyen-api-access]].

## Key takeaways

- Required path `merchantId` identifies the merchant account. The request-body table requires `transferInstrumentId`, identifying the transfer instrument with payout-bank details. `enabled` is optional and defaults to `true`; optional `enabledFromDate` is an ISO 8601 date/time controlling when payouts to that bank account become enabled. The table does not separately mark the request-body container as required.
- When `enabledFromDate` is supplied with `enabled=true`, payouts become enabled from that date. With `enabled=false`, payouts are disabled until the date; then `enabled` changes to `true` and `enabledFromDate` resets to `null`. Without a date, `enabled` indicates whether payouts are enabled.
- A 200 says the request succeeded and returns required payout-setting `id` and `transferInstrumentId`, with optional `allowed`, `enabled`, `enabledFromDate`, `priority`, and `verificationStatus`. `allowed` is set automatically: `true` when bank `verificationStatus=valid`, `false` for other statuses (`pending`, `invalid`, or `rejected`). Receiving payouts into this bank account requires **both** `allowed` and `enabled` to be `true`. A separately documented 204 says the request was processed without response content.
- The optional priority values are `first` (same day), `urgent` (next day), and `normal` (one to three days). The response description says payout timing depends on frequency, currencies and banks, and arrival can take up to three days. These descriptions do not establish that a particular payout was made or received.
- The reference lists 400, 401, 403, 422 and 500 errors. It documents no idempotency behavior, duplicate-setting outcome, deletion/reversal operation, or completed payout/settlement/bank receipt. A successful setting request and returned `id` are configuration evidence, while bank verification and effective payout enablement remain separately represented by the returned fields and date.

## Detail locators

- Purpose, transfer-instrument relationship, access condition and role: raw lines 5–18.
- Path and request body, including date transition: raw lines 20–33.
- 200/204 success and payout-setting response fields: raw lines 35–53.
- Error response schemas: raw lines 56–153.

## Related

- [[adyen-account-structure]] — company and merchant account configuration.
- [[adyen-api-access]] — API credential permissions and scope.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/payoutSettings/2026-11-03|Adyen Management API payout-setting creation reference, captured 2026-11-03]]
