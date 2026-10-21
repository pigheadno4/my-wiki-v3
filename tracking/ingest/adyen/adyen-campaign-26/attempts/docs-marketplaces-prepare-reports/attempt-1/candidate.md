---
title: "Adyen Marketplace report preparation"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/prepare-reports"
raw_files:
  - "adyen/docs/marketplaces/prepare-reports/2026-09-15.md"
tags: [adyen, marketplaces, platforms, reporting, reconciliation]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] guide describes how to configure, retrieve and combine reports for a modern [[adyen-platforms]] reconciliation process. Under [[adyen-reporting]], it first asks the platform to understand its balance-platform account structure and money flow, choose relevant reports and fee types, align reporting periods/time zones, then test with complete reports before live reconciliation (raw lines 15–35, 102–116). Configuration or test samples do not prove an actual payout or completed reconciliation.

## Key takeaways

- **Scope and period:** Reports can use different generation periods and time zones, and mismatch is a common cause of failed reconciliation. When joining reports, use the same period and timezone (raw lines 29–35, 102–107). The guide recommends combining several reports and mapping API-supplied references into their report fields to trace a transaction lifecycle (lines 84–100).
- **Column changes and roles:** Many Adyen account reports permit extra/reordered/removed columns; added columns increase file size, and changing them can affect automated ingestion. Customer Area column configuration requires one of Merchant admin, Merchant report, Merchant financial or Merchant POS Report roles (raw lines 36–73). Recommended additions are Store where stores are used, Split payment data to compare instructions with balance-platform postings, AMS Booking Date for monthly invoice period alignment, and Funds Destination **only** for a Classic-to-modern balance-platform upgrade with parallel reconciliation (lines 42–52). These are conditional recommendations, not universally required fields.
- **Join keys:** Payment/Settlement `Psp Reference` maps to Accounting `Psp Payment Psp Reference`; `Merchant Reference` maps to `Psp Payment Merchant Reference`; modification references map to `Psp Modification Merchant Reference`; and a per-split `Reference` appears in the Accounting report (raw lines 91–100). The guide recommends unique payment, modification and split references even though the named API fields are described as not required. A split reference has no corresponding Payment/Settlement report field in this table; do not infer a direct join without the relevant report detail.
- **Retrieval and testing:** Account reports route to manual/automatic reporting guides, while balance-platform reports route to the platform report-generation guide (raw lines 75–82). Before live use, test reconciliation with complete sample or TEST-environment reports. The worked reconciliation guides show selected rows and columns, so they are not complete datasets for validation (lines 109–116).

## Detail locators

- Prerequisite account structure, money flow, report/fee selection and timezone setup: raw lines 19–35.
- Column configuration, role gate and conditional Store/split/AMS/Funds Destination recommendations: raw lines 36–73.
- Retrieval routes, cross-report reference mapping and period/timezone alignment: raw lines 75–107.
- Complete-report test recommendation: raw lines 109–116.

## Evidence boundary

This is report-preparation guidance, not an account-specific accounting conclusion. Correct columns, matching references and aligned reporting periods enable investigation but do not prove complete reconciliation, booked funds, settlement, payout or bank receipt. The Classic Funds Destination column is explicitly an upgrade/parallel-reconciliation aid; this page otherwise concerns the current Marketplace balance-platform route.

## Related

- [[adyen-reporting]] — report and reconciliation concept.
- [[adyen-platforms]] — current Marketplace/Platforms model.
- [[source-adyen-docs-platforms-prepare-reports-generate-download-reports]] — existing Platforms-path balance-platform report generation and download route.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — accounting report fields and grain.

## Raw Sources

- [[raw/adyen/docs/marketplaces/prepare-reports/2026-09-15|Pinned Marketplace report-preparation guide, captured 2026-09-15]]
