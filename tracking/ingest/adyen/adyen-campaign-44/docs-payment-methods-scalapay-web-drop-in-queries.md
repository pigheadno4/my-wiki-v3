# Scalapay Web Drop-in retrieval checks

## Q1 — Purpose, scope, and what not to infer

**Question:** What does the captured Scalapay Web Drop-in add-on cover?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-scalapay-web-drop-in]] → [[raw/adyen/docs/payment-methods/scalapay/web-drop-in/2026-09-15]]. It describes adding Scalapay to existing Sessions or Advanced Web Drop-in, field tables, TEST examples and account setup (raw lines 15–69, 71–447). It does not prove current merchant enablement or successful payment, nor provide a method-specific capture/refund/final-outcome procedure. [[source-adyen-docs-payment-methods-scalapay]] supplies the BNPL product and snapshot feature matrix; the generic tokenization See also link here does not establish recurring support.

## Q2 — Central capability, prerequisites, and warnings

**Question:** Which prerequisites and request fields differ by Sessions and Advanced paths?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-scalapay-web-drop-in]] → [[raw/adyen/docs/payment-methods/scalapay/web-drop-in/2026-09-15]]. Each path requires its matching existing Web Drop-in flow and Customer Area addition; activation defaults to standard pricing and account-manager eligibility check for Enterprise pricing (raw lines 21–39). The guide calls /sessions the Drop-in v5+ default and /payments an additional-use-case route; both tables mark countryCode in IT/FR/PT/ES and shopperName required (raw lines 45–69). The Advanced sample uses scalapay_3x and EUR, but C#/Go snippets have lowercase countryCode member names, so do not treat them as verified compilable requests (raw lines 71–96, 225–234, 306–314). The page says no Scalapay-specific Drop-in configuration; test and live Customer Area steps are distinct (raw lines 430–440).
