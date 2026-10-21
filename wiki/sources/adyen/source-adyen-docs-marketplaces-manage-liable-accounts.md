---
title: "Adyen Marketplaces: Manage liable balance accounts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-liable-accounts"
raw_files:
  - "adyen/docs/marketplaces/manage-liable-accounts/2026-09-15.md"
tags: [adyen, marketplaces, platforms, liable-accounts, balance-accounts]
---

## Overview

This 2026-09-15 **Marketplaces / Adyen for Platforms** guide distinguishes three **marketplace-owned liable balance accounts**: the **main liable balance account**, **reserved incorrect splits account**, and **reserved compensation account**. These hold or route the marketplace’s funds; they are not user balance accounts, and the guide does not show a particular payment, transfer or payout completing. [[adyen-platforms]]

## Account roles and money flow

- **Main liable balance account:** holds most marketplace funds; transaction commissions are booked there. The marketplace may also use it to pay users’ transaction fees or transfer funds to users to correct balances. See [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15|raw lines 25–27]].
- **Reserved incorrect splits account:** if a split targets a nonexistent balance account, or one unable to receive because it or its holder is closed/suspended or the holder lacks the receive-funds capability, Adyen books those funds to this marketplace account. The page points to a later **internal transfer** from that account to correct balances; the fallback booking is not proof that the intended user received funds. See [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15|raw lines 29–37]].
- **Reserved compensation account:** covers negative user/marketplace balance accounts caused by refunds or chargebacks. The captured rule says Adyen allows a negative balance for **up to 30 days**; if it remains negative for **more than 30 days**, Adyen debits this reserved account on the **first day of the following month**. That debit can leave the reserved account negative, which the marketplace must offset by top-up or an internal transfer from another balance account. See [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15|raw lines 39–45]]. This timing is source-described, not a transaction-specific compensation record.

## Detail locators

- Account ownership and the three account names: [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15|raw lines 15–23]].
- Main commission/fee/correction routing and incorrect-split destination conditions: [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15|raw lines 25–37]].
- Negative-balance compensation timing and deficit remedy: [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15|raw lines 39–45]].

## Related

- [[adyen-platforms]] — modern Platforms balance and split context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15|Manage liable balance accounts (captured 2026-09-15)]]
