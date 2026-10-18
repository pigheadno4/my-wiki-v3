---
title: "Adyen Business Accounts: Query third-party transfer transactions"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/transactions"
raw_files:
  - "adyen/docs/business-accounts/transactions/2026-09-15.md"
tags: [adyen, business-accounts, transfers, transactions, reconciliation]
---

## Overview

This 2023-modified page, captured 2026-09-15 under Business Accounts, explains on-demand transaction lookup through the Transfers API `GET /transactions` and `GET /transactions/{id}`. The list can be scoped to a balance platform, account holder or balance account. Despite the page title's third-party-transfer focus, the guide's requirements also name Adyen for Platforms, Issuing or Payouts integrations, and its examples cover internal and external transfers. A query response is transaction/accounting evidence within its stated status, not proof of a recipient bank's receipt.

## Key takeaways

- The page requires an eligible integration, a Transfers API credential with the TransferService Webservice Retrieve role assigned through an Adyen contact, and transfers enabled for the source balance account. Its rendered requirements row is malformed; these are the legible conditions in raw lines 21–27, not proof that any credential or account has them.
- For the list request, the guide marks at least one of `balancePlatform`, `accountHolderId` or `balanceAccountId`, plus `createdSince` and `createdUntil`, as required query parameters. It describes `limit`, `sortOrder`, `cursor` and `paymentInstrumentId` as additional filters/pagination inputs. The response uses `data` and conditional `_links`; the next page uses the returned cursor. A specific transaction can be requested by `transactionId` at `GET /transactions/{id}`. The sample curl contains an unexplained `accountHolder` fragment and some generated SDK snippets are malformed or version-specific, so use the parameter table and current API reference for implementation rather than copying them unexamined.
- In this guide, positive `amount.value` means incoming funds added to the balance account; negative means outgoing funds deducted. `pending` incoming is not yet added and `pending` outgoing is reserved for deduction; `booked` means added or deducted, respectively. These statuses concern the Adyen balance account and must not be read as confirmation of an external beneficiary's bank receipt.
- `bookingDate` records when funds are reserved/pending in the balance account in the after-cut-off example, while `valueDate` indicates when they are deducted or made available. The page says outgoing funds are deducted at the booked stage. Example JSON shows references and identifiers for transfers, account holders and balance accounts, plus external/internal category data; treat those sample values and field presence as illustrations.

## Detail locators

- Opening and `Requirements` — Transfers API purpose, query scopes and integration/role/source-account conditions (raw lines 15–27).
- `Use cases` and `Get a list of transactions` — internal/external examples, required and optional query parameters (raw lines 29–54).
- Request/response examples — test-environment curl and version-labeled SDK snippets, `data`/`_links` pagination and transaction-ID lookup (raw lines 56–354).
- `Identify incoming and outgoing funds` — sign, reference and `pending`/`booked` meanings (raw lines 356–368).
- `External transactions` and `Internal transactions` — illustrative outgoing/incoming transaction objects and transfer category examples (raw lines 370–538).
- `Booking and value dates` — after-cut-off reserved-versus-deducted distinction (raw lines 540–549).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-business-accounts]]
- Platform context: [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/business-accounts/transactions/2026-09-15|2026-09-15 Business Accounts transaction-query guide]]
