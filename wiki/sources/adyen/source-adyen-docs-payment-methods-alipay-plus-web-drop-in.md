---
title: "Adyen Alipay+ Web Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay-plus/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipay-plus/web-drop-in/2026-09-15.md"
tags: [adyen, alipay-plus, web, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen page describes Alipay+-specific additions to an existing Web Drop-in integration for Sessions or Advanced server-side flow. Both paths require redirect handling and Customer Area method addition. It is an add-on guide; its sample redirect response is an intermediate action, not successful payment or wallet-level eligibility proof. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, handling `action.type: redirect`, and adding Alipay+ in Customer Area. The page says no extra parameters are needed when creating the base payment session. It offers an *optional* individual-method import for tree shaking; the shown import names lowercase `redirect`.
- Advanced requires an existing Web Drop-in Advanced integration, redirect handling, and Customer Area method addition; no Advanced Checkout API minimum is stated. Its prerequisite link contains an unresolved encoded `getParameter('platform')` template despite Web Drop-in link text. The optional import again uses lowercase `redirect`.
- For Advanced `/payments`, the page marks `channel` required and says to set it to the applicable **Web**, **iOS**, or **Android** value. It says `browserInfo` is required when `channel` is **Web**. The illustrative request uses `paymentMethod.type: alipay_plus`, SGD/SG values, lowercase `"channel": "web"`, and `browserInfo`; its example response has `resultCode: RedirectShopper` and a redirect action. The lowercase sample value differs from the table's capitalized **Web** label and should not be normalized into a verified enum.
- Both testing sections state there is **no Alipay+ test environment**, recommend live penny tests with an Alipay+ wallet app/card and checking the live Customer Area, and say a request for **Alipay** must be submitted there before accepting live **Alipay+** payments. Preserve that Alipay-versus-Alipay+ wording without assuming identical methods or completed approval. The Advanced sample nevertheless targets `https://checkout-test.adyen.com/v72/payments`; it does not establish a usable Alipay+ sandbox. No live test or provider action was performed.

## Detail locators

- Sessions prerequisites, request, and optional import: pinned raw lines 25–54; first testing/live statements: lines 56–68.
- Advanced prerequisites and unresolved template link: lines 70–80; optional import: lines 82–92; Advanced request table: lines 94–103.
- Illustrative TEST-endpoint request and redirect response: lines 105–166; repeated testing/live statements: lines 168–180.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay-plus]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay-plus/web-drop-in/2026-09-15|Alipay+ Web Drop-in, 2026-09-15]]
