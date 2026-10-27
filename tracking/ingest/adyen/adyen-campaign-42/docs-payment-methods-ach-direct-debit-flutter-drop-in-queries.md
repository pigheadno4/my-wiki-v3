# Fixed retrieval checks — ACH Flutter Drop-in

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ach-direct-debit-flutter-drop-in.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

This 2026-09-15 page is a **short ACH-specific add-on** to existing Flutter Drop-in Sessions and Advanced integrations (primary raw `raw/adyen/docs/payment-methods/ach-direct-debit/flutter-drop-in/2026-09-15.md:15-25,67-76`; canonical source stem `source-adyen-docs-payment-methods-ach-direct-debit-flutter-drop-in`). It does not give a full Flutter integration, consumer account-validation procedure, SEC/mandate detail or final bank-outcome procedure; it stops after no-extra-configuration/request statements and TEST fixtures (`:39-65,78-106`). A TEST bank/account example or simulated `chargeback:R01` does not establish live bank validity, merchant activation or successful/settled debit (`:55-65,96-106`). Follow approved ACH overview `source-adyen-docs-payment-methods-ach-direct-debit` and giact validation child for separate obligations.

## Q2. What are the central capability, prerequisites and warnings?

Sessions requires existing Flutter Drop-in Sessions, Checkout API **v68+** and Support addition of ACH in Customer Area (`:25-35`). Its requirement link points to an **Advanced** Flutter flow although the `/sessions` creation link points to Sessions (`:33,41`). The source adds no ACH-specific `/sessions` fields or configuration (`:39-47`). Advanced requires existing Flutter Drop-in Advanced and ACH addition; it adds no ACH-specific configuration or `/payments` fields and states no separate API minimum (`:67-88`). No-extra-fields does not remove base flow, consumer validation or mandate responsibilities. Both sections show formatted account/routing TEST inputs and return simulation via `ownerName=chargeback:R01`; return rules are delegated to the linked ACH chargebacks guide (`:49-65,90-106`). This page makes no claim of immediate final authorization or settlement.
