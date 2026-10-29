# Klarna Debit Risk Web Component retrieval checks

## Q1 — What page is this and what must an answer avoid inferring?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-debit-risk-web-component]]` → `[[raw/adyen/docs/payment-methods/klarna-debit-risk/web-component/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-klarna-debit-risk-web-component`. Full pinned raw path: `raw/adyen/docs/payment-methods/klarna-debit-risk/web-component/2026-09-15.md`. Raw lines 15–42 and 1083–1121 identify a Web Components add-on for existing Sessions/Advanced flows, redirect handling and Customer Area setup. It does not establish current merchant eligibility, live enablement or successful payment execution.

## Q2 — What capability, conditions and warnings distinguish this guide?

Use the same root/provider/concept/source/raw route. Raw lines 74–105 and 1123–1154 say recurring Debit Risk uses a token for future **SEPA Direct Debit**, with an explicit-permission recommendation, a non-PII shopper reference and token creation parameters. Raw lines 455–463 and 1504–1512 restrict token payments to shopper-absent Subscription or UnscheduledCardOnFile; later requests use `sepadirectdebit`, `storedPaymentMethodId` and `ContAuth` (lines 465–489, 1514–1538). The initial-token table says `Ecommerce` at lines 102/1151, but sample code says `ContAuth` at line 128 and following examples. The JavaScript Component type lacks quotes at lines 71/1114. Raw lines 1075–1081 and 2124–2130 state test and live-account setup, not a live-payment result.
