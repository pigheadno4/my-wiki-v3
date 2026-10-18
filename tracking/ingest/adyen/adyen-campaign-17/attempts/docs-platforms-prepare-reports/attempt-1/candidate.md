---
title: "Adyen for Platforms prepare reports"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/prepare-reports"
raw_files:
  - "adyen/docs/platforms/prepare-reports/2026-09-15.md"
tags: [adyen, platforms, reporting, reconciliation, report-configuration]
---

## Overview

This Adyen for Platforms guide prepares a reconciliation workflow by selecting reports, aligning their reporting periods and time zones, configuring columns, retrieving files and matching references across Adyen-account and balance-platform reports. It advises trying the process with complete reports before live use. Configuration and a successful test do not themselves establish a complete reconciliation, settled payment or beneficiary-bank receipt. [[adyen]] [[adyen-platforms]] [[adyen-reporting]]

## Key takeaways

- **Prerequisites and time basis:** understand the balance-platform account structure and funds flow, choose relevant report types and fee categories, then configure reporting time zones and columns. Different report periods and time zones are identified as common reconciliation-mismatch causes. When combining reports, check that they cover the same period and use the same time zone.
- **Column choices and impact:** reports have default columns; many Adyen-account reports permit additional columns. Extra columns increase file size, and column additions, removals or reordering can affect an automated consumer. For full financial reconciliation, the page recommends Payment accounting `Store` when stores are used, and `Split payment data` for comparing submitted splits with Accounting Report postings. `AMS Booking Date` helps align Payment accounting/Settlement details entries with an invoicing period that may straddle report boundaries. Settlement details `Funds Destination` is only relevant when upgrading from Classic for parallel reconciliation. These are recommendations, not universal required fields.
- **Column role gate and retrieval:** Customer Area report-column configuration requires one of Merchant admin, Merchant report role, Merchant financial, or Merchant POS Report role. The guide routes Adyen-account report manual/automatic retrieval and balance-platform report retrieval to separate instructions; it does not specify a download permission or retention period here.
- **Reference mapping:** use the Adyen-generated `Psp Reference` in Payment accounting/Settlement details against `Psp Payment Psp Reference` in the balance-platform Accounting Report. Payment `Merchant Reference` maps to `Psp Payment Merchant Reference`; modification references map to `Psp Modification Merchant Reference`; a split's `reference` maps to Accounting Report `Reference`. The page recommends unique values for payments, modifications and splits even where the API does not require them. Preserve payment, modification and split reference grains when joining.
- **Test boundary:** the reconciliation-use-case guides show selected rows and columns, so the page recommends complete sample reports or test transactions followed by test-environment report downloads before live use. These sources help validate parsing and joins; they do not prove a particular live booking, payout or bank credit.

## Detail locators

- Raw lines 15–27: purpose and prerequisites for account structure, report types and fees.
- Raw lines 29–52: period/time-zone setup and recommended Store, Split payment data, AMS Booking Date and Classic-only Funds Destination columns.
- Raw lines 54–73: Customer Area column setup, automation impact and eligible roles.
- Raw lines 75–82: manual/automatic download routes for Adyen-account versus balance-platform reports.
- Raw lines 84–107: multi-report combination, payment/modification/split reference mapping and matching period/time-zone checks.
- Raw lines 109–116: complete sample or test-environment report validation before live reconciliation.

## Related

- [[source-adyen-docs-platforms-reports-and-fees]] — report and fee selection hub.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — balance-platform accounting field definitions.
- [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report]] — payment accounting field definitions.
- [[source-adyen-docs-reporting-manually-get-reports]] — Adyen-account manual retrieval route.
- [[source-adyen-docs-reporting-automatically-get-reports]] — Adyen-account automatic retrieval route.

## Raw Sources

- [[raw/adyen/docs/platforms/prepare-reports/2026-09-15|Prepare reports snapshot, fetched 2026-09-15]]
