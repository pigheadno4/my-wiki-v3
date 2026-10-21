---
title: "Adyen Marketplaces payout amount calculation"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payout-amount"
raw_files:
  - "adyen/docs/marketplaces/payout-amount/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payouts, balance-accounts, reserve-account]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace guide explains the maximum amount available for a scheduled or on-demand payout to a user, based on that user's balance account. In [[adyen-platforms]], the default cap is available balance; an alternative platform-wide current-balance configuration can use the platform reserve account as collateral against future negative user balances. A cap calculation or collateral block is not evidence that a bank payout was executed or received.

## Key takeaways

- The payout must be no greater than the maximum Adyen calculates. Only one configuration can be active at a time, and it applies to all balance accounts in the platform. By default, the maximum equals the user's **available balance**; the alternative maximum equals the user's **current balance**, meaning already-settled funds, and requires Adyen contact and sufficient available funds in the platform reserve account. The reserve is distinct from the user's payout-source balance account. See raw lines 19–43 and 95–104.
- For the default available-balance cap, Adyen sums settled funds for current balance and future changes reflected in reserved and pending balances. A zero or positive net future change leaves the cap at current balance; a negative net reduces the cap. Its USD 100 current and USD -20 future example yields USD 80 available. The prose says to “subtract” a negative sum, which if read literally would yield USD 120; use the example's reduction rather than claiming that phrase is an unambiguous signed-arithmetic formula. See raw lines 47–93.
- Under the enabled current-balance alternative, if current equals available, the page says Adyen pays current. If current exceeds available, Adyen checks the platform reserve account, blocks the difference as collateral when its available funds suffice, then processes the payout; insufficient reserve funds cause the payout to fail. In the illustration, USD 1000 current and USD 800 available require USD 200 reserve collateral. This describes provider handling, not proof of an individual payout or beneficiary-bank credit. See raw lines 95–155.
- Collateral is gradually unblocked as incoming funds compensate the user's negative available balance. If that balance stays negative for 30 days, Adyen says it transfers the remaining collateral from the platform reserve account to the user's balance account and sends an internal-transfer webhook. This is an internal collateral movement, distinct from the earlier user bank payout. The examples show partial and full compensation, not a universal release timetable before that condition. See raw lines 157–224.
- Adyen recommends checking the user's balance before initiating a payout through Balance Platform API GET `/balanceAccounts/{id}`, Customer Area, or balance webhooks. The page links managed, scheduled custom and on-demand payout guides but does not specify their bank routing, returns, retries or receipt evidence. See raw lines 226–238.

## Detail locators

- Purpose, prerequisites and platform-wide default/current configuration choice: raw lines 17–45.
- Available-balance method, three future-change examples and signed-wording tension: raw lines 47–93.
- Current-balance reserve sufficiency and payout failure branch: raw lines 95–124.
- USD 1000/800/200 reserve example: raw lines 128–155.
- Collateral release, 30-day internal transfer and examples: raw lines 157–224.
- Pre-payout balance checks and payout route links: raw lines 226–238.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — canonical modern platform payout and balance-account concept.
- [[source-adyen-docs-platforms-payout-amount]] — separate Platforms URL for the corresponding calculation guide.
- [[source-adyen-docs-marketplaces-manage-reserve-account]] — platform reserve-account context.
- [[source-adyen-docs-marketplaces-payout-webhooks]] — payout transfer and bank status evidence.
- [[adyen-platform-internal-transfers]] — separate internal transfer route for later collateral movement.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payout-amount/2026-09-15|Marketplace payout amount — pinned 2026-09-15 raw snapshot]]
