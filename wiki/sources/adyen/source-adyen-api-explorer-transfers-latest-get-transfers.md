---
title: "Adyen Transfers API: list transfers"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/get/transfers"
raw_files:
  - "adyen/api-explorer/transfers/latest/get/transfers/2026-09-15.md"
tags: [adyen, transfers, balance-platform, api-reference, pagination]
---

## Overview

Captured Transfers API v4 test-server reference for `GET /transfers`, a read of transfers related to a balance account, account holder, or balance platform. It covers categories beyond internal transfers, including bank, card, issued-card, platform-payment, and top-up records. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request must include at least one of `balanceAccountId`, `accountHolderId`, or `balancePlatform`; the query table marks each individually optional because they are alternatives. `paymentInstrumentId` also needs one of these scope identifiers and must relate to a supplied balance account or account holder. When both account-holder and balance-account IDs are supplied, they must be related.
- `createdSince` and `createdUntil` are both marked required, use ISO 8601, and bound a window of no more than six months. `limit` defaults to 10 and permits at most 100 per page; `sortOrder` defaults to ascending creation date. Cursor pagination supplies next/previous links when applicable.
- The 200 schema has optional `_links` and `data`; each returned transfer has required `amount`, `category`, and `status` properties in the item schema. The `status` descriptions distinguish `received`, `authorised` (funds reserved), and `booked` (deducted from the user's balance account), as well as `refused`, `failed`, and `returned`. A list result or `booked` outbound status alone does not prove beneficiary-bank receipt or final settlement across categories; inspect applicable tracking and event records.
- The example next-page URL spans March to December 2021, exceeding the stated six-month date-window rule. Treat it as illustrative, not an exception to the parameter constraint.

## Detail locators

- Raw `## Parameters` / `### Query parameters`: scope/filter conditions, date window, category/reference, pagination and sort rules.
- Raw `## Responses` / `### 200 Success`: nested transfer, event, review, tracking, status and error-model fields. Nested properties marked required are conditional on their containing object being present.
- Raw `## Response examples`: two illustrative internal-transfer rows and a next-page link.

## Related

- [[adyen-platform-internal-transfers]] — internal balance-account movements are only one category in this list.
- [[source-adyen-docs-platforms-view-transfers-details]] — Platforms guide to list/detail inspection and event tracking.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/get/transfers/2026-09-15|Transfers API v4 GET /transfers reference (2026-09-15 capture)]]
