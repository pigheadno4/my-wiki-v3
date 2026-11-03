---
title: "Adyen Balance Platform API v2: list balance-platform transfer limits"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, transfer-limits, api]
---

## Overview

This 2026-11-03 Balance Platform API reference documents `GET /balancePlatforms/{id}/transferLimits` for filtering and viewing transfer limits configured for a balance platform. Its captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is a documentation route, not proof of current live availability or caller eligibility. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- The required string path `id` is the balance-platform identifier. Optional query filters are `status` (`active`, `inactive`, `pendingSCA`, `scheduled`), `transferType` (`instant` or `all` priorities), and `scope` (`perTransaction` or `perDay`). `pendingSCA` is pending user SCA; `scheduled` denotes a future activation date. The page lists no request body, defaults, pagination, query limits, or idempotency field.
- The `200` response requires a `transferLimits` array. For each listed limit, the schema requires `amount.currency` (three-character ISO currency code), `amount.value` (integer minor units), `id`, `limitStatus`, `scope`, `startsAt`, and `transferType`. `endsAt`, `reference`, and `scaInformation` are optional. Within a supplied `scaInformation` object, `status` is required and `exemption` optional. `notPerformed` can mean unsuccessful SCA **or** an exemption; it cannot alone prove failed authentication. A future `startsAt` schedules a limit; the `endsAt` description says an omitted end date leaves the limit active until overridden.
- This GET reports configured limit records and their reported states; it does not create, approve, delete, enforce, or execute a transfer. An `active` entry or `performed` SCA status is not proof of any transfer's authorization, booking, settlement, or bank receipt. The page documents 404 (one transfer limit not found) and 422 (validation error), but gives no authentication role, 401/403 schema, asynchronous approval timing, failure/reversal process, or version/conflict behavior for this read. The two-limit response example is illustrative, not proof of current configuration or transfer capacity.

## Detail locators

- Purpose, TEST server, balance-platform path ID and optional filters: pinned raw lines 5–25.
- `200` array and nested field schema, units, lifecycle status and SCA semantics: pinned raw lines 27–48.
- Error descriptions and schemas: pinned raw lines 51–86; illustrative list example: lines 88–132.

## Related

- [[adyen-business-accounts]] — transfer-limit context for Business Accounts.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-platform]] — separate captured guide to balance-platform transfer-limit management.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transferLimits/2026-11-03|Balance Platform GET transfer limits snapshot]]