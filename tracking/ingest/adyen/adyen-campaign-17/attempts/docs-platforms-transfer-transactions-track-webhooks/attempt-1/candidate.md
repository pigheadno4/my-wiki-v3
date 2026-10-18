---
title: "Adyen balance-platform transaction webhooks"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/transfer-transactions/track-webhooks"
raw_files:
  - "adyen/docs/platforms/transfer-transactions/track-webhooks/2026-09-15.md"
tags: [adyen, platforms, transactions, transfers, webhooks]
---

## Overview

This 2026-09-15 Adyen documentation explains `balancePlatform.transaction.created` webhooks as balance-account debit or credit notifications for transfers involving a bank account, another balance account or a card. It contrasts them with Transfer webhooks, which report transfer status changes. The page is under Platforms but lists Adyen for Platforms, Issuing or Payouts integrations as eligible integration types. It is event-shape guidance, not proof of a particular bank payout, card outcome, final settlement or legal ownership. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Distinct event grains:** A Transfer webhook can arrive for each transfer status change, while the Transaction webhook is sent only when transfer funds are credited to or debited from a balance account. The `data.id` in these examples identifies the transaction event; `data.transfer.id` identifies the related transfer. Do not treat the transaction ID, related transfer ID, webhook event, or example reference as interchangeable. A balance-account booking does not prove beneficiary-bank receipt.
- **Setup:** The page lists Adyen for Platforms, Issuing or Payouts integration. It says to subscribe to Standard and Transaction webhooks, with Transfer webhooks optional, and to ensure the server can receive and accept webhooks. Transfer webhooks add status context when used together; optional here does not mean transaction events represent every status change.
- **Outgoing debit:** For an external bank payout or an internal balance-account transfer, the page illustrates `POST /transfers` followed by `balancePlatform.transaction.created` after booking. The negative `amount.value` in the sample is a debit from the named source `balanceAccount`; `accountHolder` is the holder of that source account, and `transfer` describes the related transfer. The examples' EUR 100 and IDs are illustrative, not an executed payout or account balance proof.
- **Incoming credit:** The page describes incoming external/top-up and internal-transfer cases where the target balance account is credited after booking. The positive `amount.value` and `balanceAccount` identify the receiving side in the examples. Its incoming-external prose says an incoming third-party transfer is booked, but that example's `transfer.categoryData.type` is `platformPayment` with payment PSP references. Do not generalize that payload as the canonical third-party bank-transfer schema without checking the appropriate raw/API source.
- **Example and outcome boundary:** The outgoing external and internal examples reuse the same placeholder transaction `data.id` despite different related transfer IDs; incoming examples likewise reuse a placeholder transaction ID across distinct transfer categories. The examples are test payloads with `status=booked`, not a canonical cross-event join or proof that an external bank received funds. The page does not document payout failure/return or later bank acknowledgement; use the separate payout-transfer webhook guide for those states.

## Detail locators

- Definition, Transfer versus Transaction webhook frequency, requirements and internal/external direction: raw lines 15–39.
- Outgoing external transfer request, transaction fields and test debit sample: lines 40–127. Outgoing internal request and debit sample: lines 129–207.
- Incoming external prose and positive booked sample with `platformPayment` category data: lines 209–272. Incoming internal credit sample: lines 274–327. Related tracking and payout routes: lines 329–338.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform and balance-account context.
- [[source-adyen-docs-platforms-payout-webhooks]] — Transfer webhook payout status, bank-tracking, failure and return states.
- [[source-adyen-docs-platforms-view-transfers-details]] — transfer record/event-history retrieval across payment, bank and internal categories.

## Related raw API references

- The raw page links to Transaction and Transfer webhook API definitions, Transfers API POST, internal fund transfers, third-party transfer webhooks and payout reconciliation. Read those separately for current schemas and lifecycle guarantees.

## Raw Sources

- [[raw/adyen/docs/platforms/transfer-transactions/track-webhooks/2026-09-15|Adyen Docs: Track transactions with webhooks (2026-09-15 snapshot)]]
