---
title: "Alipay+ Android Component | Adyen Docs"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay-plus/android-component"
raw_files:
  - "adyen/docs/payment-methods/alipay-plus/android-component/2026-09-15.md"
tags: [adyen, alipay-plus, android, components, redirect, wallet]
---

## Overview

This [[adyen]] page gives **Alipay+**-specific additions to an existing Android **Components** integration, separately for Sessions and Advanced server-side flows. It uses `InstantPaymentComponent` for `alipay_plus` with a redirect action. The page does not define each Alipay+ wallet's country, currency, shopper eligibility or final transaction outcome; see [[adyen-online-payments]] and the pinned raw.

## Key takeaways

- **Sessions prerequisites and request:** The page requires an existing Sessions Android Components integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and Alipay+ added in Customer Area. It says no Alipay+-specific `/sessions` request parameters are needed. See raw lines 25–42.
- **Advanced prerequisites and request:** The page requires an existing Advanced Android Components integration, additional-action handling for `action.type: redirect`, and Alipay+ Customer Area setup. It says no Alipay+-specific `/payments` parameters are needed when making a payment. These no-extra-parameter statements are within an already-built base integration; they do not eliminate its ordinary server request, callback or result handling. See raw lines 156–164 and 268–272.
- **Android Component setup:** Both sections import the `redirect` module; with Jetpack Compose, they also import `components-compose`. The dependency versions are `YOUR_VERSION` placeholders, not a fixed minimum. The guide uses `InstantPaymentComponent`, selecting `alipay_plus` from the Session or `/paymentMethods` response. Compose examples use `AdyenComponent` and a per-Component key; non-Compose examples attach the Component to a view. See raw lines 44–65, 89–142, 166–187 and 211–266.
- **Optional button configuration:** The table describes `setSubmitButtonVisible` with default `true`; setting it to `false` hides the submit button. The illustrated configuration block contains placeholders, so it should be read with the relevant main integration guide rather than as a complete executable example. See raw lines 67–87 and 189–209.
- **Testing and live gate:** The page says **there is no test environment for Alipay+**. It recommends live penny tests using an Alipay+ wallet app and checking the live Customer Area, then says a live Customer Area request is needed before accepting live payments. These are documented guidance and prerequisites, not proof that a live test was performed, that a merchant is enabled, or that a payment succeeded. See raw lines 144–154 and 274–284.

> [!warning] Live-request name mismatch
> The setup prerequisites say to add **Alipay+** in Customer Area, but both live-acceptance instructions say to submit a request for **Alipay**. The page does not explain whether those names identify the same enablement request. Preserve the Alipay+ method scope and verify the intended live request with Adyen rather than silently treating the two names as equivalent. See raw lines 36, 154, 164 and 284.

## Detail locators

- Sessions import, optional configuration and Compose/non-Compose initialization examples: raw lines 44–142. Advanced counterparts: raw lines 166–266.
- No wallet-by-wallet country/currency matrix, recurring-token path, refund/capture procedure, return-URL mechanics or payment-result webhook contract appears in this method-specific page; these require separate authority.

## Related

- [[adyen-online-payments]] — main online payment integration and method routes.
- [[adyen-android-sdk]] — version-qualified native Components context; this page's `YOUR_VERSION` placeholders do not pin that SDK.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay-plus/android-component/2026-09-15|Alipay+ Android Component, 2026-09-15 snapshot]]
