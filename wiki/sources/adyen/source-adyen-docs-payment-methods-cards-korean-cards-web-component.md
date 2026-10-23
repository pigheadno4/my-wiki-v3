---
title: "Adyen Korean Card Payments via redirect Web Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/korean-cards/web-component"
raw_files:
  - "adyen/docs/payment-methods/cards/korean-cards/web-component/2026-09-15.md"
tags: [adyen, korean-cards, web-component, redirect, cards]
---

## Overview

This [[adyen]] guide describes **Korean Card Payments via redirect** as an addition to an **existing Web Components integration**, with separate Sessions and Advanced server-side flows. It gives method-specific changes and points back to the main integration guide for common payment and redirect behavior. It does not itself establish a merchant's method enablement, geographic availability, authorization, capture, or settlement. [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** The page requires an existing Sessions Web Components integration, Checkout API **v68 or later**, handling `action.type: redirect`, and adding the method in Customer Area. It says no additional `/sessions` parameters or method-specific configuration are needed; import `Redirect` and initialize the method-specific component. See raw lines 23–71.
- **Advanced flow:** The page separately requires an existing Advanced Web Components integration, redirect handling, and adding the method in Customer Area. It likewise imports and initializes `Redirect`, and says no additional `/payments` parameters are needed. The Advanced section does **not** state the Sessions section's v68+ requirement as its own version prerequisite. See raw lines 80–118.
- Both initialization snippets use `new Redirect(checkout, { type:kcp_creditcard })` with **unquoted `kcp_creditcard`**. The guide does not define that JavaScript identifier; do not treat the fragment as self-contained, copy-ready code without checking the applicable Web integration and method type. This example issue does not change the separate method-setup and redirect requirements. See raw lines 64–72 and 102–112.
- For both flows, the guide says to contact Support to set up the test environment. Before accepting live card payments, it says to assess PCI DSS compliance and submit the required SAQ A. These steps are stated prerequisites, not evidence of successful setup or compliance. See raw lines 74–78 and 120–124.
- The page gives no `countryCode`, currency, Web SDK version, payment-result, webhook, or capture procedure specific to this Web Component. Its “no additional parameters” statements are **relative to the existing integration**, not a complete session or payment request. Follow the appropriate main-flow documentation for those shared operations. See raw lines 19–23, 40–42, 58–66, and 114–118.

## Detail locators

- Sessions prerequisites, imports and initialization: raw lines 25–72.
- Advanced prerequisites, imports and initialization: raw lines 80–112.
- Advanced `/payments` statement and both test/live checklists: raw lines 74–78 and 114–124.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/korean-cards/web-component/2026-09-15|Adyen Korean cards Web Component snapshot]]
