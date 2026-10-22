---
title: "Adyen Payout Service balance-platform report generation and download"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/prepare-reports/generate-download-reports"
raw_files:
  - "adyen/docs/payouts/payout-service/prepare-reports/generate-download-reports/2026-09-15.md"
tags: [adyen, payout-service, balance-platform, reports, reconciliation]
---

## Overview

This 2026-09-15-captured [[adyen]] Payout Service guide explains scheduled or manual generation of balance-platform reports, availability notification, and Customer Area or authenticated HTTP download. It documents report access and retrieval, not a verified reconciliation or payout outcome. See [[adyen-reporting]].

## Key takeaways

- **Access and notification:** The requirements list Customer Area **Generate Balance Platform reports** and **Download Balance Platform reports** roles; for programmatic download they list a **Report service user** API key with **BalancePlatform Report Download** role. Subscribe to `balancePlatform.report.created` to learn when a generated report is available. These are access prerequisites, not evidence that a user or key has been granted them. See pinned raw lines 21–28.
- **Generate:** On the correct merchant account's Customer Area Reports page, choose Automatic (schedule based) or Manual (generate once). Deselecting Automatic generation deletes the schedule. Schedule timing depends on report type and balance-platform configuration. Manual options can include bulk generation, date range, balance-account/account-holder filter, and time zone; generation may take a few minutes. See pinned raw lines 30–75.
- **Availability and environment:** `balancePlatform.report.created` carries a `downloadUrl`; its illustrated event is explicitly TEST (`environment: test` and a `balanceplatform-test.adyen.com` URL). A generation request is not a downloadable file until availability, and the sample URL is not a LIVE endpoint. See pinned raw lines 77–96.
- **Format and access boundary:** Reports are CSV, except the Accounting report can also be TSV. Customer Area offers a Generated reports download. For HTTP GET, the guide says to ask an Adyen contact for report credentials, authenticate with the API key or report basic-auth password, and use the webhook's `downloadUrl`. The webhook URL alone is not an unauthenticated report grant; keep report credentials and downloaded data protected. See pinned raw lines 98–144.

## Detail locators

- Roles and report-created webhook requirement: pinned raw lines 21–28.
- Automatic schedule, deletion and manual options: pinned raw lines 30–75.
- TEST webhook payload and `downloadUrl`: pinned raw lines 77–96.
- CSV/TSV formats, Customer Area and credentialed GET examples: pinned raw lines 98–144.

## Related

- [[adyen-reporting]] — reciprocal report concept.
- [[source-adyen-docs-payouts-payout-service-reconcile-balances]] — separate merchant-to-balance-platform reconciliation guide.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/prepare-reports/generate-download-reports/2026-09-15|Payout Service get platform reports, captured 2026-09-15]]
