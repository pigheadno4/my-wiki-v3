---
title: "Adyen Marketplace balance-platform report generation and download"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/prepare-reports/generate-download-reports"
raw_files:
  - "adyen/docs/marketplaces/prepare-reports/generate-download-reports/2026-09-15.md"
tags: [adyen, marketplaces, reporting, report-download]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] guide explains scheduled or one-time generation of balance-platform reports in Customer Area, the `balancePlatform.report.created` availability notification, and Customer Area or authenticated HTTP GET download. It is a report-retrieval procedure, not a definition of any report's accounting grain or proof of a payout. See [[adyen-reporting]] and [[adyen-platforms]].

## Key takeaways

- **Role and credential gates:** The page lists Customer Area Generate Balance Platform reports and Download Balance Platform reports roles; programmatic download requires a Report service user API key with the BalancePlatform Report Download role. Its HTTP GET instructions separately say to obtain report credentials from an Adyen contact and authenticate with an API key or report basic-auth password. A listed role or sample credential is not evidence of an operator's current grant. See pinned raw lines 21–28 and 115–125.
- **Generation and schedule effect:** Automatic generation is configured per report type under the correct merchant account's Reports > Manage report. Deselecting the Automatic generation toggle deletes its schedule. The schedule depends on report type and balance-platform configuration. Manual generation is one-time; bulk, date/period, balance-account/account-holder and time-zone choices depend on report type, and generation can take a few minutes. See pinned raw lines 30–75.
- **Availability versus file:** `balancePlatform.report.created` says a generated report is available and carries a `downloadUrl` with report metadata. It is a pointer to a downloadable report, not its rows or a reconciliation result. Reports can be retrieved from the Generated reports table or with authenticated HTTP GET using the report name, credentials and webhook URL. The examples use test URLs. See pinned raw lines 77–96 and 98–144.
- **Format and evidence boundary:** Reports are CSV, and the Accounting report can also be TSV. The guide recommends system or spreadsheet reconciliation but does not specify the grain, complete period or financial correctness of an individual report. Validate the downloaded file against its report-specific field/period guide before inferring balances, settlement or bank receipt. See pinned raw lines 98–102.

## Detail locators

- Access roles, webhook subscription and generation modes: pinned raw lines 15–28.
- Automatic schedule controls and deletion effect: pinned raw lines 30–50.
- One-time report generation, conditional filters/time zone and waiting: pinned raw lines 52–75.
- Report-created webhook and test download URL: pinned raw lines 77–96.
- File format, Customer Area and authenticated HTTP GET download examples: pinned raw lines 98–144.

## Related

- [[adyen-reporting]] — reciprocal reporting concept.
- [[source-adyen-docs-platforms-prepare-reports-generate-download-reports]] — same dated guide under the Platforms path.
- [[source-adyen-docs-marketplaces-prepare-reports]] — Marketplace preparation guide for report selection, periods and fields.

## Raw Sources

- [[raw/adyen/docs/marketplaces/prepare-reports/generate-download-reports/2026-09-15|Marketplace balance-platform report generation, captured 2026-09-15]]
