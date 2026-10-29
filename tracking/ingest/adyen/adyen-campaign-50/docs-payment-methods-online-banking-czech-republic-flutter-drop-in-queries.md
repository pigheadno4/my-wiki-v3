# docs-payment-methods-online-banking-czech-republic-flutter-drop-in retrieval checks

## Q1 — Purpose and route

Query: What is the Online banking Czech Republic Flutter Drop-in page for, and what does it not prove?

Expected: A 2026-09-15-captured Flutter Drop-in add-on for existing Sessions and Advanced flows, covering redirect prerequisites, setup and test/live guidance. It does not prove current enablement, payment execution or final paid status. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-czech-republic-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/online-banking-czech-republic/flutter-drop-in/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-czech-republic/flutter-drop-in/2026-09-15.md`. Evidence: heading lines 15–23 and flow headings 25 and 58.

## Q2 — Requirements and discrepancy

Query: What request and redirect requirements does the Flutter Drop-in guide state, and where do its routes/setup instructions diverge?

Expected: Sessions requires existing Flutter Drop-in Sessions, Checkout API v68+, redirect handling, and says contact Support to add the method; it states no extra /sessions or configuration parameters (raw lines 25–48). Advanced requires existing Flutter Drop-in Advanced, redirect handling and Customer Area setup; it states no extra configuration or /payments parameters (lines 58–80). The no-extra-fields claim is scoped to Drop-in and does not override selected issuer handling in the separate [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]. Sessions prerequisite points to Advanced even though its redirect/request links target Sessions (lines 33, 35, 42); Support versus Customer Area setup wording differs (lines 36, 68). Test with real details/small amounts and check test Payment list before adding for live are captured instructions (lines 50–56, 82–88), not test evidence. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-czech-republic-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/online-banking-czech-republic/flutter-drop-in/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-czech-republic/flutter-drop-in/2026-09-15.md`.
