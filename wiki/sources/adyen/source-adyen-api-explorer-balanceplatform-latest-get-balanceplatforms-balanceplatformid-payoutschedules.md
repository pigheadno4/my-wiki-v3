---
title: "Adyen Balance Platform API v2: GET /balancePlatforms/{balancePlatformId}/payoutSchedules"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules/2026-11-02.md"
tags: [adyen, balance-platform, managed-payouts, payout-schedules, api]
---

## Overview

This 2026-11-02 Balance Platform API v2 reference describes `GET /balancePlatforms/{balancePlatformId}/payoutSchedules`, which lists managed payout schedules configured for one balance platform. It shows the TEST server `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is a documentation route, not independently verified live availability. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required **path** parameter `balancePlatformId` identifies the balance platform. Optional `currency` and `countryCode` **query** parameters filter the list. The page provides no request body, pagination parameters, default filter values, or idempotency contract for this GET.
- A 200 response requires a `balancePlatformPayoutSchedules` array. Each listed schedule has required `balancePlatformId`, `createdAt`, `payoutScheduleDescription`, `userSettlementDelay`, `userSettlementTime`, and `userSettlementTimeZone` fields; its schedule `id` is marked optional. Optional fields describe automatic application to new balance accounts, enabled state after creation, currency/country, default frequency and reference, amount thresholds, retained funds, and update time.
- `defaultFrequencyValue` is allowed only for monthly or weekly schedules, with documented ranges of 1–31 and 1–5 respectively. The description gives next-business-day initiation for a weekend monthly date and last-day initiation when a 29th–31st does not exist. `maxPayoutAmount` defaults to 0 meaning no maximum; `minPayoutAmount` and `retainedAmount` default to 0. If a balance account has less than the retained amount, schedule execution is not initiated. Consult the raw field table for exact conditions.
- `payoutScheduleDescription` labels Standard and Accelerated timing relative to settled funds. This GET reports configuration; it does not establish application to a particular balance account, an initiated or successful payout, transfer booking, settlement, or beneficiary-bank receipt. `automaticApplication` and `enabled` are optional reported settings, not evidence that a specific execution occurred.
- Documented failures are 401 (authentication required), 404 (resource not found), 422 (request validation), and 500 (server unable to process). The page names no specific caller role, response example, or reversal behavior.

## Detail locators

- Purpose, captured server, required path parameter and optional filters: pinned raw lines 5–24.
- 200 schedule fields, defaults, conditional frequency and retained-funds gate: pinned raw lines 26–54.
- Error response shapes: pinned raw lines 57–130.

## Related

- [[adyen-platforms]] — managed payout schedule context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-balanceplatforms-balanceplatformid-payoutschedules-id]] — separate single-schedule read.
- [[source-adyen-docs-platforms-managed-payouts-use-managed-payouts]] — separate application and lifecycle guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules/2026-11-02|Balance-platform managed payout schedule list snapshot]]