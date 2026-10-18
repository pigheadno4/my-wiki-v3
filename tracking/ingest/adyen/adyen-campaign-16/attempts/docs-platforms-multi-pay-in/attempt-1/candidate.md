---
title: "Multi pay-in overview | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/multi-pay-in"
raw_files:
  - "adyen/docs/platforms/multi-pay-in/2026-09-15.md"
tags: [adyen, platforms, multi-pay-in, third-party-payments, balance-accounts, refunds]
---

## Overview

This [[adyen]] for Platforms page introduces **multi pay-in**, a service that brings Adyen-acquired and third-party pay-in-partner volume into one Adyen balance-platform environment. Third-party payment proceeds first enter a dedicated multi pay-in account and are then allocated to user and platform liable balance accounts. The page describes a product flow, not proof that a particular partner, region, currency, account or payment is enabled, settled, booked or paid out. See [[adyen-multi-pay-in]] and [[adyen-platforms]].

## Key takeaways

- **Prerequisites and limit.** The guide requires an Adyen for Platforms **online payments** integration, credentials for **Checkout API and Transfers API**, Transfer and/or Transaction webhook subscription, and account-holder `sendToBalanceAccount` and `receiveFromBalanceAccount` capabilities. Multi pay-in **does not support separate authorization and capture**. These are stated requirements, not evidence that any account currently has the capabilities or that a third-party provider supports a proposed flow. [Raw: Requirements, lines 21–34]
- **Account identity and time boundary.** Adyen says it creates a multi pay-in account in the balance platform when the service is requested, one per pay-in partner, to receive that partner's payouts. It says this account is legally held by Adyen solely for the users' benefit while their funds await allocation. The platform must allocate funds received there to balance accounts within **24 hours** for the stated regulatory reason. This source does not specify a region/currency availability list or prove legal ownership, Merchant-of-Record status, or the destination of a particular transaction. [Raw: How it works and 1. Receive funds, lines 36–50]
- **Allocate third-party payments.** After funds reach the source multi pay-in account, the platform makes Checkout POST `/payments` requests with split instructions to allocate each payment to a user's balance account and, where applicable, its own liable balance account. With no split instructions, the page says **all funds and fees book to the liable balance account**. The diagram illustrates a user sale credit, platform commission, partner-deducted processing fees and balance-platform payouts; it is an example, not a universal fee allocation or completed funds movement. The linked allocation guide supplies per-payment request and webhook details. [Raw: 2. Allocate payments, lines 52–77]
- **Refund responsibility.** A partial or full third-party-payment refund can use multi pay-in, but the process varies by partner. The page's general sequence has the **pay-in partner transfer money back to the customer's payment method** and withhold that amount from a later payout batch; the platform then requests an Adyen Checkout refund to debit specified balance accounts and move the offset to the multi pay-in account. An Adyen debit or internal offset alone does not prove the partner returned funds to the customer. The refund diagram mixes EUR 98/EUR 2 balance deductions with a **USD 100** full-refund transfer; do not infer a conversion rate or a validated currency-consistent refund from it. [Raw: 3. Refund payments, lines 79–104]

## Detail locators

- Raw `Requirements` (lines 21–34): online-channel/API/webhook/capability prerequisites and separate-authorisation/capture limitation.
- Raw `How it works` and `1. Receive funds` (lines 36–50): pay-in partner, source account, Adyen-held-for-user-benefit wording and 24-hour allocation.
- Raw `2. Allocate payments` (lines 52–77): Checkout allocation, split fallback and illustrative diagram; deeper request and webhook behavior is in the linked allocation source.
- Raw `3. Refund payments` (lines 79–104): partner-owned customer return, Adyen debit/offset sequence and inconsistent example currencies.
- Raw `Next steps` (lines 106–126): separate receive-funds, top-up, allocation and refund navigation; these links do not by themselves prove behavior or outcomes.

## Related

- [[adyen-multi-pay-in]] — focused service concept
- [[adyen-platforms]] — platform/user and balance-account context
- [[source-adyen-docs-platforms-multi-pay-in-payments]] — detailed allocation route
- [[source-adyen-docs-platforms-multi-pay-in-refunds]] — detailed refund route
- [[source-adyen-docs-platforms-multi-pay-in-top-up-multi-pay-in]] — internal top-up route

## Raw Sources

- [[raw/adyen/docs/platforms/multi-pay-in/2026-09-15|Adyen multi pay-in overview — collected 2026-09-15]]
