# docs-payment-methods-bancontact-bancontact-card-android-component — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bancontact-bancontact-card-android-component]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-bancontact-bancontact-card-android-component]] is the pinned Bancontact **card** Android Component guide for v5.0.0, released October 2023, with Sessions and Advanced prerequisites; it points older versions to another guide (raw/adyen/docs/payment-methods/bancontact/bancontact-card/android-component/2026-09-15.md:15–39). It is not Bancontact Mobile app-switch/QR documentation. This page's setup and TEST examples do not prove current SDK compatibility, WIP eligibility, merchant enablement or a successful live payment (raw lines 69–98, 126–149, 465–504).

## Q2 — What central capability, prerequisites, and warnings are stated?

An existing Android Components Sessions or Advanced integration at minimum SDK v5.0.0 and Bancontact card in Customer Area are prerequisites. Bancontact card adds no method-specific `/sessions` or `/payments` fields and no extra Component configuration in the base flow (raw/adyen/docs/payment-methods/bancontact/bancontact-card/android-component/2026-09-15.md:23–67). WIP recurring is distinct and requires signup, eligibility, Support and amount limits; explicit shopper permission is strongly recommended, the first consent transaction uses SCA, and token issuance occurs after settlement through `recurring.token.created` (raw lines 69–113). Later token charges send `storedPaymentMethodId`, the same shopper reference, `ContAuth` and `Subscription` or `UnscheduledCardOnFile` (raw lines 115–124). The co-badged Visa test-card fixture may route to Bancontact or Visa depending on setup, and live Customer Area setup is separate (raw lines 465–504).
