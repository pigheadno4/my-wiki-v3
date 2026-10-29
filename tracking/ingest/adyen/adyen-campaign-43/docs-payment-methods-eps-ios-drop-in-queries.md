# docs-payment-methods-eps-ios-drop-in — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-eps-ios-drop-in]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-eps-ios-drop-in]] adds EPS to an **existing iOS Drop-in** integration and separates Sessions from Advanced requirements (raw/adyen/docs/payment-methods/eps/ios-drop-in/2026-09-15.md:15–46, 97–119). It is not a full redirect-result or final payment-status guide. Test payment lookup and a separate live EPS request do not prove live approval, authorization, settlement or recurring-payment success (raw lines 89–95, 162–168).

## Q2 — What central capability, prerequisites, and warnings are stated?

Sessions requires existing iOS Drop-in, Checkout API v68+ and EPS in Customer Area; no EPS-specific `/sessions` parameters or Drop-in configuration are added (raw/adyen/docs/payment-methods/eps/ios-drop-in/2026-09-15.md:25–46). Advanced requires existing iOS Drop-in, EPS setup and handling for `action.type: redirect`; it adds no EPS-specific configuration or `/payments` parameters and states no separate API minimum (raw lines 97–119). Recurring is **through SEPA Direct Debit**: explicit permission and schedule/amount disclosure are strongly recommended, the source specifies `/payments` for token creation even under Sessions, token issuance is after settlement, and later charges use `storedPaymentMethodId`, shopper reference, `ContAuth` and a recurring processing model (raw lines 48–87, 121–160). Live EPS acceptance requires a separate request in live Customer Area (raw lines 89–95, 162–168).
