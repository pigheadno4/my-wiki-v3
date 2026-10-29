# Retrieval checks: Boleto Bancário

## Q1 — Purpose and scope
Query: What does Adyen's Boleto Bancário overview describe, and what should not be inferred from voucher issuance?
Expected: This 2026-09-15 capture describes a Brazilian voucher-based method, specifically Boleto de Proposta, with cash, ATM and online-banking payment paths plus integration routes. Paying the voucher accepts the offer; merely issuing it does not show payment completion, current merchant eligibility or live success. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boleto-bancario]] → [[raw/adyen/docs/payment-methods/boleto-bancario/2026-09-15|pinned raw]]. Verify canonical stem `/payment-methods/boleto-bancario`, raw lines 15–35 and **How do you want to integrate?** lines 45–87.

## Q2 — Expiry and capability boundaries
Query: What happens when a Boleto is unpaid, and how does the captured overview scope guarantees and capabilities?
Expected: It says unpaid before due date leaves transaction open in Customer Area for 15 days, then Boleto expires and status becomes Offer cancelled. It describes Boleto de Proposta acceptance by paying; no payment should be inferred at issue/due date. The 2026-09-15 page says payments guaranteed/no chargeback risk, while table labels Cash and ATM/voucher/BR/BRL and marks recurring, refunds, partial refunds, captures and chargebacks unsupported. Attribute these to the historical page rather than a current financial guarantee. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-boleto-bancario]] → [[raw/adyen/docs/payment-methods/boleto-bancario/2026-09-15|pinned raw]]. Verify canonical stem and raw lines 23–43.
