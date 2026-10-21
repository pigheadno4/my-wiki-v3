---
title: "Track Marketplace transactions with the Transfers API"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/transfer-transactions/track-api"
raw_files:
  - "adyen/docs/marketplaces/transfer-transactions/track-api/2026-09-15.md"
tags: [adyen, marketplaces, transactions, transfers, balance-accounts]
---

## Overview

This pinned Marketplace guide explains on-demand **transaction** queries through the Transfers API's `/transactions` endpoint. A transaction row describes a balance-account credit or debit related to a payment, internal transfer or external payout. Queries can cover a balance platform, account holder or balance account. This is recorded ledger state, not evidence that a beneficiary bank received a payout. See [[adyen]] and [[adyen-platforms]] (raw lines 15–36).

## Key takeaways

- The stated integration scope is Adyen for Platforms, Issuing or Payouts. The API credential needs **TransferService Webservice Retrieve role**, and the source balance account must have transfers enabled (raw lines 21–27).
- GET `/transactions` requires at least one of `balancePlatform`, `accountHolderId` or `balanceAccountId`, plus ISO 8601 `createdSince` and `createdUntil`. Optional `limit`, `sortOrder`, `cursor` and `paymentInstrumentId` refine the query. The response's `data` holds matching transactions and `_links` can provide a cursor for pagination. GET `/transactions/{id}` reads one transaction (raw lines 38–54, 226–229, 354).
- **Positive** `amount.value` adds funds to that balance account; **negative** deducts them. Incoming/outgoing rows can result from external or internal transfers. `pending` means an incoming credit is not yet added or an outgoing debit is reserved; `booked` means the corresponding balance-account credit or deduction occurred. Use `valueDate` for availability/deduction and `bookingDate` for recorded pending/reserved state, especially around bank cutoffs (raw lines 356–368, 539–548).
- The examples show bank-payout debit, payment credit, and internal-transfer debit/credit shapes with transfer references and separate booking/value dates. Their identifiers and amounts are **not** a reconciled pair: the list response has EUR-suffixed transaction IDs beside USD amounts, and its illustrated internal outgoing **-10000 USD** and incoming **+1000 USD** have different transfer IDs. Do not infer a matched two-sided transfer from those rows (raw lines 231–352, 379–537).
- The TEST curl example includes a bare `accountHolder` query fragment and date-only values despite the parameter table's ISO 8601 date-time examples. Use the stated parameter descriptions and current API contract before constructing requests; the sample is illustrative, not a validated query (raw lines 44–66). A booked bank-payout debit confirms deduction from the balance account, not beneficiary-bank receipt (raw lines 362–375, 379–416).

## Detail locators

- Requirements and list-query parameters: raw lines 19–54.
- TEST request/response, pagination and sample discrepancies: raw lines 56–354.
- Signed direction and pending/booked semantics: raw lines 356–368.
- External/internal example shapes and booking/value date definitions: raw lines 370–548.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-platform-internal-transfers]]
- [[adyen-reporting]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/transfer-transactions/track-api/2026-09-15|Pinned transaction API guide]]
