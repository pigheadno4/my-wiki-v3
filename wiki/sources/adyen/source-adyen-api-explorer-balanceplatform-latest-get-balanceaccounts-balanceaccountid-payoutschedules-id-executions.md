---
title: "GET managed payout schedule executions | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/executions"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/executions/2026-11-02.md"
tags: [adyen, balance-platform, managed-payouts, payout-schedules, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions` to view attempts to make payouts under one managed payout schedule on a specified balance account. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` in the documentation URL does not establish live availability. See [[adyen-platforms]] for platform context.

## Key takeaways

- The required path identifiers select a balance account (`balanceAccountId`) and its payout schedule (`id`). The query table marks `offset` required while also giving default 1 and describing it as the page number; preserve that tension rather than treating it as an item skip count. Optional `limit` defaults to 10. Optional comma-separated `results` filters current execution statuses: `succeeded` (sent), `failed` (not sent due to error) and `skipped` (not triggered as expected). No maximum page size is stated here. [Raw: lines 14–26]
- A 200 response requires `payoutScheduleExecutions`, an array. Within each execution, `id`, `result`, `resultDetails`, and `triggeredAt` are marked optional; optional details include human-readable `reason`, `reasonCode` and a `transferId` for a transfer from executing the payout. The illustrated skipped/no-balance and succeeded/transfer-ID records are examples, not guarantees of those outcomes. [Raw: lines 30–43, 121–147]
- This read reports recorded payout attempts and their current result values. `succeeded` is described as payout sent, not bank receipt; a listed transfer ID does not itself prove final transfer booking or arrival. `failed` and `skipped` are distinct: the former could not be sent because of an error, while the latter was not triggered as expected. [Raw: lines 7, 26, 36–43]
- The captured error headings cover 401 authentication, 404 missing resource, 422 validation and 500 server processing. The page gives no role grant, idempotency input, deletion behavior, reversal contract or webhook timing for this GET. [Raw: lines 46–119]

## Detail locators

- Purpose, TEST v2 server, path and query inputs: pinned raw lines 5–26.
- Success schema and result meanings: lines 28–43; error schemas: lines 46–119.
- Illustrative success response: lines 121–147.

## Related

- [[adyen-platforms]] — platform managed-payout context.
- [[source-adyen-docs-platforms-managed-payouts-view-payout-executions]] — separate guide for execution monitoring and transfer tracking.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/executions/2026-11-02|Captured API Explorer page (2026-11-02)]]
