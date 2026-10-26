# Q1 — Purpose, scope and limits

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ideal-web-component.md` → pinned raw.

The source is a 2026-09-15 iDEAL | Wero method add-on for an **existing Web Components** integration, divided by Sessions and Advanced server-side flow (raw `adyen/docs/payment-methods/ideal/web-component/2026-09-15.md:15-25,346-354`). It does not provide a complete base integration, establish current method enablement or prove a successful live transaction. The Sessions requirement states Checkout API v68+; the Advanced requirements do not state that minimum (raw lines 33-36, 350-354). No extra ordinary `/sessions` or `/payments` method parameters are requested (raw lines 38-42, 380-384), while recurring tokenization has its own standard parameters (raw lines 83-101, 395-413).

# Q2 — Central capability, prerequisites and warnings

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ideal-web-component.md`. For recurring retrieval, `wiki/adyen-index.md` → `wiki/concepts/adyen-tokenization.md` → the same source.

Import and initialize the Web `Redirect` component with `type: 'ideal'`; both flows require an existing Web Components integration, redirect handling and Customer Area method addition (raw `adyen/docs/payment-methods/ideal/web-component/2026-09-15.md:25-72,346-384`). Recurring iDEAL | Wero payments go through SEPA Direct Debit token creation; a `recurring.token.created` webhook returns `storedPaymentMethodId`, and later token payments are restricted here to shopper-absent `UnscheduledCardOnFile` or `Subscription` (raw lines 74-101, 386-413). The sample `Received` response is intermediate; webhooks track payment success (raw lines 301-306,613-618). TEST is described as unreliable, so the guide **recommends** live penny tests; TEST simulation applies only when the environment is working, and expiration can result in `Pending` or `Received` (raw lines 308-344,620-656). The snapshot alone does not establish current eligibility or an executed test.
