---
title: "Adyen Payout Service transaction-created webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/transfer-transactions/transaction-webhooks"
raw_files:
  - "adyen/docs/payouts/payout-service/transfer-transactions/transaction-webhooks/2026-09-15.md"
tags: [adyen, payout-service, transaction-webhooks, transfers, balance-accounts]
---

## Overview

This Payout Service-path guide (modified and captured 2026-09-15) describes `balancePlatform.transaction.created` webhooks when funds are **debited from or credited to a balance account** in transfers involving external bank/card counterparties or another balance account. It distinguishes these accounting notifications from Transfer webhooks for transfer status changes. Its prerequisite table also names **Adyen for Platforms, Issuing or Payouts** integrations, so the URL path alone does not narrow the event's scope. A booked balance-account debit is not proof that a third-party bank or card beneficiary received funds. See [[adyen]] and [[adyen-payouts]].

## Key takeaways

- **Subscriptions and event timing:** The page lists a server able to receive and accept webhooks and subscription to Standard and Transaction webhooks; it marks Transfer webhooks optional in the table. Transfer webhooks cover status changes, while transaction webhooks are sent only when funds from a transfer are credited or debited on a balance account. The example transaction events have `status: booked` and `environment: test`; use actual transfer-specific events for a real outcome.
- **Direction and resource ownership:** Outgoing external cases cover third-party bank and card payouts; outgoing internal cases cover funds sent from one balance account to another. Incoming internal cases cover the receiving balance account. `data.id` is the transaction-event identifier, while nested `data.transfer.id` identifies the related transfer record; `data.accountHolder` and `data.balanceAccount` refer to the source for outgoing events and destination for incoming internal events. Negative `amount.value` denotes an outgoing debit in examples; positive denotes incoming credit. The outgoing and incoming internal TEST examples use distinct transaction **and nested transfer** IDs, and this page does not identify those IDs as the same transfer's paired sides.
- **Example amount conflict:** The outgoing external prose calls for **EUR 100.00**, but its request JSON uses `amount.value: 150000` EUR, while the shown transaction webhook has `amount.value: -10000` EUR. The raw does not reconcile the request/event amounts; do not use this example to assert a booked amount or reconciliation rule. The internal request also renders `value` as a quoted string while its transaction examples show numeric values; avoid treating the snippets as a validated schema.
- **Evidence boundary:** A transaction-created webhook establishes the balance-account debit/credit reported by that event. It is different from initial request acceptance and from a bank/card network's later delivery or receipt. The page's examples are TEST payloads and cannot prove a live account's funding or payout completion.

## Detail locators

- Event purpose, Transfer-versus-Transaction webhook distinction, integration/subscription prerequisites: pinned raw lines 15-38.
- Outgoing external request, booked webhook fields and amount mismatch: pinned raw lines 40-135.
- Outgoing internal example and quoted request value: pinned raw lines 137-215.
- Incoming internal booked example and resource owner: pinned raw lines 217-274.

## Related

- [[adyen-payouts]] — main Payout Service concept and reciprocal source route.
- [[adyen-platform-internal-transfers]] — related balance-account-to-balance-account movement.

## Related raw API references

- [[raw/adyen/docs/payouts/payout-service/transfer-transactions/2026-09-15|Transaction lookup guide]] — related transaction-query page; separately reviewed or promoted by its own job.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/transfer-transactions/transaction-webhooks/2026-09-15|Payout Service transaction-webhook guide, captured 2026-09-15]]
