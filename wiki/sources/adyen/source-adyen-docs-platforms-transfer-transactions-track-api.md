---
title: "Adyen Transfers API transaction tracking"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/transfer-transactions/track-api"
raw_files:
  - "adyen/docs/platforms/transfer-transactions/track-api/2026-09-15.md"
tags: [adyen, platforms, transfers-api, transactions, reconciliation]
---

## Overview

This 2026-09-15 Adyen guide describes read-only Transfers API queries for balance-platform transactions. It applies to Adyen for Platforms, Issuing or Payouts integrations and covers both internal balance-account transfers and external payment/payout movements. List queries can scope to a balance platform, account holder or balance account; a transaction ID can retrieve one transaction. The returned transaction rows and dates support account-level tracking, not a new transfer request or proof of external bank receipt. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Access and list selection:** The guide says the API credential needs the TransferService Webservice Retrieve role assigned by Adyen, and transfers enabled for the source balance account. GET /transactions requires at least one of balancePlatform, accountHolderId or balanceAccountId, plus createdSince and createdUntil in ISO 8601 date-time form. It lists optional limit, sortOrder, cursor and paymentInstrumentId. The response has data and _links; follow the previous response's cursor to page. GET /transactions/{id} targets one transaction by transactionId. These are guide-level query conditions, not proof a credential has access to a particular account or that a result set is complete without pagination.
- **Account-relative movement:** A positive amount.value means incoming funds added to the specified balance account; negative means outgoing deduction. Pending incoming means not yet added and pending outgoing means reserved for deduction; booked marks the balance-account addition or deduction. The transfer reference can come from the sender on incoming rows or from the platform's /transfers request on outgoing rows. Internal and external flows can each yield incoming or outgoing transactions; transaction direction alone does not identify the underlying payment rail. Inspect transfer/category data and the actual account and transfer identifiers.
- **Date and outcome boundary:** bookingDate records when funds are recorded as reserved or pending in the balance account; valueDate indicates when funds are deducted or made available. The guide uses an after-cutoff external payout as a reservation example and says outgoing funds are deducted at booked stage. A pending row, value date, or booked debit is not proof that an external beneficiary bank received a payout. A booked internal entry documents one account-side booking; use actual counterpart evidence to establish its other side.
- **Sample caveats:** The examples use a TEST /btl/v4 endpoint and dated SDK snippets. The list response contains EUR-suffixed transaction IDs beside USD amounts, and the separate internal outgoing/incoming examples reuse illustrative IDs and the same account holder/balance-account descriptions with different transfer IDs. The sample curl includes an extra bare accountHolder query token and date-only values although the table asks for ISO 8601 date-time; its Java snippet also has malformed syntax. Do not infer currency from an ID suffix, a stable two-leg join, or production-ready request code from these samples. Use the documented field meaning and actual response records for reconciliation.

## Detail locators

- Scope, integration types and Retrieve role/source-account gate: pinned raw lines 15-36.
- Required scope/date filters, optional pagination and TEST/SDK examples: pinned raw lines 38-225.
- data/_links list response, mixed ID/currency samples and single-ID GET: pinned raw lines 226-354.
- Signed amount, pending/booked meaning, reference and external/internal distinctions: pinned raw lines 356-377.
- External and internal transaction examples, including reused identifiers: pinned raw lines 379-537.
- bookingDate/valueDate meaning, cutoff example and booked debit boundary: pinned raw lines 539-548.

## Related

- [[adyen-platforms]] — main Platforms concept and reciprocal source route.
- [[adyen-platform-internal-transfers]] — related internal balance-account movement, one transaction category covered here.
- [[source-adyen-docs-platforms-internal-fund-transfers]] — internal versus external transfer orientation.

## Related raw API references

- [[raw/adyen/docs/platforms/transfer-transactions/track-webhooks/2026-09-15|Track transactions with webhooks]] — separate event route; not evidence for this entry.

## Raw Sources

- [[raw/adyen/docs/platforms/transfer-transactions/track-api/2026-09-15|Adyen Track transactions with API requests, captured 2026-09-15]]
