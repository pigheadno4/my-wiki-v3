---
title: "Adyen merchant-account balance management"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/manage-your-balances"
raw_files:
  - "adyen/docs/account/manage-your-balances/2026-09-16.md"
tags: [adyen, merchant-account, balances, funds-transfer]
---

## Overview

This Adyen webpage snapshot explains how merchant-account balances are allotted and how a merchant can top up an account or transfer funds between eligible merchant accounts through Customer Area or the Balance Control API. It names **pending balance, refund reserve, next payout amount, deposit, and negative refund allowance**; Adyen determines fixed deposit and negative-refund-allowance amounts (raw lines 19–32). It does not by itself show that a top-up payment was received, a transfer was performed, or a bank payout arrived. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- An increase first enters the merchant account's **pending balance**; after settlement, Adyen allots funds to the other balances. A top-up may state a reason: reserve funding, deposit funding, or offsetting a negative payable amount. Reserve funding above the threshold automatically increases that threshold to prevent those funds joining the next payout batch (raw lines 34–44).
- Without a top-up reason, Adyen lists an allocation priority: cover a negative pending/next-payout amount, meet mandatory deposit requirements, bring reserve to its threshold, then pending balance and (once settled) next payout amount. The page gives the same priority for increases from processed payments or account transfers (raw lines 46–68). The described automatic **allocation** and threshold adjustment are not a claim that Adyen automatically obtains new funding.
- A generated top-up payment adds funds only **when Adyen receives it**. The page gives EUR/USD arrival within two business days and up to four business days for other currencies, with special transfer details for some currencies such as ZAR (raw lines 84–90). Generation or initiation is not receipt.
- Cross-account transfers require two merchant accounts under the **same company account and legal entity** with at least one common processing currency; that currency is used for the transfer (raw lines 107–111). Customer Area transfer instructions require `Merchant financial` (line 115), while the general requirements table lists either `Merchant financial` or `Manage key financial tasks` for Customer Area reserve/top-up/transfer work (lines 79–81). Keep the transfer-specific role statement rather than silently treating the broader table as sufficient. The Balance Control API requires the `Balance control API - Balances management` credential role.
- The API `POST /balanceTransfers` request specifies minor-unit `amount.value`, currency, source/destination merchants and transfer type; `reference` is optional, maximum 80 characters (raw lines 129–150). The documented response carries a `pspReference` and `createdAt`, described as the time the transfer was performed (lines 173–187). The Customer Area activity log and Company Payout/Settlement details reports are follow-up routes for balance adjustments (lines 189–201), not proof of an external bank deposit.

## Detail locators

- `Fund allotment`, raw lines 34–70: reason-specific allocation and no-reason/payment/transfer priority.
- `Requirements` and `Top up your account`, raw lines 72–105: integration, roles, preparation, timing, and Customer Area steps.
- `Transfer funds between accounts`, raw lines 107–187: shared-account/legal-entity/currency condition, Customer Area role and steps, API field table and response.
- `Keep track of balance changes`, raw lines 189–201: activity log and report navigation.

## Related

- [[adyen-account-structure]] — merchant/company account hierarchy and access scope.
- [[adyen-reporting]] — report evidence boundaries for balance-transfer review.

## Raw Sources

- [[raw/adyen/docs/account/manage-your-balances/2026-09-16|Manage your balances, fetched 2026-09-16]]
