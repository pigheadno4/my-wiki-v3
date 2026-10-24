---
title: "Boost Wallet Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/web-component"
raw_files:
  - "adyen/docs/payment-methods/boost/web-component/2026-09-15.md"
tags: [adyen, boost, wallet, web, components, redirect]
---

## Overview

This 2026-09-15 Adyen page adds Boost Wallet to an existing Web Components integration. It provides separate Sessions and Advanced flow instructions centered on the `Redirect` Component. It is a method-specific add-on, not a standalone checkout guide or evidence of a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites:** The existing integration must use Web Components Sessions flow, Checkout API v68 or later, and redirect handling for `action.type: redirect`; Boost Wallet must be added in Customer Area. The page says no extra `/sessions` parameters or Boost-specific configuration are needed. (raw lines 25–42, 56–66)
- **Advanced prerequisites:** The existing Web Components Advanced flow must handle the redirect action and have Boost Wallet added in Customer Area. The guide says no extra `/payments` parameters are needed; it does not state a Checkout API minimum for this flow. (raw lines 78–86, 100–116)
- **Client component and example defect:** Both flows import `Redirect` from `@adyen/adyen-web` and say to initialize Boost Wallet with that class. The example `new Redirect(checkout, { type:molpay_boost })` also uses `NoneComponent` and `#None-container` placeholders, and `molpay_boost` is not quoted in the shown JavaScript. Treat this as a source snippet defect, not a verified runnable integration. (raw lines 44–72, 88–110)
- **Environment boundary:** The guide states Boost Wallet has no test environment and calls for penny tests in LIVE. This is historical documentation guidance, not authorization to run a live transaction or proof of present availability, payment success, capture or settlement. (raw lines 74–76, 118–120)
- **Scope:** This page does not provide a return `/payments/details` sequence, webhook outcome procedure, country/currency row or refund/capture/recurring capability table. Use the linked main integration and Boost overview for those separate questions; the redirect requirement alone does not establish a final result. (raw lines 19–23, 25–120)

## Detail locators

- Sessions requirements, request/configuration additions and import: raw lines 25–60.
- Sessions initialization example and environment statement: raw lines 62–76.
- Advanced requirements, import, initialization example and `/payments` statement: raw lines 78–120.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boost]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/web-component/2026-09-15|Adyen Boost Wallet Web Component guide, 2026-09-15 snapshot]]
