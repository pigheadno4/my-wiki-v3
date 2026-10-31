---
title: "Adyen Transfer webhooks v4: transfer created event"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfer-webhooks/latest/post/balancePlatform.transfer.created"
raw_files:
  - "adyen/api-explorer/transfer-webhooks/latest/post/balancePlatform.transfer.created/2026-09-15.md"
tags: [adyen, webhooks, transfers, balance-platform]
---

## Overview

Captured `balancePlatform.transfer.created` incoming webhook reference in the Transfer webhooks catalog, whose separately captured overview is headed v4. Adyen says it sends this event when there are fund movements on a platform. The `POST` heading describes an event delivered to a receiver, not a merchant API operation. This schema spans incoming and outgoing transfer categories, so the event name alone does not prove that funds were booked or reached a bank. See [[adyen]], [[adyen-webhooks]], and [[adyen-platforms]].

## Key takeaways

- The request-body table requires top-level `data` and `environment` (`test` or `live`); top-level `type` and `timestamp` are marked optional. Within `data`, `amount` with minor-unit `value` and `currency`, `category`, and `status` are required. The listed categories are `bank`, `card`, `internal`, `issuedCard`, `platformPayment`, and `topUp`; direction, transfer/resource IDs, counterparties, event history and sequence number are optional. Some nested descriptions impose category-specific conditions despite `No` in their table rows: for example, `ultimateParty` full name for bank and individual-name/type details for card. Read the exact nested field context before treating an optional row as universally absent or required.
- `status` describes a transfer result, with examples ranging from `received` (outgoing request created) and `authorised` (funds reserved) to `booked` (deducted from the user's balance account), `refused`, `failed` (counterparty-bank rejection), and `returned` (counterparty-bank return). These are distinct stages. In particular, `booked` is balance-account deduction, not beneficiary-bank receipt. A future execution date leaves status `received` and reason `pending` until that date according to its field description.
- Optional `events` separate `accounting` from `tracking`; an event `transactionId` is sent only for accounting events where the balance changes. The optional transfer `sequenceNumber` starts at 1 and can help restore per-transfer order if webhooks arrive out of order; it is not a delivery-order guarantee. `eventId` is documented only for `issuedCard`. These identifiers and the transfer's `id`, `reference`, and beneficiary reference have different roles.
- The four TEST examples cover incoming internal, initiated on-demand top-up, initiated scheduled top-up, and outgoing external bank transfer. They show `received` status, including a negative `received` register mutation for the outgoing bank example, but are illustrative snapshots rather than proof of later authorization, booking, settlement, or bank receipt. The two top-up examples use different `category` values (`topUp` and `platformPayment`), so they do not establish one universal top-up category mapping.
- The response section says any `2xx` accepts the webhook; optional `notificationResponse` appears in its `200 Success` table. This is receiver acknowledgement, not transfer outcome. The endpoint does not supply delivery, retry, deduplication or signature guarantees. The `latest` route and captured v4 family heading do not prove which version is currently served.

## Detail locators

- Event trigger and required envelope/core transfer fields: pinned raw lines 5–21, 32, 93–94, 115–117.
- Transfer categories, optional identities, event/tracking and accounting fields, future execution, status meanings, conditional `ultimateParty` details: `## Parameters` → `### Request body`, lines 22–114.
- Four `## Request examples`: incoming internal lines 121–175; on-demand top-up 177–239; scheduled top-up 241–298; outgoing external bank 300–362.
- `## Responses` → `### 200 Success`, lines 363–371.

## Related

- [[adyen-platform-internal-transfers]] — one category-specific flow; this contract also spans other transfer categories.

## Raw Sources

- [[raw/adyen/api-explorer/transfer-webhooks/latest/post/balancePlatform.transfer.created/2026-09-15|Captured transfer created webhook reference (2026-09-15)]]
