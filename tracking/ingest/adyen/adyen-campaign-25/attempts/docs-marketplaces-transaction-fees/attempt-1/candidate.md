---
title: "Adyen Marketplaces: Transaction fees"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/transaction-fees"
raw_files:
  - "adyen/docs/marketplaces/transaction-fees/2026-09-15.md"
tags: [adyen, marketplaces, platforms, transaction-fees, split-payments]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Marketplaces guide explains how to book payment transaction fees, calculated after the payment request, to a marketplace user's balance account or the marketplace's liable balance account. It is fee-allocation and reconciliation guidance, not proof of a completed payment, capture, payout, or bank receipt. [[adyen-platforms]]

## Key takeaways

- The stated prerequisite is that the platform already processes payments; the page adds no further preparation for this fee feature. By default, payment-related transaction fees are deducted from the marketplace's **liable balance account**. Split instructions can instead book **Interchange**, **SchemeFee**, **AdyenMarkup**, or **AdyenCommission** to a user's balance account. Aggregated processing costs (including refused/cancelled payments and 3DS enrollment) and tiered-pricing discounts **cannot be passed to users in individual payment requests**. See [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15|raw lines 19–37]].
- `AcquiringFees` groups interchange and scheme fees; `AdyenFees` groups Adyen commission and markup; `PaymentFee` groups all transaction fees. More granular split instructions override the corresponding part of an aggregate, leaving other fee portions at the aggregate's target. The worked `AdyenMarkup`/user-directed `PaymentFee` example illustrates that precedence. See [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15|raw lines 39–93]].
- The guide recommends fee split instructions in payment or capture requests even when booking to liable for reconciliation. If no transaction-fee booking instruction is supplied, Adyen adds `PaymentFee` and books all transaction fees to the liable balance account. Its worked Checkout `/payments` or `/sessions` example places additional `AcquiringFees` and `AdyenFees` entries in `splits`; the field table marks `account`, `type`, and unique `reference` required, and `description` optional. The fee amounts are not known at request time. See [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15|raw lines 19, 53, 95–115]].
- For fee movement, the guide describes per-split Transfer created/updated and Transaction created webhooks, including received, authorised, captured, and booked stages, plus the Balance Platform Accounting Report's aggregate rows and granular Platform Payment columns. Webhook stages and test example payloads are not interchangeable with a real account debit or payout. See [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15|raw lines 808–824, 826–1444, 1446–1450]].

## Example conflicts and evidence boundary

- The prose/request describe a **EUR 80.00** payment split into EUR 75.00 user and EUR 5.00 marketplace commission, and the test `/v72/payments` request uses `EUR 8000`; its example authorization response instead shows `EUR 40000`. Treat response amount as an inconsistent illustration, not the result of that exact request (raw lines 97–102, 123–175, 780–805).
- The request/prose book `AdyenFees` to the **liable** balance account, but the Adyen-fee tab's introductory sentence says the **user** balance account. The subsequent transfer prose/payload returns to liable. The field-table `account` description also says user although the worked `AdyenFees` item targets liable. Do not infer a universal account destination from those conflicting examples (raw lines 99–115, 168–172, 1137–1167).
- The acquiring-fee captured transfer switches its `balanceAccount.id` to `BA...02` after `BA...01` in received/authorised and booked events. The Adyen-fee booked transaction uses a user account and a different transfer ID from its liable-account transfer, and repeats the acquiring-fee booked-transaction ID. These test payloads cannot be joined into one coherent ledger trace; use actual per-split events and report rows for reconciliation (raw lines 839–857, 1000–1011, 1097–1133, 1160–1167, 1384–1393, 1407–1439).

## Detail locators

- Fee types, aggregate hierarchy and override table: [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15|raw lines 25–93]].
- EUR request, test Checkout v72 sample, SDK versions and illustrative authorization response: [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15|raw lines 95–805]].
- Per-split webhooks, example inconsistencies, report treatment and default: [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15|raw lines 808–1450]].

## Related

- [[adyen-platforms]] — provider concept and Marketplace/Platforms route.
- [[source-adyen-docs-marketplaces-process-payments]] — online payments and balance-account split overview.
- [[source-adyen-docs-platforms-online-payments-transaction-fees]] — related Platforms transaction-fee guide; keep its scope and its own examples distinct.
- [[adyen]] — company context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15|Marketplace transaction fees (captured 2026-09-15)]]
