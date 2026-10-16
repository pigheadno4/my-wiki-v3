---
title: "Adyen manually generate and download reports"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/manually-get-reports"
raw_files:
  - "adyen/docs/reporting/manually-get-reports/2026-09-15.md"
tags: [adyen, reporting, customer-area, manual-generation, downloads]
---

## Overview

This Adyen guide describes a one-time manual report generation and download flow in Customer Area. Report availability can be at company-account, merchant-account, or both levels, depending on the report. It gives a retrieval procedure, not the meaning or financial outcome of any report's records. [[adyen]] [[adyen-reporting]]

## Key takeaways

- Manual generation and download require either the **Merchant Report** or **Generate key financial reports** user role.
- In Customer Area, use **Reports → Report overview** to locate a report, select **Manage report → Manual (generate once)**, choose report-specific options such as date range or file type, and select **Generate report**. The choices depend on the report type; this guide does not impose one universal date range, file format, or time zone.
- The **Report is successfully queued** message means generation has been requested. Generation may take several hours, depending on size or concurrent demand. To download, select the report name and choose the generated item under **Generated reports**; a queue message alone is not an available file.
- The captured guide says that, starting January 13, 2024, generated reports are retained for two years from generation and older reports must be regenerated in Customer Area. It explicitly exempts invoices from that report-retention rule and says invoices remain available indefinitely. These are captured documentation claims, not verification of an account's current availability.
- Report generation or download is not proof of settlement, reconciliation completion, or bank receipt. Interpret an exported report under its own account, period, field, and time-zone rules.

## Detail locators

- Opening, lines 19–23: company-versus-merchant report availability, two-year report retention, invoice exception, and automatic-report alternative.
- `## Manually generate and download a report`, lines 25–45: role prerequisite, Customer Area navigation, report-specific settings, queued state, possible delay, and download route.

## Related

- [[adyen-reporting]] — provider report routes and evidence boundary.
- [[source-adyen-docs-reporting-automatically-get-reports]] — separate automatic generation route.

## Raw Sources

- [[raw/adyen/docs/reporting/manually-get-reports/2026-09-15|Adyen manual report generation guide, fetched 2026-09-15]]
