---
title: "Adyen Payment webhooks: incomingTransfer.created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payment-webhooks/latest/post/balancePlatform.incomingTransfer.created"
raw_files:
  - "adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.incomingTransfer.created/2026-09-15.md"
tags: [adyen, platforms, payment-webhooks, incoming-transfers, deprecated]
---

## Overview

This 2026-09-15 API Explorer reference describes the incoming `balancePlatform.incomingTransfer.created` webhook in the Payment webhooks family. Adyen sends it when incoming funds are due to a refund or funds transfer. Use `data.paymentId` to relate the event to the original refund or funds-transfer request and inspect the content to distinguish those cases: the refund includes the target payment instrument, while an incoming funds transfer includes only balance-account information. The separate [[source-adyen-api-explorer-payment-webhooks-latest-overview|Payment webhooks overview]] labels this v1 family deprecated and directs readers to accounting webhooks; its migration notice does not change the event contract captured here. [[adyen]] [[adyen-platforms]] [[adyen-webhooks]]

## Key takeaways

- Required top-level fields are `data`, `environment` (`test` or `live`) and `type`. `timestamp` is optional and is when the event was queued. In `data`, account-holder, balance-account, counterparty, payment-instrument and related platform-payment objects, resource `id`, `paymentId`, `reference`, amounts and dates are listed as optional. If `amount` or `originalAmount` is supplied, its nested `currency` and minor-unit `value` fields are required by the table; the parent objects themselves are not required.
- For `balancePlatform.incomingTransfer.created`, the status table lists `PendingIncomingTransfer`. It lists `Refunded` or `IncomingTransfer` for the separate updated event. The sample is a test `PendingIncomingTransfer` with a positive EUR amount, balance-account and counterparty balance-account IDs; it illustrates a pending state, not final credit or bank receipt. The amount description defines positive as added to the balance account and negative as deducted, but the sample is not execution evidence.
- The response table says to send any HTTP `2xx` to accept the webhook. Receiver acceptance is distinct from the incoming transfer's later status. `valueDate`, if present, is an expected settlement date; it is not a settled-funds guarantee.

## Detail locators

- Trigger and refund-versus-transfer content distinction: raw lines 5–11.
- Request-body requiredness, identities, amount signs and conditional nested amount fields: raw lines 13–60; event-specific status table, `valueDate`, environment and type: lines 61–70.
- Test JSON example and its pending state: raw lines 72–114.
- Receiver response: raw `## Responses` → `### 200 Success`, lines 115–123.

## Related

- [[source-adyen-api-explorer-payment-webhooks-latest-overview]] — separate v1 family deprecation and accounting-webhook migration notice.
- [[source-adyen-api-explorer-transfer-webhooks-latest-overview]] — distinct Transfer webhooks v4 catalog; use its child event references for current transfer payloads and states.
- [[adyen-platforms]] — modern balance-platform context.

## Raw Sources

- [[raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.incomingTransfer.created/2026-09-15|Payment webhook incomingTransfer.created (2026-09-15)]]
