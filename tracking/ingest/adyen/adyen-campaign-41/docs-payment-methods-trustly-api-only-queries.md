# docs-payment-methods-trustly-api-only retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-trustly-api-only]].

## Q1 — What is this source for, and what cannot be inferred?

The 2023-modified guide captured 2026-09-15 adds Trustly to an existing API-only integration: merchant form/discovery, server `/payments`, redirect, `/payments/details`, result and webhook handling (pinned raw lines 5–26, 28–49, 361–438). Its `RedirectShopper` action is intermediate (lines 361–375). It does not prove current merchant/bank enablement, that a shopper returned, or receipt of funds. Its Authorised/three-day row conflicts with the overview's explicit authorized-but-unfunded and chargeback warning (this guide line 426; [[source-adyen-docs-payment-methods-trustly]] raw lines 38–53). Canonical source stem: `source-adyen-docs-payment-methods-trustly-api-only`.

## Q2 — What are the central prerequisites, flow and warnings?

The guide requires existing API-only integration and Trustly added in test Customer Area (pinned raw lines 21–26). Optional `/paymentMethods` discovery uses supported country/currency, minor-unit amount and Web/iOS/Android channel; SE/SEK are examples (lines 34–41). The server sends `paymentMethod.type: trustly` and a shopper country code for hosted-page preselection, with QZ as the stated Kosovo exception (lines 43–49); its examples include a return URL (lines 53–70). After redirect, URL-decoded `redirectResult` goes to `/payments/details`; Pending/Received awaits AUTHORISATION webhook, and missing return also relies on webhooks (lines 377–438). Mobile default-browser and in-app GET browser choices are recommendations (lines 379–385). An Authorised result is not guaranteed funding under the related overview; LIVE acceptance separately requires a live Customer Area request (this guide lines 426, 446; overview raw lines 38–53). Canonical source stem: `source-adyen-docs-payment-methods-trustly-api-only`.
