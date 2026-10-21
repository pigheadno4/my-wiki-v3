---
title: "Adyen Marketplaces: Balance types"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/balance-types"
raw_files:
  - "adyen/docs/marketplaces/balance-types/2026-09-15.md"
tags: [adyen, marketplaces, platforms, balance-accounts, balances]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplaces guide defines five balance types **per currency** in a balance account: **Balance/current**, **Available**, **Pending**, **Pending available**, and **Reserved**. It gives viewing routes and example timelines for future settlement, holds and negative spendable amounts. These are balance categories and illustrations, not evidence of a particular payment's settlement, a completed transfer, payout or bank receipt. [[adyen-platforms]]

## Categories and viewing routes

- **Balance/current** is described as the sum of already settled transactions. **Pending** sums transactions that will settle later and can be positive or negative. **Reserved** includes authorised outgoing-transfer funds not yet booked plus blocked funds, with Capital repayment and current-balance payout collateral as examples. **Available** is the balance available for transfers; **Pending available** is the balance expected to become available after pending settlement. Keep settled, pending, reserved and transfer-available states separate. See [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|raw lines 19–30]].
- A balance account can hold one or multiple currencies. The source points to GET `/balanceAccounts/{id}`, `balancePlatform.balanceAccount.balance.updated` and Customer Area **Balance accounts > Balances** for all per-currency balances. It says configurable balance-change notifications can inform a decision to top up or transfer internally to avoid negative balances; the page does not show that any such movement happened. See [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|raw lines 32–40]].

## Formula and example conflict

- The printed **Available** formula is the lower of current balance and **current minus the sum of pending and reserved balances**. This conflicts with the examples. On January 1, Example 1 gives current **EUR 100**, pending **EUR 20**, reserved **EUR 30**, and Available **EUR 70**; the literal lower-of formula yields **EUR 50**. Example 2 gives current **EUR 50**, pending **EUR -70**, reserved **EUR 0**, and Available **EUR -20**; the literal formula yields **EUR 50**. See [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|raw lines 23–25, 58–64, 72–86]].
- The printed **Pending available** formula is the lower of pending and pending plus available. In Example 2, Pending **EUR -70** and Available **EUR -20** would yield **EUR -90** from that literal formula, but the table shows Pending available **EUR -70**. Example 3 separately shows Pending **EUR 50** versus Pending available **EUR 20** when current/available is **EUR -30**. Neither printed formula can be used as an unqualified executable balance or payout-control rule from this snapshot alone. See [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|raw lines 26–28, 78–86, 90–104]].
- Example 1 illustrates a settled incoming EUR 100, a later EUR 20 settlement, and a EUR 30 refund hold that reduces Available before the refund settles. The tables are illustrative per-user-account dates, not a universal sequence or a reconciliation record for a specific payment. See [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|raw lines 48–68]].

## Detail locators

- Per-currency categories, literal formulas and reserve components: [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|raw lines 19–30]].
- Balance-change notification and API/webhook/Customer Area read routes: [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|raw lines 32–40]].
- Example 1 timeline and Example 2/3 formula conflicts: [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|raw lines 42–104]].

## Related

- [[adyen-platforms]] — platform balance-account context.
- [[source-adyen-docs-platforms-balance-types]] — related Platforms-path balance-type snapshot with its own raw evidence.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/balance-types/2026-09-15|Marketplace balance types (captured 2026-09-15)]]
