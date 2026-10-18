---
title: "Split transactions between balance accounts | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/split-transactions"
raw_files:
  - "adyen/docs/platforms/online-payments/split-transactions/2026-09-15.md"
tags: [adyen, platforms, online-payments, split-transactions, balance-accounts]
---

## Overview

This 2024-last-modified [[adyen]] for Platforms overview, captured 2026-09-15, maps how online transaction amounts and fees are assigned to users' balance accounts and the platform's liable balance account. A store-linked automatic split configuration can supply instructions, while split instructions in an API request override that profile. If neither supplies instructions, the whole transaction amount and fees book to the liable balance account. These are booking rules; the page does not determine a legal seller, merchant of record, payee, payment outcome or bank payout. [[adyen-platforms]]

## Request timing and booking scope

- The overview routes per-transaction instructions to Checkout `/payments` or `/sessions` at authorization, `/payments/{paymentPspReference}/amountUpdates` for an authorization amount update, `/payments/{paymentPspReference}/captures` at capture, and `/payments/{paymentPspReference}/refunds` for refunds. Capture-time splitting is possible only for payment methods supporting separate captures. Potential chargeback booking logic is placed in `platformChargebackLogic` on an authorization or capture request, rather than in the payment/refund `splits` array. See raw lines 39–53 and 105–116.
- For payments, the page lists sale amount, platform commission, payment fees, currency-conversion remainder and user top-up as possible booking subjects; for refunds it lists returned sale amount, refunded commission, refund fees and conversion remainder; for chargebacks it lists disputed amount and chargeback fees. This is orientation to split subjects, not a promise that each product, payment method, fee or lifecycle operation is eligible in every account. See raw lines 55–81.
- Payment and refund requests use a `splits` array with one object per part of the full transaction amount. `type` identifies a split's purpose; the table at raw lines 118–140 distinguishes `BalanceAccount`, `Commission`, fee aggregates and granular fees, `VAT`, `Remainder`, `Surcharge` and `TopUp`, with type-specific required or recommended `account`, `amount` and `reference` fields. For a `BalanceAccount` split the table lists `account`, `amount` and `reference` as required. The page says an unspecified `account` routes a split to the liable balance account, but that general statement should not be read as making a required `BalanceAccount.account` optional or defining invalid-account behavior.

## Evidence and source boundaries

- This overview provides no webhook trace or executed transaction. Request instructions, profile settings and split-type tables do not prove authorization, capture, refund, chargeback, balance booking, payout or bank receipt. Specific authorization, capture, refund, chargeback, fee and automatic-configuration guides supply their own conditions and outcome evidence; do not infer invalid-account fallbacks, capability status, partial-operation behavior or fee allocation from this overview alone.
- **Pinned wording/navigation caveats:** the refund list calls the returned commission a “marketplace's commission” at raw line 72 even though the page frames the integration as a platform; that word does not establish a marketplace or merchant-of-record model. The payment/refund related-links list points “Split a payment at capture” to an in-person URL at raw line 102, while this page's Next steps link points to the online capture route at lines 148–150. Use the route appropriate to the online flow rather than treating the first link as online behavior evidence.

## Detail locators

- **Store profile, request override and liable-account default:** raw lines 19–30.
- **Authorization/amount-update/capture/refund endpoints and separate-capture condition:** raw lines 39–53.
- **Payment, refund and chargeback booking subjects:** raw lines 55–81.
- **`splits` object scope, API links and chargeback-logic route:** raw lines 83–116.
- **Split-type field table, account wording and remaining online-capture link:** raw lines 118–154.

## Related

- [[adyen-platforms]]
- [[adyen-automatic-split-configuration]] — store-linked profile context
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-payments-at-authorization]] — authorization-time conditions
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-payments-at-capture]] — online capture conditions
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-refunds]] — refund conditions
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-chargebacks]] — chargeback conditions
- [[source-adyen-docs-platforms-online-payments-transaction-fees]] — fee allocation detail

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/split-transactions/2026-09-15|Adyen Platforms online split-transactions overview — collected 2026-09-15]]
