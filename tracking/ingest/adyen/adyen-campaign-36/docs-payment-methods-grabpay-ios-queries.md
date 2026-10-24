# GrabPay iOS chooser retrieval questions

## Q1 — What is this page's purpose and scope, and what cannot be inferred?

It is an **iOS navigation chooser** for GrabPay, linking method-specific Drop-in and Components guides (raw lines 15–27; [[source-adyen-docs-payment-methods-grabpay-ios]]). The page does not supply SDK versions, Wallet/PayLater conditions, country/currency eligibility, Customer Area setup, return handling or payment outcomes; those cannot be inferred from child links. Its source metadata says last modified 2019 (raw line 11), with the pinned capture dated 2026-09-15 (line 2), so the snapshot is not proof of current availability. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-grabpay-ios]] → [[raw/adyen/docs/payment-methods/grabpay/ios/2026-09-15]].

## Q2 — What integration options and prerequisite routes are visible?

The chooser labels **Drop-in** as an all-in-one UI route and **Components** as a prebuilt rendering route (raw lines 19–27). It points to general iOS Drop-in and Components **Sessions-flow** guides (line 29), but does not state that Sessions is the only possible server flow or give the actual child-guide requirements. No transaction authorization, capture or settlement follows from these navigation labels ([[source-adyen-docs-payment-methods-grabpay-ios]]). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-grabpay-ios]] → [[raw/adyen/docs/payment-methods/grabpay/ios/2026-09-15]].
