# docs-payment-methods-online-banking-poland-android-drop-in retrieval checks

## Q1 — Purpose and route

Query: What is the Online banking Poland Android Drop-in page for, and what does the snapshot not prove?

Expected: A 2026-09-15-captured Android Drop-in add-on for existing Sessions and Advanced integrations, documenting request fields, optional submit-button display, Advanced redirect and test/live steps. It does not establish current merchant eligibility, an executable recipe from the abbreviated Kotlin snippet, or final payment success. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-poland-android-drop-in]] → [[raw/adyen/docs/payment-methods/online-banking-poland/android-drop-in/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-poland/android-drop-in/2026-09-15.md`. Evidence: heading lines 15–23, flow headings 25 and 298, raw lines 268–339 and 673–693.

## Q2 — Requirements, response and cautions

Query: How do the Sessions and Advanced Android Drop-in requirements differ, and what cautions apply to the examples?

Expected: Sessions requires existing Android Drop-in Sessions, Checkout API v68+, Customer Area method setup and shopperEmail <=50 characters in /sessions (raw lines 25–44). PL/PLN 1000 and app-style returnUrl are sample values (lines 46–67). Both flows document optional setSubmitButtonVisible, false hiding the button and true default (lines 268–287, 308–327). Advanced requires existing Android Drop-in, redirect handling, method setup, required shopperEmail <=50, and an issuer field not marked required in the table (lines 298–339). The example onlineBanking_PL/141/PLN 1000 and web returnUrl are examples (lines 341–364); RedirectShopper plus action.type redirect is not final success (lines 673–687). Both Kotlin config snippets have an extra anonymous brace block and are not complete executable recipes (lines 280–287 and 320–327). Test/live steps are at lines 290–296 and 689–693. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-poland-android-drop-in]] → [[raw/adyen/docs/payment-methods/online-banking-poland/android-drop-in/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-poland/android-drop-in/2026-09-15.md`.
