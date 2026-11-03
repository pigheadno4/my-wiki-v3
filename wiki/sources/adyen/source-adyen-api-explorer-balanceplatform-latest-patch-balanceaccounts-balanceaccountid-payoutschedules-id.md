---
title: "Adyen Balance Platform API v2 PATCH applied payout schedule"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02.md"
tags: [adyen, balance-platform, platforms, managed-payouts, payout-schedules]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform API v2 TEST reference documents `PATCH /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}`: update a managed payout schedule already applied to a balance account. The required path IDs identify the balance account and its applied payout schedule, not the platform-level schedule or destination transfer instrument. Omitted optional request parameters remain unchanged. The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` URL does not establish current version or live eligibility. See [[adyen-platforms]].

## Key takeaways

- The request table marks every body field **No** and does not separately state whole-body requiredness. Fields include `description`, `enabled`, `frequency`, `frequencyValue`, min/max payout amounts, `reference`, `referenceForBeneficiary`, `retainedAmount`, `salesDayClosingTime` and `transferInstrumentId`. The example changes description, enabled and retained amount only; it is not a universal request shape (raw lines 14–45). The `enabled` request description says “immediately after it is created” even though this operation is PATCH of an applied schedule; it does not turn PATCH into creation.
- `frequency` accepts daily, weekdays, weekly or monthly and defaults to the applied platform schedule's `defaultFrequency` where a default applies. `frequencyValue` is allowed only for weekly (1–5) or monthly (1–31). The page says a monthly weekend date moves initiation to the next business day, and a nonexistent 29th–31st moves it to that month's last day. It does not define weekday-number mapping. Description has a 140-character maximum and may be truncated (raw lines 24–27, 58–61).
- Min and max payout amounts and retained amount each have a stated default of 0; the raw does not state currency units. If funds are below `retainedAmount`, execution is not initiated. `salesDayClosingTime` is in the balance account time zone, 00:00–07:00, in HH:mm:ss format. `transferInstrumentId` is the destination instrument ID. The request's `reference` is shown only in the schedule; the response says it does not appear on payout statements (raw lines 28–34, 63–69).
- A 200 says the update request succeeded. The response marks `balanceAccountId`, `balancePlatformPayoutScheduleId`, `createdAt` and `transferInstrumentId` required; its account-level payout-schedule `id`, `enabled`, schedule settings, currency and `updatedAt` are marked optional. The response example shows `enabled: false` and illustrative amounts, not an executed payout (raw lines 46–70, 148–171).

> [!warning] Contradiction
> The request description allows letters, digits, hyphen and space for `referenceForBeneficiary`, with spaces possibly replaced by hyphens, but the response description lists only letters and digits (raw lines 31 and 66). The snapshot does not resolve accepted versus returned characters or guarantee what a beneficiary bank displays.

- The page lists 401 authentication, 404 not found, 422 validation and 500 server errors (raw lines 73–146). It specifies no idempotency, schedule deletion, propagation timing, payout-execution result, reversal or bank-receipt contract. Updating a schedule, including setting `enabled`, is configuration evidence; execution and financial outcomes require separate evidence.

## Detail locators

- Purpose, TEST v2 host, two path IDs and optional request fields: raw lines 5–34.
- Request example, success schema and response example: raw lines 36–70, 148–171.
- Error schemas: raw lines 73–146.
- Beneficiary-reference character mismatch: raw lines 31 and 66.

## Related

- [[adyen-platforms]] — managed schedule and balance-account context.
- [[source-adyen-docs-platforms-managed-payouts-use-managed-payouts]] — separate application, management and execution-boundary guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/balanceAccounts/(balanceAccountId)/payoutSchedules/(id)/2026-11-02|PATCH applied payout schedule reference, captured 2026-11-02]]