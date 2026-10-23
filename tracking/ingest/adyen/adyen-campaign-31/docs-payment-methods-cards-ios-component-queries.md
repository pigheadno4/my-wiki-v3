# iOS Card Component retrieval checks

Q1. What integration does this card guide extend, and what setup and flow choices precede using it?

It extends an existing **iOS Components** integration. Choose the server-side Sessions or Advanced flow already built, and add cards in Customer Area before beginning. The guide calls `/sessions` the default with Components v5.0.0 or later; additional use cases can use `/payments`. The basic card request needs no extra card-specific fields. Raw lines 19–46. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-ios-component]] → [[raw/adyen/docs/payment-methods/cards/ios-component/2026-09-15]].

Q2. What material consent, example-conflict and live-payment boundaries must be retained?

The page strongly recommends explicit permission for future recurring payments (raw lines 207–217). Its Advanced prose says `showsStorePaymentMethodField: true` shows a storage checkbox, while the adjacent Swift snippet sets `false`; selected-checkbox data is described for `didSubmit` (raw lines 851–869). Its Sessions examples also differ between `askForConsent` and `enabled` (raw lines 225–268). Token webhooks, test `test_` values, idempotency-key examples and client configuration do not prove authorization, capture or settlement. Before live card payments the guide calls for testing, live card setup and PCI DSS assessment plus SAQ A submission (raw lines 2411–2421). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-ios-component]] → [[raw/adyen/docs/payment-methods/cards/ios-component/2026-09-15]].
