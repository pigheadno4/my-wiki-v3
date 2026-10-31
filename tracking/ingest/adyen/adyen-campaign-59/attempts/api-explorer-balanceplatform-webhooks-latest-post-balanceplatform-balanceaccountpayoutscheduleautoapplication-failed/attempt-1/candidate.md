---
title: "Adyen managed payout schedule automatic application failed webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, managed-payouts]
---

## Overview

Captured API Explorer reference for Adyen's incoming `balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed` webhook. Adyen sends it when a managed payout schedule could not be automatically applied to a balance account. This reports a schedule-configuration failure, not a payout execution, transfer, or bank-credit outcome. The `latest` URL was captured on 2026-09-15; it does not identify a fixed API version.

## Key takeaways

- The webhook body table requires top-level `data`, `environment`, and `type`; `timestamp` is optional. `environment` can be `test` or `live`. Within `data`, all listed properties are marked optional: `balanceAccountId`, `balancePlatform`, `balancePlatformPayoutScheduleId`, `reason`, and `transferInstrumentId`.
- `balanceAccountId` identifies the balance account on which application failed. `balancePlatformPayoutScheduleId` identifies the schedule that was not applied. `reason` can explain why. `transferInstrumentId`, when present, identifies the linked transfer instrument described as the counterparty account for that schedule. The table does not enumerate reason values or guarantee any optional field appears in every event.
- The response section instructs the receiver to return any HTTP `2xx` to accept the webhook. The captured reference gives no example payload or event-specific delivery, ordering, retry, deduplication, signature, recovery, or financial-finality rule.

## Detail locators

- Event name and trigger: raw lines 5–7.
- Request body requiredness, IDs, reason, transfer instrument and environment: raw lines 11–22.
- Response and acknowledgment: raw lines 24–32.

## Related

- [[adyen]]; [[adyen-webhooks]]; [[adyen-platforms]].

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed/2026-09-15|2026-09-15 captured API Explorer reference]]
