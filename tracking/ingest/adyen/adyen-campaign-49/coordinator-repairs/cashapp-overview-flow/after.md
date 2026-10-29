---
title: "Adyen Cash App Pay payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/2026-09-15.md"
tags: [adyen, cash-app-pay, us, usd, wallet]
---

## Overview

This Adyen Docs Cash App Pay overview was last modified **2023-11-08** and captured **2026-09-15**. It describes a **US digital wallet** funded from Cash App balance or a linked credit card, debit card, or bank account. It gives a US/USD capability matrix, conditional authorization-adjustment rules, chargeback timing, and Web/iOS/Android/API-only routes. Cash App Pay is a distinct method from Cash App Afterpay; this snapshot does not establish current merchant eligibility or a successful transaction. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The matrix classifies Cash App Pay as a **direct wallet** for **US/USD**. It marks recurring, refunds, partial refunds, multiple partial refunds, separate captures, partial captures, and chargebacks available; **multiple partial captures** are crossed. These are method-overview capability marks, not an integration recipe or merchant-specific feature entitlement. See raw lines 23–27.
- When the final amount increases after initial authorization, the page says an **incremental increase** can be made on the existing transaction for one consolidated capture. Cash App Pay supports **increase only**, requires **auto-capture disabled/manual capture**, and supports **synchronous rather than asynchronous** adjustment. Access requires **manual approval from Cash App via Adyen**. Do not present authorization adjustment as enabled by default, a decrease, or an asynchronously confirmed operation. See raw lines 29–38.
- Shoppers can initiate a chargeback directly with Cash App Pay up to **120 days after the payment, cancellation, or expected receipt of goods or services**. On a dispute the funds are charged back; the merchant has **13 days to defend**. The page says no response within 13 days loses the dispute in the shopper's favor, while a timely successful defense returns the funds. These are this historical page's stated deadlines, not current legal advice. See raw lines 40–44.
- The page routes to prebuilt UI guides for Web, iOS and Android, and an API-only route for a merchant-built website or mobile UI. Follow those child guides for request fields and flow behavior. See raw lines 46–70.

> [!warning] Contradiction — overview and API-only flow labels
> This captured overview calls the payment flow **Direct** (raw lines 25–27), while [[source-adyen-docs-payment-methods-cash-app-pay-api-only|the API-only guide]] explicitly uses `paymentMethod.subtype: redirect` and a returned redirect action (child raw lines 47–53, 374–388). Retain both labels; the method-level overview does not eliminate the child integration's redirect or result-handling requirements. Neither label proves a completed payment.

## Detail locators

- Method identity, funding sources and capability matrix: raw lines 23–27.
- Authorization-adjustment conditions and approval: raw lines 29–38.
- Chargeback initiation and defense windows: raw lines 40–44.
- Web/iOS/Android/API-only integration routes: raw lines 46–70.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/2026-09-15|Fully read Cash App Pay overview raw]]
