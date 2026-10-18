---
title: "Adyen Platforms process payments"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/process-payments"
raw_files:
  - "adyen/docs/platforms/process-payments/2026-09-15.md"
tags: [adyen, platforms, payments, split-transactions, balance-accounts]
---

## Overview

This Adyen for Platforms overview (last modified 2023-04-28; captured 2026-09-15) describes online and in-person payments processed on behalf of platform users, split instructions for booking funds/fees to user and platform liable balance accounts, and later settlement and payout orientation. It is not a merchant-of-record determination, a current payment-method entitlement, or evidence that an example payment, settlement or payout occurred. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Channel prerequisites:** Online processing first requires an Adyen online-payments integration and checkout UI for website/mobile acceptance. In-person processing first requires the platform POS app to integrate with Adyen terminals and Terminal API. The page does not give SDK/API versions or an end-to-end payment implementation. Payment-method names are broad categories, not a merchant-specific availability list.
- **Split ownership and precedence:** For each transaction, instructions can book funds across users' balance accounts and the platform's liable balance account and allocate fees/costs. The page says define split instructions in each online or in-person request, or in store-level split configuration profiles. Request instructions override profile instructions. If neither supplies split instructions, the whole transaction amount and fees are booked to the liable balance account. This default is a booking rule, not a statement of legal ownership or seller/payee identity.
- **Booking, settlement and payout:** The page says Adyen settles processed funds to platform balance accounts according to the defined splits, with settlement models and payout schedules routing funds to transfer instruments. Its two USD 100 example payments book USD 95/96 to user balance accounts, USD 5/4 commission to liable balance account and USD 2/1 fees from liable balance account, then illustrate USD 191 to the user's and USD 6 to the platform's transfer instrument. These are example amounts in one currency and not universal fee, currency-conversion, payout-timing or bank-receipt rules.
- **Event visibility:** The page points to Transfer and Transaction webhooks for payment-related events and statuses. A webhook status or diagram alone does not prove final bank receipt. This overview does not describe authorization/capture, refund, chargeback, partial/failure booking or payment-facilitator conditions; consult separately read flow-specific sources before asserting those behaviors.

## Detail locators

- Platform/user scope and online versus in-person integration prerequisites: pinned raw lines 15-31.
- Split instructions, request-over-profile precedence and liable-account default: pinned raw lines 33-39.
- Balance-account settlement and transfer-instrument orientation: pinned raw lines 41-45.
- Illustrative USD booking, fees, commission and payout schedule: pinned raw lines 47-79.
- Transfer/Transaction webhook navigation: pinned raw lines 81-83.

## Related

- [[adyen-platforms]] — platform payments and split-account concept with reciprocal source route.
- [[adyen-payments]] — broader Adyen payment-channel orientation, not the platform booking rule.

## Raw Sources

- [[raw/adyen/docs/platforms/process-payments/2026-09-15|Adyen Process payments, captured 2026-09-15]]
