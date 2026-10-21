---
title: "Adyen Payout Service settlement to balance platform"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/settle-funds"
raw_files:
  - "adyen/docs/payouts/payout-service/settle-funds/2026-09-15.md"
tags: [adyen, payout-service, settlement, balance-platform]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service guide explains how payment proceeds move from merchant accounts into configured balance-platform accounts after fees. It covers merchant-to-platform settlement, within the broader [[adyen-financial-products]] Payout Service route, rather than an onward disbursement to a beneficiary bank (raw lines 17–28).

## Key takeaways

- **Availability before transfer:** Store payments first arrive pending in a merchant account. After its configured settlement delay (T+2 by default), funds become available there; Adyen then deducts payment fees (raw lines 23–24). T+2 is a documented default, not a promise for every configuration.
- **Batch and report grain:** Adyen groups the remaining amount into payable batches according to the configured settlement frequency, which can create multiple batches per day. A Settlement Details Report can be generated per batch and includes transactions, fees, refunds, chargebacks and other balance modifications (raw lines 25–26).
- **Destination and movement:** Each payable batch settles as one internal transfer to the balance platform, into the balance account configured for that merchant account (raw lines 27–28). This step is distinct from an external payout request or beneficiary-bank receipt.
- **Illustration and source mismatch:** The two-branch hotel example sends EUR 285 net from the EUR merchant account and SEK 380 net from the SEK merchant account to their respective configured balance accounts (raw lines 30–68). Its intermediate line says “EUR 400.00” becomes available in the SEK merchant account, although the guest payment, SEK fee and net batch are stated in SEK. Treat that as an unresolved currency inconsistency in the example, not a currency-conversion rule (raw lines 43, 48, 57–68).

## Detail locators

- Six-step pending → available → fees → payable batch/report → internal transfer → configured balance account flow: raw lines 21–28.
- Hotel branch currencies, customer payments and settlement-delay illustration: raw lines 30–48.
- Per-account fees, net batches and destination balance accounts: raw lines 50–68.

## Evidence boundary

This document describes the configured settlement flow and an illustrative calculation. It does not establish a particular merchant's configured delay or frequency, prove that an actual batch booked, or prove an onward payout or receipt by an external beneficiary. Keep merchant-account availability, the internal transfer into a platform balance account and any later payout as separate states. The example's SEK/EUR mismatch remains visible rather than silently repaired.

## Related

- [[adyen-financial-products]] — Payout Service product-family route.
- [[source-adyen-docs-payouts-payout-service]] — Payout Service landing and downstream guide navigation.
- [[source-adyen-docs-payouts-payout-service-getting-paid-on-demand-payouts]] — separate on-demand bank-transfer request and tracking.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/settle-funds/2026-09-15|Pinned Payout Service settlement guide, captured 2026-09-15]]
