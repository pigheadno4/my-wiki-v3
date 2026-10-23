# Retrieval checks — docs-payment-methods-cards-android-component-earlier-versions

Q1. What does this historical Android Card Component guide cover, and what is required before a card payment request?

A1. It covers Card Component v4.x.x for an existing Advanced-flow Android Components integration (raw lines 15–29). Cards must be added and a client key obtained; the app supplies country/currency in `/paymentMethods`, selects `scheme`, attaches the Card Component, and sends Component data to its server for `/payments` when the shopper proceeds to pay (raw lines 31–94, 134–142). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-android-component-earlier-versions]] → [[raw/adyen/docs/payment-methods/cards/android-component/earlier-versions/2026-09-15]].

Q2. What payment-outcome and example conflicts constrain use of this guide?

A2. `resultCode` supports shopper display and the outcome also arrives by webhook; `Authorised` still needs capture if manual capture applies, and 3D Secure may return other codes (raw lines 490–524). The observer snippet calls `sendPayment` on validity although prose requires shopper proceeding to pay (raw lines 94–103); storage-switch prose names `showStoredPaymentMethods` but snippet uses `.setShowStorePaymentField(false)` (raw lines 539–545); a stored-card example uses `ContAuth` and `UnscheduledCardOnFile` despite nearby shopper-proceeds wording (raw lines 548–581). Live checklist includes PCI DSS assessment and SAQ A (raw lines 858–870). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-android-component-earlier-versions]] → [[raw/adyen/docs/payment-methods/cards/android-component/earlier-versions/2026-09-15]].
