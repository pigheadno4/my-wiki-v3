---
title: "Adyen for Platforms reports and fee types"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reports-and-fees"
raw_files:
  - "adyen/docs/platforms/reports-and-fees/2026-09-15.md"
tags: [adyen, platforms, reports, reconciliation, fees]
---

## Overview

This 2023-modified Adyen for Platforms page, captured 2026-09-15, maps Adyen-account and balance-platform reports to bookkeeping, split-payment reconciliation and fee categories. It says a full monthly financial reconciliation combines reports from both account scopes; narrower tasks may use one report. Reports can be generated on a schedule or manually, but this page is a selection guide rather than a completed reconciliation or bank-receipt record. [[adyen]] [[adyen-platforms]] [[adyen-reporting]]

## Key takeaways

- **Account scopes and monthly set:** Adyen-account reports cover payment processing and invoices; balance-platform reports connect events and balance changes to account holders, including user and liable accounts. For full financial reconciliation, the page marks Payment accounting report, Monthly invoice and Balance Platform Accounting Report as required, with Settlement details report optional. Received payment details, Balance Platform Balance and Balance Platform Statement reports serve other described views. Use the linked report pages for exact fields, timing, generation settings and procedures.
- **Split entry mapping:** the hub says payment/capture split instructions determine credit/debit accounts. A payment split between two or more balance accounts appears as separate `platformPayment` lines in the Balance Platform Accounting Report, joinable by matching `Psp Payment Psp Reference`. It states that absent split instructions Adyen uses the liable account, giving a partial-refund debit as its example; transaction-specific refund behavior and exceptions belong to the detailed split guide. A matching report reference does not prove payment settlement or payout.
- **Different fee grains:** Balance Platform Accounting Report breaks down per-transaction Interchange, Scheme, Markup and Commission for captured funds booked to balance accounts. Payment accounting report includes all per-transaction payment fees plus Processing fees, which can arise from instructions without balance-booked funds. Monthly invoice totals monthly fees and adjustments, including listed platform-service charges. Settlement details report has aggregate Processing-fee and invoice-adjustment lines that can later be traced into the liable balance account's accounting report. The page says Adyen deducts fees from settlement and defaults them to the platform liable balance account; do not treat that default as a specific transaction outcome.
- **Fee-location navigation:** the table routes FanF and Merchant Location Fee to the Monthly invoice with US-specific qualifications, and Fund Transfer Service, Payout Service and KYC Service Fee to the Monthly invoice. These names and assessment bases are catalog entries, not a price schedule or proof that a platform incurred a fee.
- **Evidence boundary:** a report catalog, split line, fee category or invoice total alone does not establish a complete month close, account-specific transfer completion, beneficiary-bank credit or legal fund ownership. The linked report and reconciliation guides own their own data grains and checks.

## Detail locators

- Raw lines 15–32: report-generation purpose and Adyen-account versus balance-platform report selection.
- Raw lines 38–57: report catalog, required/optional monthly set and account scopes.
- Raw lines 59–65: split-instruction lines, `platformPayment` category, PSP-reference matching and liable-account fallback statement.
- Raw lines 67–79: settlement deduction/default liable booking and distinct fee/report grains.
- Raw lines 80–93: fee examples, assessment basis, report locations and US-only qualifiers.
- Raw lines 95–111: report-preparation and reconciliation next-step links.

## Related

- [[source-adyen-docs-reporting-platform-reports]] — platform reporting hub and scope navigation.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — balance-account event field reference.
- [[source-adyen-docs-platforms-reports-and-fees-payout-report]] — scheduled-payout report field reference.
- [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report]] — payment-event accounting report reference.
- [[source-adyen-docs-reporting-invoice-reconciliation-payment-processing-invoice]] — monthly invoice reference.

## Raw Sources

- [[raw/adyen/docs/platforms/reports-and-fees/2026-09-15|Platforms reports and fee types snapshot, fetched 2026-09-15]]
