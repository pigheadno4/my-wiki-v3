# Retrieval checks — Touch'n Go Web Drop-in

## Q1. What is this source's purpose and scope, and what cannot be inferred?

`source-adyen-docs-payment-methods-touchngo-web-drop-in` is a method add-on for an existing Web Drop-in Sessions or Advanced integration (raw lines 15–37). It supplies setup and no-extra-field guidance but no redirect/result procedure, account-eligibility proof, country/currency scope or verified transaction outcome (raw lines 39–60). Its `/sessions` v5.0.0-or-later line describes the default Drop-in endpoint, not a stated minimum for all Touch'n Go integrations (raw lines 41–44). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-touchngo-web-drop-in]] → [[raw/adyen/docs/payment-methods/touchngo/web-drop-in/2026-09-15]].

## Q2. What central capability, prerequisites and warnings matter?

Both Sessions and Advanced require an existing Web Drop-in integration and tell the merchant to contact Support to add Touch'n Go in Customer Area (raw lines 25–37). This page says no additional Touch'n Go API fields or Drop-in configuration are needed; general `/sessions` or `/payments` requirements depend on the base integration (raw lines 39–48). Test payment status is checked in test Customer Area, while live acceptance separately requires Support to add the method in live Customer Area (raw lines 50–54). These steps do not establish enablement or payment success. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-touchngo-web-drop-in]] → [[raw/adyen/docs/payment-methods/touchngo/web-drop-in/2026-09-15]].
