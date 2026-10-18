---
title: "Reconcile payments | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reconciliation-use-cases/reconcile-payments"
raw_files:
  - "adyen/docs/platforms/reconciliation-use-cases/reconcile-payments/2026-09-15.md"
tags: [adyen, platforms, reconciliation, payments, reports]
---

## Overview

This [[adyen]] for Platforms worked example traces a processed payment from merchant-account lifecycle events in the Payment accounting report to split bookings on balance-platform accounts in the Balance Platform Accounting Report. It uses daily scheduled reports, a EUR 100 example and shared payment/modification references to explain matching, not a completed reconciliation for any live account. See [[adyen-reporting]] for the reporting route and evidence boundary.

## Key takeaways

- Payment processing starts on the Adyen merchant account. The example moves through `Received`, `Authorized` and `SentForSettle`; at `SentForSettle`, captured funds are booked to balance accounts according to splits in the payment or capture request. Booking date marks account booking; value date marks when funds are available and is usually later. [Raw: lines 21–33]
- The Payment accounting report has payment-lifecycle event rows and a Booking Date timestamp. The example's PSP reference `F2FTV3THPB9Z2C33` and Merchant Reference `UUID1` identify the payment across reports, API messages and webhooks; the `SentForSettle` row additionally carries modification PSP/Merchant references `GXH5DJ7C6WVFZP73` and `UUID1a`. Those identifiers and timestamps are illustrative. [Raw: lines 39–60]
- In the Balance Platform Accounting Report, the same payment/modification references appear on separate account-and-split rows. `Status`/`Type`, account identity, Booking Date and Value Date matter: the sample progresses through `received`, `authorised` and `captured` capture rows, with Transaction Id shown on captured rows. Do not sum lifecycle rows as if each were a distinct payment or treat a received/reserved value as available balance. [Raw: lines 62–85]
- The illustrated split credits EUR 97.00 to the platform user's balance account and EUR 3.00 commission to the liable balance account, while EUR -2.57 in fees is debited from the platform's fees balance account. The captured rows show a 2023-01-18 booking date and 2023-01-20 value date; the page calls this example T+2, not a universal availability promise. The selected report columns and fees do not establish the actual split or payout date for another payment. [Raw: lines 46, 69–85]
- **Column-label conflict in this capture:** the prose says amounts are in `Balance (BC)`, but the displayed table header labels the corresponding balance column `Balance (PC)` (X), while its `BC` column is `Platform Payment Cost Currency`. Check the actual exported report's column names and schema before building a field mapping; do not silently equate those labels. [Raw: lines 66–67, 72, 74–76]
- The guide recommends API responses and webhooks for individual transaction status and ledger updates, then daily Balance Platform Accounting Report reconciliation for funds from all payments. These sample/report entries do not prove that a particular reconciliation ran, a payment finally settled, or funds reached a bank account. [Raw: lines 88–92]

## Detail locators

- Payment flow, report cadence, booking versus value date: raw lines 17–33.
- Payment accounting report event grain, PSP/Merchant and modification references, signed lifecycle columns and illustrative timestamps/fees: raw lines 37–60.
- Balance Platform Accounting Report statuses, split accounts, signed `Received`/`Reserved`/`Balance` transitions, value date, fee columns and header conflict: raw lines 62–86.
- Recommendation and linked report definitions: raw lines 88–98.

## Related

- [[adyen-reporting]] — reporting and reconciliation evidence boundary
- [[adyen-platforms]] — balance-account and split context
- [Reconciliation use cases](https://docs.adyen.com/platforms/reconciliation-use-cases) — parent navigation
- [Payment accounting report](https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report) — linked payment-event report
- [Balance Platform Accounting Report](https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report) — linked account-booking report
- [Reconcile fees](https://docs.adyen.com/platforms/reconciliation-use-cases/reconcile-fees) — fee detail

## Raw Sources

- [[raw/adyen/docs/platforms/reconciliation-use-cases/reconcile-payments/2026-09-15|Adyen Platforms reconcile payments — collected 2026-09-15]]
