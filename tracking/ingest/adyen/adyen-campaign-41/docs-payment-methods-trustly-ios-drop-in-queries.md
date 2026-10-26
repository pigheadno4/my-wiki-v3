# docs-payment-methods-trustly-ios-drop-in retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-trustly-ios-drop-in]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 page is a Trustly add-on for an existing iOS Drop-in integration, with endpoint choice, version-tabbed no-extra-configuration statements and test/live setup (pinned raw lines 15–51). It provides no redirect result, return or final webhook sequence. It cannot prove current merchant enablement, payment success or receipt of funds; the related Trustly overview warns a successful AUTHORISATION can precede an unfunded transfer and chargeback (overview raw lines 38–53). Canonical source stem: `source-adyen-docs-payment-methods-trustly-ios-drop-in`.

## Q2 — What are prerequisites, version conditions and warnings?

The page requires an existing iOS Drop-in integration and Trustly in test Customer Area, says no extra Trustly-specific fields, and calls `/sessions` default for Drop-in v5.0.0+ while `/payments` serves additional use cases (pinned raw lines 21–33). Both v5+ and v4.x.x tabs say no Trustly-specific Drop-in integration; ordinary base requirements remain (lines 35–43). The See also link is to iOS Components despite Drop-in page identity (lines 53–57). TEST has a `YYMMDD-XXXX` Login ID/Personal number format and Customer Area status route; LIVE requires a separate live Customer Area request (lines 45–51). Any base-flow authorization remains distinct from funding under the overview's warning (overview raw lines 38–53). Canonical source stem: `source-adyen-docs-payment-methods-trustly-ios-drop-in`.
