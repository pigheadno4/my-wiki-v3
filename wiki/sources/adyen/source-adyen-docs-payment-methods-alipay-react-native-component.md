---
title: "Alipay React Native Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/alipay/react-native-component/2026-09-15.md"
tags: [adyen, alipay, react-native, components, redirect]
---

## Overview

This 2026-09-15-modified and captured [[adyen]] Alipay page gives **React Native Components** additions for an existing integration, routed through [[adyen-online-payments]]. Its heading says “Alipay React Component,” but the path and prerequisite text specify **React Native**. The page explicitly says React Native Components **do not support Sessions flow**; its PayPay-like two-flow framing must not be read as Sessions availability.

## Key takeaways

- The only described route is an existing **Advanced-flow React Native Components** integration with redirect handling for `action.type: redirect` and Alipay added in Adyen Customer Area. The “Integration type” hyperlink points to an Advanced **Drop-in** URL while the prose says Components and the redirect/payment links point to Advanced **Components**; preserve that navigation mismatch instead of treating Drop-in as the component prerequisite.
- The page says no **additional Alipay-specific** configuration and no additional `/payments` parameters. These statements supplement the linked main Advanced integration and do not remove its base request, client callback or redirect/return requirements. This page does not state a Checkout API or React Native SDK version, payment currency or regional eligibility rule.
- It **recommends** live penny tests using an Alipay wallet app with a credit/debit card and viewing those test-payment details in **live Customer Area**. It separately says a request for Alipay in live Customer Area is needed **before accepting live payments**. The recommendation does not prove a test was performed, that the request was approved, or that an authorization, capture or settlement succeeded.
- The page gives no TEST-environment fixture, post-redirect result or webhook-final-outcome procedure. A configured method or a redirect is not payment-completion evidence; follow the main Advanced integration and provider outcome guidance for those steps.

## Detail locators

- [[raw/adyen/docs/payment-methods/alipay/react-native-component/2026-09-15|Pinned raw]], lines 15–29: page identity, supplementary scope and unsupported React Native Components Sessions flow.
- Same raw, lines 31–41: Advanced prerequisite and Drop-in/Components hyperlink mismatch, redirect action and Customer Area step.
- Same raw, lines 43–53: no additional Alipay-specific configuration or `/payments` parameters.
- Same raw, lines 55–63: recommended live penny tests, live Customer Area inspection and live method request prerequisite.

## Related

- [[source-adyen-docs-payment-methods-alipay-react-native-drop-in]] — distinct React Native **Drop-in** route; do not transfer its Sessions support to Components.
- [[source-adyen-docs-payment-methods-alipay]] — Alipay overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/react-native-component/2026-09-15|Alipay React Native Component]]
