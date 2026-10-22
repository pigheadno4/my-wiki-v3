---
title: "Adyen Payout Service card-payout transfer webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-cards/payout-webhooks"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-cards/payout-webhooks/2026-09-15.md"
tags: [adyen, payout-service, card-payouts, transfer-webhooks]
---

## Overview

This 2023-modified, 2026-09-15-captured Payout Service guide describes Transfer webhooks for outgoing payouts from a balance account to a Mastercard or Visa card. It distinguishes initiation and accounting status from later card-scheme tracking and failure. It is a webhook guide, not proof that funds reached a card. [[adyen]] [[adyen-payouts]]

## Key takeaways

- The guide requires a Payout Service integration, a server able to receive and accept webhooks, and Customer Area subscriptions to both Transfer and Transaction webhooks. It identifies the card-payout Transfer events by `category=card`, `direction=outgoing` and `type=cardTransfer`. See raw lines 28-46. The examples here cover Transfer events; this page does not detail Transaction webhook payloads.
- `balancePlatform.transfer.created` reports an initiated outgoing request. `balancePlatform.transfer.updated` reports subsequent statuses: `authorised` reserves the amount; `booked` deducts it and includes `events.transactionId`. Booking is explicitly not final: scheme or issuing-bank rejection may still cause failure. See raw lines 59-72, 305-307 and 584-592.
- After booking, a flagged transfer can enter Adyen internal review. Its `trackingData.status=pending` and `trackingData.type=internalReview` are tracking fields while the sample's transfer `status` remains `booked`. The page recommends fuller `counterparty.card.cardHolder` details to speed review; that recommendation is not a universal request requirement. Review failure is reported in a tracking event with `reason=refusedForRegulatoryReasons`, `status=failed`, `type=internalReview`, and the page directs the reader to Support. See raw lines 920-929, 1030-1048 and 1296-1302.
- Card-scheme acceptance is another tracking event, with `trackingData.status=accepted` and `type=confirmation`; the sample transfer `status` still reads `booked`. The page says the scheme will process the payout and funds will arrive soon, not that the cardholder has received them. See raw lines 1304-1313 and 1412-1432.
- A later `balancePlatform.transfer.updated` may report `status=failed` after unsuccessful automatic retries, with a transaction identifier and failure information. The failed example follows a booked event, shows a compensating positive balance mutation, and includes `networkReason` code `14` / “Invalid card number.” The reason-code table gives conditional remediation by code; do not treat it as an unconditional retry instruction. See raw lines 1436-1446, 1531-1572 and 1829-1844.
- **Source wording conflict:** the opening says a balance-account payout goes to “your bank account,” and the failure paragraph names an external banking system, while the page title, card identifier table and samples identify Mastercard/Visa card payouts. Keep this entry card-scoped; the bank wording does not establish a bank-transfer payload. The narrative says its examples pay EUR 100.00, whereas sample JSON uses `amount.value=100` EUR. The page does not reconcile those figures; do not use these samples to compute a card payout amount. See raw lines 17-25, 44-57, 89-94 and 1436-1438.

## Detail locators

- `## Requirements` and `## Identify payout-related webhooks`, raw lines 28-57: webhook setup, category/direction/type and event list.
- `## Payout initiated`, raw lines 59-303: one-off raw card, tokenized one-off and recurring request examples.
- `## Payout authorised` and `## Payout booked`, raw lines 305-919: reservation versus deduction, transaction ID and nonfinal booking.
- `## Payout pending`, raw lines 920-1303: post-booking internal review, conditional failure and sample tracking fields.
- `## Payout accepted`, raw lines 1304-1435: scheme-processing confirmation, not arrival.
- `## Payout failed` and `## Reason codes`, raw lines 1436-1844: post-booking failure examples, reversal mutation, network reason and code-specific actions.

## Related

- [[adyen-payouts]] — Payout Service and legacy Online Payout API separation.
- [[source-adyen-docs-payouts-payout-service-payout-lifecycle]] — broader Payout Service lifecycle.
- [[source-adyen-docs-payouts-payout-service-getting-paid-payout-webhooks]] — separate bank-payout webhook guide.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-cards/payout-webhooks/2026-09-15|Adyen card-payout webhook guide, captured 2026-09-15]]
