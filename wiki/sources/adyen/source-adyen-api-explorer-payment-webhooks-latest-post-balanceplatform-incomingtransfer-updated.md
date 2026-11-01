---
title: "Adyen deprecated Payment webhook: incoming transfer updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payment-webhooks/latest/post/balancePlatform.incomingTransfer.updated"
raw_files:
  - "adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.incomingTransfer.updated/2026-09-15.md"
tags: [adyen, platforms, payment-webhooks, incoming-transfers, deprecated]
---

## Overview

This `balancePlatform.incomingTransfer.updated` reference describes an incoming Adyen Payment webhook when funds were added to a balance account due to a refund or funds transfer. Its parent Payment webhooks v1 overview marks this family deprecated and directs use of accounting webhooks in the Transfer-webhooks API Explorer instead. This endpoint snapshot documents the legacy event, not the replacement Transfer webhook contract. [[adyen]] [[adyen-platforms]] [[adyen-webhooks]]

## Key takeaways

- The page says `data.id` tracks the original incoming-transfer resource from `balancePlatform.incomingTransfer.created`. The optional `paymentId` instead traces the original payment authorisation, refund, or funds-transfer request from `balancePlatform.payment.created`. These are different resource references. See raw lines 5–13, 40, 47.
- For this event type, `data.status` is `Refunded` for refunds or `IncomingTransfer` for incoming fund transfers. The generic status table also lists values for other webhook types; do not assign those to this event. See raw lines 9–13 and 63.
- The request table requires outer `data`, `environment`, and `type`. It marks `data.id`, `data.status`, `data.amount`, `data.balanceAccount`, and other details optional. If an optional `amount` or `originalAmount` object is present, its `currency` and minor-unit `value` are required within it. Positive and negative values indicate addition to and deduction from the balance account, respectively. See raw lines 17–72.
- `modification` is optional and describes the amount and type of the modification triggering this notification; `paymentId`, platform-payment references, `reference`, and `referenceForBeneficiary` have separate meanings. Consult the request table at raw lines 39–63 before correlating resources.
- The receiver can return any HTTP `2xx` status to accept the webhook. This receipt is separate from the event's funds-movement meaning. See raw lines 117–125.

## Detail locators

- Event identity, trigger, statuses and resource correlation: raw lines 5–13.
- Full request schema, requiredness and reference fields: raw lines 15–72.
- Sample incoming-transfer payload: raw lines 74–116.
- Receiver response: raw lines 117–125.
- Family deprecation and replacement direction: [[source-adyen-api-explorer-payment-webhooks-latest-overview]], raw lines 5–7.

## Related

- [[adyen-platforms]]
- [[adyen-webhooks]]
- [[source-adyen-api-explorer-payment-webhooks-latest-overview]]

## Raw Sources

- [[raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.incomingTransfer.updated/2026-09-15|Incoming transfer updated endpoint snapshot]]
