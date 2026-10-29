# docs-payment-methods-boleto-bancario-ios retrieval checks

## Q1 — purpose and limits
Query: What does the Boleto Bancário iOS page itself document?
Expected: A captured router to iOS Drop-in and BoletoComponent child guides, not the voucher request, expiry or paid-state contract. It does not establish current merchant eligibility or completed payment. Route: [[wiki/index]] → [[wiki/adyen-index]] → [[wiki/concepts/adyen-online-payments]] → [[wiki/sources/adyen/source-adyen-docs-payment-methods-boleto-bancario-ios]] → [[raw/adyen/docs/payment-methods/boleto-bancario/ios/2026-09-15]]. Canonical stem: `/payment-methods/boleto-bancario/ios`. Verify raw lines 15–27.

## Q2 — UI and base-guide routes
Query: Which Boleto Bancário iOS UI choices and main flows are linked?
Expected: Drop-in is all-in-one UI; Components names BoletoComponent. The page links Sessions and Advanced base integration guides for both choices and says to build the main integration first. Follow a child method guide for CPF/CNPJ, voucher and test/live behavior; the router does not equate voucher issuance with paid status. Route: [[wiki/index]] → [[wiki/adyen-index]] → [[wiki/concepts/adyen-online-payments]] → [[wiki/sources/adyen/source-adyen-docs-payment-methods-boleto-bancario-ios]] → [[raw/adyen/docs/payment-methods/boleto-bancario/ios/2026-09-15]]. Canonical stem: `/payment-methods/boleto-bancario/ios`. Verify raw lines 19–36.
