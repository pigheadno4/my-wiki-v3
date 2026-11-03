---
title: "Adyen Balance Platform API v2: GET a platform managed payout schedule"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules/(id)/2026-11-02.md"
tags: [adyen, balance-platform, managed-payouts, payout-schedules, api]
---

## Overview

This 2026-11-02-captured Balance Platform API v2 reference describes `GET /balancePlatforms/{balancePlatformId}/payoutSchedules/{id}`, a read of one managed payout schedule configured on a balance platform. Both path strings are required: `balancePlatformId` identifies the platform and `id` the platform payout configuration. The only displayed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` documentation path does not prove current live version, access or platform eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The 200 response table requires `balancePlatformId`, `createdAt`, `payoutScheduleDescription`, `userSettlementDelay`, `userSettlementTime` and `userSettlementTimeZone`. It marks the returned schedule `id`, `automaticApplication`, `enabled`, country/currency, defaults, amount thresholds and `updatedAt` optional. The page lists no query parameters or request body.
- `automaticApplication` describes whether the schedule is automatically applied to **new** balance accounts; its presence does not prove that it was applied to any particular account. `enabled` is described as whether the schedule is enabled immediately after creation, so the field's wording should not be expanded into an execution history. `defaultReference` is copied when applied to a balance account.
- `defaultFrequencyValue` is allowed only for monthly or weekly `defaultFrequency`: monthly 1–31, weekly 1–5. The table says a specified monthly date on a weekend moves initiation to the next business day, and a missing 29th–31st moves it to that month's last day. `maxPayoutAmount` and `minPayoutAmount` default to 0; max 0 means no maximum. `retainedAmount` defaults to 0 and blocks initiation when available funds are below it. The integer amount fields are not given an explicit unit on this page.
- `payoutScheduleDescription` lists Standard and Accelerated with relative fund-arrival descriptions after settlement. These are schedule-type descriptions, not evidence that a payout was initiated, a transfer succeeded or a beneficiary received funds. A 200 GET response establishes configuration readback only; applying a schedule to a balance account, execution and transfer outcome require separate evidence. This reference lists 401, 404, 422 and 500 responses, but no response examples.

## Detail locators

- Endpoint, TEST server and two required path identifiers: pinned raw lines 5–18.
- 200 schedule response fields, defaults, frequency/date conditions, amount thresholds and schedule types: `## Responses > ### 200 Success`, lines 20–47.
- Authentication, not-found, validation and server-error schemas: `## Responses`, lines 50–123.

## Related

- [[adyen-platforms]] — managed payout context and source routes.
- [[source-adyen-docs-platforms-managed-payouts-use-managed-payouts]] — separate application and account-level lifecycle guide.
- [[source-adyen-docs-platforms-managed-payouts-view-payout-executions]] — separate execution-result guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(balancePlatformId)/payoutSchedules/(id)/2026-11-02|Platform managed payout schedule GET snapshot]]