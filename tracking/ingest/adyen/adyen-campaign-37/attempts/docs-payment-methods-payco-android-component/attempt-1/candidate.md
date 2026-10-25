---
title: "PayCo Android Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payco/android-component"
raw_files:
  - "adyen/docs/payment-methods/payco/android-component/2026-09-15.md"
tags: [adyen, payco, android, components, online-payments]
---

## Overview

This 2026-09-15 guide adds PayCo to an existing Adyen Android Components integration, with separate Sessions and Advanced server-side paths. Both use a redirect action and `InstantPaymentComponent` for method type `kcp_payco`. These are integration instructions, not evidence of a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites and request:** the merchant needs an existing Android Components Sessions integration, Checkout API v68 or later, redirect handling (`action.type: redirect`) and PayCo added in Customer Area. The page says no PayCo-specific `/sessions` parameters or Component configuration are needed. It does not state the Android SDK version represented by the code's `YOUR_VERSION` placeholder. (raw lines 25–48, 52–71)
- **Sessions Component route:** with Jetpack Compose, the snippets include `instant` and `components-compose` modules, get `kcp_payco` from `checkoutSession`, supply a Component key described as unique per screen/session/reset, and wrap the Component in `AdyenComponent`. Without Compose, they include `instant`, get the same session method and attach the Component to a view. These are example constructions, not a payment result. (raw lines 50–126)
- **Advanced path:** an existing Advanced Android Components integration must handle the redirect action and have PayCo added in Customer Area. Its examples select `kcp_payco` from the `/paymentMethods` response before constructing `InstantPaymentComponent`; Compose adds `components-compose`, while non-Compose uses `instant` alone. The page says no PayCo-specific Component configuration or `/payments` parameters are needed. It states no Advanced Checkout API minimum. (raw lines 134–234)
- **Testing and limits:** both flow sections say there are no PayCo-specific test credentials and direct merchants to Adyen Support for testing assistance. The page gives no live-enablement procedure, shopper return, final webhook/status sequence, or evidence of authorization, capture or settlement. (raw lines 128–132, 236–240)

## Detail locators

- Sessions prerequisites, no extra request fields and no configuration: raw lines 29–42, 67–71.
- Sessions module and `InstantPaymentComponent` examples: raw lines 44–126.
- Advanced prerequisites, action and module setup: raw lines 134–177.
- Advanced `kcp_payco` discovery, Component examples and no extra payment fields: raw lines 179–234.
- Testing assistance and no method-specific credentials: raw lines 128–132, 236–240.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payco/android-component/2026-09-15|Adyen PayCo Android Component guide, 2026-09-15 snapshot]]
