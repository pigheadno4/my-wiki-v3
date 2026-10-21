---
title: "Adyen Marketplace split chargeback booking"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/split-transactions/split-chargebacks"
raw_files:
  - "adyen/docs/marketplaces/split-transactions/split-chargebacks/2026-09-15.md"
tags: [adyen, marketplaces, platforms, chargebacks, split-payments]
---

## Overview

This 2023-modified Marketplace guide captured 2026-09-15 explains how the **disputed amount** in an online-payment chargeback is booked among marketplace balance accounts. By default, Adyen debits the marketplace's liable balance account when an issuer starts a dispute after a customer reverses a user's payment. A successful defense or customer repayment produces a chargeback reversal credit to the liable account; a second chargeback debits it again if the issuer rejects the defense. The marketplace may instead configure user-account or split-ratio booking. This is balance-account chargeback allocation, not proof that a dispute was won, funds settled to a bank or a payout succeeded. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The page says an online-payment-capable marketplace has no special extra requirements to handle chargebacks. It may accept a chargeback for the user or ask for defense documents and upload them. The default disputed-amount debit, reversal credit and second-chargeback debit are all directed to the liable balance account unless booking logic is changed (raw lines 19–35).
- `platformChargebackLogic.behavior` has three choices: `deductFromLiableAccount`, `deductFromOneBalanceAccount` with required `targetAccount`, or `deductAccordingToSplitRatio` using the original payment/session `splits` ratio. `costAllocationAccount` separately selects where chargeback fees are booked; in the use cases, omitted fees default to the liable balance account. The full disputed amount or portions are allocated to balance accounts, so fee allocation is a separate decision from the disputed amount (raw lines 37–66, 80–92, 767–782, 1475–1503).
- Support configures a balance-platform default. Per-payment logic overrides that default, and logic in a capture request overrides logic in the payment request. The payment-level object can be sent with Checkout `/payments`, `/sessions` or `/payments/{paymentPspReference}/captures`; listen to `CHARGEBACK` for an occurrence. These request examples use TEST Checkout v72 and versioned SDK snippets; configuring a potential chargeback does not establish a live chargeback or booking (raw lines 45–68, 80–96).
- **Destination fallback:** Checkout validates split-instruction format but not the named balance accounts. Even a successful transaction can book somewhere other than the requested account. If the account is nonexistent or belongs to a closed account holder, the **full transaction and fees** book to the marketplace liable balance account; an internal transfer may then correct balances. A successful request is therefore not target-account booking proof (raw lines 70–74).
- For single-user-account allocation, the guide says the chargeback currency and amount need not match the original payment. For ratio allocation, it applies the original split **ratio**, not original amounts, to the disputed amount. Its worked example describes an original USD 100 split 70:20:10 and a USD 88 dispute, but parentheticals say EUR 88 while the displayed allocated lines say USD. Retain the 7:2:1 arithmetic, not the example's mixed-currency labeling as a reliable FX rule (raw lines 767–780, 1475–1503).
- For fund-movement tracking, acknowledge transfer and transaction webhooks per split item. `balancePlatform.transfer.created` at `received` and later `transfer.updated` at `authorised` precede debit booking; the example then shows `transfer.updated` status `chargeback` with `transactionId` and a `balancePlatform.transaction.created` status `booked`. The prose calls the cumulative array `event` while examples use `events`; example PaymentFee and Commission account IDs/transfer-event labels also disagree with adjacent sample payloads, so use them as illustrative rather than a canonical ledger (raw lines 2189–2207, 2222–2522, 2524–2837, 2839–3152). The Balance Platform Accounting Report carries chargeback fee type before transfer description (lines 3154–3156).

## Detail locators

- Chargeback, reversal and second-chargeback liable-account direction: raw lines 19–35. Behavior, fee target and precedence: lines 37–68. Invalid/closed target fallback: lines 70–74.
- TEST v72 liable-account example: lines 76–766. User-balance-account example and independent chargeback amount/currency: lines 767–1474. Original-ratio example including USD/EUR mismatch: lines 1475–2188.
- Split-grain webhook tracking and `event`/`events` discrepancy: lines 2189–2207; disputed-amount webhooks: 2209–2522; fees: 2524–2837; commission: 2839–3152. Report route: lines 3154–3160.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern Platforms model and Marketplace route.
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-chargebacks]] — separate Platforms-path guide to chargeback booking.
- [[source-adyen-docs-marketplaces]] — marketplace integration overview.
- [[adyen-classic-platforms]] — distinct legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/split-transactions/split-chargebacks/2026-09-15|Marketplace split chargebacks — 2026-09-15 snapshot]]
