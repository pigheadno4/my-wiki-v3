---
title: "Adyen Alipay+ Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay-plus/web-component"
raw_files:
  - "adyen/docs/payment-methods/alipay-plus/web-component/2026-09-15.md"
tags: [adyen, alipay-plus, web-components, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen guide adds Alipay+ to an existing Web Components integration. It has separate Sessions and Advanced server-side paths; both use the Web `redirect` Component and require redirect handling. It is method-specific guidance, with the base integration guides retaining the full payment lifecycle. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-alipay-plus]] for the network overview and wallet-specific eligibility boundary.

## Key takeaways

- Sessions requires an existing Web Components Sessions flow, Checkout API v68 or later, redirect handling, and adding Alipay+ in Customer Area. The page says no extra `/sessions` parameters or Alipay+ configuration are needed; import `redirect` and initialize the redirect Component.
- Advanced requires an existing Web Components Advanced flow, redirect handling, and Customer Area setup. Import and initialize `redirect`; for `/payments`, the guide lists `channel` (Web, iOS, or Android) and `browserInfo` when the channel is Web. The request example uses `paymentMethod.type: alipay_plus` and the response example includes a redirect action and `RedirectShopper`, which is an intermediate shopper handoff rather than a final authorization or settlement result.
- Both flow sections state that Alipay+ has no test environment, recommend live penny tests, and say a live Customer Area request for **Alipay** is needed before accepting live Alipay+ payments. Those are documentation statements, not proof of merchant approval, wallet eligibility, or successful payment. The Advanced example nonetheless targets `checkout-test.adyen.com/v72/payments`; the page does not reconcile that example with its no-test-environment statement.

## Detail locators

- Sessions prerequisites and redirect action: pinned raw lines 23–36; no extra session parameters, import, configuration, and initialization: lines 40–75.
- Advanced prerequisites, import, and initialization: lines 90–125; `/payments` `channel` and conditional `browserInfo`: lines 128–137.
- Advanced example request, including example-only SGD/SG values and test endpoint: lines 139–175; redirect response example: lines 177–200.
- No-test-environment, recommended live penny tests, and live request wording appear in both sections: lines 78–88 and 202–212.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay-plus]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay-plus/web-component/2026-09-15|Alipay+ Web Component, 2026-09-15]]
