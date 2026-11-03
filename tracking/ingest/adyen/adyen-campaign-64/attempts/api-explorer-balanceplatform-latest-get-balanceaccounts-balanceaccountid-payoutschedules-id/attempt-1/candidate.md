---
title: "Balance Platform API: Get a balance account managed payout schedule"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02.md"
tags: [adyen, balance-platform, managed-payouts, api]
---

## Overview

This captured Balance Platform API v2 `GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}` reference returns one specified managed payout schedule applied to a balance account. The only listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. This is a configuration read, not a payout execution or bank receipt. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Both path fields are required: `balanceAccountId` identifies the balance account and `id` its payout schedule. No query parameters or request body are described. See **Parameters**.
- A 200 response requires `balanceAccountId`, `balancePlatformPayoutScheduleId` (the platform schedule applied), `createdAt`, and `transferInstrumentId` (the payout destination instrument). Its account-level `id` is optional in the response schema, distinct from the required path `id` and platform schedule ID. Optional fields include currency, description, `enabled`, frequency and frequencyValue, amount thresholds, references, retained amount, sales-day closing time, and updatedAt. See **200 Success**.
- The response schema describes `enabled` as whether the schedule is active. Frequency can be daily, weekdays, weekly, or monthly; `frequencyValue` is allowed only for weekly (1–5) or monthly (1–31). A selected weekend monthly date shifts initiation to the next business day, and a missing 29th–31st shifts to the month's last day. Description has a 140-character maximum and may be truncated. The schedule's frequency, description, beneficiary reference and frequency value default from the applied platform schedule; minimum/maximum payout and retained amounts default to 0. If balance funds are below the retained amount, execution is not initiated. See **200 Success**, lines 31–42.
- A returned schedule shows the read request succeeded and describes configuration. It does not prove an execution was initiated, a transfer was booked, or a bank received funds. The reference lists 401 authentication required, 404 resource not found, 422 validation error, and 500 server error; it does not specify a caller role, idempotency behavior, deletion or propagation timing, reversal or version conflict. The `latest` URL and test server are capture evidence, not proof of current live eligibility.

## Detail locators

- **Parameters**, lines 12–18: required account and schedule path identifiers.
- **200 Success**, lines 20–44: response fields, inherited defaults and scheduling conditions.
- **Client/Server Errors**, lines 47–120: statuses and error shape.
- **Response examples**, lines 122–144: illustrative schedule values, not execution evidence.

## Related

- [[adyen-platforms]] — managed payout configuration context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02|Captured managed payout schedule GET reference (2026-11-02)]]
