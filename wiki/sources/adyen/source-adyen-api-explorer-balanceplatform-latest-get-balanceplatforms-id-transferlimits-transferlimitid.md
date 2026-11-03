---
title: "GET /balancePlatforms/{id}/transferLimits/{transferLimitId} — Get a transfer limit | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits/(transferLimitId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits/(transferLimitId)/2026-11-03.md"
tags: [adyen, balance-platform-api, transfer-limits, business-accounts, api-reference]
---

## Overview

This 2026-11-03-captured Balance Platform API `/bcl/v2` reference retrieves the details of one transfer limit under a balance platform. The listed server is TEST-only `https://balanceplatform-api-test.adyen.com/bcl/v2`; the capture does not establish a live endpoint or account-specific eligibility. [[adyen]] [[adyen-business-accounts]]

## Key takeaways

- `GET /balancePlatforms/{id}/transferLimits/{transferLimitId}` requires two string path IDs: `id` identifies the balance platform, while `transferLimitId` identifies the transfer limit. The page lists no query parameters, body, caller role, endpoint-specific idempotency key, or request default.
- A `200` response reports required `amount` (`currency` and integer `value` in minor units), limit `id`, `limitStatus`, `scope`, `startsAt`, and `transferType`. `scope` is `perTransaction` or `perDay`; `transferType` is `instant` or `all`. The amount is the maximum per transfer or per day according to `scope`. Optional fields are `endsAt`, `reference`, and `scaInformation`.
- `limitStatus` can be `active`, `inactive`, `pendingSCA`, or `scheduled`. `startsAt` describes activation time, and a future start schedules activation; the page says a limit without an end date stays active until overridden by a new limit. `endsAt`, when present, is the time it becomes inactive.
- Within optional `scaInformation`, `exemption` is optional and `status` is required if that object appears. `status=notPerformed` can mean unsuccessful SCA **or an exemption**, `pending` means pending authentication, and `performed` means successful authentication. The exemption enum includes `lowerLimit`, `notRegulated`, `setByPlatform`, `initialLimit`, and `alreadyPerformed`; the raw definitions govern their exact scope. Do not read `notPerformed` alone as an authentication failure.
- The listed error responses are `404` (limit not found) and `422` (request validation), with optional top-level problem-detail fields. This GET readback does not create, approve, or enforce a limit; it does not prove a user completed SCA or that any transfer was authorized, booked, settled, or received by a bank.

## Detail locators

- Purpose, TEST server, and separate required path IDs: raw lines 5–18.
- `200` schema, amount units, status, scope, dates, transfer type, SCA and exemption definitions: raw lines 20–40.
- `404` and `422` error schemas: raw lines 43–78. Illustrative `200` response: raw lines 80–102.

## Related

- [[adyen-business-accounts]] — Business Accounts transfer-limit context.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-platform]] — separate platform-wide limit guide.
- [[source-adyen-api-explorer-balanceplatform-latest-post-balanceaccounts-id-transferlimits-approve]] — separate balance-account limit approval endpoint.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits/(transferLimitId)/2026-11-03|GET platform transfer limit captured 2026-11-03]]
