---
title: "Generate and download Adyen balance platform reports | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/prepare-reports/generate-download-reports"
raw_files:
  - "adyen/docs/platforms/prepare-reports/generate-download-reports/2026-09-15.md"
tags: [adyen, platforms, reporting, customer-area, report-download]
---

## Overview

This Adyen for Platforms guide explains how to generate balance-platform reports on a schedule or manually in Customer Area, receive `balancePlatform.report.created` when a generated report is available, and download the file in Customer Area or with authenticated HTTP GET. It covers report retrieval rather than the event grain, accounting meaning, or completeness of any particular report. The 2026-09-15 snapshot does not establish that a current report exists, that its rows reconcile, or that a bank payout arrived. [[adyen]] [[adyen-reporting]] [[adyen-platforms]]

## Key takeaways

- **Access:** Customer Area requires the listed **Generate Balance Platform reports** and **Download Balance Platform reports** roles. Programmatic download calls for a **Report service user** API key with the **BalancePlatform Report Download role**; the HTTP GET section also directs the reader to obtain report credentials from an Adyen contact and authenticate with an API key or report basic-auth password. Role and credential descriptions do not prove a particular user's current grant.
- **Generation:** In the correct merchant account's Reports page, automatic generation is selected per report type under **Manage report**. Deselecting **Automatic generation** deletes the generation schedule. The schedule depends on report type and balance-platform configuration; this page gives no universal delivery time. Manual generation is one-time; bulk, date/period, balance-account/account-holder and time-zone options are conditional on report type. Generation can take a few minutes.
- **Availability and download:** `balancePlatform.report.created` signals that a generated report is available and carries a `downloadUrl`, file name, report type, balance platform and creation date. The webhook is a download pointer, not the report contents. Download from the generated-reports table or authenticated HTTP GET using the report name, credentials and webhook `downloadUrl`; sample URLs and commands use a test environment. Actual report contents and period must be checked after retrieval.
- **Formats and reconciliation boundary:** Reports are CSV; the Accounting report may also be TSV. The page recommends loading files into a system or spreadsheet for reconciliation, but does not provide a method for matching split, payout or bank-receipt events or validate any report's totals. Follow the relevant report's field and period guide before financial conclusions.

## Detail locators

- Generation modes and access/webhook prerequisites: pinned raw lines 15–28.
- Automatic schedule setup, destructive toggle and report-dependent schedule: pinned raw lines 30–50.
- Manual generation, conditional filters/time zone and generation wait: pinned raw lines 52–75.
- `balancePlatform.report.created` availability notification and `downloadUrl` example: pinned raw lines 77–96.
- CSV/Accounting TSV formats, Customer Area download and authenticated HTTP GET with test examples: pinned raw lines 98–144.

## Related

- [[adyen-reporting]] — main report-discovery and evidence-boundary concept.
- [[source-adyen-docs-platforms-prepare-reports]] — separate preparation guide for choosing fields and aligning report periods.
- [[adyen-platforms]] — platform and account context.

## Raw Sources

- [[raw/adyen/docs/platforms/prepare-reports/generate-download-reports/2026-09-15|Generate and download platform reports — 2026-09-15 snapshot]]
