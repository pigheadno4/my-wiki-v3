---
title: "Adyen settlement reconciliation hub"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/settlement-reconciliation"
raw_files:
  - "adyen/docs/reporting/settlement-reconciliation/2026-09-15.md"
tags: [adyen, reporting, settlement-reconciliation, payout-batches, navigation]
---

## Overview

This Adyen Docs landing page (2022-08-03 last-modified metadata; captured 2026-09-15) routes merchants to transaction-level or batch-level settlement reconciliation guides. It links payout-batch closure to settlement and tells merchants to configure payout frequency before reconciling. It is a **navigation hub**: the linked guides own report fields, amounts, currencies, dates, roles and matching procedures, and this page is not evidence that a specific bank credit arrived. See [[adyen-reporting]] and [[adyen]].

## Key takeaways

- The page says a settlement from Adyen follows batch closure and asks the merchant to configure payout frequency before settlement reconciliation. It does not specify a particular payout cutoff, schedule, batch identifier, or bank posting date. [Raw lines 14–18]
- The **transaction-level** route is for seeing payments, refunds, chargebacks and transaction costs included in a single payout batch. This hub labels that route but does not give transaction rows, formulas or exception handling. [Raw lines 22–24]
- The **batch-level** route is for viewing payout batches, matching them to a bank statement and reviewing bank/card commission costs per batch. A report-to-statement matching workflow is distinct from this hub independently proving receipt. [Raw lines 26–28]
- Adyen for Platforms merchants are directed to the Platform reports overview instead. Invoice reconciliation and fiscal-period closing are additional navigation routes, not described processes on this page. [Raw lines 20, 30–33]

## Detail locators

- Settlement/payout-frequency context and scope exception: raw lines 16–20. Transaction-level and batch-level route labels: raw lines 22–28. Related reporting navigation: raw lines 30–33.
- This page provides no report schema, permissions, currency unit, time zone, transfer reference, bank-arrival confirmation, or final accounting conclusion; retrieve the route-specific source and bank statement for an actual reconciliation question.

## Related

- [[adyen-reporting]]
- [[adyen]]
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level]]
- [[source-adyen-docs-reporting-settlement-reconciliation-batch-level]]

## Raw Sources

- [[raw/adyen/docs/reporting/settlement-reconciliation/2026-09-15|Adyen settlement reconciliation hub, 2026-09-15 snapshot]]
