---
title: "Adyen automatic report generation and download"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/automatically-get-reports"
raw_files:
  - "adyen/docs/reporting/automatically-get-reports/2026-09-15.md"
tags: [adyen, reporting, automation, webhooks, report-download]
---

## Overview

This [[adyen]] guide describes a sequence for automatically generating Customer Area reports, receiving a **REPORT_AVAILABLE** webhook after generation, and downloading the report file by authenticated HTTP GET. The webhook announces an available file and supplies its filename and download URL; it is not the report file or evidence that a merchant's payments settled. See [[adyen-reporting]] for the broader reporting route.

## Key takeaways

- To turn on automatic generation in Customer Area, the user needs **Merchant Report** or **Generate key financial reports**. Select a report, enable automatic generation, and choose the format. Some reports require additional frequency settings. For those schedules, the page lists daily (between 02:00 and 10:00 CET, previous 24 hours), weekly (selected day, previous seven days), monthly (selected day, previous calendar month), and quarterly (selected day, previous quarter); the account time-zone setting affects generation. A merchant-country setting and store/terminal display options are optional in this scheduling section. These are guide-specific descriptions, not a universal schedule for every report. [Raw: Step 1, lines 27–60]
- Set up a webhook endpoint and Customer Area webhook configuration. After a report is generated, **REPORT_AVAILABLE** includes `pspReference` as the file name and `reason` as the download URL. The sample JSON and SOAP notifications are examples; receiving a notification does not itself retrieve or validate the file. [Raw: Step 2, lines 62–127]
- Downloading by HTTP GET requires a **Report service user** API credential. Creating one requires **Merchant admin** or **Manage API credentials**; choose **Report user**, assign **Merchant Report Download role**, and optionally limit access to particular merchant accounts. The guide offers an API key or Basic auth for download and says to copy and securely store generated credentials. It recommends gzip compression. [Raw: Steps 3 and 5, lines 129–163 and 174–210]
- PGP encryption is optional: register a PGP public key with **Reports** as its purpose to encrypt future generated report files. Encryption and authenticated retrieval are separate steps. [Raw: Step 4, lines 165–172]
- The page warns that a report-generation platform migration affects Received payment details, Interactive payment accounting, and Settlement details reports, potentially requiring changes in report ingestion logic, including for manually downloaded files. File-name parsing examples for several reports are navigation and format details; report-specific sources own their fields, account scope and reconciliation meanings. [Raw: Important changes, lines 21–25; Parsing file names, lines 211–232]
- This 2026-09-15 snapshot has embedded last-modified metadata from 2023. It does not establish current account permission, successful webhook delivery, file contents, payout arrival, or financial finality.

## Detail locators

- Migration and ingestion warning: `Important changes`, lines 21–25.
- Generation role, Customer Area setup, formats, schedules, time-zone and optional filters: `Step 1: Automate generating reports`, lines 27–60.
- Notification event, file name, URL, and JSON/SOAP examples: `Step 2: Get webhooks when reports are available`, lines 62–127.
- Credential-creation roles, authentication setup, download role and merchant-account access: `Step 3: Create a Report service user API credential`, lines 129–163.
- Optional PGP setup and effect on future reports: `Step 4 (Optional): Encrypt report files`, lines 165–172.
- Authenticated GET, compression, examples and filename formats: `Step 5: Download reports`, lines 174–232.

## Related

- [[adyen]] — provider page.
- [[adyen-reporting]] — reporting concept.
- [[adyen-webhooks]] — general webhook architecture; this source owns the report-availability payload.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — Settlement details report fields and reconciliation meaning.

## Raw Sources

- [[raw/adyen/docs/reporting/automatically-get-reports/2026-09-15|Adyen Get reports automatically (2026-09-15)]]
