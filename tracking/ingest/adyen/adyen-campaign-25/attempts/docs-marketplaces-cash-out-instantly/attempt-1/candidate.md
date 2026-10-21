---
title: "Adyen Marketplace CashOut overview"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/cash-out-instantly"
raw_files:
  - "adyen/docs/marketplaces/cash-out-instantly/2026-09-15.md"
tags: [adyen, marketplaces, platforms, cashout, pending-balance]
---

## Overview

This 2020-modified Marketplace-path [[adyen]] CashOut overview, captured 2026-09-15, describes a user-requested cashout of funds in a user's **pending available** balance before normal settlement makes them available. A cashout can credit the user's balance account; an instant payout to the user's transfer instrument is a separate, conditional leg when specified. This belongs to the modern [[adyen-platforms]] balance-account model (raw lines 15–25, 41–46).

## Key takeaways

- **Amount and money movement:** The cashout amount must be no more than the user's pending available balance; if a fee is charged, the amount plus fee must fit that balance (raw lines 29–35). The four *possible* legs are Cashout Funding credit to the user's balance account, Cashout Instant Payout to the user's transfer instrument only if specified, optional Cashout Fee debit from the user account to the marketplace's liable balance account, and later Cashout Repayment debit when the captured payments settle (lines 41–46). The example's January 1 sale and two-day delay would make funds available January 3 (lines 29–31), but its repayment sentence calls January 1 the settlement date (line 46). Treat that as a source inconsistency, not an exact repayment schedule.
- **Availability and bank return:** The snapshot lists Australia/AUD, EEA/EUR, US/USD and UK/GBP, but support also depends on the receiving bank's ability to accept instant payouts (raw lines 48–57). If the bank cannot, the funds are returned and the cashout amount is restored to the source balance account's pending available balance. Australian instant payouts may be delayed by ANZ rail rate limiting (lines 50–59). This is regional snapshot guidance, not live eligibility or guaranteed receipt.
- **Limits and timing:** The listed minimum is 0.01; a rolling 24-hour maximum per balance account is configured at balance-platform level with Adyen approval. The page lists no maximum count per day, yet successful requests on the same balance account have a cooldown until the previous request finishes processing—usually about one minute, up to ten (raw lines 61–68). Pass-through-settlement payment methods, such as the example Affirm, do not contribute to pending available and cannot be cashed out (line 69).
- **Reconciliation and tests:** The daily Statement report tracks balance movements. The Payout report is generated when scheduled payouts occur; after a full cashout, no scheduled payout may occur for that balance account that day and no Payout report is generated for it (raw lines 71–83). Transfer webhooks provide real-time transfer tracking (lines 85–87). The page instructs TEST-only cashout-priority bank details, with insufficient funds and missing `sendToTransferInstrument` capability as failure tests (lines 89–99); they do not establish a live outcome.

## Detail locators

- Pending-available context, example amount/fee conditions and conditional funding/payout/fee/repayment legs: raw lines 15–46.
- Snapshot countries/currencies, receiving-bank return and Australia delay: raw lines 48–59.
- Amount, rolling maximum, cooldown, count and pass-through limits: raw lines 61–69.
- Statement/Payout reports, webhooks and TEST scenarios: raw lines 71–99.

## Evidence boundary

CashOut makes pending balance available in the platform ledger; the optional instant bank payout, later settlement repayment, transfer status and beneficiary bank receipt are distinct events. The illustrative sales timeline conflicts internally on the settlement date (raw lines 29–31, 46), so it cannot prove a specific repayment date. A request, funding entry, report row or test result does not prove bank receipt. This modern Marketplace flow is separate from Classic Platforms and ordinary payout scheduling.

## Related

- [[adyen-platforms]] — current platform and marketplace context.
- [[source-adyen-docs-marketplaces-cash-out-instantly-cashout-request]] — request details and conditions.
- [[source-adyen-docs-marketplaces-cash-out-instantly-cashout-webhooks]] — transfer-leg event tracking.

## Raw Sources

- [[raw/adyen/docs/marketplaces/cash-out-instantly/2026-09-15|Pinned Marketplace CashOut overview, captured 2026-09-15]]
