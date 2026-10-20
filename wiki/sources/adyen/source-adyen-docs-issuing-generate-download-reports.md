---
title: "Adyen Issuing: Generate and download Balance Platform reports"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/generate-download-reports"
raw_files:
  - "adyen/docs/issuing/generate-download-reports/2026-09-15.md"
tags: [adyen, issuing, balance-platform, reports, reconciliation]
---

## Overview

This 2021-modified, 2026-09-15-captured guide explains how to schedule or manually generate Balance Platform reports in Customer Area, receive a report-available webhook, and download the resulting file from Customer Area or with an authenticated HTTP GET. It documents report access and delivery, not the accuracy or completeness of a particular report's accounting rows. [[adyen]] [[adyen-reporting]] [[adyen-issuing]]

## Key takeaways

- The requirements table names Customer Area roles to generate and download Balance Platform reports, a Report service user API key with the BalancePlatform Report Download role for downloading, and subscription to `balancePlatform.report.created`. For programmatic GET, the guide says to obtain report credentials from Adyen and use an API key or report basic-authentication password with the webhook's `downloadUrl`.
- Automatic generation is configured per report in the correct merchant account's Customer Area. The schedule depends on report type and balance-platform configuration. Deselecting the Automatic generation toggle deletes the schedule. Manual generation can offer bulk, period, balance-account/account-holder and time-zone choices depending on report type; generation can take a few minutes.
- `balancePlatform.report.created` signals that a generated report is available and carries its download URL; the shown webhook is a test-environment example. Reports are CSV, with TSV also available for the Accounting report. A generated/downloaded file is an input to reconciliation, not evidence here that any specific balance, payment or settlement is correct.

## Detail locators

- Roles, webhook subscription and schedule setup/deletion: raw lines 19–50. Manual generation and conditional options: raw lines 52–75.
- Report-created webhook and `downloadUrl` example: raw lines 77–96. CSV/Accounting TSV and Customer Area download path: raw lines 98–113.
- Programmatic report credentials, GET inputs and basic-auth/API-key test-host examples: raw lines 115–144. The sample report URLs and filename dates are illustrative; use the actual webhook URL for the generated report.

## Related

- [[adyen]] — provider.
- [[adyen-reporting]] — main report-generation and download route.
- [[adyen-issuing]] — Issuing and balance-platform context.
- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report]] — Accounting Report content reference.

## Raw Sources

- [[raw/adyen/docs/issuing/generate-download-reports/2026-09-15|Generate and download Balance Platform reports — 2026-09-15 snapshot]]
