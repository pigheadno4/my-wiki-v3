---
title: "Adyen PayCo Web Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payco/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payco/web-drop-in/2026-09-15.md"
tags: [adyen, payco, web, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen page describes PayCo-specific additions to an existing Web Drop-in integration, split between Sessions and Advanced server-side flows. It addresses prerequisites, optional import optimization, request additions, and testing assistance; it does not document a complete payment result. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and adding PayCo in the Customer Area. The page says no additional parameters are needed when creating the payment session.
- Advanced requires an existing Web Drop-in Advanced integration, redirect handling, and adding PayCo in the Customer Area. The page says no additional parameters are needed in the `/payments` request. It does not state an Advanced-path Checkout API minimum. Its prerequisite link has an unresolved encoded `getParameter('platform')` template in the URL; the *text* specifies Web Drop-in, but the link should not be treated as a verified Web-specific destination.
- In either path, importing individual payment methods is optional for tree shaking; if using that import approach, the page says to include `Redirect` and shows `AdyenCheckout, Dropin, Redirect` imported from `@adyen/adyen-web`. It gives no PayCo-specific Drop-in initialization code.
- Under both “Test and go live” headings, the page says there are no specific PayCo test credentials and directs readers to Adyen Support for testing assistance. No successful test, live activation, or final payment outcome is shown.

## Detail locators

- Sessions requirements: pinned raw lines 25–36; no additional `/sessions` parameters: lines 38–42; optional import: lines 44–54; testing: lines 56–62.
- Advanced requirements and unresolved template URL: lines 64–74; optional import: lines 76–86; no additional `/payments` parameters: lines 88–92; repeated testing guidance: lines 94–100.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payco/web-drop-in/2026-09-15|PayCo Web Drop-in, 2026-09-15]]
