---
title: "Adyen account balance types"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/balances"
raw_files:
  - "adyen/docs/account/balances/2026-09-15.md"
tags: [adyen, account-balances, reserve, deposit, payouts]
---

## Overview

This dated Adyen balances guide (2021-11-22 last-modified metadata; captured 2026-09-15) defines funds held in merchant accounts, a company-account sum, and the distinction between **available funds** and **deposit**. It names five components—pending, next payout, reserve, conditional negative refund allowance, and deposit—with different purposes. A balance category or projected next payout is not proof that funds reached the merchant's bank. See [[adyen-account-structure]] and [[adyen]].

## Key takeaways

- Balances belong to the business and are held in Adyen merchant accounts. The company view is described as the sum of balances in its merchant accounts. The page links Customer Area/Balance Control API viewing and management, plus a merchant-account activity log. It does not itself specify user roles, API credentials, or how to aggregate different currencies; use the separate view/manage guides for those. [Raw lines 17–35]
- **Available funds** are defined here as balances the merchant can adjust: **pending** gross sales/refunds not yet settled by scheme or payment method; **next payout**, a changing amount to be settled to the bank at the next payout; **reserve**, merchant-configured cover for refunds, chargebacks and other expenses when in-process funds are insufficient; and **negative refund allowance**, additional refund capacity only if Adyen grants eligibility. The stated formula is the sum of those four components when the allowance applies. None of that formula alone records completed bank receipt. [Raw lines 37–49]
- **Deposit** is separate from available funds. Adyen withholds it against potential processing losses/liabilities, calculates its requirement daily using factors including processing volume and chargebacks/refunds, and can raise or lower that requirement. An increase books sales funds to deposit; a decrease releases excess deposit into next payout. The merchant configures reserve but cannot set the deposit amount. [Raw lines 51–59]
- The **Activity log** is a history of balance adjustments, including transfers, payouts, currency exchange and top-ups. It helps trace adjustments; it does not substitute for a bank posting or reconcile an individual payment on this page. [Raw lines 61–63]

## Detail locators

- Merchant/company scope and two balance categories: raw lines 17–35. Available-funds four-component formula and meanings: raw lines 37–49. Deposit computation and transfer to/from next payout: raw lines 51–59. Activity log: raw lines 61–63.
- The page's links to next-payout, reserve, deposit, view, and manage guides are navigation; exact roles, currency presentation, payout timing and API shape are owned by those separate sources.
- This snapshot is conceptual. It does not identify a live bank balance, bank receipt, merchant-of-record allocation, or a completed payout.

## Related

- [[adyen-account-structure]]
- [[adyen]]
- [[source-adyen-docs-account-view-your-balances]]

## Raw Sources

- [[raw/adyen/docs/account/balances/2026-09-15|Adyen balances, 2026-09-15 snapshot]]
