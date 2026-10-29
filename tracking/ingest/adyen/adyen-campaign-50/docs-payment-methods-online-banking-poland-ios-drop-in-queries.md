# Fixed queries — Online banking Poland iOS Drop-in

## Q1 — purpose, scope and limits

**Query:** What does the captured Poland iOS Drop-in guide establish, and what does its redirect response not establish?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/online-banking-poland/ios-drop-in` is a 2026-09-15-captured iOS Drop-in Sessions/Advanced add-on for required shopper email, Advanced issuer/redirect and test/live setup. `RedirectShopper`/`action.type: redirect` is a bank handoff, not confirmed payment or live account enablement. Method-level Przelewy24 PL/PLN context is in `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland.md` (full pinned `raw/adyen/docs/payment-methods/online-banking-poland/ios-drop-in/2026-09-15.md`, `# Online banking Poland iOS Drop-in` lines 15–23; Advanced response lines 643–657). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-ios-drop-in.md`.

## Q2 — flow requirements, issuer and examples

**Query:** What are the Sessions and Advanced iOS Drop-in requirements for Online banking Poland, and is issuer required?

**Expected answer:** Sessions requires existing iOS Drop-in Sessions, Checkout API v68+, Customer Area setup and `shopperEmail` at most 50 characters in `/sessions` (pinned `raw/adyen/docs/payment-methods/online-banking-poland/ios-drop-in/2026-09-15.md`, `## Sessions flow Drop-in` lines 25–44). Both flows say no method-specific configuration (lines 268–272, 294–298). Advanced requires existing iOS Drop-in Advanced, redirect handling and Customer Area setup; `shopperEmail` is required in `/payments`, while `paymentMethod.issuer` is listed **without a required mark** (lines 282–309). The Advanced table does not specify the Sessions v68 minimum. Samples use `onlineBanking_PL`, `issuer: 141`, PLN and a website-style return URL; the issuer is an example, and the URL should be checked against iOS return handling (lines 311–335). Curl snippets lack continuation after `-X POST` and some SDK snippets omit request construction (lines 50–67, 69–135, 315–335). Advanced response is RedirectShopper/redirect, not finality (lines 643–657). Test status is checked in test Customer Area, and live acceptance requires a live method request (lines 274–280, 659–665). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-ios-drop-in.md`.
