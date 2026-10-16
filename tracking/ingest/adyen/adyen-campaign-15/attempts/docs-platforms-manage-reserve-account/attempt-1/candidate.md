---
title: "Manage a reserve account | Adyen for Platforms"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-reserve-account"
raw_files:
  - "adyen/docs/platforms/manage-reserve-account/2026-09-15.md"
tags: [adyen, platforms, reserve-account, balance-accounts, transfers, collateral]
---

## Overview

This 2026-09-15 [[adyen]] for Platforms guide defines the platform **reserve account** as a type of balance account linked to the **liable account holder**. Its funds serve as collateral for negative user-balance amounts caused by transfers initiated by the platform or its users. This is distinct from a user's balance account and from the **reserved compensation account**, which the page says covers negatives from refunds or chargebacks. [[adyen-platforms]]

## Transfer and collateral sequence

- A reserve account allows transfer requests that would create a negative balance on a user's balance account, subject to enough available reserve funds. The page gives paying out a user's **current balance** as an example because later negative balance changes can leave that user's account below zero; this example is not a rule that every payout becomes negative.
- When such a transfer is requested, Adyen checks the reserve-account balance. If insufficient, the **transfer request fails**. If sufficient, Adyen blocks collateral equal to the negative balance caused by the transfer request, then processes the transfer. The collateral is unblocked when the user's balance account receives enough funds to compensate for the negative balance. A request, authorization or collateral block alone does not prove completed transfer, bank payout or immediate release of collateral; the page gives no fixed release time.
- Adyen recommends constantly checking **available** reserve balance. If it is insufficient, Adyen cannot authorize transfers that create negative balances. The guide lists ways to increase available reserve balance: an internal transfer from another balance account, receiving funds through split payments, or topping up the reserve account. These are available funding routes, not evidence that any top-up, split or transfer has occurred.
- This short page does not specify role grants, minimum reserve percentages, country/currency limits or an API request schema. Follow the linked operation guides and actual account state before taking action; this snapshot does not establish current enablement.

## Detail locators

- **Reserve, liable-holder and reserved-compensation distinctions; current-balance example:** raw lines 15–23.
- **Sufficient-balance check, equal collateral block, processing and unblock condition:** raw lines 25–32.
- **Available-balance recommendation and three funding routes:** raw lines 34–42.

## Related

- [[adyen-platforms]]
- [[adyen-payouts]] — separate payout outcome

## Raw Sources

- [[raw/adyen/docs/platforms/manage-reserve-account/2026-09-15|Adyen Platforms reserve-account guide — collected 2026-09-15]]
