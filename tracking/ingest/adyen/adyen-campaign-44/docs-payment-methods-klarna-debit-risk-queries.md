# Klarna Debit Risk retrieval checks

## Q1 — What is Klarna Debit Risk, and what must not be inferred from this source?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-debit-risk]]` → `[[raw/adyen/docs/payment-methods/klarna-debit-risk/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-klarna-debit-risk`. Full pinned raw path: `raw/adyen/docs/payment-methods/klarna-debit-risk/2026-09-15.md`. Raw lines 15–28 identify a primarily high-risk segment bank-account payment method for specific sectors, distinguish online-banking-only Debit Risk from Klarna Pay Now's direct debit plus online banking, and state Debit Risk's non-guaranteed settlement. This dated documentation does not prove current merchant eligibility, shopper availability, successful settlement, or a defensive route for non-settlement chargebacks.

## Q2 — What central capabilities and warnings should a retrieval answer preserve?

Use the same root/provider/concept/source/raw route. Raw lines 30–42 list redirect, AT/BE/DE/NL/ES and EUR, refunds and partial/multiple partial refunds, no separate or partial capture, and the qualified recurring and chargeback marks. The recurring `See note` is not explained in this 81-line capture. Raw `## Chargebacks` lines 44–48 say a successful `AUTHORISATION` means checks passed and transfer was initiated, yet issuer-side risk/AML blocks can prevent funds arriving; Adyen then books a chargeback and sends `CHARGEBACK`. Raw `## How do you want to integrate?` lines 50–74 route Web, iOS, Android and API-only details without establishing their versions or prerequisites.
