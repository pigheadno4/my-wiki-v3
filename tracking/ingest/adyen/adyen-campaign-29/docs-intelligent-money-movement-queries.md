# Q1 — What does this Intelligent Money Movement overview say about the product and funds path?

Route: [[index]] → [[adyen-index]] → [[adyen-financial-products]] → [[source-adyen-docs-intelligent-money-movement]] → [[raw/adyen/docs/intelligent-money-movement/2026-09-15]].

The captured page calls IMM an **enterprise** cash-management solution combining Adyen payment processing with balance-platform enterprise financial features (raw lines 15-19). It lists incoming processed payments and bank transfers, enterprise-account fund management, payouts to third-party bank accounts/cards or a verified bank account, and Adyen-issued debit-card spending (raw lines 21-26). Its example flow sequences purchase processing, merchant-account settlement, transfer to a balance account, balance-account settlement, then enterprise-account third-party payouts or issued-card payments; bank funding is an additional option (raw lines 28-45). A separate integration-overview link can be generated from selected offerings (raw lines 49-63).

# Q2 — Does the overview establish an implementable or approved architecture or a completed payment/payout?

No. It is a product and flow overview with a link to a separate generated integration overview, not that generated plan (raw lines 49-63). It gives no account-specific eligibility, enabled capability, API request, role/legal-entity mapping, region/currency/timing constraint, card transaction result or beneficiary receipt. The source's enterprise scope must remain separate from the existing [[adyen-financial-products]] concept's platform-user product-family scope. Merchant-account settlement, balance-account settlement, later outbound use and beneficiary receipt are distinct stages; the page only states its high-level sequence (raw lines 28-45).
