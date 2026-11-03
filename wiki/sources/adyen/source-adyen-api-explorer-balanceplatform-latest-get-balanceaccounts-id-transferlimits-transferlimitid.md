---
title: "Adyen Balance Platform API v2: GET /balanceAccounts/{id}/transferLimits/{transferLimitId}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/(transferLimitId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/(transferLimitId)/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, transfer-limits, api]
---

## Overview

This 2026-11-03 Balance Platform API reference describes `GET /balanceAccounts/{id}/transferLimits/{transferLimitId}`, a read of one transfer limit by its balance-account and transfer-limit identifiers. The only displayed server is the v2 TEST base `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` URL and this captured read do not establish LIVE access or eligibility. See [[adyen]], [[adyen-business-accounts]] and [[adyen-platforms]].

## Key takeaways

- Both path parameters are required: `id` identifies the balance account, and `transferLimitId` identifies the transfer limit. No query parameters or request body appear in this captured endpoint reference.
- A 200 returns `amount` (required currency and integer value in minor units), limit `id`, `limitStatus`, `scope`, `startsAt` and `transferType` as required response fields. `scope` is `perTransaction` or `perDay`; `transferType` is `instant` or `all`, where `all` covers transfers regardless of priority. The amount is the maximum per transfer or per day according to scope.
- `limitStatus` may be `active`, `inactive`, `pendingSCA` or `scheduled`. `startsAt` is the stated activation date/time, including a future scheduled limit; optional `endsAt` gives inactivation time, and the table says a limit without an end date stays active until overridden by a new limit. Optional `reference` is the caller's reference.
- Optional `scaInformation` describes Strong Customer Authentication; its nested `status` is marked required when the object is present and can be `notPerformed`, `pending` or `performed`. The table says `notPerformed` can mean unsuccessful authentication **or** an exemption, so it cannot be read as a single outcome. The optional exemption enum includes `lowerLimit`, `notRegulated`, `setByPlatform`, `initialLimit` and `alreadyPerformed`; a returned exemption label alone does not prove an account-specific regulatory exemption or completed SCA.
- The endpoint documents 404 when a transfer limit cannot be found and 422 for request validation errors. Its illustrative 200 body shows `active` with `initialLimit` and `notPerformed`; example timestamps and states do not prove current activity, enforcement, available transfer capacity, approval, booked funds or bank receipt.

## Detail locators

- Purpose, TEST server and required path IDs: pinned raw lines 5–18.
- Complete success fields, amount units, scope, transfer type and lifecycle/SCA enums: `## Responses > ### 200 Success`, lines 20–40.
- 404 and 422 error descriptions and response schemas: `## Responses`, lines 43–78.
- Illustrative 200 transfer-limit body: `## Response examples > ### 200 Success`, lines 80–103; it is not a current account-specific state or successful transfer.

## Related

- [[adyen-business-accounts]] — Business Accounts financial-product context.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — separate balance-account transfer-limit guide.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-platform]] — separate platform-scope limit guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/(transferLimitId)/2026-11-03|GET balance-account transfer limit, 2026-11-03 capture]]