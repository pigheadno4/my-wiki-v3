---
title: "Classic Platforms prepare reconciliation reports"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/prepare-reports"
raw_files:
  - "adyen/docs/classic-platforms/prepare-reports/2026-09-15.md"
tags: [adyen, classic-platforms, reporting, reconciliation]
---

## Overview

This Classic Adyen for Platforms guide (last modified 2023-01-09; captured 2026-09-15) explains how to configure, obtain and combine Adyen account and Marketplace Payments accounting reports for financial reconciliation. It points new integrations to a different guide. Its report routes belong under [[adyen-classic-platforms]], with provider context at [[adyen]]; report configuration or illustrative rows alone do not prove that a particular payment settled or payout reached a bank.

## Key takeaways

- Before preparing reports, the guide asks the platform to understand the payment lifecycle, its Classic account structure and funds flow, relevant report types and fee categories (raw lines 21–27). Reporting periods and time zones may differ; the page identifies period/time-zone mismatch as a common cause of failed reconciliation (raw lines 29–34, 69–74).
- Some reports allow optional extra columns, which increase file size. Adyen account report columns are configured in Customer Area; additional Platform report columns require Support. The page **recommends** extra columns for full financial reconciliation, including Settlement details **Split Payment Data** to compare split instructions with Marketplace Payments accounting fund postings, **AMS Booking Date** for invoice periods, and conditional store or dispute/batch identifiers in Marketplace Payments accounting (raw lines 36–50). Recommendations are not a claim that every column is mandatory for every use case.
- Reports can be downloaded manually from Customer Area or generated/downloaded automatically; for repeated full reconciliation, the guide suggests automated ingestion and combination (raw lines 52–54). Combining several reports is necessary for the guide's full reconciliation method across a transaction lifecycle (raw lines 56–60).
- Join **Psp Reference** in Settlement details or Payment accounting to **Payment Psp Reference** in Marketplace Payments accounting. **Merchant Reference** joins to **Payment Merchant Reference**, but the API does **not require merchant references to be unique**; the guide recommends unique values per transaction to aid matching (raw lines 60–67). The reports must cover the same period and use the same time zone (raw lines 69–74).
- Before live reconciliation, Adyen recommends testing with **complete** reports. The common use-case guides show selected rows and columns only; complete examples can be downloaded from Reporting documentation or generated from test transactions and test-environment reports (raw lines 76–83). A successful test join does not itself establish live financial outcomes.

## Detail locators

- Prerequisite links for lifecycle, account structure, report types and fees: raw lines 21–27. The linked pages own their detailed definitions.
- Optional report-column configuration and per-column purpose/conditions: raw lines 36–50. Split instructions and fund postings are distinct evidence surfaces.
- Manual/automatic download routes: raw lines 52–54. Reference mapping and time-zone/period checks: raw lines 56–74.
- Complete-report testing versus selected sample rows: raw lines 76–83.

## Related

- [[adyen-classic-platforms]] — Classic model and source route.
- [[adyen]] — provider.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/prepare-reports/2026-09-15|Classic Platforms prepare reports, captured 2026-09-15]]
