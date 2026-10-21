---
title: "Book an FX refund remainder to a Marketplace platform"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/currency-conversion/refunds/your-platform"
raw_files:
  - "adyen/docs/marketplaces/currency-conversion/refunds/your-platform/2026-09-15.md"
tags: [adyen, marketplaces, currency-conversion, refunds]
---

## Overview

This pinned Marketplace guide describes refunding a captured, currency-converted online payment while routing the refund remainder to the **platform's liable balance account**. The customer originally paid in the processing currency, while the user received the settlement currency. The guide is marked **limited availability / pilot** and says its process may change; it does not establish current eligibility. See [[adyen]] and [[adyen-currencies-and-fx]].

## Key takeaways

- In the example, the customer paid **PLN 201.74** for goods worth **CZK 1000.00** to the user. The refund uses those original amounts; the stated intent is to credit the customer the amount originally paid, debit the user the amount originally received, and book the FX remainder to the platform's liable balance account (raw lines 24–30, 46–51, 59–62).
- Prerequisites are an Adyen online payments integration and Checkout UI, Checkout API credentials, standard webhook handling with transfer or transaction webhooks, the listed account-holder capabilities, Support-configured merchant currencies, and a **captured** payment before initiating a refund (raw lines 32–44).
- POST `/payments/{paymentPspReference}/refunds` with original processing-currency `amount` (**PLN 201.74**) and original settlement-currency `splits.amount` (**CZK 1000.00**) directed to the user's balance account. Add a `Remainder` split with `account` set to the **platform liable balance account ID**; no remainder amount is specified. The curl is a Checkout v72 TEST example (raw lines 53–99).
- **Source wording conflict:** raw line 26 says “book the remainder amount to the customer,” but the title, line 24, line 30, procedure, and examples assign it to the platform's liable balance account. Follow the explicit split destination when interpreting this dated guide; do not infer a separate customer-remainder allocation (raw lines 15–30, 55–99).
- The illustrative response has `status: received`. It shows request receipt and splits, not a completed refund, customer credit, final FX booking, settlement, or bank payout (raw lines 502–536). The guide does not provide a completed-outcome example.

## Detail locators

- Pilot warning, economic actors, prerequisites and flow: raw lines 15–51.
- Checkout request fields and TEST examples: raw lines 53–500.
- `received` example response: raw lines 502–536.

## Related

- [[adyen]]
- [[adyen-currencies-and-fx]]
- [[adyen-platforms]]
- [[source-adyen-docs-marketplaces-currency-conversion-refunds-your-user]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/currency-conversion/refunds/your-platform/2026-09-15|Pinned FX refund guide]]
