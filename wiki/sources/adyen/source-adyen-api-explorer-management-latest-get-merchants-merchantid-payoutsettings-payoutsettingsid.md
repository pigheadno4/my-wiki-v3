---
title: "Adyen Management API v3: Get a merchant payout setting"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings/(payoutSettingsId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03.md"
tags: [adyen, management-api, merchant-account, payout-settings]
---

## Overview

This 2026-11-03-captured Management API v3 reference describes `GET /merchants/{merchantId}/payoutSettings/{payoutSettingsId}`, a read of one payout setting for a merchant account. The listed server is TEST `https://management-test.adyen.com/v3`. Adyen says to use this endpoint when the integration requires it, such as Adyen for Platforms Manage, and that an Adyen contact sets up access. The `latest` URL and TEST server do not establish current Live availability or account eligibility. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- The API credential needs `Management API—Payout account settings read`. Both string path IDs are required: `merchantId` identifies the merchant account and `payoutSettingsId` identifies the payout setting. The page lists no query parameters, request body, numeric rate limit or idempotency semantics.
- A 200 says the request succeeded. The response requires setting `id` and `transferInstrumentId`, the latter identifying the transfer instrument containing bank-account details. Optional fields are `allowed`, `enabled`, `enabledFromDate`, `priority` and `verificationStatus`. A separate 204 means processing succeeded without additional content.
- The table says `allowed` is set automatically: true when `verificationStatus` is `valid`, false for other statuses. `enabled` defaults to true, but the page says **both** `enabled` and `allowed` must be true to receive payouts into that bank account. The optional `enabledFromDate` governs when payouts are enabled; with `enabled=false`, the field says `enabled` changes to true and the date resets to null on that date. These are setting semantics, not evidence that a payout was sent or received.
- `verificationStatus` can be `valid`, `pending`, `invalid` or `rejected`. `priority` values are `first` (same day), `urgent` (next day) and `normal` (one to three days); the page qualifies arrival by payout frequency and the currencies and banks involved, saying funds may take up to three days to reach the bank. The priority description is not a bank-receipt guarantee.
- Error responses listed are 400, 401, 403, 422 and 500. A readback does not create or update the setting, start verification, approve the bank account, activate merchant processing, book a payout or prove recipient-bank receipt. The page gives no deletion, propagation, reversal or asynchronous completion result for this GET.

## Detail locators

- Purpose, conditional integration use, Adyen-contact access, required role, TEST server and path IDs: pinned raw lines 5–24.
- 200 field requiredness, allowed/enabled/date/priority/status semantics: lines 26–40; 204 no-content result: lines 43–44.
- Error descriptions and problem fields: lines 47–144.

## Related

- [[adyen-account-structure]] — merchant-account and bank-setting context.
- [[adyen-platforms]] — route-specific Platforms Manage context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03|Merchant payout setting GET snapshot]]
