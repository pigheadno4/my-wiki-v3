# Retrieval checks — NAPAS card API-only

Q1. What is the page's purpose and scope, and what cannot be inferred? `source-adyen-docs-payment-methods-napas-card-api-only` describes an existing API-only merchant form plus NAPAS redirect, return via `/payments/details`, and webhook outcome if pending or no return. VN/VND and Web/iOS/Android are its `/paymentMethods` discovery parameters; neither form display nor redirect proves present merchant eligibility, authorization, capture or settlement. Raw lines 15–41, 150–228.

Q2. What central capability, prerequisites and warnings matter? Add NAPAS card in test Customer Area; the merchant form need not collect shopper details. The NAPAS-labeled guide unexpectedly uses `momo_atm` for discovery, payment and action, so preserve rather than normalize that identifier. `/payments` returns a redirect action; after return, submit decoded `redirectResult` to `/payments/details`; `Pending`/`Received` await AUTHORISATION webhook, and browser-close flows use AUTHORISATION/OFFER_CLOSED. TEST fixtures and live Customer Area request are separate. Raw lines 21–47, 62–65, 150–228, 230–243.

Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-napas-card-api-only]] → [[raw/adyen/docs/payment-methods/napas-card/api-only/2026-09-15]].
