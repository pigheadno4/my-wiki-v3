---
title: "Adyen PaySafeCard Android Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/android-component"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/android-component/2026-09-15.md"
tags: [adyen, paysafecard, android, components, redirect]
---

## Overview

This captured [[adyen]] guide adds PaySafeCard to an existing Android Components integration. It separates Sessions and Advanced server flows, specifies the PaySafeCard `shopperReference` addition, shows an `InstantPaymentComponent` with or without Jetpack Compose, and gives test/live steps. The page is a method-specific add-on, not a complete Android integration or proof of current account eligibility or a completed live payment. [[adyen-online-payments]]

## Key takeaways

- **Sessions requirements and request:** The guide requires an existing Android Components Sessions integration, Checkout API v68 or later, redirect handling, and PaySafeCard added in Customer Area. Its `/sessions` table marks `shopperReference` required: a merchant reference uniquely identifying the shopper, such as user or account ID. The curl example uses EUR 1000 minor units, `countryCode: NL` and an Android app-scheme `returnUrl`; those are sample values, not a general country/currency or return-route rule (pinned raw lines 25–69).
- **Advanced requirements and request:** The Advanced section requires an existing Android Components Advanced integration, handling `action.type: redirect`, and Customer Area setup. Its requirements row does not state a Checkout API minimum. The `/payments` table again marks `shopperReference` required. The example response is `RedirectShopper` with a redirect action, which is an additional shopper step rather than final authorization (lines 364–372, 460–469, 755–769).
- **Android Component:** Both flows import `com.adyen.checkout:instant:YOUR_VERSION`; Compose adds `components-compose:YOUR_VERSION`. The guide says no further PaySafeCard-specific configuration parameters are needed. Both launch `InstantPaymentComponent` for the `paysafecard` method. Sessions gets the method from `checkoutSession`; Advanced finds it in the `/paymentMethods` response. Compose examples specify a unique key to create a new Component for a different screen/session or reset; the non-Compose examples attach it to a view (lines 270–352, 374–458).
- **Test and live:** The page gives a 16-digit test code and routes test status checks to the test Customer Area. Before live acceptance, it says to contact Adyen Support to add PaySafeCard in the live Customer Area; the displayed Support link itself points to the test Customer Area. These instructions and test code do not establish live enablement or payment success (lines 354–362, 771–779).

> [!warning] Source request examples
> The Advanced `/payments` examples show `shopperReference` but omit a `paymentMethod` object, despite the Component selecting the `paysafecard` method (raw lines 416–419, 475–489 and 512–752). Treat those examples as method-specific additions, not complete payment requests; use the linked base Advanced integration for the full request and action handling. The Sessions Java, PHP, C#, Go and TypeScript snippets also omit construction of `createCheckoutSessionRequest` (lines 71–137, 171–192, 250–268). Both curl request examples put `-X POST` on a line without continuation before `-d` (lines 53–69, 475–490). The Sessions sample uses an app-scheme returnUrl while the Advanced sample uses HTTPS (lines 64, 486); check base Android return handling rather than treating either as a universal recipe.

## Detail locators

- Sessions prerequisites, required field and server samples: pinned raw lines 25–268.
- Sessions imports, Component setup and test/live: lines 270–362.
- Advanced prerequisites, imports and Component setup: lines 364–458.
- Advanced required field, payment examples, redirect sample and test/live: lines 460–779.

## Related

- [[adyen-online-payments]] — provider online-payments architecture and method routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/android-component/2026-09-15|PaySafeCard Android Component guide, captured 2026-09-15]]
