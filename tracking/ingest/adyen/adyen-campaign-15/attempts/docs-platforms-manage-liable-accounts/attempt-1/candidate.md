---
title: "Manage liable balance accounts in Adyen for Platforms"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-liable-accounts"
raw_files:
  - "adyen/docs/platforms/manage-liable-accounts/2026-09-15.md"
tags: [adyen, platforms, liable-accounts, splits, negative-balances]
---

## Overview

This 2026-09-15 Adyen for Platforms page distinguishes three liable balance accounts that belong to the platform and hold its funds: the main liable balance account, reserved incorrect splits account and reserved compensation account. These are platform-side balances, not a user's legal entity, account holder, balance account or bank transfer instrument. The page describes conditional booking and compensation behavior; it gives no Customer Area role or API-permission procedure, account-specific balance, merchant-of-record determination or proof of money movement.

## Key takeaways

- The main liable balance account holds most platform funds. Transaction commissions are booked there. The platform can use it to pay users' transaction fees or transfer funds to users, including balance corrections. The page describes possible uses, not an instruction to execute a transfer.
- If a payment split is directed to a balance account that does not exist or cannot receive funds, Adyen books those funds to the reserved incorrect splits account. The page lists closed or suspended balance-account status, closed or suspended account-holder status, and missing receive-funds capability as reasons an account cannot receive funds. It links to internal transfers for later correction; the misbooking or correction does not itself prove a particular user's final balance or bank receipt.
- The reserved compensation account covers negative balances in the platform. Refunds or chargebacks can put balance accounts negative. The page says Adyen allows a negative balance for up to 30 days; if it lasts more than 30 days, Adyen debits the reserved compensation account on the first day of the following month. That reserved account can itself become negative, in which case the platform must offset it by top-up or internal transfer. This timing is a dated provider rule, not evidence that compensation occurred for an account.
- No role grant, credential, user-verification outcome, financial-ownership transfer or merchant-of-record status is established by the account labels on this page. The linked payment-splitting, internal-transfer and top-up pages provide further navigation, not imported execution evidence.

## Detail locators

- `# Manage liable balance accounts`: three platform-owned account types.
- `## Main liable balance account`: commissions, fees and transfer uses.
- `## Reserved incorrect splits account`: failed split destination conditions and internal-correction route.
- `## Reserved compensation account`: refund/chargeback negatives, 30-day condition, following-month debit and offset route.

## Related

- [[adyen-platforms]] — provider platform concept and source route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-liable-accounts/2026-09-15|Adyen liable balance account guide (fetched 2026-09-15)]]
