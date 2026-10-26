# Swish for iOS retrieval checks

Q1. What purpose and scope, and what cannot be inferred?

A1. This 2026-09-15 source is a Swish iOS chooser: it links to a Drop-in child for an all-in-one UI and a Components child naming `InstantPaymentComponent` (raw lines 15-27). It says to build the main integration first and links iOS Drop-in and Components for Sessions and Advanced (lines 29-36). The chooser does not itself establish request fields, minimum SDK/API versions, QR behavior, testing, eligibility, live setup or payment outcomes; those require child or main-guide evidence. Canonical source stem: `source-adyen-docs-payment-methods-swish-ios`. Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-swish-ios]]`.

Q2. What are the central capability, prerequisites and warnings?

A2. The navigation offers Swish through iOS Drop-in or iOS Components, with the Components link naming `InstantPaymentComponent` (raw lines 19-27). It directs merchants to create the main integration first and supplies separate Sessions/Advanced links for each UI choice (lines 29-36). These links are routes, not evidence that Swish is enabled, that any payment action works, or that a live payment succeeded. Canonical source stem: `source-adyen-docs-payment-methods-swish-ios`. Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-swish-ios]]`.
