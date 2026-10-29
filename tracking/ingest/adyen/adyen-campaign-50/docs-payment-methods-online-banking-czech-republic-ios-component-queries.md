# docs-payment-methods-online-banking-czech-republic-ios-component retrieval checks

## Q1 — Purpose and route

Query: What is the Czech Republic iOS Component guide for, and what does this snapshot not prove?

Expected: A 2026-09-15-captured iOS Components add-on for existing Sessions and Advanced integrations, documenting request additions, initialization, redirect and test/live steps. It does not prove current enablement, executable Swift code, or final payment success. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-czech-republic-ios-component]] → [[raw/adyen/docs/payment-methods/online-banking-czech-republic/ios-component/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-czech-republic/ios-component/2026-09-15.md`. Evidence: heading lines 15–23, flow headings 25 and 83, raw lines 50–73 and 101–123.

## Q2 — Requirements and source conflicts

Query: Which request fields and redirects apply to Czech Republic iOS Components Sessions and Advanced, and what example caveats matter?

Expected: Sessions requires existing iOS Components Sessions, Checkout API v68+, action.type redirect handling and Customer Area method setup, while specifying no extra /sessions parameters or method configuration (raw lines 25–48). Advanced requires existing iOS Components Advanced, action.type redirect handling and setup, with no extra configuration or /payments parameters in this guide (lines 83–99, 125–129). These no-extra-field statements do not override the separate API-only issuer-selection route [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]. Initialization prose names OnlineBankingComponent, but both snippets use None.self and a configuration object despite the no-extra-configuration prose (lines 50–73, 101–123). Advanced Components prerequisite links to integration=Drop-in while its redirect link targets Components (lines 91–92); verify the iOS Components base route. Test with real details/small amounts, check test Payment list and add method for live are captured instructions, not test evidence (lines 75–81, 131–137). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-czech-republic-ios-component]] → [[raw/adyen/docs/payment-methods/online-banking-czech-republic/ios-component/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-czech-republic/ios-component/2026-09-15.md`.
