---
title: "Webhook structures and types for platforms | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/webhook-types"
raw_files:
  - "adyen/docs/platforms/webhook-types/2026-09-15.md"
tags: [adyen, platforms, webhooks, transfers, balances]
---

## Overview

This 2026-09-15 Adyen for Platforms catalog maps webhook families, event `type` values, broad payload structure and object-specific meanings. It is a routing reference for asynchronous platform events, not evidence that a particular subscription was configured, an event was delivered, a payout reached a bank, or funds actually moved. See [[adyen]], [[adyen-platforms]], and [[adyen-webhooks]].

## Key takeaways

- The catalog says webhooks may follow resource creation/update, request initiation, or funds movement. A general body has `data`, `environment` and `type`; `data` varies by type and some types include `data.status`. The listed initial groups are Configuration, onboarding on invite, payment method, Transfer, negative-balance warning and Report, while a separate Balance section also appears later (raw lines 19–46, 175–181).
- Configuration events cover account holders, balance accounts, managed payout schedules at balance-platform/balance-account/payout-execution grains, custom payout sweeps, payment instruments and an optionally enabled risk signal. A payout-schedule execution `succeeded` means a payout was initiated and its resulting `transferId` is in `resultDetails`; skipped/failed executions have distinct reasons. Schedule creation or an initiated payout does not prove booking or beneficiary-bank receipt (raw lines 80–132).
- Onboarding-on-invite `accountHolder.onboarded` concerns default resources; payment-method events concern request outcomes/removal; transfer `created` is a request and `updated` is a request status change. The table distinguishes payment/capture, refund, chargeback, payout, internal transfer and third-party bank transfer using category/type/counterparty fields. These are object/event distinctions, not one interchangeable payment status (raw lines 134–173).
- Balance `balanceAccount.balance.updated` reports a balance change. The negative-balance compensation warning reports a transfer scheduled after more than 20 days negative balance, and report-created means a report is ready for download. Legacy payment webhook types are explicitly deprecated in favor of transfer webhooks; their status examples must not be used as the current platform event path (raw lines 175–210).
- Some managed-payout schedule rows visibly include spaces after `balancePlatform.` in rendered link labels. Consult the linked API Explorer schema for exact event identifiers and payloads rather than copying those labels verbatim (raw lines 100–111). The example `accountHolder.created` payload is a test illustration, not a delivered event for a real account (raw lines 48–78).

## Detail locators

- General structure/example: raw lines 34–78.
- Configuration resource and payout-schedule event tables: raw lines 80–132.
- Onboarding, payment method, Transfer event distinctions and classification table: raw lines 134–173.
- Balance, negative-balance warning, report, and deprecated payment groups: raw lines 175–210.

## Related

- [[adyen-webhooks]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-payout-webhooks]]

## Raw Sources

- [[raw/adyen/docs/platforms/webhook-types/2026-09-15|Pinned Adyen platform webhook types catalog]]
