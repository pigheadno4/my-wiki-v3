---
title: "Process online payments for Adyen for Platforms"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments"
raw_files:
  - "adyen/docs/platforms/online-payments/2026-09-15.md"
tags: [adyen, platforms, online-payments, split-payments, balance-accounts]
---

## Overview

This Adyen for Platforms online-payments overview, last modified 2023-04-28 and captured 2026-09-15, explains how a platform processes online transactions on behalf of users and directs payment amounts, commissions, fees and costs between user balance accounts and the platform's liable balance account. It gives prerequisites, split-instruction precedence and an illustrative flow from customer payment through booking, settlement and payout. It does not establish a specific merchant of record, legal fund owner, successful authorization, completed settlement or actual bank receipt.

## Key takeaways

- The stated prerequisites are an Adyen online-payments integration and checkout UI; Checkout API and Transfers API credentials; a server able to receive standard webhooks, with subscription to transfer and/or transaction webhooks; and account holders with `receivePayments`, `receiveFromPlatformPayments` and `sendToTransferInstrument` capabilities. If `receiveFromPlatformPayments` is not in a valid state, funds cannot be allocated to that account holder's balance account and the full amount is booked to the platform's liable balance account. Credential possession or a capability name alone does not prove a valid grant.
- For the online-payments integration the page offers server-side Sessions flow (one Checkout API `/sessions` request) and Advanced flow (`/paymentMethods`, `/payments`, `/payments/details` requests). Sessions is the recommended default for most integrations; Advanced supports more use cases. The page does not set a specific Checkout API version or payment-method entitlement.
- The platform must direct funds and fees to the intended balance accounts. It can define automatic instructions with a store split-configuration profile or include split instructions per API request. Request-level instructions override profile instructions. If neither is supplied, the whole transaction amount and fees are booked to the liable balance account. A split instruction is not itself evidence of final booking or payout.
- The diagram's USD 400 payment, USD 396 user allocation, USD 4 platform commission, USD 2 fee deducted from the liable balance account and later USD 396/USD 2 payouts are one example. They are not universal fees, currencies, split ratios or guaranteed lifecycle outcomes. Booking, settlement and payout are separate stages. The page links detailed manual-split and automatic-profile guides; their behavior is not imported here.
- The captured page does not prescribe test/live activation steps or describe authorization, capture, refund or chargeback state transitions. Later payment and webhook records must establish any particular outcome.

## Detail locators

- `## Requirements`: Checkout integration/UI, credentials, webhook, capability and Sessions/Advanced prerequisites.
- `## Split transactions`: profile versus request-level instructions, precedence and missing-instruction fallback.
- `## Flow of funds`: illustrative USD 400 booking, settlement and payout sequence.
- `## Next steps`: manual and automatic split guide links.

## Related

- [[adyen-platforms]] — platform-specific integration and source route.
- [[adyen-online-payments]] — general online checkout integration context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/2026-09-15|Adyen process online payments for Platforms (fetched 2026-09-15)]]
