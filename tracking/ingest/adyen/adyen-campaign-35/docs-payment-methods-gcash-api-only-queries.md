# Retrieval queries — docs-payment-methods-gcash-api-only

## Q1 — purpose and limits

**Query:** What does the GCash API-only guide cover, and what cannot it prove?

**Answer:** It is a method-specific supplement to an existing API-only Advanced redirect integration. It covers merchant-built method selection, PH/PHP `/paymentMethods` discovery, and a separate recurring-token route; the main integration handles full payment/return flow. A `gcash` method in the response, a redirect, a TEST example or a LIVE Customer Area request does not prove current merchant eligibility, authorization or settlement. It gives no complete ordinary `/payments` payload or final result contract. Raw lines 15–29, 38–89, 91–126 and 327–335; canonical source stem [[source-adyen-docs-payment-methods-gcash-api-only]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gcash-api-only]] → [[raw/adyen/docs/payment-methods/gcash/api-only/2026-09-15]].

## Q2 — discovery, form and recurring warnings

**Query:** Which GCash discovery and recurring fields matter, and which instructions conflict?

**Answer:** For `/paymentMethods`, the table lists `countryCode: PH`, `amount.currency: PHP`, amount value and a channel such as Web/iOS/Android; its example omits channel. The flow sketch says the shopper enters details in the merchant-built form, but the dedicated form section says no shopper information needs collecting. The ordinary `/payments` line adds no GCash-specific fields, whereas recurring token creation adds `storePaymentMethod: true` and a shopper reference of at least three characters. A `recurring.token.created` webhook supplies the stored ID after the initial payment settles; later `/payments` calls use that ID, shopper reference, `ContAuth`, and Subscription or UnscheduledCardOnFile by interval. Raw lines 31–53, 57–89 and 91–126; canonical source stem [[source-adyen-docs-payment-methods-gcash-api-only]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gcash-api-only]] → [[raw/adyen/docs/payment-methods/gcash/api-only/2026-09-15]].
