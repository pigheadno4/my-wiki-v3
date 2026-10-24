---
title: "Adyen Alipay HK Web Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/web-drop-in/2026-09-15.md"
tags: [adyen, alipayhk, web-drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15 guide describes **Alipay HK method-specific additions** to an existing **Web Drop-in** integration. It separates Sessions and Advanced server-side flows, each requiring existing **`action.type: redirect` handling** and Alipay HK method setup in Adyen Customer Area. The base integration guides own the full payment, redirect-return and outcome flow; this page does not demonstrate a completed redirect or successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The page requires an existing Sessions Web Drop-in integration using **Checkout API v68 or later**, existing redirect handling and Alipay HK added in Customer Area. It says no extra **Alipay HK-specific** `/sessions` parameters are needed. The v68 minimum appears in the Sessions tab and is not stated as an Advanced-flow minimum here. (raw lines 25–42)
- **Advanced:** The page requires an existing Advanced Web Drop-in integration with redirect handling and Customer Area setup. It says no extra **Alipay HK-specific** `/payments` parameters are needed. The Advanced integration hyperlink contains an unresolved encoded `{{getParameter('platform')}}` value; follow the intended Web/Advanced route rather than treating that URL as a verified literal link. (raw lines 70–80, 94–98)
- In either flow, importing individual Adyen Web methods for tree shaking is **optional**, and the guide's example includes `Redirect` alongside `AdyenCheckout` and `Dropin`. It does not specify a Web SDK minimum or claim that this is mandatory for all import patterns. (raw lines 44–54, 82–92)
- The page provides **TEST AlipayHK credentials** and points to test Customer Area payment-list status. Those are test fixtures and an observation route, not live enablement or payment finality. Before accepting LIVE AlipayHK payments, the page requires a **request for AlipayHK in live Customer Area**; it does not say that submission alone is approval or successful processing. (raw lines 56–68, 100–112)
- Redirect handling is listed as an existing-integration prerequisite, but this add-on page gives no shopper return/deep-link, webhook-finality, authorization, capture, settlement, or refund procedure. “No additional parameters” does not waive the underlying Sessions/Advanced integration's own requirements. (raw lines 19–23, 31–42, 76–98)

## Detail locators

- Sessions requirements and `/sessions` statement: raw lines 25–42.
- Sessions optional import and TEST/LIVE gates: raw lines 44–68.
- Advanced requirements, optional import and `/payments` statement: raw lines 70–98.
- Advanced TEST/LIVE gates: raw lines 100–112.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/web-drop-in/2026-09-15|Adyen Alipay HK Web Drop-in guide, 2026-09-15 snapshot]]
