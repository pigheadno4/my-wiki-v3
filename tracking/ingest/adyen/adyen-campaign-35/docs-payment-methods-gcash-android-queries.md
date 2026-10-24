# docs-payment-methods-gcash-android — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

This is a GCash Android **integration chooser**, routing to a Drop-in child guide, a Components/`InstantPaymentComponent` child guide and four Android main integration guides (source-adyen-docs-payment-methods-gcash-android; raw lines 15–36). It does not itself establish current merchant eligibility, SDK/API versions, the full redirect/return procedure or a successful payment (raw lines 19–36).

Q2. What is the central capability, prerequisite and warning?

The page calls Drop-in an all-in-one UI option and Components an `InstantPaymentComponent` route for the redirect to GCash (raw lines 21–27). It directs readers to build the main integration first and lists Sessions and Advanced base routes for both Drop-in and Components (raw lines 29–36). The child pages, not this chooser, are needed for method-specific setup or outcome semantics; a redirect-handling label alone is not payment authorization (raw lines 25–36).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gcash-android]] → [[raw/adyen/docs/payment-methods/gcash/android/2026-09-15]].
