---
title: "Adyen Classic Platforms payout notifications"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/payouts/payout-notifications"
raw_files:
  - "adyen/docs/classic-platforms/payouts/payout-notifications/2026-09-15.md"
tags: [adyen, classic-platforms, payouts, notifications, bank-returns]
---

## Overview

This 2022-modified Classic Adyen for Platforms guide, captured 2026-09-15, defines `ACCOUNT_HOLDER_PAYOUT` notification status updates after a payout is initiated: `Initiated`, `Confirmed` and `Failed`. It directs new implementations to the separate newer integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- `Initiated` means the payout has been scheduled to be sent to the account holder's bank; `estimatedArrivalDate` can be conveyed as an expectation, not bank receipt (raw lines 18–26). `Confirmed`, available in Notification v5 or later, means funds have left Adyen and are on their way to the bank; the guide estimates a few business days, but explicitly says the receiving bank can still return the payout afterward (raw lines 28–45).
- A `Confirmed` notification can include `payoutReference` and origin-bank account number, branch code, country and bank name to help the account holder locate the payout; these describe the bank from which the payout is initiated, not proof of final credit to the recipient (raw lines 36–45).
- `Failed` lists invalid account/routing, missing or closed account, returned funds, and validation errors such as payout disabled or amount above payable balance; a validation error carries `invalidFields`. The failed payout gets a new `pspReference` distinct from the initial payout (raw lines 47–62). Update bank details through `/updateAccountHolder` where applicable; the source links its Account API v4 reference (raw line 58).
- If a scheduled payout is returned, the account holder's payout state is automatically disabled. The guide instructs updating bank details via `/updateAccountHolder` and re-enabling payout state via `/updateAccountHolderState`; the MarketPay payments accounting report can link returned and initial payouts (raw lines 64–64). This return/recovery condition is specific to configured scheduled payouts, not every `Failed` event.

## Detail locators

- Classic-only scope, notification event and status vocabulary: raw lines 16–22. Initiated and estimated arrival: raw lines 24–26.
- Confirmed v5+ qualifier, bank-in-transit meaning, origin-bank fields and possible return: raw lines 28–45. Failed reasons, `invalidFields`, new `pspReference` and bank-detail update: raw lines 47–62. Scheduled-return disablement, two update calls and report join: raw line 64.

## Related

- [[adyen-classic-platforms]] — older platform model and account holders.
- [[source-adyen-docs-classic-platforms-payouts-track-payouts]] — payout tracking and further recovery context.
- [[source-adyen-docs-classic-platforms-payouts-scheduled-payout]] — schedule and HOLD behavior.
- [[adyen-platforms]] — separate newer platform model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/payouts/payout-notifications/2026-09-15|Classic payout notifications, captured 2026-09-15]]
