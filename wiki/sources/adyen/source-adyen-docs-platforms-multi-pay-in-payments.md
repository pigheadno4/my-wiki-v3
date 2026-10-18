---
title: "Adyen Platforms multi pay-in allocation of third-party payments"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/multi-pay-in/payments"
raw_files:
  - "adyen/docs/platforms/multi-pay-in/payments/2026-09-15.md"
tags: [adyen, platforms, multi-pay-in, payments, split-payments, reconciliation]
---

## Overview

Adyen's multi pay-in guide describes allocating payments **processed by a third-party pay-in partner** after their funds are collected in a multi pay-in account, using separate split instructions to credit user and platform balance accounts. It is a distinct allocation route from an ordinary Adyen-acquired pay-in; the guide does not establish the external PSP's payment result, seller/merchant-of-record identity, legal ownership of funds, or a completed transfer. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Prerequisites are Checkout API credentials and subscription to Transfer and/or Transaction webhooks. Adyen says each individual payment must be allocated to balance accounts within 24 hours from settlement in the multi pay-in account; the page frames this as a regulatory-compliance limitation. The guide states no region list or partial-failure/atomicity rule, so do not infer either. See **Requirements**, raw lines 27–36.
- Make one POST `/payments` for **each individual third-party payment**. Its required top-level fields include `amount`, `paymentMethod.type=multi_payin`, `additionalData.tokenDataType=MultiPayIn`, `additionalData.BalancePlatform.balanceAccount` identifying the multi pay-in account, `merchantAccount`, `reference`, and `splits`. The request `reference` returns as `merchantReference`; `resultCode: Authorised` in the test example is not proof of downstream balance booking or bank receipt. See raw lines 38–52, 79–128, and 407–425.
- Each split specifies a target and amount according to its `type`. `BalanceAccount` allocates to a user's or platform's chosen balance account; `Commission` books platform commission to the liable balance account and does not require an `account` field. `AdyenMarkup`, `AdyenCommission`, `PaymentFee`, and `AdyenFees` are fee-booking types. The split `reference` is required for `BalanceAccount` and needed for refund/reconciliation. Distinguish the source multi pay-in BA from destination user BA and platform liable BA. See raw lines 54–67.
- Adyen recommends explicit transaction-fee splits. If no fee-booking instructions are supplied, it says **all transaction fees default to the platform liable balance account**. The USD 400 example allocates USD 396 to the user, USD 4 commission to the liable account, and fee deduction from liable; these are example amounts, not universal fee rates or final balances. See raw lines 69–75, 79–128, and 1361–1373.
- Webhooks and accounting report rows represent separate legs: outgoing `internal/internalTransfer` from multi pay-in, incoming `platformPayment/capture/BalanceAccount` to the user, incoming `Commission` to liable, and outgoing fee capture from the selected or default liable account. Transfer `received`, `authorised`, and `booked`/`captured` stages and a later Transaction webhook should be checked for the relevant leg; an authorization response or one leg does not prove every leg completed. See raw lines 427–450, 454–1036, 1038–1360, and 1361–1667.
- The 2024 test examples contain internal inconsistencies: the user-credit captured transfer shows balance-account suffix `00002` although the request, preceding user-credit events, and booked transaction show `00001`; the commission “Transaction booked” sample shows `-400` despite the commission-credit narrative and transfer samples showing a positive 400. Preserve exact live event IDs, account IDs, signs, currencies, and timestamps in actual reconciliation; do not use these sample values as operational proof. See raw lines 108, 767–769, 918–920, 1026–1029, 1038–1051, and 1320–1334.

## Detail locators

- **Allocation request and sample response:** raw lines 38–426. Language-library snippets use pinned versions and mostly test environments; live examples mention `liveEndpointUrlPrefix` (raw lines 130–405). They are examples, not claims of tested integration or current API version.
- **Fund movements:** raw lines 427–1667, with outgoing multi pay-in debit (438–731), user credit (732–1036), platform commission (1038–1360), and fee debit (1361–1667). Match `category`, `direction`, `type`, `platformPaymentType`, references and transaction IDs to the leg before interpreting `received`, `authorised`, `booked`, or `captured`.
- **Reports and reconciliation:** Balance Platform Accounting Report includes multi pay-in, liable, and user balance-account changes. Its excerpt has booking/value dates, time zones, currencies, amounts, statuses and separate reference fields; it is an illustrative report excerpt, not bank settlement evidence. See raw lines 1668–1688.
- **Pay out:** after settlement into the user's balance account, the guide routes to the already configured payout schedule or an on-demand payout. It does not show payout initiation or bank arrival for a given payment. See raw lines 1689–1691.
- **Refund navigation:** linked next-step guide is separate, unread behavioral authority. See raw lines 1693–1697.

## Related

- [[adyen-platforms]] — Adyen for Platforms context.
- [[adyen-reporting]] — report navigation; the exact multi pay-in report excerpt remains in this raw.
- [[source-adyen-docs-platforms-manage-liable-accounts]] — liable-balance account context.

## Raw Sources

- [[raw/adyen/docs/platforms/multi-pay-in/payments/2026-09-15|Adyen Allocate third-party payments, fetched 2026-09-15]]
