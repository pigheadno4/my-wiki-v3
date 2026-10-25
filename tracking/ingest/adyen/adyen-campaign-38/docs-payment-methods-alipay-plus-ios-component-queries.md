# docs-payment-methods-alipay-plus-ios-component retrieval queries

Canonical source: [[source-adyen-docs-payment-methods-alipay-plus-ios-component]] (`wiki/sources/adyen/source-adyen-docs-payment-methods-alipay-plus-ios-component.md`).
Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipay-plus-ios-component]] → [[raw/adyen/docs/payment-methods/alipay-plus/ios-component/2026-09-15|pinned raw]].

## Q1 — What is the purpose and scope, and what cannot be inferred?

This is a 2026-09-15 Alipay+ add-on for existing iOS Components Sessions or Advanced integrations (raw lines 15–25, 84–94). It describes generic `alipay_plus` Component setup and redirect prerequisites, not a complete integration, current wallet-level eligibility, observed authorization/capture/settlement, or tokenization/recurring capability (raw lines 33–69, 92–127). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipay-plus-ios-component]] → pinned raw above.

## Q2 — What central capability, prerequisites and warnings matter?

Sessions requires iOS Components, Checkout API v68+, redirect handling and Customer Area setup, with no extra `/sessions` or method configuration parameters (raw lines 25–48). Advanced requires the existing Components flow, redirect handling and Customer Area setup, with no extra method configuration or `/payments` parameters (raw lines 84–100, 123–127). The source shows `InstantPaymentComponent` with `.other("alipay_plus")`; the existing integration handles the redirect, while the example creates and initiates the Component, with session delegate for Sessions versus `self` in Advanced (raw lines 54–69, 106–120). The Advanced “Components” prerequisite URL points to Drop-in while its other links point to Components (raw lines 90–94, 123–127). Both flows state no TEST environment and recommend live penny tests, but Customer Area setup names **Alipay+** while the separate live request names **Alipay**; keep that naming mismatch unresolved (raw lines 33–36, 72–82, 92–94, 129–139). These are documentation statements, not permission or proof of a live payment. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipay-plus-ios-component]] → pinned raw above.
