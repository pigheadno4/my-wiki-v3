# Zip Android Component retrieval checks

## Q1 — What version and integration does this page cover, and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-zip-android-component]]` → `[[raw/adyen/docs/payment-methods/zip/android-component/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-zip-android-component`. Full pinned raw path: `raw/adyen/docs/payment-methods/zip/android-component/2026-09-15.md`. Raw lines 15–39 identify an Android Components Zip guide for v5.0.0, with Sessions/Advanced prerequisites and a separate route for earlier versions. The captured page does not prove current merchant eligibility, live setup or payment success.

## Q2 — What method-specific API and Component additions are needed?

Use the same root/provider/concept/source/raw route. Raw lines 41–67 say Zip needs no additional method-specific fields in Sessions `/sessions` or Advanced `/payments`, and no additional Zip Component configuration. The base flow remains required; Sessions continues by creating a checkout session, Advanced by launching the Component. Raw lines 69–75 give test credentials/test-area checks and a separate live Customer Area request. Do not generalize the no-extra-fields statement to earlier versions or other integration types.
