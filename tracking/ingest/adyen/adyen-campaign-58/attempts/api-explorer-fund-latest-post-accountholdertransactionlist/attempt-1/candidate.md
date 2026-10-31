---
title: "Adyen Fund API v6: POST /accountHolderTransactionList"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/post/accountHolderTransactionList"
raw_files:
  - "adyen/api-explorer/Fund/latest/post/accountHolderTransactionList/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, transactions, reconciliation]
---

## Overview

This captured Fund API page describes `POST /accountHolderTransactionList`, which returns transactions for a Classic account holder's accounts. Its listed server is Fund v6 TEST, `https://cal-test.adyen.com/cal/services/Fund/v6`. The request body requires `accountHolderCode`. Optional `transactionListsPerAccount` selects accounts and pages, and optional `transactionStatuses` selects status values.

## Key takeaways

- The page says the call returns at most 50 transactions **for each account**, ordered newest first. If `transactionListsPerAccount` is omitted, it includes the last 50 for all of the account holder's accounts. Within a supplied account entry, `accountCode` and `page` are required; page 1 is the most recent. Increment `page` to retrieve further transactions, and inspect each returned account list's optional `hasNextPage`. An omitted status filter includes all transactions. The request schema shown here has no date-range selector.
- The documented statuses distinguish pending, failed, credited/debited, reversed, chargeback, converted, manual-correction, payout, and fund-transfer entries. The full permitted-value lists are in pinned raw lines 21 and 81/118. A `Payout` status, `payoutPspReference`, or `bankAccountDetail` in this account transaction listing is not, by itself, proof of bank receipt; the page describes account transactions and payout destination details, not a receiving-bank confirmation.
- The 200 description says the request succeeded; the 202 description says the request was accepted for processing **but processing was not completed**. Both response schemas show optional `accountTransactionLists` with per-account `accountCode`, `hasNextPage`, and transaction entries. Transaction metadata includes amount, `creationDate` (date performed), references, source/destination account codes, status, and transfer code. Do not treat a 202 as a completed retrieval or financial outcome.
- The listed error classes are 400, 401 (authentication), 403 (permissions), 422 (validation), and 500. The 2026-09-15 TEST reference does not establish current live availability or a specific account holder's balances, verification state, payout settlement, or bank receipt.

## Detail locators

- Purpose, server, account scope, page/default behavior, filters, and status vocabulary: pinned raw lines 5–21.
- Illustrative basic and status-filtered request JSON: pinned raw lines 23–54.
- 200 response structure, transaction fields, and status values: pinned raw lines 55–91.
- 202 accepted-for-processing response and matching field structure: pinned raw lines 94–128.
- Error response descriptions and fields: pinned raw lines 131–193.

## Related

- [[adyen-classic-platforms]] — Classic account-holder, account, transfer, and payout context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/post/accountHolderTransactionList/2026-09-15|Fund API v6 POST /accountHolderTransactionList capture (2026-09-15)]]
