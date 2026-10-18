---
title: "Payout reconciliation methods | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/payout-reconciliation"
raw_files:
  - "adyen/docs/platforms/payout-reconciliation/2026-09-15.md"
tags: [adyen, platforms, payouts, reconciliation, reports, webhooks]
---

## Overview

This [[adyen]] for Platforms page helps choose reports and webhooks for reconciling movement from Adyen toward **users' bank accounts**. It distinguishes a per-payout transaction breakdown, a full balance-account ledger, an activity summary and real-time payout-status updates. These tools support internal reconciliation; a report row, booked balance-account movement or webhook label is not independent proof that a beneficiary bank credited a particular payout. See [[adyen-reporting]] and [[adyen-platforms]].

## Key takeaways

- **Choose the evidence grain.** The page recommends the **Payout report** for sales, refunds and fees making up one payout; the **Balance Platform Accounting report** for the full ledger of balance-account credits and debits; the **Statement report** for activity over a period; and **payout transfer webhooks** for status changes. These methods answer different questions and should not be treated as interchangeable proof of bank receipt. [Raw: Reconciliation methods, lines 21–30]
- **Availability differs by payout type.** The table marks real-time tracking, the full ledger audit trail and activity summary available for **managed payouts, custom scheduled payouts, custom on-demand payouts and cashout**. It marks transaction-level breakdown available only for **managed and custom scheduled** payouts, not custom on-demand or cashout. The Payout report is described as the primary scheduled-payout tool with a 1:1 mapping between a payout transfer and its constituent payments, refunds and adjustments. These are documented report routes, not claims that any given report has been generated or is complete for a specific account. [Raw: Availability by payout type, lines 32–41; Using the Payout report, lines 57–59]
- **Amount basis matters.** By default, Adyen says it pays out **available balance**, accounting for pending risks such as future refunds, so payout totals may differ from recently settled sales. The page says choosing **current balance** uses the full settled-funds sum and a reserve account to cover potential risks, aligning payout amount with settled transaction totals in the Payout report. That is a described configuration relationship, not proof of reserve sufficiency, a particular payout amount, or bank arrival; the linked payout-amount guide owns detailed eligibility and calculation. [Raw: Payout amount and reconciliation, lines 43–51]
- **On-demand/cashout route.** Custom on-demand payouts and cashouts are outside the automated batch cycle and **absent from the Payout report**. The page instructs a unique API-request reference, then filtering the Accounting report by it and checking final `Booked` status and value date. Payout webhooks provide status updates including success or return for synchronization. A `Booked` report entry and webhook status must be interpreted at their own transfer/bank-tracking stages; neither by itself is a beneficiary-bank statement. [Raw: Reconciliation strategies, lines 61–70]

## Detail locators

- Raw `Reconciliation methods` (lines 21–30): need-to-report/webhook mapping.
- Raw `Availability by payout type` (lines 32–41): four payout-type matrix, especially transaction-breakdown exclusion.
- Raw `Payout amount and reconciliation` (lines 43–51): available-versus-current-balance basis and reserve-account condition.
- Raw `Reconciliation strategies` (lines 53–70): scheduled report mapping, on-demand/cashout reference lookup and payout webhook route.

## Related

- [[adyen-reporting]] — provider reporting and evidence boundary
- [[adyen-platforms]] — balance-account and payout context
- [[source-adyen-docs-platforms-reports-and-fees-payout-report]] — per-payout scheduled report fields
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — balance-account ledger fields
- [[source-adyen-docs-platforms-payout-webhooks]] — payout transfer status stages
- [[source-adyen-docs-platforms-payout-amount]] — detailed payout amount controls

## Raw Sources

- [[raw/adyen/docs/platforms/payout-reconciliation/2026-09-15|Adyen Platforms payout reconciliation — collected 2026-09-15]]
