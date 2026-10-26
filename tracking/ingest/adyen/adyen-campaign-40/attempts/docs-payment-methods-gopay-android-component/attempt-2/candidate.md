---
title: "Adyen GoPay Android Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/android-component"
raw_files:
  - "adyen/docs/payment-methods/gopay/android-component/2026-09-15.md"
tags: [adyen, gopay, android, components, redirect, recurring-payments]
---

## Overview

This 2026-09-15 guide adds GoPay to an existing Android Components integration. It covers separate Sessions and Advanced server-side flows, `InstantPaymentComponent` in Views or Jetpack Compose, and conditional recurring-token paths for Subscription and CardOnFile payments. It is a dated provider guide, not current merchant enablement or proof of an executed payment. [[adyen]] [[adyen-online-payments]] [[adyen-tokenization]]

## Key takeaways

- **Sessions setup:** Requires an existing Sessions Android Components integration, Checkout API v68 or later, `action.type: redirect` handling, and GoPay added in Customer Area. The page marks `shopperInteractionDevice` and `channel` as required additions to `/sessions`. Import `com.adyen.checkout:instant` and, for Compose, `components-compose`; create an `InstantPaymentComponent` using the `gopay_wallet` payment method. It says no additional GoPay configuration parameters are needed. (raw lines 25–108, 110–157)
- **Advanced setup:** Requires an existing Advanced Android Components integration, redirect action handling and Customer Area setup. Import the same method module, use `InstantPaymentComponent` with a `gopay_wallet` method from `/paymentMethods`, and supply the table-marked `/payments` fields `paymentMethod.type: gopay_wallet`, `browserInfo` and `channel`. The sample returns `RedirectShopper` with `action.type: redirect`, an intermediate shopper handoff rather than a final outcome. The Advanced requirements section does not separately state the Sessions v68+ minimum. (raw lines 442–597)
- **Token creation after first payment:** For recurring use, the page tells the merchant to include `storePaymentMethod: true`, a shopper-unique `shopperReference` of at least three characters, and `recurringProcessingModel` in `/payments`. Only after the initial payment has settled does it say a `recurring.token.created` webhook supplies `storedPaymentMethodId`; the merchant server must receive recurring-token lifecycle events. This `/payments` token route is described even under the Sessions section, and is distinct from the base `/sessions` additions. (raw lines 159–180, 599–620)
- **Later token payments:** A Subscription `/payments` request uses the stored method ID, matching shopper reference, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription`. A CardOnFile request uses the same token/reference/ContAuth pattern with `recurringProcessingModel: CardOnFile`, but requires redirecting the shopper to GoPay for a PIN challenge, then calling `/payments/details` with `redirectResult` after return. The page identifies the later `AUTHORISATION` webhook as final payment status; `RedirectShopper` or a displayed `resultCode` is not a settlement claim. (raw lines 182–194, 399–432, 622–634, 839–872)
- **Testing and example limits:** GoPay testing requires contacting Adyen Support; live acceptance requires a separate GoPay request in live Customer Area. The Sessions and Advanced curl examples omit a line continuation after `-X POST`; their device/browser information is shown as a quoted nested object, and the Advanced Android example uses `channel: web`. Recurring examples across languages leave currency, method type and return URL blank, so they are illustrative rather than complete executable requests. The sample SDK library versions are language-specific snapshots, not an Android SDK version guarantee. (raw lines 49–73, 196–397, 434–440, 550–581, 636–837, 874–880)

## Detail locators

- Sessions prerequisites, required fields and Compose/View Component setup: raw lines 25–157.
- Sessions recurring token creation, Subscription and CardOnFile: raw lines 159–432.
- Advanced prerequisites, Component setup, request fields and redirect response: raw lines 442–597.
- Advanced recurring routes: raw lines 599–872.
- Repeated testing and live request gate: raw lines 434–440 and 874–880.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/android-component/2026-09-15|Adyen GoPay Android Component guide, 2026-09-15 snapshot]]
