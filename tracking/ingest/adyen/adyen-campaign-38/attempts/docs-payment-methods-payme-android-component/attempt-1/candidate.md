---
title: "Adyen PayMe Android Redirect Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payme/android-component"
raw_files:
  - "adyen/docs/payment-methods/payme/android-component/2026-09-15.md"
tags: [adyen, payme, android, component, redirect]
---

## Overview

This 2026-09-15 Adyen guide describes adding PayMe to an existing Android Components integration with the Redirect Component. It says to show PayMe in the payment form, redirect the shopper to the PayMe app, and handle the redirect result when the shopper returns. PayMe is stated as supported from Android Components 4.0.0. The shown `Authorised` response is an example, not evidence of an actual payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Before integration, the page says to add PayMe in the **test** Customer Area. For `/paymentMethods`, it specifies `countryCode: HK` and `amount.currency: HKD`, and says the response contains `paymentMethod.type: payme`.
- At payment creation, its table marks `paymentMethod.type: payme` and `returnURL` required, and says to get the return URL from `RedirectComponent.getReturnUrl(context)`. The example uses `returnUrl` instead of table `returnURL`; preserve that casing conflict. The table also lists `channel` and `lineItems` subfields with blank Required cells. Its `lineItems.quantity` description says number, while the example passes string `"1"`.
- The `/payments` example is JavaScript/Node-style code inside a `kotlin` fence, so its language label should not be treated as a runnable Kotlin example. A sample response shows `RedirectShopper` with redirect action, PayMe URL, and an illustrative `expiresAt`. The action is passed to the client Redirect Component. After shopper return, the page calls for a server-side POST to `/payments/details` with `actionComponentData.details`; the response's `resultCode` is used to present a result. A sample `Authorised` response does not prove a real authorization, and the final Android Components guide link points to a Sessions-flow URL although this page's procedural example uses `/payments` and `/payments/details`.
- The PayMe sandbox does not require the PayMe app. Amount endings 30/81 simulate `Authorised`, 77/90 `OfferCancelled` after the stated default ten-minute expiry, and 40/44 request-creation `Error`. These are sandbox fixtures, not live outcome proof.

## Detail locators

- Redirect Component scope, Android Components minimum, and prerequisites: pinned raw lines 15–31; method discovery: lines 33–42.
- Required payment fields, casing conflict, and example language/sample: lines 44–93; redirect response and client handoff: lines 95–115; return details and response example: lines 117–152.
- Sandbox result mapping and see-also links: lines 154–170.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payme]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payme/android-component/2026-09-15|PayMe Android Redirect Component, 2026-09-15]]
