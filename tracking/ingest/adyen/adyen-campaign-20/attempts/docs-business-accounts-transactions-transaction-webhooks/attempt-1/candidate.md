---
title: "Adyen Business Accounts: Transaction webhooks"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/transactions/transaction-webhooks"
raw_files:
  - "adyen/docs/business-accounts/transactions/transaction-webhooks/2026-09-15.md"
tags: [adyen, business-accounts, transaction-webhooks, transfers]
---

## Overview

This [[adyen]] guide explains `balancePlatform.transaction.created` webhooks for balance-account debits or credits related to external bank and internal balance-account transfers. The page sits under Business Accounts but lists Adyen for Platforms, Issuing, or Payouts integration as its prerequisite scope; its examples illustrate Business Accounts transfer patterns. A transaction webhook records balance-account movement and can complement Transfer webhooks, which report transfer status changes. The 2026-09-15 capture is marked modified that day, and payload examples are in TEST. It does not establish counterparty-bank receipt or a live transfer.

## Key takeaways

- Subscribe to Transaction webhooks and make the server able to receive and accept webhooks; the requirements table also lists Standard webhooks and treats Transfer webhooks as optional. Transfer webhooks can provide status progression; transaction webhooks are sent only when transfer funds are credited or debited from the balance account.
- The page divides transaction events by outgoing/incoming balance-account movement and external/internal transfer. It gives a booked outgoing external bank transfer, a booked outgoing internal debit, a booked incoming external bank transfer, and a booked incoming internal credit. In the example payloads, `data.id` identifies the transaction event and `data.transfer.id` identifies the related transfer; amount signs are negative for outgoing and positive for incoming. Follow the raw sections for fields and TEST payloads.
- Do not copy the examples as a consistent request/response contract. The outgoing external prose says EUR 100.00 but its request example has `value: 150000` and the transaction webhook has `value: -10000`. For the internal direct debit, the explanatory outgoing table calls `balanceAccount` the request-receiving/debited account, but its negative-amount payload names the request's initiating `balanceAccountId`; the incoming table calls `balanceAccount` the initiating/credited account, but its positive-amount payload names the request's counterparty account. The source does not resolve these account-role conflicts. Use the current API reference and actual webhook data to validate mapping.
- A `booked` transaction webhook supports the documented balance-account debit/credit, not full transfer history, bank settlement, beneficiary receipt, or user-facing statement delivery.

## Detail locators

- Opening and `Requirements` (raw lines 15–31): applicability, transaction-versus-transfer webhooks, subscription/setup.
- `Types of transaction webhooks` and `Sending funds (outgoing)` (raw lines 33–45): internal/external and outgoing taxonomy.
- `Outgoing external transactions` (raw lines 47–139): request and transaction sample, including EUR amount mismatch at 49, 61 and 104.
- `Outgoing internal transactions` (raw lines 141–220): direct-debit request, field descriptions and negative TEST event, including balance-account conflict at 157–160, 175 and 211–213.
- `Receiving funds (incoming)` (raw lines 222–339): external and internal booked events, including internal balance-account conflict at 288–296 and 330–332.

## Related

- [[adyen-business-accounts]] — Business Accounts product route.
- [[adyen-platform-internal-transfers]] — internal balance-account transfer context.
- [[adyen-webhooks]] — general webhook integration context.

## Raw Sources

- [[raw/adyen/docs/business-accounts/transactions/transaction-webhooks/2026-09-15|Adyen transaction webhooks, captured 2026-09-15]]
