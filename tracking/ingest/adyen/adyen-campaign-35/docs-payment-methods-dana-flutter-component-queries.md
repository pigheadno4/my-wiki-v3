# Retrieval queries — docs-payment-methods-dana-flutter-component

## Q1 — purpose and limits

**Query:** What does the DANA Flutter Component page cover, and what cannot be inferred from it?

**Answer:** It is a DANA-specific supplement to existing Flutter **Components** Sessions and Advanced integrations, including a separate recurring-token route. It does not show DANA-specific Flutter Component construction, a Flutter SDK minimum, an eligibility matrix, a final redirect-return result contract, or successful authorization/settlement. IDR amounts appear as recurring examples; country/currency and display limits belong to the separate DANA overview. The page's TEST/LIVE wording and live Customer Area request do not prove current activation. Raw lines 15–23, 25–46, 48–85, 286–318, 320–357 and 558–566; canonical source stem [[source-adyen-docs-payment-methods-dana-flutter-component]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-dana-flutter-component]] → [[raw/adyen/docs/payment-methods/dana/flutter-component/2026-09-15]].

## Q2 — prerequisites, token fields and link warning

**Query:** What must the base Sessions/Advanced flows do, and how does recurring differ?

**Answer:** The Sessions text requires existing Flutter Components, Checkout API v68+, redirect handling and DANA added in Customer Area; Advanced requires existing Advanced Flutter Components, redirect handling and Customer Area addition, without restating v68+ in its table. No DANA-specific extra base `/sessions` or `/payments` fields/configuration are stated. Recurring adds `storePaymentMethod` and `shopperReference` to `/payments`; after the initial payment settles, `recurring.token.created` gives the stored ID. Later requests include that ID, the shopper reference, `ContAuth`, and an interval-specific processing model. Both prerequisite links are wrong for Components: Sessions points to Advanced Drop-in and Advanced to Advanced Drop-in; adjacent links confirm Components routes. Raw lines 25–85 and 296–357; canonical source stem [[source-adyen-docs-payment-methods-dana-flutter-component]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-dana-flutter-component]] → [[raw/adyen/docs/payment-methods/dana/flutter-component/2026-09-15]].
