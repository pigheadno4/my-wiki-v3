---
title: "Adyen Platforms payout amount calculation"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/payout-amount"
raw_files:
  - "adyen/docs/platforms/payout-amount/2026-09-15.md"
tags: [adyen, platforms, payouts, balance-accounts, reserve-account]
---

## Overview

This Adyen for Platforms guide, last modified 2026-05-21 and captured 2026-09-15, explains how Adyen caps the amount payable from a user's balance account before a scheduled or on-demand payout under a managed or custom payout schedule. The cap protects the platform against possible future negative user balances. It is a calculation and collateral guide, not proof that a bank payout was executed or received. [[adyen]] · [[adyen-platforms]]

## Key takeaways

- **Two platform-wide configurations:** By default, the maximum payout equals the user's **available balance**: settled funds in the current balance, reduced when net future balance changes are negative. Future changes are reflected in reserved and pending balances; when their net is positive or zero, the maximum stays at current balance. Adyen's examples give USD 100 current with zero or positive net future changes → USD 100 available, and USD 100 current with USD -20 net future changes → USD 80 available. The prose says Adyen “subtracts the future balance changes” when that sum is negative, but literal subtraction of -20 conflicts with the USD 80 example; read it as reducing the cap by the magnitude of the negative net, not as a signed-arithmetic formula guaranteed by that sentence.
- **Current-balance alternative:** After contacting Adyen and ensuring sufficient available reserve-account balance, the platform may enable a maximum equal to the user's current balance, meaning already-settled funds. Only one configuration can be active at a time and it applies to all platform balance accounts. If current and available are equal, the page says Adyen pays the current balance. If current exceeds available, Adyen checks the **platform reserve account**, blocks the difference as collateral when sufficient, and processes the payout; if reserve funds are insufficient, the payout fails. The reserve is distinct from the user's payout-source balance account.
- **Collateral lifecycle:** The blocked reserve amount is released gradually as incoming funds compensate the user's negative available balance. If that balance remains negative for 30 days, Adyen transfers the remaining collateral from the reserve account to the user's balance account and sends an internal-fund-transfer webhook. The USD 1,000 current/USD 800 available/USD 200 collateral examples illustrate balance effects and later compensation; they do not establish a particular user's eligibility, actual payout, beneficiary bank receipt, or universal release timing before the 30-day condition.
- **Operational check:** Adyen recommends checking the user's balance-account balances before a payout through Balance Platform API GET /balanceAccounts/{id}, Customer Area, or balance webhooks. That recommendation is separate from the platform-wide configuration and reserve sufficiency requirements. This page does not specify the bank transfer's routing, cutoff, approval, return, or retry status; follow the payout-operation and payout-webhook routes for those questions.

## Detail locators

- Scope, requirements, default/current choices and platform-wide exclusivity: pinned raw lines 15–45.
- Available-balance method and three numeric examples, including wording/arithmetic tension: pinned raw lines 47–93.
- Current-balance enablement, reserve sufficiency and failure path: pinned raw lines 95–124.
- USD 1,000/800/200 reserve-block example and subsequent balances: pinned raw lines 128–155.
- Gradual release and 30-day collateral transfer with webhook: pinned raw lines 157–224.
- Balance-check options and linked managed/custom payout guides: pinned raw lines 226–238.

## Related

- [[adyen-platforms]] — main Platforms payout route and reciprocal source link.
- [[source-adyen-docs-platforms-manage-reserve-account]] — reserve account purpose and collateral precondition.
- [[source-adyen-docs-platforms-payout-webhooks]] — execution and bank-tracking states.

## Raw Sources

- [[raw/adyen/docs/platforms/payout-amount/2026-09-15|Adyen Calculating the payout amount, captured 2026-09-15]]
