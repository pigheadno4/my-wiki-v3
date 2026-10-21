---
title: "Adyen Marketplace split transactions between balance accounts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/split-transactions"
raw_files:
  - "adyen/docs/marketplaces/split-transactions/2026-09-15.md"
tags: [adyen, marketplaces, split-transactions, balance-accounts, payments]
---

## Overview

This 2024-modified Marketplace-route Adyen for Platforms guide, captured 2026-09-15, explains how transaction-specific split instructions book payment, capture and refund amounts and fees among user balance accounts and the marketplace liable balance account. It also points to chargeback booking logic. This is the modern balance-account model, not Classic `accountCode` splitting. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Supply split instructions in each relevant authorization, capture and refund request, or use an applicable split-configuration profile. If neither a profile nor API instructions are provided, the **whole transaction amount and fees** are booked to the marketplace's liable balance account (raw lines 19–21). A split instruction lacking an `account` also books that split amount to the liable balance account, subject to each split type's required fields (raw lines 96–118).
- The guide names `/payments` and `/sessions` for authorization, `/payments/{paymentPspReference}/amountUpdates` for authorization amount updates, `/payments/{paymentPspReference}/captures` for capture and `/payments/{paymentPspReference}/refunds` for refund splits (raw lines 23–37). Splitting at capture is possible only for payment methods supporting **separate captures** (raw line 31). These are request points for intended booking, not proof of authorization, capture, settlement or payout completion.
- For payment/refund API requests, use a `splits` array with an object per portion of the full transaction amount. A `BalanceAccount` split books to a user's balance account and the table marks `account`, `amount` and `reference` required; `Commission` books marketplace commission to the liable balance account and requires `amount`. Other types route individual or aggregate fees, VAT, conversion remainder, surcharge and user top-up funds, with their per-type required/recommended fields in the raw table (raw lines 69–81, 96–118). Do not assume every fee type has the same required fields or recipient.
- Potential chargeback booking is configured on the original authorization or capture request through `platformChargebackLogic`, distinct from payment/refund `splits`. It can allocate the disputed amount and chargeback fees (raw lines 62–67, 83–94). This describes a prospective booking instruction, not that a chargeback occurred.
- The document says funds can be split across any number of balance accounts within the marketplace and lists sale, commission, transaction fees, conversion remainder and top-up as payment portions, versus sale refund, refunded commission, refund fees and conversion remainder for refunds (raw lines 39–67). Account and liable destinations must be specified according to the split type; a sample transaction is not evidence that the intended balance accounts were credited or debited.

## Detail locators

- Need for booking instructions and whole-transaction liable fallback: raw lines 19–21. Endpoints and separate-capture condition: raw lines 23–37. Payment, refund and chargeback booking categories: raw lines 39–67.
- `splits` array and chargeback-logic placement: raw lines 69–94. Split type, per-type required fields and missing-account liable fallback: raw lines 96–118.

## Related

- [[adyen-platforms]] — Marketplace balance-account model.
- [[adyen-automatic-split-configuration]] — profile-based alternative and request precedence.
- [[source-adyen-docs-marketplaces-manage-liable-accounts]] — liable account destinations and failure fallback.
- [[adyen-classic-platforms]] — separate older account-code model.

## Raw Sources

- [[raw/adyen/docs/marketplaces/split-transactions/2026-09-15|Marketplace split transactions, captured 2026-09-15]]
