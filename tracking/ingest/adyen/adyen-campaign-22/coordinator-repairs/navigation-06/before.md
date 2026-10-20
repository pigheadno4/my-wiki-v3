---
title: "Adyen Issuing fund transfer webhooks"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/webhook-types/fund-transfers-webhooks"
raw_files:
  - "adyen/docs/issuing/webhook-types/fund-transfers-webhooks/2026-09-15.md"
tags: [adyen, issuing, fund-transfers, webhooks, balance-platform]
---

## Overview

This Adyen Issuing page (last modified 2020-03-16; captured 2026-09-15) maps Balance Platform webhooks for **bank transfers** moving funds between a balance account and an external source or transfer instrument. It defines `direction` relative to the balance account: `outgoing` leaves it; `incoming` enters it. The relevant transfer discriminator is `category: bank` with `type: bankTransfer`. The page sends readers to a separate deprecated page for payment webhooks related to fund transfers.

## Key takeaways

- For an outgoing transfer to a transfer instrument, `balancePlatform.transfer.created` reports a received request; `balancePlatform.transfer.updated` reports `authorised`, then `booked` when funds are deducted from the **source balance account**. The booked transfer identifies the target transfer instrument and a transaction ID. After booking, `balancePlatform.transaction.created` describes the source-account transaction.
- An outgoing `booked` status does **not** establish receipt by the external beneficiary: the guide says an additional `balancePlatform.transfer.updated` can report a later failure of the fund transfer to the transfer instrument.
- For an incoming external transfer, `balancePlatform.transfer.created` reports `received`; `balancePlatform.transfer.updated` reports `authorised`, then `booked` when funds are added to the **target balance account**. The booked event identifies the source transfer instrument and transaction ID. A `balancePlatform.transaction.created` event follows booking for the target-account transaction.
- The examples are test-environment event payloads, not evidence of a live movement of funds. Keep the transfer's top-level `id`, accounting `events[].id`/`transactionId`, and separate transaction webhook `id` distinct. The prose says “three webhooks” per direction, but also lists a later transaction-created event and an optional outgoing update; read it as three described transfer-state events rather than a fixed total webhook count.
- The authorised outgoing example is captioned `transfer.created` but has top-level `type: balancePlatform.transfer.updated`. The transaction field tables list `transfer.counterparty.transferInstrumentId`, while the shown transaction JSON omits it. Do not treat those sample payloads as a complete or self-consistent schema.

## Detail locators

- Trigger scope, discriminator and balance-account perspective: raw lines 19–38.
- Outgoing received, authorised and booked event descriptions: 40–50, 109–114, 189–196; accounting payload progression and transaction event: 198–340.
- Optional post-booking outgoing update and possible failure: 342–344.
- Incoming received, authorised and booked descriptions: 346–355, 415–420, 498–505; transaction event: 600–649.

## Related

- [[adyen-issuing]] — Issuing concept and source route.
- [[source-adyen-docs-issuing-add-manage-funds]] — Issuing funding routes.
- [[source-adyen-docs-issuing-webhook-types-payment-events]] — separate Issuing payment-event webhook guide.

## Raw Sources

- [[raw/adyen/docs/issuing/webhook-types/fund-transfers-webhooks/2026-09-15|Adyen fund transfer webhook guide, captured 2026-09-15]]
