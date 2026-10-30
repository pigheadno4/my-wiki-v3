---
title: "Adyen Transfers API v4: list transactions"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/get/transactions"
raw_files:
  - "adyen/api-explorer/transfers/latest/get/transactions/2026-09-15.md"
tags: [adyen, transfers, transactions, balance-accounts, pagination, api]
---

## Overview

This 2026-09-15-captured Transfers API reference documents `GET /transactions` on the **v4 test server** (`https://balanceplatform-api-test.adyen.com/btl/v4`). It lists transactions related to a balance account, account holder or balance platform. The page says Transfers API versions 1 and 2 are deprecated; the URL's `latest` segment does not establish present live availability or a currently deployed version. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- A request must provide at least one of `balanceAccountId`, `accountHolderId` or `balancePlatform`; `createdSince` and `createdUntil` are each marked required ISO 8601 creation-time bounds. If both account-holder and balance-account IDs are supplied, they must be related. A `paymentInstrumentId` filter requires one of the three scopes and must relate to a supplied balance-account or account-holder ID when either is supplied.
- Optional pagination and ordering controls are `limit` (default 10, maximum 100), `sortOrder` by transaction creation date (`asc` by default or `desc`), and a returned `cursor`. The first page and conditional `_links.next`/`_links.prev` support traversal. The `200` response schema marks top-level `data` and `_links` optional, so the illustrated multi-item response must not become a guaranteed shape or count.
- Each returned transaction has its own `id` and may separately include a related `transfer.id` and transfer `reference`; these are different objects. The table marks `amount` (minor-unit currency/value), `accountHolder`, `balanceAccount`, `balancePlatform`, `bookingDate`, `status` and `valueDate` required within a transaction item, while other fields are optional. `status` is `pending` or `booked`; the latter means booked to the balance account, not delivery to an external beneficiary bank. The response examples show signed amounts and a cursor link but are illustrative records, not actual account or transfer proof.
- The page lists `401` authentication, `403` insufficient permissions, `422` validation and `500` server errors but no exact credential role. The separate [[source-adyen-docs-business-accounts-transactions|Business Accounts transaction guide]] gives more product-specific role, signed-amount and date explanations; do not generalize its Business Accounts prerequisites to every v4 query context.

## Detail locators

- Purpose, deprecated older versions, scope and cursor behavior: raw lines 5–22.
- Date bounds, required scope relationships, instrument filter, page size and ordering: lines 24–37.
- Response fields, transaction versus transfer IDs, statuses, booking/value dates: lines 39–80.
- Error meanings and problem-body schema: lines 83–160.
- Illustrative signed transactions and `_links.next` cursor: lines 162–273.

## Related

- [[adyen-business-accounts]] — Business Accounts transaction-query context.
- [[adyen-platforms]] — broader platform scope.
- [[source-adyen-docs-business-accounts-transactions]] — separate product guide with role and accounting interpretation.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/get/transactions/2026-09-15|GET /transactions API Explorer capture]]
