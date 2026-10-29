---
title: "Gift cards API-only integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/api-only"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/api-only/2026-09-15.md"
tags: [adyen, gift-cards, api-only, stored-value, partial-payments]
---

## Overview

This Adyen API-only gift-card guide, last modified 2023-02-23 and captured 2026-09-15, adds gift-card payments to an **existing API-only integration** with a merchant-built payment form. It covers provider-specific setup and discovery, balance inquiry, full versus partial-order routing, payment request/result, and simulator/live onboarding. Its examples do not establish current provider coverage, merchant enablement, a protected card-data implementation or a completed live payment. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-gift-cards|gift-card overview]].

## Key takeaways

- **Provider and environment scope:** the merchant must build a separate integration for each gift-card provider and add each variant to be tested in Customer Area. The test simulator covers only a limited number of variants and approximates an end-to-end provider connection. Before live payments, the guide requires onboarding with a gift-card provider, adding the variant in live Customer Area, and contacting Adyen Support to add the card there. A test result or dated supported-card directory is not live entitlement (raw lines 28–44, 727–756; overview raw lines 19–21 and 67–115).
- **Discovery and form:** if using `/paymentMethods`, specify a country where the card is supported, a supported currency, and `channel: Web`; the examples **NL/EUR** are illustrative, not universal gift-card geography/currency. The response lists available cards with a display name, `brand` and `type: giftcard`. Render brand/logo choices and collect the selected card's number and CVC/security code in the merchant's form. These are sensitive payment details; the page does not describe complete storage or protection controls (raw lines 40–62, 64–75).
- **Balance check versus payment identity:** `/paymentMethods/balance` marks `paymentMethod.type` **as the selected brand** (for example `givex`), plus card number, CVC and merchant account required. Its response example returns `resultCode: Success` with a currency/value balance, which establishes a balance-check response in that example, not purchase authorization. By contrast, the later `/payments` table requires `paymentMethod.type: giftcard` **and a separate `paymentMethod.brand`**, plus number/CVC. Do not reuse the balance-check `type` shape unchanged for payment (raw lines 64–75, 326–356).
- **Partial-order boundary:** when balance is **at least the full payment amount**, continue to `/payments`. When balance is **less**, the guide says to create an `/orders` request so the gift card covers part and a different payment method covers the remainder. The partial-payment/order route is separate from this page's single gift-card `/payments` example; a successful balance inquiry does not by itself establish that the order was paid (raw lines 326–356; overview raw lines 23–25).
- **Payment outcome:** `/payments` returns a PSP reference, `resultCode` and merchant reference; the example is `Authorised`. Use `resultCode` to show the shopper a result, and receive the outcome asynchronously by webhook. The table distinguishes `Authorised`, `Cancelled`, `Error` and `Refused`; **manual capture requires a separate capture even after Authorised**. Provider-specific regulatory amount limits may apply; check with that provider rather than treating the examples as universal limits (raw lines 345–387, 708–725).
- **Tests and examples:** test card numbers and payment amount endings trigger simulated Authorised/Refused/Error outcomes, including invalid PIN or too many PIN attempts. These are simulator controls, not a real provider or live-card result. Sample card numbers/CVCs and server-library versions are examples, not credentials or SDK minima; the Go balance/payment snippets label v10.4.0 but import `/v9/` packages, so they are not verified copy-ready builds (raw lines 77–323, 389–705, 727–756).

## Detail locators

- Existing API-only integration, variant setup and provider onboarding: raw lines 15–44.
- Web discovery, brand/type response and merchant form: raw lines 46–62.
- Balance endpoint required fields, brand-as-type and example result: raw lines 64–75 and 326–339; language examples lines 77–323.
- Full balance versus `/orders` partial payment routing: raw lines 341–343.
- Payment endpoint's giftcard type plus brand, number/CVC and provider amount limits: raw lines 345–356; examples lines 358–705.
- Payment result/webhook and manual-capture boundary: raw lines 708–725.
- Simulator outcomes and live provider/variant/Support gate: raw lines 727–756.
- Method-level provider, funding and dated brand directory context: [[source-adyen-docs-payment-methods-gift-cards]] and its pinned raw lines 19–45, 67–115; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gift-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/api-only/2026-09-15|Gift cards API-only guide, captured 2026-09-15]]
