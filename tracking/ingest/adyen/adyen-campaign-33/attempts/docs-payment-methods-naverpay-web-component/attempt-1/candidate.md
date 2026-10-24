---
title: "Adyen NaverPay Web Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/naverpay/web-component"
raw_files:
  - "adyen/docs/payment-methods/naverpay/web-component/2026-09-15.md"
tags: [adyen, naverpay, web-components, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen guide adds **NaverPay** to an existing **Web Components** integration using the `Redirect` Component. It distinguishes Sessions and Advanced server-side flows and covers only NaverPay-specific additions; the linked base guides own complete payment and return/outcome handling. The dated text does not establish current merchant enablement or a successful redirect or payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** Existing Sessions Web Components, **Checkout API v68 or later**, `action.type: redirect` handling, and NaverPay added in Customer Area are listed. The page says no NaverPay-specific extra `/sessions` parameters or additional configuration are needed. It directs the Web import to include `Redirect` and initializes the method with that class. (raw lines 25–71)
- **Advanced:** Existing Advanced Web Components, redirect handling and Customer Area method setup are listed. Import `Redirect`, initialize with that class, and add no NaverPay-specific extra `/payments` parameters. The Advanced tab states no separate Checkout API minimum and has no no-extra-configuration sentence; do not transfer the Sessions-only v68 or configuration statement to this tab. (raw lines 78–116)
- Both initialization snippets show `new Redirect(checkout, { type:kcp_naverpay })`. Because `kcp_naverpay` is unquoted and no variable declaration appears in the page, the snippet is not self-contained executable code. The raw example can identify the intended method string but cannot prove a working mount, shopper handoff or returned result. (raw lines 64–72, 102–110)
- Both tabs state **no NaverPay test environment** and **recommend** testing with real details and small amounts in the live environment. This is advice for actual live financial operations, not a TEST fixture, approval proof, or evidence that such a transaction occurred. No provider/account operation or live test was performed for this ingestion. (raw lines 74–76, 118–120)
- The guide describes a redirect prerequisite but no return/deep-link, webhook-finality, authorization, capture, settlement or refund steps. “No additional parameters” is NaverPay-specific and does not waive the base Sessions/Advanced integration's own requirements. (raw lines 19–23, 31–42, 82–120)

## Detail locators

- Sessions prerequisites, request/configuration and `Redirect` initialization: raw lines 25–72.
- Sessions no-test-environment and live-test recommendation: raw lines 74–76.
- Advanced prerequisites, import, initialization and `/payments` statement: raw lines 78–116.
- Advanced no-test-environment and live-test recommendation: raw lines 118–120.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-naverpay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/naverpay/web-component/2026-09-15|Adyen NaverPay Web Component guide, 2026-09-15 snapshot]]
