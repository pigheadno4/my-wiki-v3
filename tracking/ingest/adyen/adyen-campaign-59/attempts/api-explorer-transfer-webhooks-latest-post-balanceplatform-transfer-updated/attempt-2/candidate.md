---
title: "Adyen Transfer webhook: transfer updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfer-webhooks/latest/post/balancePlatform.transfer.updated"
raw_files:
  - "adyen/api-explorer/transfer-webhooks/latest/post/balancePlatform.transfer.updated/2026-09-15.md"
tags: [adyen, webhooks, transfers, balance-platform]
---

## Overview

Captured incoming `balancePlatform.transfer.updated` Transfer webhook reference. Adyen sends it when a transfer's status changes. Use `data.id` to correlate with the original transfer in `balancePlatform.transfer.created`; `data.status` is the transfer result, while each `data.events[].status` describes an individual event. The captured `latest` URL is not a fixed version.

## Key takeaways

- The schema requires the top-level `data` and `environment` fields. Within `data`, `amount` (with required `currency` and minor-unit `value`), `category`, and `status` are marked required; `data.id`, outer `type`, `timestamp`, event history and other details are marked optional in the table. The prose nevertheless directs correlation by `data.id`. Category values include bank, card, internal, issuedCard, platformPayment and topUp.
- `data.status` examples distinguish `received` request creation, `refused` Adyen rejection, `authorised` reservation, `booked` balance-account deduction, `failed` counterparty-bank rejection and `returned` counterparty-bank return. The event list can contain accounting/tracking events, mutations and transaction IDs; a transaction ID is described as sent only for accounting events where the balance changes. `eventId` is only included for issuedCard category.
- Optional `sequenceNumber` increases per transfer and can help restore event sequence if webhooks arrive out of order. This does not make arrival ordered. `referenceForBeneficiary` is described as carried in related transfer webhooks for source/recipient tracking; it is distinct from internal `reference`.
- The TEST examples illustrate outgoing bank payout authorisation and booking; an ordinary internal incoming target-account leg at authorised and booked stages (raw lines 299–457); a separate incoming/outgoing internal-direct-debit booked pair (raw lines 764–942); other direct-debit cases; and authorised/captured top-ups. A bank payout's `booked` status means source balance-account deduction, not beneficiary-bank receipt. The top-up examples show balance-account credit at `captured`, but do not establish external bank debit finality.
- **Example conflicts:** `directDebit-cancelled` has nested event `cancelled` but outer `data.status: refused` (raw lines 573–667). `directDebit-failed` has nested event `refused` but outer `data.status: cancelled` (669–762). Both use `sequenceType: FRST` although the table lists `OneOff`, `First`, `Recurring`, `Final` (line 49). Do not normalize these examples into a single state or enum.
- The response says any HTTP `2xx` accepts the webhook. The source does not establish event-specific retry, deduplication, signature verification or bank-credit finality.

## Detail locators

- Trigger, correlation and status semantics: raw lines 5–9, 79, 95–96.
- Full schema and conditional fields: raw lines 13–119.
- Bank payout and internal transfer examples: raw lines 121–457.
- Direct-debit examples and conflicts: raw lines 459–762; internal direct debit examples: 764–942.
- On-demand and scheduled top-up examples: raw lines 944–1281.
- Acknowledgment: raw lines 1282–1290.

## Related

- [[adyen]]; [[adyen-webhooks]]; [[adyen-platforms]]; [[adyen-platform-internal-transfers]].

## Raw Sources

- [[raw/adyen/api-explorer/transfer-webhooks/latest/post/balancePlatform.transfer.updated/2026-09-15|2026-09-15 captured API Explorer reference]]
