# Scalapay Android Drop-in retrieval checks

## Q1 — What is this guide's scope and prerequisite?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-scalapay-android-drop-in]]` → `[[raw/adyen/docs/payment-methods/scalapay/android-drop-in/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-scalapay-android-drop-in`. Full pinned raw path: `raw/adyen/docs/payment-methods/scalapay/android-drop-in/2026-09-15.md`. Raw lines 15–39 describe existing Android Drop-in Sessions/Advanced v5.0.0+ with Customer Area method setup and account-manager pricing eligibility check before activation. The page does not establish live enablement, shopper approval or payment success.

## Q2 — Which request conditions and sample limits matter?

Use the same root/provider/concept/source/raw route. Raw lines 45–71 make `/sessions` the v5+ default and mark countryCode plus shopper first/last name required in both tables; country rows list IT/FR/PT/ES. The `/payments` table lists optional airline/lodging data with an either/or instruction. Raw lines 73–95 show only IT/EUR `scalapay_3x`; no wider currency/product/market inference follows. Raw lines 228/307 show lowercase `countryCode` in C#/Go model snippets, unlike surrounding properties. Raw lines 430–438 say no added Drop-in configuration; lines 440–446 route test cases and live Customer Area request without proving a live transaction.
