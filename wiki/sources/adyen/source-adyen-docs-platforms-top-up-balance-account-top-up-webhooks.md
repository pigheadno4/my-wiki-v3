---
title: "Balance-account top-up webhooks | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/top-up-balance-account/top-up-webhooks"
raw_files:
  - "adyen/docs/platforms/top-up-balance-account/top-up-webhooks/2026-09-15.md"
tags: [adyen, platforms, top-ups, webhooks, balance-accounts, reconciliation]
---

## Overview

This [[adyen]] for Platforms page maps **scheduled and on-demand balance-account top-ups** to Standard, Transfer and Transaction webhooks. It distinguishes receipt and authorization of an incoming request from a captured transfer and a booked balance-account transaction, and shows a separate fee leg for an on-demand payment. It is webhook interpretation guidance, not a mandate, funding-source setup, successful external debit, payout, bank receipt, or guarantee that a booked credit cannot later be disputed or returned. [[adyen-platforms]]

## Key takeaways

- **Subscriptions and trigger.** A server must be able to receive and accept the subscribed Standard, Transfer and Transaction webhooks. When a top-up request triggers a **direct debit or payment authorization**, the Standard `AUTHORISATION` webhook reports the merchant-account payment authorization; Transfer webhooks describe balance-account movements. The page states webhooks also inform failure, but supplies no concrete rejected/returned event sequence or finality rule in this snapshot. A Standard authorization by itself does not prove a user balance-account credit. [Raw: Types of webhooks and Requirements, lines 19–36]
- **Scheduled top-up leg.** A scheduled pull-sweep example credits a user's **first** balance account when a threshold is crossed. Its Transfer webhook is `category: platformPayment`, `direction: incoming`, `type: capture`: `balancePlatform.transfer.created` has `status: received`, then `.updated` has `authorised`, then `captured` with a `transactionId` when funds are credited. A `balancePlatform.transaction.created` record has `status: booked` for the corresponding balance-account credit. The EUR 5,000 trigger and EUR 1,000 sweep are examples, not universal limits or proof of an actual debit/credit. [Raw: Scheduled top-ups, lines 38–53, 55–57, 123–125, 205–338]
- **On-demand top-up leg.** The on-demand example uses a payment request with a `TopUp` split and credits EUR 1,000 to the user's first balance account. Its incoming transfer uses `category: topUp`, `direction: incoming`, `type: capture`, and `categoryData.platformPaymentType: TopUp`; it progresses `received` → `authorised` → `captured` with a transaction ID, followed by a `booked` Transaction webhook. Capture references, payment references, transfer ID, transaction ID, balance-account ID, environment and currency must be matched on the relevant leg; sample IDs and timestamps are illustrative. [Raw: On-demand top-ups > Top-up amount, lines 341–363, 365–664]
- **Separate fee leg and signs.** The same on-demand example deducts EUR 3.44 from the user's **second** balance account for transaction fees. Its fee Transfer leg is `category: platformPayment`, `direction: outgoing`, `type: capture`, `platformPaymentType: PaymentFee`. The transfer's `amount.value` is positive 344 minor units, while its stage mutations carry both positive and negative signs and the final balance movement is a 344-unit debit; the booked Transaction sample uses `amount.value: -344`. Keep the fee transfer and top-up credit separate when reconciling. [Raw: Transaction fees, lines 666–977]
- **Sample conflicts and evidence limit.** In the fee example, the outgoing transfer names the **second** balance account, but its final booked Transaction example names the **first**; that fee transaction also reuses the top-up-credit transaction ID and shows a value date before the sample creation date. Do not use these example IDs, account assignment or dates to infer a real booked fee. The page describes credited balance-account funds, not beneficiary bank receipt or external direct-debit irrevocability; it does not supply return/reversal handling. [Raw: lines 841–977; compare top-up-credit Transaction lines 629–664]

## Detail locators

- Raw `Types of webhooks` and `Requirements` (lines 19–36): Standard authorization versus balance-platform event channels and subscriptions.
- Raw `Scheduled top-ups` (lines 38–339): incoming platformPayment/capture leg, threshold example, received/authorised/captured transfer events and booked Transaction record.
- Raw `On-demand top-ups` > `Top-up amount` (lines 341–664): payment/split grain, incoming TopUp leg, references and booked credit.
- Raw `On-demand top-ups` > `Transaction fees` (lines 666–978): separate outgoing PaymentFee leg, signs and inconsistent final booked sample.

## Related

- [[adyen-platforms]] — platform/user balance-account context
- [[source-adyen-docs-platforms-top-up-balance-account-on-demand-top-ups]] — separate top-up request and funding guidance
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — separate accounting-report route

## Raw Sources

- [[raw/adyen/docs/platforms/top-up-balance-account/top-up-webhooks/2026-09-15|Adyen Platforms top-up webhooks — collected 2026-09-15]]
