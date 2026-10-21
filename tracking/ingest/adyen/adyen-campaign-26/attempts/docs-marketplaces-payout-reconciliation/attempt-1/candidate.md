---
title: "Adyen Marketplace payout reconciliation"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payout-reconciliation"
raw_files:
  - "adyen/docs/marketplaces/payout-reconciliation/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payouts, reporting, reconciliation]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] guide routes modern [[adyen-platforms]] payout reconciliation to report and webhook evidence under [[adyen-reporting]]. It distinguishes transaction-level payout composition, full balance-account ledger, period activity summary and real-time payout status by business need (raw lines 15–30). Its methods differ for scheduled sweeps versus on-demand payouts and CashOut.

## Key takeaways

- **Select evidence by question:** The Payout report is recommended for individual sales, refunds and fees within one payout; the Balance Platform Accounting Report is the full debit/credit audit trail; the Statement report summarizes account activity over a period; and payout transfer webhooks update status in real time (raw lines 21–30). The availability matrix says real-time tracking, ledger audit and activity summary span managed, custom scheduled, on-demand and CashOut types, while transaction breakdown is available only for managed and custom scheduled payouts (lines 32–41).
- **Scheduled versus ad hoc grain:** The Payout report is the primary tool for managed and custom scheduled payouts and is described as a 1:1 payout-transfer-to-contributing-transactions mapping (raw lines 57–59). On-demand payouts and CashOut are outside the automated batch cycle and are not included in that report. For those, include a unique API request reference, filter the Accounting Report by it, and confirm final **Booked** status and value date (lines 61–66). A booked balance-platform transfer is distinct from beneficiary bank credit.
- **Payout amount basis:** By default, available-balance payout calculation accounts for pending risks such as future refunds, so payout totals can differ from recently settled sales (raw lines 43–47). The page describes choosing current balance as a way to align payout totals with settled transactions, with a reserve account covering potential risks (line 49). This is a configurable approach described by the snapshot, not evidence a specific marketplace has it enabled or that a bank received funds.
- **Status and returns:** Payout webhooks provide status updates, including successful payout or return signals, without waiting for report downloads (raw lines 68–70). Use the actual payout/return events and beneficiary evidence for outcome claims; a report route, request reference or ledger booking alone does not establish bank receipt.

## Detail locators

- Reconciliation-method matrix and payout-type availability: raw lines 19–41.
- Default available-balance versus optional current-balance/reserve logic: raw lines 43–51.
- Scheduled payout report mapping, on-demand/CashOut accounting-reference procedure and real-time webhooks: raw lines 53–70.

## Evidence boundary

This guide chooses which report or webhook to inspect. It does not itself contain account-specific transaction rows, webhook events, reserve configuration, payout execution or beneficiary-bank statements. The Accounting Report's final Booked status and value date answer a balance-platform ledger question for on-demand/CashOut; they do not alone prove external bank receipt. The availability table must not be generalized into Payout Report transaction breakdown for ad hoc payouts.

## Related

- [[adyen-reporting]] — report and reconciliation concept.
- [[adyen-platforms]] — modern Marketplace balance-platform context.
- [[source-adyen-docs-platforms-reports-and-fees-payout-report]] — existing Platforms-path scheduled-sweep breakdown guide.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — ledger fields and dates.
- [[source-adyen-docs-marketplaces-payout-webhooks]] — status and return events.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payout-reconciliation/2026-09-15|Pinned Marketplace payout-reconciliation guide, captured 2026-09-15]]
