---
title: "Adyen Payout Service card-payout reconciliation"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-cards/reconciliation"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-cards/reconciliation/2026-09-15.md"
tags: [adyen, payout-service, card-payouts, reporting, reconciliation]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service guide describes reconciling **card payouts initiated from the Balance Platform**. Within [[adyen-reporting]], it joins fee lines in merchant-account Settlement Details Reports to booked transfer amounts in balance-account Balance Platform Accounting Reports. It is a reporting recipe for card disbursements, not a bank-payout or beneficiary-receipt confirmation (raw lines 15–34).

## Key takeaways

- **Use both account scopes:** Obtain the Settlement Details Report from the merchant account(s) used for card payouts and the Balance Platform Accounting Report from the balance account(s) that instruct them (raw line 23). These are separate report grains; the page does not say a single report alone covers both amount and fee.
- **Fee line and amount:** Each Balance Platform-initiated card payout appears as `BPPaidOut` in the Settlement Details Report. Its `Net Debit (NC)` is **total fees deducted**, expressly not payout amount plus fees; `Markup (NC)`, `Scheme fees (NC)` and `Interchange (NC)` break out fee categories. The capture/card-payout amount is in the Balance Platform Accounting Report (raw lines 25–32).
- **Join and status condition:** Match the Settlement Details Report `Merchant Reference` ID to the Balance Platform Accounting Report `Transfer Id` **where Status is `booked`** (raw line 34). The source does not give a report-availability lag, timezone, card-network posting milestone or recipient-card receipt status; avoid inferring those from a booked accounting row.

## Detail locators

- Payout direction and two required reports/account scopes: raw lines 19–23.
- `BPPaidOut` and fee-column semantics: raw lines 25–30.
- Capture/card-payout amount and booked-ID join: raw lines 32–34.

## Evidence boundary

The source says “capture or card payout” for the Balance Platform amount, without specifying additional capture semantics here (raw lines 32–34). Its `booked` condition qualifies the accounting-report row used for the join; it does not prove the recipient card was credited or that external settlement finished. No timing or currency-conversion rule is supplied by this short guide.

## Related

- [[adyen-reporting]] — report and reconciliation route.
- [[source-adyen-docs-payouts-payout-service-reports-and-fees-balance-platform-accounting-report]] — separate accounting-report field reference.
- [[source-adyen-docs-payouts-payout-service-pay-out-to-cards]] — Payout Service card-payout route.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-cards/reconciliation/2026-09-15|Pinned Payout Service card-payout reconciliation guide, captured 2026-09-15]]
