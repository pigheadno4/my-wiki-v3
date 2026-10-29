# docs-payment-methods-bancontact-bancontact-mobile-android-drop-in — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bancontact-bancontact-mobile-android-drop-in]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-bancontact-bancontact-mobile-android-drop-in]] is the Bancontact **Mobile** Android Drop-in v5.0.0 add-on, not the Bancontact card route or the earlier-version guide (raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/android-drop-in/2026-09-15.md:5–21). It only specifies method-specific additions to the existing Drop-in flow. Its short text does not define app-switch/QR handling, return details or final authorization; the historical live penny-test recommendation is not a performed test or merchant enablement proof (raw lines 41–79).

## Q2 — What central capability, prerequisites, and warnings are stated?

Sessions and Advanced each require existing Android Drop-in at minimum v5.0.0 and Bancontact added in Customer Area. The guide adds no Bancontact-specific `/sessions` fields in Sessions, `/payments` fields in Advanced, or extra Drop-in configuration in either path; follow the parent integration for session creation or Drop-in launch (raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/android-drop-in/2026-09-15.md:23–67). It states Bancontact Mobile has no test platform and recommends a EUR 0.01 live penny test, without documenting an executed payment or current eligibility (raw lines 69–73).
