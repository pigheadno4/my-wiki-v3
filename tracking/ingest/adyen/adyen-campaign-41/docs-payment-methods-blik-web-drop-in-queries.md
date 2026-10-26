# docs-payment-methods-blik-web-drop-in retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-blik-web-drop-in]].

## Q1 — What is this source for, and what cannot be inferred?

The 2020-modified guide captured 2026-09-15 adds BLIK to Web Drop-in, with a no-extra-field `/sessions` section and `/payments` BLIK-code and One Click sections (pinned raw lines 5–19, 21–48, 62–88, 455–478). It does not prove current merchant enablement, One Click certification or a completed payment. Its `Pending`/`await` response means the shopper still has to complete payment in the app, with outcome delivered by `AUTHORISATION` webhook (lines 397–439). Canonical source stem: `source-adyen-docs-payment-methods-blik-web-drop-in`.

## Q2 — What are central prerequisites, flow and warnings?

The page requires existing Web Drop-in v3.9.0+ and BLIK added in test Customer Area; if using Web Drop-in v6, it instructs importing the resources needed for BLIK, while Sessions v5+ is called the default and needs no BLIK-specific extra fields (pinned raw lines 21–48). Under `/payments`, code flow uses PL/PLN discovery and a six-digit shopper `blikCode`; examples use `777987`, while the test instruction uses `999000` (lines 68–109, 441–451). `Pending`/`await` requires a waiting screen; final AUTHORISATION webhook `success` reports outcome, despite a nearby sentence suggesting the original `resultCode` for shopper status (lines 397–439). One Click requests consent with shopper reference, store flag and CardOnFile model; a `recurring.token.created` webhook supplies the stored ID if consent is given (lines 455–478, 546–552). The sample consent JSON lacks a comma and renders `storePaymentMethod` as a string; the app-label prose and object example differ in key casing (lines 480–500, 554–567). One Click live guidance additionally calls for BLIK certification/enablement before live Customer Area addition (lines 569–582). Canonical source stem: `source-adyen-docs-payment-methods-blik-web-drop-in`.
