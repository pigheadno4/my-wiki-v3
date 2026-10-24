---
title: "GCash Web Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gcash/web-drop-in/2026-09-15.md"
tags: [adyen, gcash, web, drop-in, redirect, tokenization]
---

## Overview

This [[adyen]] page explains GCash-specific additions to an **existing Web Drop-in** integration for separate Sessions and Advanced server-side flows. It requires redirect handling and describes an optional recurring-token route. It is not a complete checkout guide or evidence that a merchant is enabled or a payment has completed. See [[adyen-online-payments]] and the pinned raw. The [[source-adyen-docs-payment-methods-gcash|GCash overview]] supplies the separate PH/PHP method and shopper-journey context.

## Key takeaways

- **Sessions base flow:** The prerequisites are an existing Sessions Web Drop-in integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and GCash added in Customer Area. The page says no additional GCash `/sessions` parameters are needed. See raw lines 25–42.
- **Advanced base flow:** The prerequisites are an existing Advanced Web Drop-in integration, redirect handling, and GCash setup in Customer Area. The page says no additional GCash `/payments` parameters are needed for this base flow. Its requirement link has a malformed encoded platform template; see the warning below. See raw lines 306–334.
- **Optional Web import:** For individual-payment-method tree shaking, the page says to include `Redirect` when importing Adyen Web, and shows `AdyenCheckout`, `Dropin` and `Redirect` imports. This is optional import guidance, not a required GCash-specific configuration field or a stated Web SDK version. See raw lines 44–54 and 318–328.
- **Recurring route:** Both flow sections say GCash supports recurring transactions. For token creation, `/payments` includes `storePaymentMethod: true` and a unique `shopperReference` of at least three characters. After the initial payment **has been settled**, a `recurring.token.created` webhook supplies `storedPaymentMethodId`; the merchant server must receive recurring-token lifecycle events. Later `/payments` token charges specify the stored ID, matching shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The base-flow no-extra-parameter statements do not remove these separate recurring fields. Token instructions and example requests do not establish a completed initial or later payment. See raw lines 56–93 and 336–373.
- **Testing and live gate:** The page says successful **live-payment testing** needs a real mobile number registered to a GCash account, points to Customer Area for test-payment status, and requires a GCash request in the **live Customer Area** before live acceptance. The snapshot does not prove current account eligibility or live operation. See raw lines 294–304 and 574–584.

> [!warning] Advanced prerequisite link
> The Advanced requirement names a **Web Drop-in** integration, but its URL has an encoded `{{getParameter('platform')}}` expression instead of `platform=Web`; the neighboring redirect and import links explicitly select Web Drop-in. Use the page's stated scope and verify the main-guide destination before following this prerequisite link. See raw lines 314–322.

## Detail locators

- Recurring curl, Java, PHP, C#, Node.js, Python and Ruby request examples: raw lines 95–291 and 375–571. Their `PHP` currency and TEST-library settings are examples, not a universal currency or live-readiness guarantee.
- The page links to main integration guides for redirect handling and session creation; it does not spell out the shopper's return handling or final payment-status contract. See raw lines 21–42 and 314–334.

## Related

- [[adyen-online-payments]] — main integration architecture.
- [[adyen-tokenization]] — stored-method and recurring-token context.
- [[source-adyen-docs-payment-methods-gcash]] — method-level PH/PHP and shopper journey overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/web-drop-in/2026-09-15|GCash Web Drop-in, 2026-09-15 snapshot]]
