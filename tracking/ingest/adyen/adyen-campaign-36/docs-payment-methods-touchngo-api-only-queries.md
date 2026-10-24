# docs-payment-methods-touchngo-api-only — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a Touch'n Go add-on for an existing **API-only** integration with a merchant-owned form, MY/MYR discovery and a redirect action (source-adyen-docs-payment-methods-touchngo-api-only; raw lines 15–44, 347–361). The guide is a 2019-modified historical snapshot. Its TEST examples and redirect-result sample do not prove current merchant eligibility, live setup, actual authorization or settlement (raw lines 49–64, 395–402, 424–428). The examples show `/payments` at v68 and `/payments/details` at v72, with no general minimum API version stated (raw lines 49, 380).

Q2. What are its central capability, prerequisites and warnings?

The page asks for a prior API-only integration and Support addition in Customer Area, no Touch'n Go form fields, and `/paymentMethods` with `MY`/`MYR`; `/payments` uses `paymentMethod.type: touchngo` (raw lines 21–44). The merchant redirects to `action.url`, receives a URL-decoded `redirectResult` on return, and POSTs `/payments/details`; mobile/browser security and compatibility recommendations remain advice, not proof of a completed flow (raw lines 347–393). `Pending`/`Received` is unresolved until final `AUTHORISATION` webhook, with the guide's 30-minute offer-close condition; browser nonreturn also relies on webhooks, and live acceptance requires separate Support addition in live Customer Area (raw lines 404–428).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-touchngo-api-only]] → [[raw/adyen/docs/payment-methods/touchngo/api-only/2026-09-15]].
