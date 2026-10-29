# docs-payment-methods-bancontact-bancontact-mobile-web-component — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bancontact-bancontact-mobile-web-component]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-bancontact-bancontact-mobile-web-component]] is the Bancontact **Mobile** Web Component add-on: desktop displays QR, mobile switches to the Bancontact app with QR fallback, and tablet offers both (raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/web-component/2026-09-15.md:15–25). It is not the Bancontact card integration or a standalone payment-result guide. The 2019 `last_modified` metadata coexists with v6 and v72 examples, and the page's setup/snippets do not prove current compatibility, WIP eligibility or live-payment success (raw lines 5–11, 39–45, 143–165, 482–486).

## Q2 — What central capability, prerequisites, and warnings are stated?

An existing Web Components integration and Bancontact Mobile setup in test Customer Area are prerequisites. Enable 3DS2 Additional Fields in Customer Area to receive `bcmcmobile.urlIntent`; the base `/sessions` or `/payments` path is described as needing no Bancontact-specific additional request fields (raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/web-component/2026-09-15.md:27–52). Web Components v6 imports/mounts `BcmcMobile`, while v5.x.x or earlier uses `checkout.create('bcmc_mobile')` (raw lines 39–45, 54–84). WIP recurring requires consent guidance, signup/eligibility, Support enablement and limits; after settlement, the token webhook provides `storedPaymentMethodId` for later `ContAuth` token requests (raw lines 86–141). The page says there is no Bancontact Mobile test platform despite test-area and TEST request examples, and recommends a live penny test without documenting one (raw lines 31–37, 147–165, 482–486).
