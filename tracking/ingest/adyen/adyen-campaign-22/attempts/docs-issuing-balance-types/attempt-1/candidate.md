---
title: "Adyen Issuing balance types"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/balance-types"
raw_files:
  - "adyen/docs/issuing/balance-types/2026-09-15.md"
tags: [adyen, issuing, balance-platform, balance-accounts]
---

## Overview

This 2026-09-15-captured Adyen Issuing-path guide defines five balance types for each currency in a balance account on a balance platform: current balance, available, pending, pending available, and reserved. It describes balances held in the user's balance account, not funds available to a particular card or proof of a completed transfer. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Current balance is the sum of already-settled transactions. Pending is the signed sum of transactions expected to settle later. Available is the amount available for transfers; pending available describes what will become available after pending settlement. Reserved covers authorized but not yet booked outgoing transfers and blocked funds, including the page's Capital-repayment and current-balance-payout examples. See the source table at raw lines 19–30.
- The guide gives lower-of formulas for available and pending available (raw lines 24–28), but those printed formulas do not reconcile with all worked values. In Example 2, current EUR 50, pending EUR -70 and reserved EUR 0 yield available EUR -20 and pending available EUR -70 (raw lines 72–86); the literal available formula in lines 24–25 instead yields EUR 50, and the literal pending-available formula in lines 27–28 yields EUR -90 when using the table's available value. Treat the formulas and examples as conflicting snapshot evidence, not a reliable calculation specification.
- The example also shows a negative available balance despite a positive current balance (raw lines 72–86). Example 3 distinguishes EUR 50 pending from EUR 20 pending available against a EUR -30 current balance (raw lines 90–104). These are illustrations, not a promise of future settlement or transfer success.

## Detail locators

- Balance type definitions and reservation components: raw lines 19–30. Conditional balance-change webhooks and potential top-up or inter-account transfer response: raw line 32.
- Multiple-currency balance lookup through GET /balanceAccounts/{id}, the balance.updated webhook, or Customer Area Balance accounts > Balances: raw lines 34–40.
- Three dated arithmetic examples, including reservation before refund settlement and negative available balance: raw lines 42–104.

## Related

- [[adyen-issuing]] — Issuing program and balance-platform context.

## Raw Sources

- [[raw/adyen/docs/issuing/balance-types/2026-09-15|Adyen Issuing balance types, captured 2026-09-15]]
