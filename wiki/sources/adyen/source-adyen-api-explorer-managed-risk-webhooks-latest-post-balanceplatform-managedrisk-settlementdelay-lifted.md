---
title: "Adyen Managed Risk webhook: settlementDelay.lifted"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.lifted"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.lifted/2026-09-15.md"
tags: [adyen, platforms, managed-risk, webhooks, settlement-delay]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Adyen's incoming `balancePlatform.managedRisk.settlementDelay.lifted` webhook when Adyen lifts a settlement delay from an account holder's payouts after the risk review period. It concerns a Managed Risk payout measure for an account holder, not a balance-account settlement-delay configuration change or proof of a completed payout. [[adyen]] [[adyen-platforms]] [[adyen-webhooks]]

## Key takeaways

- The payload requires `data`, `environment` (`test` or `live`), and webhook `type`. Within `data`, `accountHolderId` and `reason` are required. The account-holder identifier is the subject whose risk settings changed (raw lines 14–21).
- The `reason` enumeration is `paymentProcessingEnabled`, `settlementDelayChanged`, or `riskReviewPeriodPassed`. The example chooses `riskReviewPeriodPassed`; the event heading and example do not make that the only possible reason (raw lines 18, 25–37).
- `data.balancePlatform` and `data.creationDate` are optional. The latter is the event-trigger time in ISO 8601 extended format; optional top-level `timestamp` is the time the event was queued. The example includes `data.id`, but the request-body table does not define it, so do not assume a required or stable identifier contract from that sample (raw lines 16–20, 28–36).
- The response section lists HTTP 200 success and says any `2xx` HTTP status accepts the webhook; `notificationResponse` is optional (raw lines 39–47). Acceptance concerns delivery receipt. This page gives no amount, balance-account mutation, payout execution, bank receipt, delivery-order, retry, deduplication, or signature rule.

## Detail locators

- Event purpose: raw lines 5–7.
- Field requiredness, reason enum and distinct event/queue times: raw lines 9–21; full example and unmodeled `id`: raw lines 23–38.
- Receiver response: raw lines 39–47.

## Related

- [[adyen-platforms]] — modern account-holder and payout context, with reciprocal source route.
- [[source-adyen-api-explorer-managed-risk-webhooks-latest-overview]] — separate Managed Risk event catalog.
- [[source-adyen-docs-platforms-custom-payouts-configure-settlement-delay]] — separate balance-account settlement-delay configuration guide.

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.lifted/2026-09-15|Managed Risk settlement-delay-lifted webhook capture]]
