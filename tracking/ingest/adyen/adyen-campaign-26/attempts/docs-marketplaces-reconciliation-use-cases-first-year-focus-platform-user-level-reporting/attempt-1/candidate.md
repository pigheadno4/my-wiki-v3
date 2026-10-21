---
title: "Adyen Marketplace user-level reporting use cases"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reconciliation-use-cases/first-year-focus/platform-user-level-reporting"
raw_files:
  - "adyen/docs/marketplaces/reconciliation-use-cases/first-year-focus/platform-user-level-reporting/2026-09-15.md"
tags: [adyen, marketplaces, platforms, reporting, user-dashboards, disputes]
---

## Overview

This 2026-09-15 Marketplace first-year guide proposes **three SMB-user reporting views**: transaction/fee history to review sales, a payout summary to reconcile sales with cash flow, and dispute/chargeback status and impact. For each, it offers an Adyen UI component or a report-based custom dashboard route. It is a design and report-selection guide, not evidence that an individual user received a payout or resolved a dispute. [[adyen]] [[adyen-reporting]]

## Key takeaways

- **Transaction view:** show sales, refunds, chargebacks and other transactions with gross amount, fees and expected net payout. The guide offers the Transactions Overview Component for an embedded interface, or the daily Balance Platform Accounting Report plus automatic generation/ingestion for a custom view. The component avoids building those data pipelines; the report path allows customized delivery but needs more product/engineering work (raw lines 27–52).
- **Payout view:** explain how gross sales, refunds, fees and other items compose a net payout. The Payout Component is the UI route; the daily Payout Report is the custom-data route and includes payout records with constituent transactions. The illustrative summary nets 1000 payments minus 100 refunds, 50 fees and 30 other to 820; “other” includes chargebacks, Capital withholdings and early/instant settlement costs. A payout report or dashboard row is not independent bank-credit evidence (raw lines 54–76, 111).
- **Dispute view:** users need actionable chargebacks/RFIs with deadlines, reasons and amounts, fraud alerts, ongoing/closed status, and financial impact. The Disputes Component route supports viewing, accepting or defending disputes, document upload and status tracking. The alternative Balance Platform Accounting Report contains **financial chargeback entries only**, not non-financial dispute events or a full case-management state (raw lines 78–100).
- For financial entries, the guide names `platformPayment` chargeback, chargebackReversal and secondChargeback types, with debits/credits and separate fee lines. Its text calls the signed register **Balance (BC)**, while the linked Balance Platform Accounting Report standard column is **Balance (PC)**; verify the actual report schema before mapping that field. A financial reversal or displayed dispute status does not itself prove final case resolution (raw lines 99–107).
- The transaction example lists a `100` payment and `2` fees but `820` as the same row's Net Payout, matching the separate payout-summary total rather than simple per-transaction net. Do not treat it as a transaction-level arithmetic formula (raw lines 36–42, 64–69). The page also mentions a Marketplace offering with point-of-sale elements; that example does not establish this Marketplace route's in-person eligibility (raw lines 27–30).

## Detail locators

- SMB jobs, transaction view and component versus Accounting Report: raw lines 17–52.
- Payout composition, component versus Payout Report and “other” definition: lines 54–76, 111.
- Dispute requirements, component route, financial-report limit and field-label mismatch: lines 78–107.

## Related

- [[adyen]] — provider.
- [[adyen-reporting]] — reporting and reconciliation concept.
- [[adyen-platform-components]] — embedded dashboard component context.
- [[source-adyen-docs-platforms-reconciliation-use-cases-first-year-focus-platform-user-level-reporting]] — separate Platforms-path guide.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — accounting-report field reference.
- [[source-adyen-docs-platforms-reports-and-fees-payout-report]] — payout-report reference.
- [[source-adyen-docs-platforms-build-user-dashboards]] — component navigation.

## Raw Sources

- [[raw/adyen/docs/marketplaces/reconciliation-use-cases/first-year-focus/platform-user-level-reporting/2026-09-15|Marketplace user-level reporting — 2026-09-15 snapshot]]
