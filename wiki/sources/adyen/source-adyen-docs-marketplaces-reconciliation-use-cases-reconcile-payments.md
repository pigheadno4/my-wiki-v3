---
title: "Reconcile Marketplace payments"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reconciliation-use-cases/reconcile-payments"
raw_files:
  - "adyen/docs/marketplaces/reconciliation-use-cases/reconcile-payments/2026-09-15.md"
tags: [adyen, marketplaces, reconciliation, payments, reports]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Marketplace worked example traces a payment from merchant-account lifecycle rows in the Payment accounting report to split bookings on balance-platform accounts in the Balance Platform Accounting Report. It uses two reports scheduled daily and selected rows from an illustrative EUR 100 payment; it does not document a completed reconciliation for a live account. [[adyen-reporting]]

## Key takeaways

- The example moves through `Received`, `Authorized` and `SentForSettle`. The page describes the latter as captured funds booked to balance accounts according to splits in the payment or capture request. Booking date marks account booking; value date marks funds becoming available and is usually later. See raw lines 19–33.
- The Payment accounting report shows payment-lifecycle events and their booking timestamps. The sample PSP reference `F2FTV3THPB9Z2C33` and merchant reference `UUID1` join to the balance-platform report; its `SentForSettle` row also carries distinct modification references. The shown columns and rows are selected illustrations. See raw lines 39–60.
- The Balance Platform Accounting Report shows separate account/split rows and a `received` → `authorised` → `captured` capture progression. The example credits EUR 97.00 to a user's balance account and EUR 3.00 commission to the liable balance account, and debits EUR 2.57 in fees from a platform fees account. Its 2023-01-18 booking and 2023-01-20 value dates support this example's T+2 description, not a general availability promise. See raw lines 62–85.
- **Sample column-label conflict:** prose says `Balance (BC)` contains these amounts, while the displayed header labels that register `Balance (PC)`; `BC` appears there as `Platform Payment Cost Currency`. Verify the actual report schema before mapping this sample's prose to exported columns. See raw lines 66–76.
- For individual payment status and ledger updates, the page recommends API responses and webhooks; for funds across payments, it recommends daily Balance Platform Accounting Report reconciliation. These examples do not prove settlement, bank receipt, or a completed reconciliation for any actual payment. See raw lines 88–92.

## Detail locators

- **Purpose, report cadence and payment state/booking/value dates:** raw lines 15–33.
- **Payment accounting event and reference grain:** raw lines 37–60.
- **Balance-platform status, account/split and value-date rows, plus column-label conflict:** raw lines 62–86.
- **Individual transaction versus daily funds-reconciliation recommendation:** raw lines 88–98.

## Related

- [[adyen-reporting]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-reconciliation-use-cases-reconcile-payments|Parallel Platforms-path worked example]]
- [[source-adyen-docs-marketplaces-reports-and-fees-balance-platform-accounting-report|Balance Platform Accounting Report reference]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/reconciliation-use-cases/reconcile-payments/2026-09-15|Adyen Marketplace payment reconciliation example — collected 2026-09-15]]
