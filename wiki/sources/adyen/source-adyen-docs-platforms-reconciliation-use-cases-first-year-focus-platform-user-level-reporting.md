---
title: "Adyen Platforms user-level reporting use cases"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reconciliation-use-cases/first-year-focus/platform-user-level-reporting"
raw_files:
  - "adyen/docs/platforms/reconciliation-use-cases/first-year-focus/platform-user-level-reporting/2026-09-15.md"
tags: [adyen, platforms, reporting, reconciliation, payouts, disputes]
---

## Overview

This 2026-09-15 first-year Adyen for Platforms guide suggests reports a platform can build for its SMB users: transaction overview, payout overview, and chargeback/dispute management. It compares ready-made UI components with custom dashboards fed by Balance Platform Accounting or Payout Report data. Its templates and example values illustrate desired user views, not verified transactions, actual bank deposits, or completed dispute outcomes.

## Key takeaways

- A user-facing **Transactions overview** should list sales, refunds, chargebacks, gross amounts, charged fees, and net payout context. For point-of-sale users it can contribute to a broader register view that also includes cash. The guide presents either the Transactions Overview Component or a custom dashboard built from automatically generated Balance Platform Accounting Report CSV and an ingestion pipeline. The report is described as a platform-day data source; a platform must still scope and transform records to the individual user and match the relevant statuses, dates, balance accounts, and references before asserting that user's sale or payout.
- A **Payout overview** is a simplified set of transactions and fees that sum to a payout, with a daily example: payments, refunds, fees, and other movements. Options are the Payout Component or an ingested Payout Report, which the page says includes payouts and the transactions composing them. The example's `Other` footnote includes chargebacks, Capital-loan withholdings, and early/instant-settlement costs, so gross sales minus a single fee line is insufficient for a payout bridge. A report payout date or component view is not independent evidence that the beneficiary bank received funds.
- A **Chargebacks and disputes** view should identify unanswered chargebacks/RFIs, fraud alerts, ongoing/closed items, deadlines, reasons, amounts and financial impact. The Disputes Component supports view, accept/defend, document upload and status tracking. The Balance Platform Accounting Report is an alternative for **financial** chargeback events but does not contain non-financial dispute events, so it cannot replace the dispute workflow or prove case resolution by itself.
- In the accounting report's `platformPayment` category, `chargeback` debits the designated balance account and has negative Balance (BC), `chargebackReversal` credits it with positive Balance (BC) after a successful defense or repayment, and `secondChargeback` debits it again if the issuer rejects the defense. Chargeback and second-chargeback fees are separate report lines. These are event/report interpretations, not a guarantee that a dispute can still be defended or that a displayed reversal is final.
- The transaction and payout tables are explicitly examples. A transaction template row shows a net-payout figure that cannot be derived from the values in that same row alone; do not use these sample figures as a reconciliation formula or live accounting proof. The daily payout example uses a 2025 date narrative only illustratively; actual account period, report date and funding evidence govern any real user's answer.

## Detail locators

- `## Transactions overview`: user sales/register purpose, sample fields and component versus Accounting Report build options.
- `## Payout overview`: payout bridge, example amounts, Payout Component versus Payout Report, and `Other` footnote.
- `## Chargebacks and disputes`: operational versus financial event scope, component workflow, Balance Platform Accounting report signs and separate fees.

## Related

- [[adyen-reporting]] — main reporting/reconciliation concept.
- [[adyen-platforms]] — parent Platforms context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/reconciliation-use-cases/first-year-focus/platform-user-level-reporting/2026-09-15|Adyen Platforms user-level reporting use cases (fetched 2026-09-15)]]
