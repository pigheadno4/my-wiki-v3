---
title: "Adyen Issuing: Track balance-platform transactions"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/transactions"
raw_files:
  - "adyen/docs/issuing/transactions/2026-09-15.md"
tags: [adyen, issuing, balance-platform, transactions, transfers-api]
---

## Overview

This 2020-modified Adyen guide, captured 2026-09-15 under Issuing, explains on-demand retrieval of balance-platform transaction records through the Transfers API `GET /transactions` list endpoint and `GET /transactions/{id}` detail endpoint. Its stated integration scope includes Adyen for Platforms, Issuing or Payouts, and its examples include bank and internal transfers; the result list is not limited to issued-card payments. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The requirements table calls for one of those integrations, an API credential assigned **TransferService Webservice Retrieve role**, and transfers enabled for the source balance account. The captured table is visibly malformed around the role and enablement text; use the linked API reference or Adyen contact to resolve operational details rather than inferring a broader permission model.
- `GET /transactions` can query a whole balance platform, an account holder, or a balance account. The table says include at least one of `balancePlatform`, `accountHolderId`, or `balanceAccountId`; it also marks `createdSince` and `createdUntil` as required ISO 8601 date-time filters. Optional `paymentInstrumentId`, `limit`, `sortOrder` and `cursor` further narrow or page results. The response has matching transactions in `data` and applicable next/previous links in `_links`; pass a returned cursor on the next request. Use `GET /transactions/{id}` with a specific transaction ID for one record.
- Direction is relative to the balance account: a positive `amount.value` adds funds; a negative value deducts them. `pending` means incoming funds have not yet been added or outgoing funds are reserved for deduction. `booked` means added for incoming or deducted for outgoing. The guide distinguishes `bookingDate` (recorded as reserved/pending) from `valueDate` (deducted or made available), and says outgoing transfers are deducted at the booked stage.
- The test-environment list response illustrates transaction IDs, account holder/balance account, transfer IDs and references, amount, dates, status and `_links`. Some example snippets are malformed or inconsistent (for example, a stray `accountHolder` query item in the curl URL and invalid Java punctuation), so copy neither sample syntax nor sample `booked` records as proof of a real transfer, card capture or beneficiary receipt.

## Detail locators

- Pinned raw lines 15–29: Transfers API scope and integration/credential requirements, including the broken table formatting.
- Pinned raw lines 31–47: list filters and at-least-one scope selector; lines 49–217: test URL and versioned language examples.
- Pinned raw lines 219–223: `data`, `_links` and cursor paging; lines 224–345: illustrative response with bank and internal-transfer categories; line 347: transaction-ID detail endpoint.
- Pinned raw lines 349–370: incoming/outgoing amount sign, pending/booked effects and booking/value dates.

## Related

- [[adyen-issuing]] — Issuing account and payment context.
- [[source-adyen-docs-issuing-payment-stages-check-details-payment]] — issued-card payment detail lookup (navigation only).
- [[source-adyen-docs-issuing-payment-stages]] — separate card payment stages (navigation only).

## Raw Sources

- [[raw/adyen/docs/issuing/transactions/2026-09-15|Adyen balance-platform transaction tracking guide, captured 2026-09-15]]
