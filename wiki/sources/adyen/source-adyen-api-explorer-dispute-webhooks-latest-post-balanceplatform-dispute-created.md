---
title: "Adyen Dispute webhook: balance-platform dispute created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.created"
raw_files:
  - "adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.created/2026-09-15.md"
tags: [adyen, dispute-webhooks, balance-platform, disputes]
---

## Overview

This captured Dispute Webhooks API Explorer POST reference describes Adyen's incoming `balancePlatform.dispute.created` event when a dispute is created. The page says the webhook only informs the receiving server of requests. It is a balance-platform dispute event contract, distinct from a merchant request to accept or defend a dispute and from the separate Standard dispute notification flow. The `latest` route label gives no numbered webhook version. See [[adyen-webhooks]], [[adyen-risk-management]], and [[adyen]].

## Key takeaways

- The body table requires only `data` and outer `type`. All listed fields under `data` are optional: capture Acquirer Reference Number (`arn`), balance platform, event-trigger `creationDate`, description, disputed amount, dispute resource `id`, current dispute `status` and `statusDetail`, disputed `transactionId`, and dispute `type`. This page gives no status or type enum and no request example.
- `disputedAmount` is optional, but its `currency` and minor-unit integer `value` are marked required when the amount object is supplied. The table says the disputed amount cannot exceed the transaction amount and that omission means the whole transaction amount is disputed. This describes dispute amount, not a debit, reversal, transfer, or payment outcome.
- The optional `arn` is described as a scheme-generated reference for each capture; `transactionId` refers to the transaction for which the dispute is requested. The optional dispute `id` is a separate resource ID. The reference does not establish a match to a specific payment or transfer without the relevant identifiers.
- Any HTTP `2xx` accepts the webhook, with optional `notificationResponse`. A received dispute-creation notification or acknowledgment does not determine dispute resolution, payment finality, fund movement, or bank receipt. The page does not specify delivery ordering, retry, deduplication, or signature rules.

## Detail locators

- Event and information-only statement: pinned raw lines 5–7.
- Required envelope and optional dispute, transaction, capture and amount fields: pinned raw lines 11–27.
- Acknowledgment response: pinned raw lines 29–37.

## Related

- [[adyen-webhooks]] — webhook family and receipt context.
- [[adyen-risk-management]] — dispute monitoring and handling context.
- [[source-adyen-docs-risk-management-disputes-api-dispute-notifications]] — separate Standard dispute webhook route; do not substitute its payload for this event.

## Raw Sources

- [[raw/adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.created/2026-09-15|Balance-platform dispute created webhook reference, captured 2026-09-15]]
