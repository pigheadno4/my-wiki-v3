# docs-payment-methods-online-banking-czech-republic-android-component retrieval checks

## Q1 — Purpose and route

Query: What does Adyen's Online banking Czech Republic Android Component guide cover, and what does it not establish?

Expected: A 2026-09-15-captured Android Components add-on for existing Sessions and Advanced integrations, with module import, optional submit button, Component launch, redirect handling and test/live steps. It does not prove current merchant enablement or a successful payment. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-czech-republic-android-component]] → [[raw/adyen/docs/payment-methods/online-banking-czech-republic/android-component/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-czech-republic/android-component/2026-09-15.md`. Evidence: heading lines 15–23, Sessions lines 25–42, Advanced lines 153–161.

## Q2 — Request, Component and test details

Query: Which extra fields, imports and redirect conditions apply in the Android Components Sessions and Advanced flows?

Expected: Sessions requires existing Android Components Sessions, Checkout API v68+, redirect handling for action.type redirect and Customer Area method setup; no extra /sessions parameters are stated (raw lines 25–42). Import onlineBankingCZ and components-compose only for Compose; launch OnlineBankingCZComponent with the scoped Compose or view variant (lines 44–65, 90–143). Both flows show optional setSubmitButtonVisible, false hiding the button, true default (lines 67–87, 186–207). Advanced requires existing Android Components, action.type redirect handling and setup; the example selects from /paymentMethods and the guide says no extra /payments parameters (lines 153–161, 209–270). Do not generalize that no-extra-fields statement to API-only bank selection; see [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]. The page's test instruction is real payment details and small amounts, test Payment list status, and Customer Area addition for live acceptance (lines 145–151, 272–278); it does not prove testing occurred. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-czech-republic-android-component]] → [[raw/adyen/docs/payment-methods/online-banking-czech-republic/android-component/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-czech-republic/android-component/2026-09-15.md`.
