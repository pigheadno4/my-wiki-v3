# MobilePay for Android retrieval checks

Q1. What purpose and scope, and what cannot be inferred?

A1. This 2026-09-15 page is a MobilePay Android chooser, linking a Drop-in child for an all-in-one UI and a Components child naming `InstantPaymentComponent` for redirect handling (raw lines 15-27). It says to create the main integration first and lists Android Drop-in and Components in Sessions and Advanced flows (lines 29-36). It does not itself establish API/SDK minimums, request fields, return mechanics, account eligibility, testing or payment outcomes. Canonical source stem: `source-adyen-docs-payment-methods-mobilepay-android`. Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-android-sdk]] → [[source-adyen-docs-payment-methods-mobilepay-android]]`.

Q2. What are the central capability, prerequisites and warnings?

A2. The choice is Android Drop-in or Components; the latter's route text says `InstantPaymentComponent` handles the redirect to MobilePay (raw lines 19-27). The stated prerequisite is to create the main integration first, with four linked Sessions/Advanced guides according to UI choice (lines 29-36). The chooser does not document the child integration behavior or prove an enabled merchant account or completed payment. Canonical source stem: `source-adyen-docs-payment-methods-mobilepay-android`. Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-android-sdk]] → [[source-adyen-docs-payment-methods-mobilepay-android]]`.
