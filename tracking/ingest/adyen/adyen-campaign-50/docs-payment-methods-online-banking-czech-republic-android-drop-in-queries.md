# Fixed retrieval checks — docs-payment-methods-online-banking-czech-republic-android-drop-in

## Q1 — Find Android Drop-in purpose and flow scope

- Query: What does the Czech online banking Android Drop-in page add to Sessions and Advanced requests, and how does it differ from API-only issuer selection?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-android-drop-in.md` → `raw/adyen/docs/payment-methods/online-banking-czech-republic/android-drop-in/2026-09-15.md`. Compare `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-api-only.md` only for the UI-mode distinction.
- Expected: Existing Sessions Android Drop-in with Checkout API v68+ and method setup (raw lines 25–34); no method-specific `/sessions` parameters (36–40). Existing Advanced Android Drop-in, redirect handling and method setup (75–83); no method-specific `/payments` parameters (108–112). The API-only guide separately has merchant issuer selection and example type/issuer fields; do not universalize its request example to Drop-in.
- Scope: The v68 floor is stated in Sessions requirements only. No-additional-parameters refers to method additions, not to an empty base request. Method overview `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic.md` supplies CZ/CZK redirect context, not account entitlement.

## Q2 — Recover optional configuration and test/live qualifications

- Query: How does this Android Drop-in guide configure the submit button and describe test and live readiness?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-android-drop-in.md` → pinned raw.
- Expected: `setSubmitButtonVisible(false)` hides the button; default true; row unmarked and thus optional in both flows (raw lines 42–63, 85–106). Advanced prerequisites explicitly include redirect handling for `action.type: redirect` (79–83). Both test sections say use real payment details and small amounts, inspect test payment status in Customer Area > Payments > Payment list, and add the method in Customer Area for live acceptance (65–73, 114–120).
- Scope: The source was captured 2026-09-15. Test instructions do not prove an actual test, final authorisation, present capability or live merchant configuration.
