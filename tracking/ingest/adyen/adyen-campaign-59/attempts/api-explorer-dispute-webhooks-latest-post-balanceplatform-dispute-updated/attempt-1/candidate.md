---
title: "Adyen Dispute webhook: balance-platform dispute updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.updated"
raw_files:
  - "adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.updated/2026-09-15.md"
tags: [adyen, dispute-webhooks, disputes, balance-platform]
---

## Overview

Captured API Explorer `latest` POST reference for the incoming `balancePlatform.dispute.updated` webhook. Adyen says it sends the event when a dispute is updated and says this webhook only informs the receiving server of requests. It is an event about a dispute resource, not evidence that a dispute was won, lost, refunded, or financially settled. See [[adyen]], [[adyen-issuing]], and [[adyen-webhooks]].

## Key takeaways

- The body table requires top-level `data` and `type`. It marks every listed direct `data` field optional, including dispute resource `id`, transaction `transactionId`, `arn`, `status`, `statusDetail`, `type`, and `disputedAmount`. The table does not enumerate dispute statuses or types; `data.type` is distinct from the required top-level webhook `type`.
- `arn` is a card-scheme Acquirer Reference Number for a capture; `transactionId` refers to the transaction for which the dispute is requested. Neither ID is required by this event table, so the page does not require both to appear in each notification.
- If optional `disputedAmount` is present, its `currency` and minor-unit integer `value` are marked required within that object. Its description says a disputed amount cannot exceed the transaction amount and that if no amount was provided, the entire transaction amount is disputed. That describes the dispute amount rule; absence of `disputedAmount` in a received webhook should not be turned into a claim that this notification proves a specific full-amount outcome.
- Optional `creationDate` is the event-trigger time. The page lists no `environment` or queued `timestamp` field in this event table, and provides no request example. Any HTTP `2xx` accepts the webhook; acknowledgement does not decide or finalize the dispute. The captured `latest` route does not establish a numbered API version or current availability.

## Detail locators

- Event identity and request-only purpose: raw lines 5–7.
- Body requiredness, resource/transaction IDs, amount, and status fields: raw lines 9–27.
- Receiver acknowledgement: raw lines 29–37.

## Related

- [[adyen]]
- [[adyen-issuing]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.updated/2026-09-15|Captured dispute-updated webhook reference]]
