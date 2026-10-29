# Klarna API-only retrieval checks

## Q1 — Purpose, scope, and what not to infer

**Question:** What does Adyen's captured Klarna API-only guide cover, and what cannot be inferred from it?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-api-only]] → [[raw/adyen/docs/payment-methods/klarna/api-only/2026-09-15]]. It covers an existing merchant-built Web API-only integration with widget or redirect (raw lines 15–42, 130–155), payment/capture/token guidance (raw lines 899–1654), and test/live setup (raw lines 1723–1750). Examples and dated documentation do not establish current merchant eligibility, Klarna approval, final capture, settlement or successful live testing.

## Q2 — Central capability, prerequisites, and warnings

**Question:** How does a merchant choose the Klarna API-only path, and which conditions govern outcome, capture and reuse?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-api-only]] → [[raw/adyen/docs/payment-methods/klarna/api-only/2026-09-15]]. `paymentMethod.subtype: sdk` selects the widget and omission selects redirect; the `paymentMethod.type` values distinguish Pay Now, Pay Later and Pay Over Time (raw lines 130–155). Use matching country/currency/address and accurate line items (raw lines 91–100, 157–170). The 2024-01-31 notice makes `/payments/details` optional while retaining webhooks for final outcomes, despite step prose still showing details calls (raw lines 19, 938–955, 985–1030). Manual capture is required within 90 days unless the immediate-delay and 24-hour shipping condition applies; `received` is not final capture, so check CAPTURE webhook (raw lines 1032–1034, 1494–1525). Recurring tokens arrive after settlement; [[raw/adyen/docs/payment-methods/klarna/2026-09-15|Klarna overview raw]] lines 31–39 add Support and product-eligibility limits (guide raw lines 1609–1654).
