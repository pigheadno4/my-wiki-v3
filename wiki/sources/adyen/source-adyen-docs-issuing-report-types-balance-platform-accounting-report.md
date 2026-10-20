---
title: "Adyen Balance Platform Accounting Report"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/report-types/balance-platform-accounting-report"
raw_files:
  - "adyen/docs/issuing/report-types/balance-platform-accounting-report/2026-09-15.md"
tags: [adyen, issuing, accounting, reporting, balance-platform]
---

## Overview

Adyen's Balance Platform Accounting Report guide, captured 2026-09-15, describes a report of financial activity across balance-platform accounts for issuing, payouts and platform payments. It can support payment-lifecycle, external-bank-funds and authorization-rate analysis. The report can be generated on a schedule or manually for a selected day in Customer Area. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Most balance-platform events follow a Transfer/Transactions structure: the Transfer represents a pending credit or debit, and Transactions represent booked balance entries. Linked events share a Transfer Id; a refund starts a separate flow with a new Transfer Id that does not link to the original payment. Match Transfer Id to link a transaction to a transfer.
- The guide says a missing Transaction Id means no money movement yet, but explicitly says a `cancelled` row has a Transaction Id without real money movement, for reconciliation with the payment. Do not treat Transaction Id alone as proof of moved funds.
- A selected day's report includes balance mutations with a Booking Date for all accounts on the balance platform from 00:00 to 00:00 the next day in Central European Time (CET). Balance accounts with no transactions do not appear.
- Standard columns are included by default; additional columns can be enabled in Customer Area. The sample may omit data or columns present in a report generated for a platform's settings. The two additional `Issued Card Scheme Fee` columns explicitly say **Do not use this column**.

## Detail locators

- Generation and report purposes: raw lines 19–25. Transfer/Transaction definitions, refund flow and cancellation exception: lines 27–32.
- Sample variation and reporting window: lines 34–42. Standard columns, service scope, identifiers, statuses, dates, currency and balance registers: lines 44–77. Balance accounts without transactions: line 52.
- Payment instrument, entry mode, authorization code, counterparty and platform-payment cost fields: lines 85–132. Additional-column availability and the unusable Issued Card Scheme Fee fields: lines 145–169. Next-step links for lifecycle, cash management and authorization rate: lines 171–185.

## Related

- [[adyen-issuing]] — Issuing concept and source route.
- [[adyen-index]] — Adyen source catalog.

## Raw Sources

- [[raw/adyen/docs/issuing/report-types/balance-platform-accounting-report/2026-09-15|Balance Platform Accounting Report, captured 2026-09-15]]
