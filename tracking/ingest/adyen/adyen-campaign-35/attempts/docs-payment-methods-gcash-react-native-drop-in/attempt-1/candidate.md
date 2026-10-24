---
title: "Adyen GCash React Native Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gcash/react-native-drop-in/2026-09-15.md"
tags: [adyen, gcash, react-native, drop-in, redirect, recurring]
---

## Overview

This [[adyen]] guide describes **GCash-specific additions** to an existing **React Native Drop-in** integration, with separate **Sessions** and **Advanced** server-side sections. It requires redirect handling and provides a distinct merchant-server recurring-token path. It is not a complete standalone integration or evidence of a successful shopper return, settled payment, merchant enablement or live approval. The examples are PHP/TEST illustrations, not proof of runtime behavior. [[adyen-online-payments]]

## Key takeaways

- **Sessions base path:** The page calls for an existing React Native Drop-in **Sessions** integration, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and adding GCash in Customer Area. Its Sessions integration-type hyperlink goes to an **Advanced** guide even though the heading/prose say Sessions; use the flow-specific text and verify the main guide. It says no *additional GCash-specific* /sessions parameters or configuration are needed for the ordinary base path. See raw lines 23–48.
- **Advanced base path:** The Advanced section calls for an existing Advanced React Native Drop-in integration, redirect handling and GCash added in Customer Area. It says no extra GCash configuration or additional parameters for the ordinary base /payments request. The v68 minimum is stated in the Sessions requirements, while Advanced examples show v68; do not turn an example into a stated Advanced minimum. See raw lines 298–320 and 361–380.
- **Separate recurring token path:** In both sections the initial **/payments** token request needs `storePaymentMethod: true` and a `shopperReference` of at least **three characters**. The page says a `recurring.token.created` webhook supplies the `storedPaymentMethodId` **when the payment has settled**, and directs the merchant server to receive recurring token lifecycle events. Later /payments requests use that ID and matching shopper reference with `ContAuth`, and `Subscription` for fixed or `UnscheduledCardOnFile` for non-fixed schedules. The no-extra-base-parameter statements do not negate these recurring fields. This guide does not spell out shopper-consent mechanics. See raw lines 50–87 and 322–359.
- **Examples and status:** The recurring examples use GCash type, PHP, TEST settings and placeholders across curl, Java, PHP, C#, Node, Python and Ruby; they do not establish a transaction result or current API-library compatibility. The Test and go live sections unusually say that testing **successful live** GCash payments needs a real registered GCash mobile number, also point to a **test** Customer Area payment list, and separately require a request in **live** Customer Area before accepting live payments. Keep those environment statements distinct; neither a status lookup nor a request proves authorization or settlement. See raw lines 89–296 and 361–568.

## Detail locators

- Sessions prerequisites, base request and recurring route: raw lines 23–87.
- Sessions code examples and test/live language: raw lines 89–296.
- Advanced prerequisites, base request and recurring route: raw lines 298–359.
- Advanced examples and repeated test/live language: raw lines 361–568.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/react-native-drop-in/2026-09-15|Adyen GCash React Native Drop-in snapshot]]
