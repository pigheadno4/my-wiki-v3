---
title: "Adyen legacy Payment webhook: outgoing transfer created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payment-webhooks/latest/post/balancePlatform.outgoingTransfer.created"
raw_files:
  - "adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.outgoingTransfer.created/2026-09-15.md"
tags: [adyen, platforms, payment-webhooks, transfers, deprecated]
---

## Overview

This 2026-09-15-captured API Explorer page specifies the incoming `balancePlatform.outgoingTransfer.created` event in the legacy Payment webhooks family. Adyen sends it when funds were deducted from a balance account because of a capture or funds transfer. For captures the event's `status` is `Captured`; for outgoing fund transfers it is `OutgoingTransfer`. The `paymentId` links to the original payment authorisation or funds-transfer request. The separate [[source-adyen-docs-platforms-webhook-types|Platforms webhook-type catalog]] marks Payment webhooks deprecated in favor of Transfer webhooks; this endpoint's fields should not be substituted for a Transfer webhook contract.

## Key takeaways

- The request-body table requires outer `data`, `environment` (`test` or `live`), and `type`, plus `data.counterparty`. It marks `data.status`, `paymentId`, `amount`, `balanceAccount`, `accountHolder`, and other detail fields optional. A required parent object does not make its listed children required.
- `data.amount` is in the balance account currency after conversion if needed; `data.originalAmount` is in the original transaction currency. For either, a negative value denotes a deduction and a positive value an addition. Where the optional amount object appears, its `currency` and minor-unit `value` children are required. The shown outgoing-transfer example has `-1500` EUR, `OutgoingTransfer` status, and `counterparty.balanceAccountId`; that illustration does not define every transfer's counterparty or amount.
- The optional `platformPayment` fields provide related split and payment/modification references; optional `purposeCode` distinguishes manual `payoutManual` from scheduled `payoutSweep` triggers. Optional `merchantData` is included only for payment authorisation requests and captures. Other optional request details and allowed status values by event type are in the raw table.
- The HTTP 200 response table instructs the receiver to use any `2xx` status to accept the webhook. Acceptance of this notification is distinct from a later transfer result or bank receipt. This page's `valueDate` is an expected settlement date, not a guaranteed settlement outcome.

## Detail locators

- Event meaning, correlation and capture-versus-transfer status: raw lines 5–13.
- Requiredness, amounts, counterparty, references, conditional merchant data, purpose and status mapping: raw lines 15–89.
- Illustrative outgoing-transfer payload: raw lines 91–134.
- Receiver acknowledgment: raw lines 135–143.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern platform account and transfer context.
- [[adyen-webhooks]] — webhook-family routing.
- [[source-adyen-docs-platforms-webhook-types]] — separate evidence for Payment webhook deprecation and Transfer webhook migration.
- [[source-adyen-api-explorer-transfer-webhooks-latest-post-balanceplatform-transfer-created]] — newer transfer-created event contract; compare its own resource and status semantics.

## Raw Sources

- [[raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.outgoingTransfer.created/2026-09-15|Payment webhook outgoingTransfer.created (captured 2026-09-15)]]
