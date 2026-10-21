---
title: "Adyen Marketplace transaction webhooks for balance-account transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/transfer-transactions/track-webhooks"
raw_files:
  - "adyen/docs/marketplaces/transfer-transactions/track-webhooks/2026-09-15.md"
tags: [adyen, marketplaces, transactions, transfers, webhooks]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] guide describes `balancePlatform.transaction.created` webhooks for funds debited from or credited to a user's balance account in external or internal transfers. Transaction webhooks mark balance-account fund movements; Transfer webhooks report transfer status changes. The page lists Adyen for Platforms, Issuing or Payouts as integration types despite its Marketplace URL. See [[adyen-platforms]].

## Key takeaways

- **Event grain and setup:** A transfer-status webhook can be sent for every status change, whereas this transaction webhook is sent only when transfer funds are credited or debited at a balance account. The page requires a supported integration, Standard and Transaction webhook subscriptions, and a server able to receive and accept webhooks; Transfer webhook subscription is optional here and provides complementary status context. In samples, `data.id` identifies a transaction event and `data.transfer.id` identifies its related transfer. Neither a request nor a status webhook alone proves a balance booking. See pinned raw lines 15–39.
- **Outgoing debit:** For an external bank payout or an internal balance-account transfer, the guide illustrates `POST /transfers`, followed by `balancePlatform.transaction.created` after booking. Its negative sample `amount.value` belongs to the named source balance account and its account holder; the external sample has bank category data and the internal sample has internal category data. Balance-account debit is distinct from beneficiary-bank credit. See pinned raw lines 40–207.
- **Incoming credit:** The guide covers incoming external/top-up and internal transfer bookings. Its positive sample amounts and target `balanceAccount` identify the receiving side. The incoming-external prose describes a booked incoming third-party transfer, but its sample `transfer.categoryData.type` is `platformPayment` and contains payment PSP references; do not use that payload as a canonical bank top-up schema without checking the separate API/webhook reference. See pinned raw lines 209–327.
- **Sample identity and outcome boundaries:** Outgoing external/internal samples reuse one illustrative transaction `data.id` while showing different `transfer.id` values; incoming external/internal samples also reuse a transaction ID. Treat those IDs as examples, not a cross-event join. The displayed `status: booked` records a balance-account mutation, not a bank payout arrival, final settlement, card outcome or legal fund ownership. This page does not define payout failures/returns; follow its payout-webhook route for that lifecycle. See pinned raw lines 87–127, 168–207, 230–327 and 329–338.

## Detail locators

- Transaction versus Transfer webhook meaning, integration and subscription requirements: pinned raw lines 15–39.
- Outgoing external request/debit sample and fields: pinned raw lines 40–127; outgoing internal request/debit sample: lines 129–207.
- Incoming external credit description and `platformPayment` example: pinned raw lines 209–272; incoming internal credit: lines 274–327.
- Related API, payout status and reconciliation routes: pinned raw lines 329–338.

## Related

- [[adyen-platforms]] — reciprocal platform concept.
- [[source-adyen-docs-platforms-transfer-transactions-track-webhooks]] — same dated guide under the Platforms path.
- [[source-adyen-docs-marketplaces-payout-webhooks]] — payout Transfer webhook status, tracing and return route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/transfer-transactions/track-webhooks/2026-09-15|Marketplace transaction webhook guide, captured 2026-09-15]]
