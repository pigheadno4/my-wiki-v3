---
title: "Adyen Marketplace top-up webhooks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/top-up-balance-account/top-up-webhooks"
raw_files:
  - "adyen/docs/marketplaces/top-up-balance-account/top-up-webhooks/2026-09-15.md"
tags: [adyen, marketplaces, platforms, top-ups, webhooks]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace-path guide explains the webhook stages for topping up a user's balance account through scheduled pull sweeps or on-demand payment requests. It belongs under [[adyen-platforms]]. A received or authorised transfer is a stage, while the guide associates a captured transfer and transaction.created booked event with the balance-account credit; the examples do not establish external funding finality or any bank receipt.

## Key takeaways

- Requirements name Adyen for Platforms and subscriptions to Standard, Transfer and Transaction webhooks, with a server able to receive and accept them. Standard AUTHORISATION applies when the request triggers a direct debit or payment authorisation; Transfer webhooks report incoming balance-account transfers/payments. See raw lines 21–36.
- Scheduled pull-sweep top-ups use an incoming `platformPayment` transfer of type `capture`. The illustrative EUR 5,000 threshold triggers a EUR 1,000 credit to the user's first balance account. Transfer-created `received` and transfer-updated `authorised` precede transfer-updated `captured` with a `transactionId`; the credited transaction.created sample has `status: booked`. See raw lines 38–57, 123–125 and 205–337.
- On-demand top-ups originate in payment requests and incur transaction fees. The guide says to expect webhook legs for each involved balance account and each `splits` entry in POST `/payments`. The example credits EUR 1,000 to the first user balance account and deducts EUR 3.44 in fees from the second. See raw lines 341–350.
- The on-demand credit leg is incoming `category: topUp`, `type: capture`, `platformPaymentType: TopUp`; the fee leg is outgoing `category: platformPayment`, `type: capture`, `platformPaymentType: PaymentFee`. Each has received, authorised and captured transfer stages, followed by a booked transaction.created sample when credited or deducted. Use the payment, modification, transfer and transaction references to reconcile the separate legs; do not treat a payment request or an AUTHORISATION alone as the booked credit. See raw lines 354–367, 523–664 and 666–675, 839–955.
- The fee example conflicts internally: prose and transfer payload identify the second balance account (`BA...02`) for the EUR 3.44 deduction, but the final fee transaction.created sample identifies the first (`BA...01`), and its transaction ID repeats the top-up credit sample ID. Its value date also precedes its booking date. Treat these TEST sample identifiers/dates as inconsistent examples, not a matching rule. See raw lines 345–350, 693–705, 913–927 and 943–976.

## Detail locators

- Scheduled webhook field values and lifecycle: raw lines 38–339.
- On-demand credit leg, payment references and booked event: raw lines 341–664.
- On-demand fee leg and booked-event sample conflict: raw lines 666–978.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-top-up-balance-account-top-up-webhooks]]
- [[source-adyen-docs-platforms-top-up-balance-account-scheduled-top-ups]]
- [[source-adyen-docs-platforms-top-up-balance-account-on-demand-top-ups]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/top-up-balance-account/top-up-webhooks/2026-09-15|Marketplace top-up webhook guide, 2026-09-15]]
