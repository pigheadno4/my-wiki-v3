---
title: "Adyen Boleto Bancário for Android integration router"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/android"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/android/2026-09-15.md"
tags: [adyen, boleto-bancario, android, integration-router, online-payments]
---

## Overview

This 2026-09-15-captured Adyen page is a short Android integration router for Boleto Bancário. It links separate Drop-in and Components child guides and four main Android Sessions/Advanced integration guides. It does not provide Android method request fields, SDK versions, voucher status, test/live setup, or proof that a Boleto was paid. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Android choices:** The page describes Drop-in as an all-in-one UI route and Components as a `BoletoComponent` route. Its Components link text says the Component handles a “redirect to Boleto Bancário.” This is a navigation label, not enough to infer an `action.type: redirect` or a completed shopper payment; read the Android Component child guide for its actual action contract. [Raw: lines 19–27]
- **Main integration first:** It explicitly says to follow the main integration guides before adding Boleto Bancário, then links Android Drop-in and Components for both Sessions and Advanced flows. This router does not choose among those four combinations. [Raw: lines 29–36]
- **Method-level context:** The separately approved [[source-adyen-docs-payment-methods-boleto-bancario]] overview describes a BR/BRL voucher method and later offline shopper payment. Those claims belong to that overview; this Android page alone is navigation and does not establish a redirect or voucher implementation sequence. [Raw: lines 15–36]

## Detail locators

- Android Drop-in and Components child routes: pinned raw lines 19–27.
- Main-integration instruction and four base guide links: pinned raw lines 29–36.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-boleto-bancario]] — approved method overview for the Boleto voucher journey and capabilities.

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/android/2026-09-15|Boleto Bancário Android router, captured 2026-09-15]]
