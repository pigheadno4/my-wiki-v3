---
title: "Adyen NaverPay Web Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/naverpay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/naverpay/web-drop-in/2026-09-15.md"
tags: [adyen, naverpay, web, drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen guide describes **NaverPay-specific additions** to an existing **Web Drop-in** integration, separately for Sessions and Advanced server-side flows. It points to the main integration guides for the underlying payment flow. The dated page does not establish current merchant eligibility or a successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The listed prerequisites are an existing Sessions Web Drop-in integration, **Checkout API v68 or later**, `action.type: redirect` handling, and NaverPay added in Customer Area. The page says no NaverPay-specific extra `/sessions` parameters are needed. It optionally shows importing `Redirect` for tree shaking when importing individual Adyen Web methods. (raw lines 25–54)
- **Advanced:** The listed prerequisites are an existing Advanced Web Drop-in integration, `action.type: redirect` handling, and NaverPay added in Customer Area. The page says no NaverPay-specific extra `/payments` parameters are needed and optionally shows the same `Redirect` import. The Advanced table states no separate Checkout API minimum; do not transfer the Sessions-only v68 requirement to that section. Its **Integration type** link has an unresolved encoded `getParameter('platform')` template in the `platform` query value; neighboring redirect and import links use `platform=Web`. Follow the Web-qualified links or main guide directly rather than treating the templated URL as a resolved Web link. (raw lines 62–90, especially 70–71 and 78)
- **Both flows:** The page states there is **no NaverPay test environment** and **recommends** testing in the live environment with real details and small amounts. This is a recommendation involving actual live financial operations, not a TEST fixture, merchant approval, or evidence that a transaction was run. No live test was performed for this ingestion. (raw lines 56–60, 92–96)
- The no-extra-parameters statements are NaverPay-specific and do not waive the base Drop-in integration's own request requirements. This page has no shopper-return, webhook-finality, authorization, capture, settlement or refund procedure or result; redirect readiness alone does not prove a payment outcome. (raw lines 19–23, 25–96)

## Detail locators

- Sessions requirements, `/sessions` and optional import: raw lines 25–54.
- Sessions live-test recommendation: raw lines 56–60.
- Advanced requirements, optional import and `/payments`: raw lines 62–90.
- Advanced live-test recommendation: raw lines 92–96.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-naverpay]]
- [[source-adyen-docs-payment-methods-naverpay-web-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/naverpay/web-drop-in/2026-09-15|Adyen NaverPay Web Drop-in guide, 2026-09-15 snapshot]]
