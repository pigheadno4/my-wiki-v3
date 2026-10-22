---
title: "Adyen Payout Service transfer-transaction lookup"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/transfer-transactions"
raw_files:
  - "adyen/docs/payouts/payout-service/transfer-transactions/2026-09-15.md"
tags: [adyen, payout-service, transfers-api, transactions, balance-accounts]
---

## Overview

This Payout Service-path guide (last modified 2023-09-07; captured 2026-09-15) explains querying **balance-account transaction records** through the Transfers API `/transactions` endpoints. It distinguishes the transaction's own `id` and signed amount from its related `transfer.id`, and covers platform, account-holder and balance-account scopes. Its prerequisites explicitly allow **Adyen for Platforms, Issuing or Payouts** integrations; the URL alone does not narrow this retrieval API to Payout Service. A transaction booked on an outgoing balance account is not proof that an external beneficiary bank or card recipient received funds. See [[adyen]] and [[adyen-payouts]].

## Key takeaways

- **Access and list query:** The guide requires a Transfers API credential with **TransferService Webservice Retrieve** assigned through Adyen contact and says transfers must be enabled for the source balance account. `GET /transactions` needs at least one of `balancePlatform`, `accountHolderId` or `balanceAccountId`, plus `createdSince` and `createdUntil`; it offers optional limit, sort order, cursor and payment-instrument filter. The result's `data` holds transaction records and `_links` supports cursor pagination. `GET /transactions/{id}` retrieves a specific transaction by its **transactionId**. The sample cURL includes a bare `accountHolder` query token alongside `accountHolderId`; examples are TEST illustrations, not a validated production template.
- **Transaction grain and direction:** Each result has a transaction `id`, `amount`, `status`, balance-platform/holder/account identifiers and a nested related `transfer.id`. The sign of `amount.value` is the direction for that balance account: **positive adds funds**, **negative deducts funds**. Incoming reference is the sender's when provided; outgoing reference is the one supplied in the transfer request. A transaction can be `pending` before credit or debit, or `booked` once the balance-account change occurs. This is different from transfer-request acceptance and from external bank receipt.
- **External versus internal:** The page names external payouts to third-party bank accounts or cards and internal transfers between balance accounts. It gives a booked negative example for an external bank payout, and separate negative outgoing and positive incoming internal examples. The two internal example transaction IDs and nested transfer IDs differ by leg; do not collapse the legs into one transaction. The list sample has a bank-payout transaction `id` ending in **EUR** while its `amount.currency` says **USD** (raw lines 240-247); use that sample only as an illustration of fields, not currency reconciliation.
- **Booking and value dates:** `bookingDate` records when funds are reserved or pending on the balance account; `valueDate` records when funds are deducted or made available. The after-bank-cutoff example keeps outgoing funds reserved before deduction, and the guide states outgoing deductions occur at the booked stage. Neither date alone establishes external beneficiary receipt.

## Detail locators

- API scope, integration and credential prerequisites: pinned raw lines 15-36.
- List identifiers/date filters, pagination, specific-transaction route and illustrative sample: pinned raw lines 38-354.
- Direction sign, pending/booked semantics and bank/card versus internal examples: pinned raw lines 356-487.
- BookingDate/valueDate distinction and outgoing deduction stage: pinned raw lines 489-498.

## Related

- [[adyen-payouts]] — main Payout Service concept and reciprocal source route.
- [[adyen-platform-internal-transfers]] — related two-sided balance-account movement.
- [[source-adyen-docs-payouts-payout-service-view-transfers-details]] — transfer-level list/detail retrieval, distinct from transaction records.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/transfer-transactions/2026-09-15|Payout Service transfer-transaction guide, captured 2026-09-15]]
