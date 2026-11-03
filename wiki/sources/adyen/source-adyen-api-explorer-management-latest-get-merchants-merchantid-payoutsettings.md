---
title: "Adyen Management API v3: list merchant payout settings"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings/2026-11-03.md"
tags: [adyen, management-api, merchant-accounts, payout-settings, bank-accounts]
---

## Overview

This 2026-11-03 [[adyen]] Management API reference describes `GET /merchants/{merchantId}/payoutSettings`, a read of payout settings for the merchant account named by the required path `merchantId`. It names Adyen for Platforms Manage as an example of an integration that may need the endpoint; an Adyen contact sets up access, and the API credential needs `Management API—Payout account settings read`. The captured server is `https://management-test.adyen.com/v3`; no live server URL is supplied here. This is configuration readback, not a payout request or proof of funds reaching a bank. [[adyen-account-structure]]

## Key takeaways

- The only documented input is the required string path ID of the merchant account. No query parameter or request body is shown. `200` means the read request succeeded; its optional `data` array is described as payout accounts. Each array item requires a payout-setting `id` and a `transferInstrumentId` identifying the bank-account transfer instrument. Those IDs are separate from the merchant-account path ID.
- Optional `verificationStatus` values are `valid`, `pending`, `invalid` and `rejected`. Optional `allowed` is set automatically: true when verification is valid and false otherwise. Optional `enabled` defaults to true, but payouts to the bank account require **both** `enabled` and `allowed` true. A default switch, valid verification or returned setting alone does not establish payout execution or bank receipt.
- Optional ISO 8601 `enabledFromDate` schedules when payouts are enabled: if `enabled` is true, payouts start on the specified date; if false, they remain disabled until that date, when `enabled` becomes true and the date field resets to null. Without a date, `enabled` indicates the setting. Optional `priority` values are `first` (same day), `urgent` (next day) and `normal` (one to three days); the text qualifies bank arrival by payout frequency, currency and banks, saying funds may take up to three days to reach the account. These timings are descriptive, not a guarantee for a specific payout.
- The page also lists `204` success without content and `400`, `401`, `403`, `422` and `500` errors. It does not document an idempotency rule, modification or deletion action, propagation timing, review/approval result, activation of a merchant account, payout reversal or transfer state for this GET.

## Detail locators

- **Purpose, access setup, role and captured v3 test server:** raw lines 5–16.
- **Merchant path identifier:** raw lines 18–23.
- **Optional list, required item identifiers, verification and payout-switch rules, date and priority:** raw lines 25–40.
- **204 and error response schemas:** raw lines 43–144.

## Related

- [[adyen-account-structure]] — merchant-account scope and payout configuration.
- [[adyen-api-access]] — credential role and account-scope context.
- [[source-adyen-docs-account-manage-payout-account-details]] — separate Customer Area add, edit and review guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/payoutSettings/2026-11-03|Management API v3 payout-settings GET — collected 2026-11-03]]