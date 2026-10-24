---
title: "Alipay HK Android Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/android-component"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/android-component/2026-09-15.md"
tags: [adyen, alipay-hk, android, components, online-payments]
---

## Overview

This [[adyen]] guide, captured 2026-09-15, adds Alipay HK to an **existing Android Components** integration. It provides separate Sessions and Advanced flow instructions for the instant-payment Component and points back to the main integration guides for the shared flow. It is a method-specific implementation guide, not evidence of current merchant eligibility, a completed payment, or authorization, capture or settlement. See [[adyen-online-payments]] and raw lines 15–23.

## Key takeaways

- For **Sessions flow**, the guide requires an existing Sessions Android Components integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and adding Alipay HK in Customer Area. It says no additional `/sessions` parameters or Alipay HK configuration parameters are needed. These are additions to the existing integration, not a complete server implementation. See raw lines 25–42 and 67–71.
- Import `com.adyen.checkout:instant:YOUR_VERSION`; add `components-compose:YOUR_VERSION` when using Jetpack Compose. In Sessions, obtain `alipay_hk` from `checkoutSession`, then create `InstantPaymentComponent`; the Compose sample uses a unique key to create a new Component for another screen/session or reset. Without Compose, attach the Component to the view. `YOUR_VERSION` is a placeholder, not a stated minimum Android SDK version. See raw lines 44–125.
- For **Advanced flow**, the guide requires an existing Advanced Android Components integration, handling the additional redirect action, and adding Alipay HK in Customer Area. It selects `alipay_hk` from the `/paymentMethods` response, creates `InstantPaymentComponent`, and says no method-specific configuration or additional `/payments` parameters are needed. The Advanced section does **not** state the Sessions section's Checkout API v68 minimum for that flow. See raw lines 140–240.
- The page provides AlipayHK test credentials and directs checking **test payment status** in the test Customer Area. It separately says a request for AlipayHK in the **live** Customer Area is needed before accepting live payments. Test credentials, Component setup and a live request do not themselves establish successful payments or current availability. The page does not state country/currency support, recurring/token consent, a final webhook outcome contract, or capture/settlement behavior; use their specific authorities for those topics. See raw lines 128–138 and 242–252.

## Detail locators

- Sessions requirements, method-specific request and configuration, Compose/non-Compose imports and launch: raw lines 25–125.
- Advanced requirements, imports and Component launch from `/paymentMethods`: raw lines 140–234.
- Advanced method-specific `/payments` parameter statement: raw lines 236–240.
- Test credentials and test-versus-live Customer Area instructions, repeated under both flows: raw lines 128–138 and 242–252.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/android-component/2026-09-15|Alipay HK Android Component guide — captured 2026-09-15]]
