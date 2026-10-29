---
title: "Alma Android Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/android-component"
raw_files:
  - "adyen/docs/payment-methods/alma/android-component/2026-09-15.md"
tags: [adyen, alma, android, components, redirect, installments]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Alma to an existing Android Components integration with Sessions or Advanced flow. It supplies the InstantPaymentComponent setup, optional request additions, redirect action and test/live routes. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alma|the Alma overview]] for the captured FR/EUR and feature matrix. TEST examples do not prove current merchant eligibility or a completed payment.

## Key takeaways

- Sessions requires an existing Android Components Sessions integration, Checkout API v68 or later, and Alma added in Customer Area. Advanced requires its Android Components base integration, additional-action handling for `action.type: redirect`, and Customer Area setup. The Sessions example uses TEST Checkout API v71; Advanced uses v72.
- The Alma-specific `/sessions` and `/payments` tables list telephone number, shopper email, billing and delivery addresses with blank Required cells. Advanced also lists optional `additionalData.alma.installments_count`: set `3` or `4` to choose installments, or omit to let the shopper choose. Do not infer these fields are mandatory from their presence in the examples.
- Import `com.adyen.checkout:instant`; with Jetpack Compose also import `components-compose`. Both flows use `InstantPaymentComponent`, with separate Compose and XML/non-Compose examples. Compose examples require a unique Component key for each different screen/session or reset. The guide says no additional Alma configuration parameters are needed.
- The Sessions TEST example uses FR/EUR and an Android app-scheme `returnUrl` placeholder `adyencheckout://your.package.name` (raw line 64). The Advanced FR/EUR example instead uses an HTTPS return URL (line 300), and the response shows `RedirectShopper`/`action.type: redirect`. The capture does not explain the difference or show a completed app return; validate the return route for the actual integration. The Advanced example also uses `shopperLocale: en-US` with country FR, which is example scope only.
- Check TEST payment status in Customer Area. The page says a live Customer Area request for Alma is needed before accepting live payments. It does not define capture, refund or final asynchronous status behavior; use the overview and main integration guides for their respective scope.

## Detail locators

- Sessions prerequisites, optional field table and FR/EUR app-scheme TEST example: pinned raw lines 25–84. Module and InstantPaymentComponent setup: lines 86–168.
- Advanced prerequisites, setup and optional installments field: lines 176–285. FR/EUR HTTPS return example and redirect response: lines 286–340. Test/live route: lines 342–346.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-alma]] — method scope and capability matrix

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/android-component/2026-09-15|Alma Android Component guide, captured 2026-09-15]]
