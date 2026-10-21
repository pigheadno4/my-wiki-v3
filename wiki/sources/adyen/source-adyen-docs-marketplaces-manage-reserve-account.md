---
title: "Adyen Marketplace reserve account"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-reserve-account"
raw_files:
  - "adyen/docs/marketplaces/manage-reserve-account/2026-09-15.md"
tags: [adyen, marketplaces, reserve-account, collateral, transfers]
---

## Overview

This 2026-09-15 Marketplace-route Adyen for Platforms guide defines the platform **reserve account** as a balance account linked to the liable account holder. It supplies collateral for user-balance deficits caused by transfers initiated by the platform or its users, and is distinct from the **reserved compensation account** for refund/chargeback deficits. [[adyen]] [[adyen-platforms]]

## Key takeaways

- A reserve account enables transfers that would make a user's balance account negative. It is liable-account-holder-linked, rather than an ordinary user balance account; the reserved compensation account has a different purpose, covering negative balances caused by refunds or chargebacks (raw lines 19–21). A platform configured to pay out users' **current balance** is one example of needing reserve collateral if later balance changes become negative (raw line 23).
- When a transfer request would create a negative user balance, Adyen checks whether the reserve account has enough available funds. If insufficient, the transfer request fails. If sufficient, Adyen blocks collateral equal to the transfer-caused negative balance, then processes the transfer; collateral is unblocked when the user account receives enough funds to compensate the negative balance (raw lines 25–32). A request or collateral block alone is not proof of completed payout or beneficiary-bank receipt.
- The guide recommends monitoring the reserve account's available balance. Its listed ways to increase it are internal transfer from another balance account, receiving split-payment funds into the reserve account, and topping up the reserve account (raw lines 34–42). These are funding routes, not evidence that a particular reserve was funded or that a transfer succeeded.

## Detail locators

- Reserve ownership/purpose, reserved-compensation distinction and current-balance payout example: raw lines 19–23. Collateral check, failure, block/process/release sequence: raw lines 25–32. Monitoring and three funding routes: raw lines 34–42.

## Related

- [[adyen-platforms]] — modern balance-platform and Marketplace route.
- [[source-adyen-docs-platforms-manage-reserve-account]] — related Platforms reserve-account guide; retain this Marketplace source's own snapshot.
- [[source-adyen-docs-platforms-payout-amount]] — current-balance payout cap and collateral conditions.
- [[adyen-classic-platforms]] — older account model with separate negative-balance rules.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-reserve-account/2026-09-15|Marketplace reserve account, captured 2026-09-15]]
