---
title: "Adyen Management API v3: Update a merchant payout setting"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/payoutSettings/(payoutSettingsId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03.md"
tags: [adyen, management-api, merchant-account, payout-settings]
---

## Overview

The captured [[adyen]] Management API v3 TEST reference documents `PATCH /merchants/{merchantId}/payoutSettings/{payoutSettingsId}` to enable or disable the identified merchant-account payout setting. The merchant account ID and payout-setting ID are distinct required path identifiers. This operation concerns the bank-account payout configuration, not a payout instruction or bank receipt. See [[adyen-account-structure]].

## Key takeaways

- The only documented request-body field is optional boolean `enabled`, with a stated default of `true`. The page says both `enabled` and `allowed` must be true to receive payouts to that bank account. It does not mark the whole body required or document a way to set `allowed` in this PATCH body.
- In the 200 response, `allowed` is optional and set automatically from bank-account `verificationStatus`: true for `valid`, false for other statuses. The response also describes optional `enabledFromDate` timing, `priority`, and `verificationStatus`; these are response fields here, not documented PATCH inputs. The response marks payout-setting `id` and bank-account `transferInstrumentId` required, while other listed fields are optional.
- A 200 means the request succeeded and returns a setting representation; 204 means it was processed without content. Neither response establishes that a payout was initiated, booked, settled, or received by a bank. The response's timing and priority descriptions are conditional and do not guarantee arrival.
- This endpoint is for integrations that require it, such as Adyen for Platforms Manage. An Adyen contact sets up access, and the API credential needs the `Management API—Payout account settings read and write` role. The captured server is `https://management-test.adyen.com/v3`.

## Detail locators

- Purpose, access setup, required role, TEST v3 server: pinned raw lines 5–16.
- Required path IDs and optional `enabled` body field/default: pinned raw lines 18–30.
- 200 fields, verification/status and date/priority semantics; 204 response: pinned raw lines 32–50.
- 400, 401, 403, 422, and 500 error cases and nested `invalidFields` schema: pinned raw lines 53–150. The generic error `requestId`/`pspReference` wording is not a payout result.
- No idempotency, rate limit, deletion/reversal, asynchronous approval, or propagation-time contract appears in this capture. The `latest` URL and 2026-11-03 snapshot do not prove present availability or account eligibility.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03|2026-11-03 pinned API Explorer snapshot]]
