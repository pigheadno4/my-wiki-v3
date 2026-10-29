# Atome Android Component retrieval checks

## Q1 — Which integration does this guide cover, and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-atome-android-component]]` → `[[raw/adyen/docs/payment-methods/atome/android-component/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-atome-android-component`. Full pinned raw path: `raw/adyen/docs/payment-methods/atome/android-component/2026-09-15.md`. Raw lines 15–36 and 846–854 describe Atome additions to existing Android Components Sessions or Advanced integrations. The captured guide does not prove current account availability, merchant entitlement, final payment success, or live enablement.

## Q2 — What are the flow-specific requirements, component steps and warnings?

Use the same root/provider/concept/source/raw route. Sessions requires Checkout API v68+, redirect handling, Atome in Customer Area, and required shopper/contact/billing/line-item/country fields; Advanced has its own redirect-action and `/payments` table with `paymentMethod.type=atome` (raw lines 25–52, 846–957). Both specify MY/MYR or SG/SGD, conditionally optional delivery address, the instant module and `InstantPaymentComponent` (lines 732–813, 856–940). Partial-refund amount, sandbox shopper accounts and live Support request are at lines 816–844 and 1688–1716. The Advanced “successful payment” example is actually `RedirectShopper`, not final authorization (lines 1674–1685); the Sessions curl block has duplicate countryCode and a missing command continuation (lines 54–78).
