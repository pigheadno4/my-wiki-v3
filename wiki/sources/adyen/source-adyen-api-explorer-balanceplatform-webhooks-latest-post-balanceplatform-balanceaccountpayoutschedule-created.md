---
title: "Adyen Balance Platform webhook: managed payout schedule created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.created/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, managed-payouts]
---

## Overview

This captured Balance Platform Webhooks API Explorer POST reference describes the incoming `balancePlatform.balanceAccountPayoutSchedule.created` webhook Adyen sends when a managed payout schedule is successfully created on a balance account. It is a schedule-creation event contract, not an instruction to initiate a payout. The `latest` path is a captured label; this raw page gives no numbered webhook API version. See [[adyen-webhooks]], [[adyen-platforms]], and [[adyen]].

## Key takeaways

- The request body table marks `data`, `environment`, and `type` required. `environment` can be `test` or `live`; optional `timestamp` is when the event was queued. Every listed property within `data` is marked optional, including `balanceAccountId`, `balanceAccountPayoutScheduleId`, and `balancePlatform`. The first two identify the affected balance account and applied schedule when supplied. The page supplies no example payload or further constraints on the `type` property's value beyond the event title.
- Optional schedule fields include `currency`, `description`, `enabled`, `frequency`, `frequencyValue`, payout amount limits, references, retained amount, sales-day closing time, and destination `transferInstrumentId`. The table lists daily, weekdays, weekly and monthly frequencies. It permits `frequencyValue` only for weekly or monthly schedules and gives their ranges and calendar adjustments. `retainedAmount` can prevent an execution from starting when available funds are below it. These are schema descriptions, not evidence that any payout execution occurred.
- The response section says any HTTP `2xx` accepts the webhook; `notificationResponse` is optional. Successful schedule creation and webhook acceptance do not establish payout initiation, booking, settlement, or bank receipt. This page does not establish delivery ordering, retry or deduplication behavior, signature verification, or a final financial outcome.

## Detail locators

- Event title and creation trigger: pinned raw lines 5–7.
- Envelope requirements and resource identifiers: pinned raw lines 11–18 and 30–32.
- Optional schedule fields, frequency rules, and retained amount: pinned raw lines 19–29.
- Webhook acceptance response: pinned raw lines 34–42.

## Related

- [[adyen-webhooks]] — webhook family and acceptance context.
- [[adyen-platforms]] — managed payout schedule context.
- [[source-adyen-docs-platforms-managed-payouts-use-managed-payouts]] — separate configuration guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.created/2026-09-15|Managed payout schedule created webhook reference, captured 2026-09-15]]
