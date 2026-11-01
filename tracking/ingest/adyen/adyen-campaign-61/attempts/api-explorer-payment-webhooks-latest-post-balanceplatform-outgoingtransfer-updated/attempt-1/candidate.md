---
title: "Adyen legacy outgoing transfer updated webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payment-webhooks/latest/post/balancePlatform.outgoingTransfer.updated"
raw_files:
  - "adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.outgoingTransfer.updated/2026-09-15.md"
tags: [adyen, platforms, payment-webhooks, outgoing-transfers, deprecated]
---

## Overview

This captured endpoint reference defines Adyen's incoming `balancePlatform.outgoingTransfer.updated` webhook. Adyen sends updated information after funds have been deducted from a balance account, including a possible transfer failure. Use `data.id` to track the original outgoing-transfer resource from `balancePlatform.outgoingTransfer.created`. See [[adyen]] and [[adyen-platforms]].

The **separate Payment webhooks v1 overview** labels this family deprecated and directs readers to accounting webhooks instead. Keep this legacy event contract separate from the newer Transfer and Transaction webhook families; their event schemas and states must be read from their own references. [[source-adyen-api-explorer-payment-webhooks-latest-overview]]

## Key takeaways

- Required top-level fields are `data`, `environment` (`test` or `live`), and `type`. The request-body table marks `data.counterparty` required; `data.id`, `status`, `amount`, `balanceAccount`, `accountHolder`, `paymentId`, `purposeCode`, `valueDate` and many other details optional. Currency and minor-unit value are required **within** optional `amount` or `originalAmount` objects.
- For this specific `type`, the table lists `TransferConfirmed`, `TransferSentOut`, and `TransferFailed` status values. The `TransferFailed` example is illustrative, not a universal outcome. `paymentId` traces the original payment authorisation, refund or funds-transfer request from `balancePlatform.payment.created`; it is distinct from `data.id` for the outgoing-transfer resource.
- The schema calls `valueDate` an expected settlement date. It identifies `payoutManual` for a one-off `/transfers` payout and `payoutSweep` for a scheduled sweep. Signed amount values describe addition to or deduction from the balance account, not bank credit.
- The response section says any HTTP `2xx` accepts the webhook. Receiver acceptance does not prove the transfer's final state or bank receipt.

## Detail locators

- Purpose and ID correlation: pinned raw lines 5–9.
- Request-body schema, including optional fields, references, statuses and timing: lines 11–85.
- Illustrative failure payload: lines 87–130.
- Response acceptance: lines 131–139.

## Related

- [[adyen-platforms]]
- [[source-adyen-api-explorer-transfer-webhooks-latest-overview]]

## Raw Sources

- [[raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.outgoingTransfer.updated/2026-09-15|Outgoing transfer updated endpoint capture]]

## Related raw API references

- [[raw/adyen/api-explorer/payment-webhooks/latest/overview/2026-09-15|Payment webhooks v1 family overview]]
