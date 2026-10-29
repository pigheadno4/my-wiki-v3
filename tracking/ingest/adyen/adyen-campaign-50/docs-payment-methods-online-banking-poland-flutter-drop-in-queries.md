# docs-payment-methods-online-banking-poland-flutter-drop-in retrieval checks

## Q1 — Purpose and route

Query: What does the Online banking Poland Flutter Drop-in add-on cover, and what does this snapshot not establish?

Expected: The 2026-09-15-captured Flutter Drop-in guide adds Online banking Poland to existing Sessions or Advanced flow, with request fields, redirect and test/live instructions. It does not prove current account enablement or final successful payment. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-poland-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/online-banking-poland/flutter-drop-in/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-poland/flutter-drop-in/2026-09-15.md`. Evidence: heading lines 15–23, flow headings 25 and 282, raw lines 643–663.

## Q2 — Central requirements and conflicts

Query: What are the Flutter Sessions and Advanced requirements, response state, and source caveats?

Expected: Sessions requires existing Flutter Drop-in Sessions, Checkout API v68+, redirect handling, Support-assisted method setup and shopperEmail <=50 characters in /sessions (raw lines 25–46). PL/PLN 1000 and the app-style returnUrl are sample values (lines 48–68). Advanced requires existing Flutter Drop-in Advanced, redirect handling, method setup in Customer Area, required shopperEmail <=50, and an issuer field not marked required in the table (lines 282–309). The example onlineBanking_PL/141/PLN 1000 and web returnUrl are examples (lines 311–331); RedirectShopper and action.type redirect are intermediate, not final success (lines 643–657). Both flows say no extra configuration (lines 270–274, 294–298); test/live steps are at lines 276–280 and 659–663. Warn that Sessions base link points to Advanced while naming Sessions (line 33), and Support versus Customer Area setup wording differs (lines 36, 292). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-poland-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/online-banking-poland/flutter-drop-in/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-poland/flutter-drop-in/2026-09-15.md`.
