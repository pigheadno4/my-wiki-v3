# docs-payment-methods-payme — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

This is Adyen's **PayMe method overview**: it identifies the Hong Kong wallet, bank-funded balance, desktop QR/mobile app handoff and Hong Kong local-entity prerequisite (source-adyen-docs-payment-methods-payme; raw lines 15–23). Its matrix is scoped to HK/HKD and an additional-action wallet flow (raw lines 25–27). The snapshot does not establish current eligibility, merchant onboarding approval, SDK/API versions, payment authorization, capture or settlement (raw lines 15–53).

Q2. What is its central capability, prerequisite and warning?

The page says the merchant needs a local Hong Kong entity; its matrix marks refunds, partial refunds and multiple partial refunds supported, while recurring, separate/partial/multiple-partial captures and chargebacks are marked unsupported (source-adyen-docs-payment-methods-payme; raw lines 23–27). Desktop shoppers scan a QR code and mobile shoppers are redirected to PayMe's app (raw line 21). Web, iOS, Android and API-only links route readers to implementation details (raw lines 29–53); the matrix and app handoff do not prove a completed payment or define refund execution/status rules (raw lines 21–27).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-payme]] → [[raw/adyen/docs/payment-methods/payme/2026-09-15]].
