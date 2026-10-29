# Cash App Pay Android Drop-in retrieval checks

## Q1 — Purpose and scope

Query: What does the Cash App Pay Android Drop-in guide add, and does it prove a current live payment?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-pay-android-drop-in.md` → `raw/adyen/docs/payment-methods/cash-app-pay/android-drop-in/2026-09-15.md`. Canonical stem: `/payment-methods/cash-app-pay/android-drop-in`; raw heading `# Cash App Pay Drop-in integration` at line 14. Expected answer: a 2026-09-15-captured method add-on to existing Android Drop-in Sessions or Advanced integration, explicitly for v5.0.0 released October 2023 with an earlier-versions route. It covers no-extra-method-field/configuration guidance, outcomes and tokenization overview; it is Cash App Pay, not Cash App Afterpay, and does not demonstrate merchant enablement or live payment. Raw lines 14–64, 80–90. The approved `source-adyen-docs-payment-methods-cash-app-pay` overview is a separate route for captured US/USD method context.

## Q2 — Prerequisites, pending result and later payment

Query: What do Sessions and Advanced require, and how should Received, Authorised and tokenization be read?

Expected route: same root/provider/concept/source/raw chain. Both flow sections require an existing Android Drop-in integration at v5.0.0+ and Cash App Pay added in Customer Area; neither adds method-specific /sessions or /payments fields or configuration, but base integration requirements still apply (raw lines 20–64). The guide says use /payments/details resultCode and an asynchronous outcome webhook. **Received** leaves final status unknown and points to an AUTHORISATION webhook update; **Authorised** is successful in the table, but a merchant using manual capture must capture separately. Cancelled, Error and Refused have distinct shopper guidance (raw lines 66–78). Tokenization for recurring/card-on-file is described, with explicit permission strongly recommended, but no Android token-creation recipe is given. Test magic values and live Customer Area addition are documented steps, not executed proof (raw lines 80–90).
