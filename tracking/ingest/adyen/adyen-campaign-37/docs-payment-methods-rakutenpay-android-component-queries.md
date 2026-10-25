# docs-payment-methods-rakutenpay-android-component retrieval queries

Canonical source: [[source-adyen-docs-payment-methods-rakutenpay-android-component]] (`wiki/sources/adyen/source-adyen-docs-payment-methods-rakutenpay-android-component.md`).
Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-android-component]] → [[raw/adyen/docs/payment-methods/rakutenpay/android-component/2026-09-15|pinned raw]].

## Q1 — What is the purpose and scope, and what cannot be inferred?

This is a Rakuten Pay add-on for an **existing Android Components** integration, with separate Sessions and Advanced flow instructions (raw lines 15–25, 160–168). It does not establish current merchant approval, country/currency eligibility, LIVE operation or a completed payment; those cannot be inferred from the setup, redirect or TEST simulator statements (raw lines 31–42, 152–158, 286–292). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-android-component]] → pinned raw above.

## Q2 — What central capability, prerequisites and warnings matter?

Sessions requires Android Components, Checkout API v68+, redirect handling and Customer Area setup, with no extra `/sessions` parameters (raw lines 25–42). Advanced requires the existing Components flow, handling a `redirect` additional action and Customer Area setup; it states no extra `/payments` parameters and gives no Advanced API minimum (raw lines 160–168, 272–276). Both use `InstantPaymentComponent` to create and show the Rakuten Pay Component, while the existing integration handles the redirect action; Compose and non-Compose imports/examples are shown with `YOUR_VERSION` placeholders, optional submit-button visibility, and an extra brace in configuration examples (raw lines 44–142, 170–270). Recurring card-on-file use is review-gated, cadence-restricted and requires application for each Recurring Processing Model; explicit shopper permission is strongly recommended (raw lines 144–150, 278–284). TEST uses the named DGFT closed-loop acquirer account and simulator without the Rakuten Pay app, not a proved LIVE outcome (raw lines 152–158, 286–292). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-android-component]] → pinned raw above.
