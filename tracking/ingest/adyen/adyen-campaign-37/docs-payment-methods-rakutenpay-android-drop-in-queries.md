# Rakuten Pay Android Drop-in retrieval checks

## Q1 — Purpose, scope, and non-inferences

`source-adyen-docs-payment-methods-rakutenpay-android-drop-in` is the 2026-09-15 method-specific add-on for existing Android Drop-in integrations using either Sessions or Advanced server-side flow (raw lines 15–34, 84–92). It does not by itself establish a standalone integration, current eligibility, a live Rakuten Pay app handoff, approval for recurring/card-on-file use or a completed payment. The described TEST path uses a DGFT simulator without the Rakuten Pay app (raw lines 74–82). Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-android-drop-in]] → [[raw/adyen/docs/payment-methods/rakutenpay/android-drop-in/2026-09-15]].

## Q2 — Central capability, prerequisites, warnings

Sessions requires an existing Android Sessions Drop-in and Checkout API v68+, Customer Area setup, and no extra `/sessions` parameters (raw lines 29–40). Advanced requires an existing Android Drop-in with redirect handling, Customer Area setup and no extra `/payments` parameters (raw lines 86–92, 116–120). Both show optional submit-button visibility configuration (raw lines 44–62, 96–114). Recurring card-on-file is review/application-gated, with a restriction when there is no periodic cadence and a strong recommendation to ask shopper permission; TEST uses the named DGFT closed-loop acquirer account and simulator (raw lines 66–82, 122–136). Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-android-drop-in]] → [[raw/adyen/docs/payment-methods/rakutenpay/android-drop-in/2026-09-15]].
