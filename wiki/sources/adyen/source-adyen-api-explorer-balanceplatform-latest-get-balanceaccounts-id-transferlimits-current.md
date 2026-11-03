---
title: "GET /balanceAccounts/{id}/transferLimits/current — Current transfer-limit lookup | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/current"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/current/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, transfer-limits, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /balanceAccounts/{id}/transferLimits/current` to read transfer limits described as currently applying to a balance account. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is in the URL, while the server path identifies v2. See [[adyen-business-accounts]] for transfer-limit context. [Raw: lines 5–10]

## Key takeaways

- The required string path `id` identifies the balance account. Optional query filters are `transferType` (`instant` priority or `all` priorities) and `scope` (`perTransaction` or `perDay`). The page lists no request body, caller-role name, filter defaults, pagination, list limit or GET idempotency contract. [Raw: lines 12–24]
- A 200 means the request succeeded and requires a `transferLimits` array. In each returned limit, the table requires `amount` with three-character ISO currency and integer minor-unit value, limit `id`, `limitStatus`, `scope`, `startsAt` and `transferType`. Optional fields include `endsAt`, reference and `scaInformation`; if `scaInformation` is present, its `status` is required. Scope determines whether the maximum is per transfer or per day. See the raw table for exact status, SCA and exemption enums and date formats. [Raw: lines 26–47]

> [!warning] Contradiction
> The purpose says this route gets limits that currently apply [Raw: line 7], but the returned `limitStatus` enum also includes `inactive`, `pendingSCA` and `scheduled` [Raw: line 40]. The snapshot does not resolve whether such rows are actually returned by this `current` route. Do not treat route naming or a listed row alone as proof that every limit is active.

- `limitStatus` distinguishes active, inactive, pending SCA and future-scheduled states. `scaInformation.status` distinguishes not performed, pending and performed; `notPerformed` can mean failed authentication or an exemption. `endsAt` can make a limit inactive; absent an end date, the description says it stays active until overridden. These response fields describe limit state, not whether a transfer was approved, booked or received. [Raw: lines 38–46]
- The 200 example shows one active per-day instant EUR limit with `initialLimit` exemption and `notPerformed` SCA status. It illustrates one record, not a real account's current limits or a compliance determination. Documented errors are 404, described as one transfer limit not found, and 422 validation; this page lists no 401/403 response, role, approval action, activation event, version/conflict behavior or transfer outcome. [Raw: lines 50–113]

## Detail locators

- Purpose, TEST v2 server, balance-account ID and optional filters: pinned raw lines 5–24.
- 200 amount, scope, state, SCA fields and dates: lines 26–47; sample: lines 87–113.
- Error responses and their optional problem-body fields: lines 50–85.

## Related

- [[adyen-business-accounts]] — Business Accounts transfer-limit context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transferLimits/current/2026-11-03|Current balance-account transfer limits — captured 2026-11-03]]