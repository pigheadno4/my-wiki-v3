---
title: "Transaction webhooks v4 overview | Adyen API Explorer"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transaction-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/transaction-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, transaction-webhooks, balance-platform, transfers]
---

## Overview

This captured Adyen API Explorer page is headed **Transaction webhooks v4**. It says Adyen sends transaction-information webhooks after a transfer is booked in a balance account, and lists one incoming event route: `POST balancePlatform.transaction.created`. The page suggests using these webhooks to update dashboard balances and track incoming or outgoing funds. [[adyen]] [[adyen-webhooks]] [[adyen-platforms]]

## Key takeaways

- The overview's trigger is a transfer booked in a balance account. The catalog entry is a Transaction webhook, not the transfer-initiation request or a Transfer-status webhook. Its text does not itself define whether an event represents a debit, a credit, or multiple ledger entries, and does not provide a payload schema, transaction/transfer identifiers, amounts or status fields. Use the event reference and [[source-adyen-docs-platforms-transfer-transactions-track-webhooks|Platforms Transaction webhook guide]] for that detail. [Raw: lines 5–20]
- The title explicitly says **v4** even though the captured route contains `latest`. This is a 2026-09-15 documentation snapshot, not proof of the current live version, a particular account's booking, recipient-bank receipt, delivery behavior or settlement. [Raw: lines 1–7]

## Detail locators

- Version label and booked-transfer trigger: heading and opening paragraph, lines 5–7.
- Suggested dashboard and fund-tracking uses: lines 9–13.
- Single event route: Endpoints table, lines 15–20.

## Related

- [[adyen-webhooks]] — event-family context.
- [[adyen-platforms]] — balance-account and transfer context.
- [[source-adyen-docs-platforms-transfer-transactions-track-webhooks]] — booked debit/credit event examples and Transaction-versus-Transfer distinctions.

## Raw Sources

- [[raw/adyen/api-explorer/transaction-webhooks/latest/overview/2026-09-15|Adyen Transaction webhooks v4 overview — captured 2026-09-15]]
