# Transactions components retrieval checks

Q1. What must a platform configure for its users to view transactions and initiate refunds through the Transactions components?
Expected forward route: [[adyen-index]] → [[adyen-platform-components]] → ## Sources → [[source-adyen-docs-platforms-components-overview-after-payment-transactions-component]] → [[raw/adyen/docs/platforms/components-overview/after-payment/transactions-component/2026-09-15]]. Inspect raw lines 44–56 and 177–183 for integration/API credential roles, session-role requirement, and method-dependent refund support; lines 229–246 for account-holder scoped session, origin, and product.

Q2. Can the Transactions Overview CSV or refund status alone establish a complete ledger or that the shopper received a refund?
Expected forward route: [[adyen-index]] → [[adyen-platform-components]] → ## Sources → [[source-adyen-docs-platforms-components-overview-after-payment-transactions-component]] → [[raw/adyen/docs/platforms/components-overview/after-payment/transactions-component/2026-09-15]]. Inspect raw lines 53–54 and 68–76 for first-100-row CSV and displayed insights, and lines 179–190 for user request, API call, and status message; the page does not establish bank/shopper receipt.
