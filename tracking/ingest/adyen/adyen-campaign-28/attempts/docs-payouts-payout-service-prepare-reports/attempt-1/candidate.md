---
title: "Adyen Payout Service report preparation"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/prepare-reports"
raw_files:
  - "adyen/docs/payouts/payout-service/prepare-reports/2026-09-15.md"
tags: [adyen, payout-service, reporting, reconciliation]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service guide is a preparation checklist for configuring and obtaining reports before reconciling activity. It routes to relevant report/fee references and separate report-generation instructions within [[adyen-reporting]]; it does not itself inventory report fields or establish that a particular report was generated (raw lines 15–27, 63–70).

## Key takeaways

- **Prepare the reconciliation model:** First understand the balance platform's account structure and funds flow, identify the reports relevant to the use case, and understand fee types. Adyen recommends ensuring reports have the necessary information and testing reconciliation processes before live use (raw lines 19–27).
- **Align periods and columns:** Configure report time zones because report periods and zones differ and mismatches commonly cause reconciliation failures. Adyen account reports have default columns; many allow added columns, but additions enlarge files and column changes can affect an automated system consuming them (raw lines 29–44).
- **Role-gated column edits:** The listed Customer Area roles for **configuring columns** are Merchant admin, Merchant report role, Merchant financial or Merchant POS Report role. The page gives Settings → Report columns steps, including selecting/ordering fields and saving (raw lines 42–61). These roles are scoped to this edit, not stated here as the complete access rule for generating or downloading every report.
- **Retrieval and testing routes:** The page points Adyen account reports to manual/automatic reporting guides and balance-platform reports to a separate platform-report guide. It recommends complete sample or TEST-transaction reports for pre-live reconciliation checks because example reconciliation guides show only selected rows and columns (raw lines 63–79).

## Detail locators

- Account/funds-flow, relevant-report and fee prerequisites: raw lines 21–27.
- Time-zone alignment and configurable-column tradeoffs: raw lines 29–44.
- Column-edit roles and Customer Area workflow: raw lines 46–61.
- Distinct Adyen-account versus balance-platform report retrieval routes and full-report testing: raw lines 63–79.

## Evidence boundary

This page concerns report preparation, not report creation, file delivery or verification of a particular payment, transfer, payout or bank receipt. Follow the linked report-specific guides for report grain, time zone, generation/download authorization and field semantics. A successful report configuration does not prove the underlying financial event or completed reconciliation.

## Related

- [[adyen-reporting]] — reporting and reconciliation routes.
- [[source-adyen-docs-payouts-payout-service-reports-and-fees-balance-platform-accounting-report]] — separate balance-platform report reference.
- [[source-adyen-docs-payouts-payout-service-reconcile-balances]] — separate merchant-to-balance-platform reconciliation workflow.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/prepare-reports/2026-09-15|Pinned Payout Service report-preparation guide, captured 2026-09-15]]
