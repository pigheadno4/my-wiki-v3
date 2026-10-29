# Scalapay Android Component retrieval checks

## Q1 — What is this guide's scope and prerequisite?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-scalapay-android-component]]` → `[[raw/adyen/docs/payment-methods/scalapay/android-component/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-scalapay-android-component`. Full pinned raw path: `raw/adyen/docs/payment-methods/scalapay/android-component/2026-09-15.md`. Raw lines 15–32 and 137–146 scope it to existing Android Components Sessions/Advanced integrations, minimum 5.0.0, Customer Area method setup and an account-manager pricing eligibility check before activation. It does not prove live activation or payment success.

## Q2 — What central method setup and sample limits matter?

Use the same root/provider/concept/source/raw route. Raw lines 34–71 say Sessions needs no extra request or configuration parameters; lines 83–135 launch `PaymentMethodTypes.SCALAPAY` with instant Component snippets. Raw lines 148–231 give Advanced setup but the Compose example creates `cardComponent` and renders `instantComponent` (lines 198–210), so it is not copy-ready. Raw lines 233–262 show one Advanced `scalapay_3x` IT/EUR/return-URL example, with server library variants through line 594; no product-wide eligibility follows. Raw lines 596–602 route test cases and require a live Customer Area request before accepting live Scalapay payments.
