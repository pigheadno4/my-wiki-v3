---
title: "Adyen Issuing merchant-to-balance-platform settlement"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/settle-funds"
raw_files:
  - "adyen/docs/issuing/settle-funds/2026-09-15.md"
tags: [adyen, issuing, settlement, balance-platform, acquiring]
---

## Overview

This 2026-09-15-captured Issuing-path guide describes how Adyen-acquired customer payments move from a store's merchant account to the balance platform. It is a merchant-account-to-configured-balance-account settlement route: pending merchant funds become available after the configured delay, fees are deducted, the remainder is grouped into payable batches, and Adyen describes an internal transfer for each batch. It does not describe an external-bank payout or guarantee completion for a particular merchant. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Payments arrive pending in the merchant account. The guide calls T+2 the default configured settlement delay, not a fixed rule; afterward funds become available in that merchant account. Adyen deducts payment fees before grouping the remaining funds into payable batches according to the configured settlement frequency, which can produce multiple batches per day (raw lines 19–25).
- The guide says a Settlement Details Report can be generated for each payable batch, including transactions, fees, refunds, chargebacks and other modifications. It then describes each batch as one internal transfer to the balance platform, settling into the balance account configured for that merchant account (raw lines 26–28). Report availability and a described transfer step do not independently prove a particular balance-account booking.
- The hotel illustration has Amsterdam EUR 200 and EUR 100 payments, plus Stockholm SEK 400; after EUR 15 and SEK 20 illustrated fees, the stated net batches are EUR 285 and SEK 380 for their respective configured balance accounts (raw lines 30–68). At raw line 48, the text instead calls the Stockholm merchant-account amount `EUR 400.00`, conflicting with the SEK payment, SEK fees and SEK net batch. Preserve this source currency error; do not interpret it as conversion evidence.

## Detail locators

- Pending merchant funds, configurable delay and fees: raw lines 19–25. Batch report, internal transfer and merchant-to-balance-account destination: raw lines 26–28.
- Two-branch, two-currency hotel example and inconsistent line-48 currency: raw lines 30–68.

## Related

- [[adyen-issuing]] — Issuing and balance-platform context.
- [[source-adyen-docs-issuing-add-manage-funds]] — related funding-route overview.

## Raw Sources

- [[raw/adyen/docs/issuing/settle-funds/2026-09-15|Settle funds, captured 2026-09-15]]
