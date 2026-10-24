---
title: "Adyen Alipay API-only integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/api-only"
raw_files:
  - "adyen/docs/payment-methods/alipay/api-only/2026-09-15.md"
tags: [adyen, alipay, api-only, web, online-payments]
---

## Overview

This [[adyen]] guide, modified and captured 2026-09-15, adds Alipay to an existing **Advanced API-only integration** whose linked main flow is Web. It covers `/paymentMethods` discovery filters, merchant-built selection UI, `/payments` and redirect handoff, then live-request and penny-test guidance. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alipay|Alipay overview]] for the separate outside-China merchant-processing boundary. This page's method response and examples do not prove current eligibility, final authorization, capture or settlement. See primary raw lines 15–29 and 44–97.

## Key takeaways

- Prerequisites are an existing Web-linked Advanced API-only integration, `action.type: redirect` handling, and Alipay added in Customer Area. The shopper chooses Alipay in the merchant-built UI; the existing integration handles the redirect. The page does not itself specify app deep links, a return callback, webhook/final-result handling or a Checkout API minimum. See raw lines 23–40 and 99–101.
- For `/paymentMethods`, the page lists eligible `countryCode` values **AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HK, HR, HU, ID, IS, IT, JP, KR, LT, LU, LV, MT, MY, NL, NO, NZ, PH, PL, PR, PT, RO, SE, SG, SI, SK, TH, TW, US, VN**, and `amount.currency` values **AUD, CAD, CHF, DKK, EUR, GBP, HKD, JPY, MYR, NOK, NZD, SEK, SGD, THB, USD** to include Alipay in the response. This is a source-dated discovery list, not approval for every country/currency pair or merchant. The TEST `/v72/paymentMethods` NL/EUR request and `alipay` response are examples, not a required API version or observed live availability. See raw lines 44–83.
- The page's **How it works** steps say the shopper enters details in the payment form and that the request includes extra item information; its specific **Build your payment form** section says no shopper information needs collecting, and its **/payments** section says no extra Alipay parameters are needed. These statements conflict. Keep the specific Alipay-only field guidance qualified; base Advanced request fields still come from the main flow, and the high-level steps do not establish required item fields. See raw lines 31–40 and 85–87.
- The curl example has `-X POST` without a continuation before the next `-d` line, so its shown shell command is not paste-ready. It also includes an `idempotency-key` as an example; this page does not say that header is an Alipay-specific requirement. See raw lines 53–70.
- The guide recommends live penny tests with an Alipay wallet/card and viewing payment details in **live Customer Area**. It says a live Customer Area request for Alipay is required before accepting live payments. This is provider configuration guidance; no actual account, wallet, card or financial operation is performed here, and the guide does not show a final webhook, capture or settlement. See raw lines 89–97.

## Detail locators

- **Advanced Web API-only prerequisites, redirect and high-level/form conflict:** raw lines 19–40.
- **Country/currency method-discovery list and versioned TEST samples:** raw lines 44–83.
- **No-extra-Alipay `/payments` fields and live setup:** raw lines 85–101.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay]]
- [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/api-only/2026-09-15|Alipay API-only — captured 2026-09-15]]
