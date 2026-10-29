# C44 worker query check: Klarna Debit Risk Android Component

## Q1 — purpose, scope, non-inference

**Query:** Which integration does this guide cover, and what does it prove?

**Answer:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-debit-risk-android-component]] routes to the 2026-09-15 Android Components add-on for Klarna Debit Risk, in Sessions and Advanced flows. It establishes documentation requirements, not present merchant enablement or a successful live payment. The pinned full raw is `raw/adyen/docs/payment-methods/klarna-debit-risk/android-component/2026-09-15.md`; verified locators: introduction 15–23, Sessions 25–127, Advanced 1137–1237, test/live 2240–2246.

## Q2 — capability, prerequisites, warnings

**Query:** What must an Android merchant add, and how does recurring work?

**Answer:** Existing Android Components integration, method addition in Customer Area, `directEbanking` via `InstantPaymentComponent`, and redirect handling are needed; Sessions specifies Checkout API v68+. Ordinary Sessions/Advanced payments need no extra method fields or component configuration. Recurring first stores SEPA details through a Klarna Debit Risk payment; later shopper-absent token charges use `sepadirectdebit` for Subscription or UnscheduledCardOnFile, with permission recommended. The token-creation field tables mark countryCode required and online shopperInteraction Ecommerce while examples omit countryCode and use ContAuth. Verified locators: raw 29–42, 75–125, 130–159, 509–517, 1137–1237, 1241–1270, 1620–1628.
