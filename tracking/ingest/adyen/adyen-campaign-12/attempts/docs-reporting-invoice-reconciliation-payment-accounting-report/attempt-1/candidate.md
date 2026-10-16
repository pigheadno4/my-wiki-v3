---
title: "Adyen Payment accounting report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report"
raw_files:
  - "adyen/docs/reporting/invoice-reconciliation/payment-accounting-report/2026-09-15.md"
tags: [adyen, reporting, payment-accounting, invoice-reconciliation]
---

## Overview

Adyen's Payment accounting report documents payment-lifecycle status changes, events and modifications, with costs by status for invoice reconciliation. This 2026-09-15 snapshot describes company- and merchant-account availability; it does not establish current account access. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- Each line below the report header is a separate **entry**, not necessarily one complete payment. The `Record Type` identifies an accounting event; the table includes pending, failed, reversed, externally settled and later-settled cases. A row or status alone is not proof of final funds or bank arrival.
- Standard columns distinguish the **Booking Date** and its account time-zone code, **Main Currency/Amount**, **Payment Currency** registers (`Received`, `Authorised`, `Captured`), **Settlement Currency** registers (`Payable`, `Commission`, `Markup`, `Scheme Fees`, `Interchange`), and separate **Processing Fee Currency/Amount**. The report describes debit or credit amounts on registers; do not collapse these amounts, currencies or event signs into one net transaction amount. Commission is split into markup, scheme fees and interchange instead when the acquirer provides interchange-level data.
- The **Interactive payment accounting** report is manually generated with selected date range, time zone and columns, and can have columns different from the standard report. For reconciliation to the payment processing invoice, Adyen instructs a first-of-month to first-of-next-month window at `00:00:00` in Central European Time because the invoice uses CET. The ordinary report uses the account's time-zone setting.
- The interactive filename convention changed in February 2025 so newly generated reports no longer overwrite previous ones; automated ingestion may need updating. Configuring columns or their order can affect automated consumers and requires one of the listed Customer Area roles.

## Detail locators

- Generation, account scope and interactive invoice window: pinned raw lines 19–46.
- Entry grain and standard field meanings, including currencies, dates and fee registers: pinned raw lines 54–100.
- Optional fields, including Amsterdam timestamps, payout date when available, ICSF details, modification reference and installment fields: pinned raw lines 102–173.
- Column configuration roles and steps: pinned raw lines 175–194.
- Record-type meanings, including `RefundNotProcessed`, `SettledReversed` and deprecated bulk journal types: pinned raw lines 196–253. These are event descriptions, not an accounting sign-off rule.

## Related

- [[adyen-reporting]] — Adyen reporting concept route.
- [[payment-reconciliation-reporting]] — cross-provider reporting context; its provider-specific examples do not define this Adyen report.

## Raw Sources

- [[raw/adyen/docs/reporting/invoice-reconciliation/payment-accounting-report/2026-09-15|Adyen Payment accounting report, captured 2026-09-15]]
