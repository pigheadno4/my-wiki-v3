---
title: "Marketplace reports and fee types"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reports-and-fees"
raw_files:
  - "adyen/docs/marketplaces/reports-and-fees/2026-09-15.md"
tags: [adyen, marketplaces, reporting, reconciliation, fees]
---

## Overview

This pinned Marketplace reporting hub explains which **Adyen account** and **balance platform** reports serve financial reconciliation and how payment splits and fees appear across them. Reports can be scheduled or generated on demand. A complete **monthly** financial reconciliation needs a combination of account and platform reports; some narrower tasks use one report. This catalog is a route to report-specific definitions, not evidence that a particular merchant's books reconcile. See [[adyen]] and [[adyen-reporting]] (raw lines 15–34).

## Key takeaways

- **Adyen account scope:** the Received payment details report covers individual payment interactions and statuses; **Payment accounting** is required for full reconciliation and covers payment lifecycle events and associated fees, but excludes balance-platform charges for payouts, fund transfers and KYC checks. **Settlement details** is optional for full reconciliation and includes payment funds/costs, monthly-invoice balance adjustments, and one-off inbound wire deposits. The **Monthly invoice** is required for fee and adjustment totals for the preceding month (raw lines 38–47).
- **Balance platform scope:** the **Balance Platform Accounting Report** is required for full reconciliation. Its daily or interactive view tracks balance changes and individual account-holder/balance-account events across liable and user accounts. The **Balance Report** gives daily opening/closing balances across all accounts; the **Statement Report** covers accounts with a balance change that day and events including scheduled or on-demand payouts (raw lines 49–57).
- Payment or capture **split instructions** determine account-holder credits/debits. Accounting Report splits appear as separate `Category = platformPayment` lines, joinable by matching `Psp Payment Psp Reference`. Without split instructions, Adyen credits or debits the **liable account**; the page uses a partial refund with omitted splits as a debit example (raw lines 59–65).
- Fees are deducted from settlement and default to the platform liable balance account. Captured-funds transaction fees (Interchange, Scheme, Markup, Commission) appear in the Balance Platform Accounting Report and the Adyen-account payment/settlement reports. Processing fees can arise from instructions without balance-booked funds and are detailed in Payment accounting; monthly invoice and Settlement details carry broader totals and adjustments. Report location varies by fee type and region; the fee table marks FanF and Merchant Location Fee **US-only** (raw lines 67–93).
- A report row, webhook match, or invoice line alone is not proof of complete reconciliation, a successful payout, or beneficiary-bank receipt. Use the linked report's exact grain, dates, account scope and fields for a specific accounting question (raw lines 30–78).

## Detail locators

- Account-versus-platform report selection and monthly requirement: raw lines 30–57.
- Split line matching and liable fallback: raw lines 59–65.
- Fee locations, charge basis and US-only entries: raw lines 67–93.
- Report preparation and reconciliation next steps: raw lines 95–111.

## Related

- [[adyen]]
- [[adyen-reporting]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/reports-and-fees/2026-09-15|Pinned reports and fees hub]]
