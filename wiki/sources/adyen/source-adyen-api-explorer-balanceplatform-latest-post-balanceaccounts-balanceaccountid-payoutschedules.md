---
title: "Adyen Balance Platform API v2: Apply a managed payout schedule"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/payoutSchedules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/payoutSchedules/2026-11-02.md"
tags: [adyen, platforms, balance-platform, payout-schedules, api-reference]
---

## Overview

Captured Balance Platform API v2 TEST `POST /balanceAccounts/{balanceAccountId}/payoutSchedules` reference for applying an existing balance-platform managed payout schedule to a particular balance account. It creates account-level schedule configuration for [[adyen]] [[adyen-platforms]], rather than initiating or completing a payout.

## Key takeaways

- The path requires the balance-account `balanceAccountId`; the body requires the existing `balancePlatformPayoutScheduleId` and destination `transferInstrumentId`. The response schema marks the separate account-level schedule `id` optional; the balance-account, platform-schedule and transfer-instrument IDs are required response fields. The only listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`.
- Optional account-level settings include `currency`, `description`, `enabled`, `frequency`, `frequencyValue`, maximum/minimum payout amounts, merchant `reference`, beneficiary reference, retained amount, and sales-day closing time. The description, frequency, frequency value and beneficiary reference default from the platform schedule; minimum, maximum and retained amounts default to 0. The raw does not give a default for `enabled` or `currency`.
- Frequencies are daily, weekdays, weekly, or monthly. `frequencyValue` is allowed only for weekly (1–5) or monthly (1–31); a monthly weekend date moves initiation to the next business day, and nonexistent dates 29–31 move initiation to the month's last day. The 140-character description may be truncated. Sales-day closing time is HH:mm:ss between 00:00 and 07:00 in the balance account time zone.
- If available funds are less than `retainedAmount`, execution is not initiated. The merchant `reference` appears only in the schedule and not on payout statements; `referenceForBeneficiary` is sent to the recipient and included in payout webhooks. The request allows letters, digits, hyphen and space for that beneficiary reference, while the response description lists letters and digits only; preserve this source inconsistency rather than treating either as a proven universal validator.
- A 200 says the application request succeeded. Its schema requires the parent schedule ID, balance-account ID, destination transfer-instrument ID and creation timestamp; the account-level schedule `id` and other configuration fields are optional. It does not prove any scheduled execution, transfer, settlement or bank receipt.

## Detail locators

- Purpose, TEST server and required identities: pinned raw lines 5–23 and 35. Optional fields, defaults, limits and conditional timing: lines 24–34. Request example: lines 37–55.
- Success response: lines 56–80 and example lines 158–180. Error schemas: 401, 404, 422 and 500 at lines 83–156.

## Related

- [[adyen-platforms]] — balance-account and managed-payout context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(balanceAccountId)/payoutSchedules/2026-11-02|Pinned 2026-11-02 API reference]]
