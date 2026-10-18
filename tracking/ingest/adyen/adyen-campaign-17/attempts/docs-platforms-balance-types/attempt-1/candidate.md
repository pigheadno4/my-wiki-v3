---
title: "Adyen Platforms balance types"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/balance-types"
raw_files:
  - "adyen/docs/platforms/balance-types/2026-09-15.md"
tags: [adyen, platforms, balance-accounts, balances, reconciliation]
---

## Overview

This 2026-09-15 Adyen for Platforms snapshot defines five balance types for each currency held in a balance account: Balance/current, Available, Pending, Pending available and Reserved. It shows how future settlement and holds can change spendable funds, and where to view per-currency balances. These are account-balance categories, not proof that a particular payment settled, a payout reached a bank or an account holder owns funds legally. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Per-currency categories:** A balance account may contain one or several currencies, each with these balance types. `Balance` or current balance is the sum of already settled transactions. `Pending` is the sum of transactions expected to settle later and may be positive or negative. `Reserved` includes authorized outgoing-transfer funds not yet booked and blocked funds, with Capital repayments and collateral for paying out current balance given as examples. Do not equate pending or reserved with already settled, freely transferable funds.
- **Available and pending available:** The page calls `Available` the amount available for transfers and gives a lower-of-current-balance versus current-balance-minus-pending-and-reserved formula. It calls `Pending available` the amount that will become available after pending settlement, with a lower-of-pending versus pending-plus-available formula. The stated Available formula conflicts with the page's worked tables: on January 1 in Example 1, current EUR 100, pending EUR 20 and reserved EUR 30 would yield EUR 50 if read literally, while the table shows Available EUR 70; in Example 2, current EUR 50 and pending EUR -70 would yield EUR 50, while the table shows Available EUR -20. Treat the illustrative balances as evidence of intended effects, not a reliable executable formula from this snapshot alone; verify the current Adyen definition before implementing calculations or payout controls.
- **Consequential examples:** Example 1 shows an incoming payment settling while a EUR 30 refund reserve keeps Available below current balance, then the refund settlement clears the hold. Example 2 shows a positive current balance with negative Available because of a future refund. Example 3 distinguishes Pending EUR 50 from Pending available EUR 20 when current/available is EUR -30. These are illustrative account timelines, not account-specific ledger or authorization evidence.
- **Observe and respond:** For all currencies in a balance account, the page points to `GET /balanceAccounts/{id}`, `balancePlatform.balanceAccount.balance.updated` webhooks, and Customer Area **Balance accounts > Balances**. It says configurable balance-change notifications can help a platform decide whether to top up or transfer funds to avoid negative balances. That is operational guidance, not an instruction to move funds automatically or proof that a top-up succeeded.

## Detail locators

- Per-currency premise and five balance definitions, including literal formulas and reserve components: raw lines 19–30. Configurable balance notifications and optional top-up/internal-transfer response: line 32. API/webhook/Customer Area viewing routes: lines 34–40.
- Example 1 settlement/refund reserve timeline: lines 48–68. Example 2 negative Available despite positive current balance: lines 72–86. Example 3 Pending versus Pending available: lines 90–104. Links to separate balance-update, top-up and internal-transfer guides: lines 106–116.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform balance-account context.
- [[source-adyen-docs-platforms-manage-balance-accounts]] — balance-account resource creation and management; distinct from balance-type calculations.

## Related raw API references

- The raw page links to Balance Platform API account retrieval, balance-update webhooks, balance notifications, top-ups and internal fund transfers. Consult those sources independently for current schema and movement conditions.

## Raw Sources

- [[raw/adyen/docs/platforms/balance-types/2026-09-15|Adyen Docs: Balance types (2026-09-15 snapshot)]]
