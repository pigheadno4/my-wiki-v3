---
title: "Adyen Online banking Thailand Android Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/android-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/android-component/2026-09-15.md"
tags: [adyen, online-banking-thailand, android, components, redirect]
---

## Overview

This 2026-09-15 Adyen guide gives method-specific additions for Online banking Thailand in an existing Android Components integration, separately for Sessions and Advanced flow. It covers the `MolpayComponent`, optional submit-button visibility, redirect prerequisites and TEST/live steps. It is not a complete integration guide or proof of current bank, issuer or merchant eligibility, or a completed payment. See [[adyen]] and [[adyen-android-sdk]].

## Key takeaways

- Sessions requires an existing Android Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Online banking Thailand added in Customer Area. The page adds no method-specific fields to the base `/sessions` request. Advanced requires an existing Android Components Advanced integration, additional-action handling for the same redirect action, and Customer Area setup; it adds no method-specific fields to the base `/payments` request. The v68+ line is stated for Sessions here, not as an Advanced-flow minimum.
- Import `com.adyen.checkout:molpay:YOUR_VERSION`; the Jetpack Compose examples also import `components-compose`. The Component class is `MolpayComponent` with `PaymentMethodTypes.MOLPAY_THAILAND`. Sessions gets the method from `checkoutSession`; Advanced filters the merchant's `/paymentMethods` response. Compose uses `AdyenComponent` and a distinct key when a new Component must be created for a different screen or payment session; non-Compose attaches the Component to a view.
- `setSubmitButtonVisible` is an optional configuration: `false` hides the button and the stated default is `true`. The adjacent Kotlin configuration snippets contain an extra nested brace and placeholder `value`; treat them as illustrative, not complete compile-ready configuration.
- For testing, the page says to use an issuer ID available for the Component in the respective country/region and inspect payment status in the Adyen test Customer Area. Live Online banking Thailand acceptance requires a separate request in the live Customer Area. The page names neither a fixed issuer catalog nor a currency, and it does not define final authorization, capture or settlement behavior. Redirect setup, Component rendering and a shopper return alone are not payment-outcome proof.

## Detail locators

- Sessions prerequisites, no-extra-fields base request, imports and optional configuration: pinned raw lines 25–87.
- Sessions Compose/non-Compose launch and `MOLPAY_THAILAND` selection: pinned raw lines 89–142.
- Sessions test/live steps: pinned raw lines 144–150.
- Advanced prerequisites, imports and optional configuration: pinned raw lines 152–205.
- Advanced Compose/non-Compose launch from `/paymentMethods`, no-extra-fields `/payments` statement and test/live steps: pinned raw lines 207–276. The Advanced `paymentMethod` lookup can return no match in the example; the page supplies no method-specific fallback or result handling here.

## Related

- [[adyen-android-sdk]] — native Component and server-flow boundaries
- [[adyen-online-payments]] — Sessions, Advanced and redirect outcome concepts

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/android-component/2026-09-15|Online banking Thailand Android Component guide, 2026-09-15]]
