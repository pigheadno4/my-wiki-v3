# Fixed queries — Online banking Poland React Native Component

## Q1 — purpose, scope and limits

**Query:** Does the captured Online banking Poland React Native Component guide support Sessions, and what does its redirect response prove?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/online-banking-poland/react-native-component` is a 2026-09-15-captured **Advanced-only** React Native Components add-on. It explicitly says React Native Components do **not** support Sessions. `RedirectShopper`/`action.type: redirect` represents bank handoff, not confirmed payment or current merchant entitlement. Method-level Przelewy24/PL/PLN context is in `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland.md` (full pinned `raw/adyen/docs/payment-methods/online-banking-poland/react-native-component/2026-09-15.md`, `## Sessions flow Component` lines 25–29; Advanced response lines 392–406). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-react-native-component.md`.

## Q2 — Advanced prerequisites, issuer and example caveats

**Query:** What does the captured React Native Components Advanced guide require for Poland online banking, and is issuer mandatory?

**Expected answer:** Advanced requires existing React Native Components, redirect handling and Customer Area method addition (pinned `raw/adyen/docs/payment-methods/online-banking-poland/react-native-component/2026-09-15.md`, `## Advanced flow Component` lines 31–41). The Components prerequisite links to a **Drop-in** base guide, so verify the right base route; this page states no Checkout API minimum. No extra method-specific configuration is needed (lines 43–47). In `/payments`, `shopperEmail` is required and at most 50 characters; `paymentMethod.issuer` is listed **without a required mark**, even though examples use `issuer: 141` with `onlineBanking_PL` (lines 49–84). The curl sample lacks a continuation after `-X POST` before `-d` (lines 64–84). The sample response is RedirectShopper/redirect, not finality (lines 392–406). Test status is checked in test Customer Area and live acceptance requires a live method request (lines 408–412). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-react-native-component.md`.
