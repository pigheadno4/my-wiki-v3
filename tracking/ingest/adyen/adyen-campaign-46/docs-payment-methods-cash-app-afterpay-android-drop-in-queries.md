# Cash App Afterpay Android Drop-in retrieval checks

## Q1 — What version and integration does this guide cover, and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-cash-app-afterpay-android-drop-in]]` → `[[raw/adyen/docs/payment-methods/cash-app-afterpay/android-drop-in/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-cash-app-afterpay-android-drop-in`. Full pinned raw path: `raw/adyen/docs/payment-methods/cash-app-afterpay/android-drop-in/2026-09-15.md`. Raw lines 15–39 identify an Android Drop-in v5.0.0 guide, with separate Sessions and Advanced prerequisites and a link for earlier versions. The captured page does not establish current account eligibility, live activation or payment success.

## Q2 — What does this version add to API/configuration, and how is it tested?

Use the same root/provider/concept/source/raw route. Raw lines 41–67 say neither `/sessions` nor `/payments` needs Cash App Afterpay-specific extra fields, and neither Drop-in flow needs method-specific configuration; the base integration remains required. Raw lines 69–87 describe US sandbox shopper/test-card setup and a separate live Customer Area request. The no-extra-fields statement is specific to this Android Drop-in v5.0.0 page, not a general rule for other versions or integrations.
