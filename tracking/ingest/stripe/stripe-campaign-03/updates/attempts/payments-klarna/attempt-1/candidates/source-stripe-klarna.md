---
title: "Stripe: Klarna Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/klarna"
raw_files:
  - "stripe-payments-klarna-2026-11-07.md"
  - "stripe-klarna-2025.md"
tags: [stripe, bnpl, klarna, buy-now-pay-later, installments, subscriptions, connect, cross-border]
---

## Overview

Stripe's Klarna payment-method overview covers customer payment options, geographic and amount conditions, cross-border presentment, refunds, Connect, and country filtering. A customer is redirected to Klarna to choose an offered option and returns to the merchant site to complete the order. When a payment is accepted, the merchant receives the order amount minus fees in the Stripe account; Klarna collects from the customer and bears loss if that customer cannot repay. The page separately specifies **standard payout timing**, so the accepted-payment description is not an instant-payout or settlement promise. See [[stripe-klarna]], [[stripe-bnpl]], and [[stripe]].

## Key takeaways

- The 2026-11-07 capture lists 23 customer countries, 32 Stripe-account business countries and 13 presentment currencies (raw lines 15-101). These are dated documentation lists, not proof of a particular merchant or customer's eligibility. The same high-level lists appear in the 2026-05-06 capture (old raw lines 14-100).
- Klarna presents Pay in full, Pay later, Pay in 3 or 4, and Financing subject to customer location, currency, transaction amount, payment use case and Klarna's changeable geographic and cart ranges (new raw lines 135-143, 614-763). Financing may include interest and is subject to creditworthiness; a listed range does not establish approval (new raw lines 735-753).
- In the November country and all-country tables, Italy has **one-time Financing at 35-3,000 EUR**; the May Financing row omits Italy (new raw lines 452-468, 735-753; old raw lines 242-258). The November Pay in 3 EUR ceiling for France, Ireland, Italy and Spain is **3,000**, versus **1,500** in May (new raw lines 721-725; old raw lines 228-241). Read these as dated table changes, not guaranteed live options.
- Recurring use cases are documented, with country and plan restrictions. Setting `setup_future_usage` classifies a Klarna payment as recurring and limits visible options; otherwise eligible plans might not display on hosted, embedded or Elements payment pages (new raw lines 135-143). The May footnote described the parameter as making the payment no longer one-time and named Payment Method Messaging Element and Payment Element (old raw line 260). It does **not** make all recurring Klarna payments unavailable.
- The get-started section directs merchants to Klarna rules and gives B2B as an unsupported example. It points to Checkout hosted or embedded pages and Elements with PaymentIntents for integrations. Klarna on Stripe Terminal is identified only as a **private preview** with an access-request route (new raw lines 107-133); this does not establish preview access.

## Availability conflicts and limits

> [!warning] Contradiction in the 2026-11-07 capture
> Multiple individual country **Pay later** rows list short- or long-term subscriptions (for example Austria, Belgium and the UK: new raw lines 251-282, 403-415), but the same page's all-country footnote and limitations say **only Germany, Sweden and the United States** support Pay later for subscriptions and on-demand payments (new raw lines 755-775). The May footnote also gives only those three (old raw line 266). Do not treat the country rows as an established expansion of subscription eligibility; resolve this conflict before making a country-specific launch claim.

The November limitations also restrict US territories to Puerto Rico; exclude specified US states for Pay later, Pay in 4 and Financing; limit Pay in full to one-time payments in Australia, Norway and Poland; and limit Pay in 3 or 4 to one-time payments in Australia, New Zealand and Poland (new raw lines 755-777). The May footnote additionally named Finland in the last restriction, although Finland was absent from its Pay in 3 or 4 country row (old raw lines 207-241, 268). November's Finland country table has Pay in full, Pay later and Financing, not Pay in 3 or 4 (new raw lines 371-384); footnote removal alone does not establish Finnish installment availability.

## Cross-border, refunds and Connect

- The EEA, United Kingdom and Switzerland business rows allow customers in the EEA, UK or Switzerland with presentment in the **customer location currency**. The "other countries" row requires customer location to match the business location and uses the business location currency (new raw lines 779-794; old raw lines 272-288). This table is a documented rule, not account eligibility.
- Refunds can be made within 180 days after payment completion, usually take 5-7 business days but can take longer, and may be full or partial, including multiple partial refunds up to the original charge (new raw lines 796-803; old raw lines 290-297). For a partial refund **greater than** the remaining order balance, Klarna reduces the outstanding balance and returns the difference; for one **less than** the remaining balance, it reduces the balance and spreads refunds across remaining payments. A payment escalated to a dispute cannot be refunded.
- Connect platforms can use all charge types. Connected accounts with full Dashboard access, including Standard, may enable Klarna there; `klarna_payments` being `active` identifies enabled capability. Accounts without full Dashboard access, including Express and Custom, require a capability request (new raw lines 805-815; old raw lines 299-309).
- For dynamic payment methods in Payment Element or Checkout Session, the method displays only if the customer country is supported. Stripe determines that country first from the two-letter shipping-address country, then geocoded client IP (new raw lines 817-824; old raw lines 311-318).

## Detail locators

- November customer/business locations, currencies, product and payment properties: new raw lines 15-101.
- November region/country selectors and per-country option/use-case/amount tables: new raw lines 135-614; all-country table and footnotes: new raw lines 614-763.
- May all-country option/use-case/amount table and footnotes: old raw lines 121-270.
- Cross-border, refunds, Connect and country filtering: new raw lines 779-824; old raw lines 272-318.

## Raw Sources

- [[raw/stripe-payments-klarna-2026-11-07|Klarna payments — 2026-11-07 capture]]
- [[raw/stripe-klarna-2025|Klarna payments — 2026-05-06 capture (historical filename)]]
