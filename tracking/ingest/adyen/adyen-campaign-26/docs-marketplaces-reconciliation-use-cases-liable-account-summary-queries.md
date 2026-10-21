# Retrieval checks — docs-marketplaces-reconciliation-use-cases-liable-account-summary

Q1. What does the Marketplace Liable account summary show, and what access and filters apply?

A1. It is a Customer Area dashboard of starting/ending liable-account balances and aggregated commissions, costs and movements for a selected period (raw lines 15–28). The **Download Balance Platform reports** role is required; at merchant-account level it shows liable accounts for the configured balance platform, filterable by date, one/all liable accounts and currency. Data uses the account timezone and Sales day payout configuration and is available after sales-day close; categories appear only with underlying data (raw lines 30–52). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-reconciliation-use-cases-liable-account-summary]] → [[raw/adyen/docs/marketplaces/reconciliation-use-cases/liable-account-summary/2026-09-15]].

Q2. Can this dashboard alone supply transaction-level reconciliation or match the monthly invoice fees exactly?

A2. No. It has no transaction-level data; the guide sends constituent transactions to the Balance Platform Accounting Report and says other reports are needed for a complete workflow (raw lines 60–70). It includes only fees charged to the liable account, uses that account's timezone versus invoice CET, and split fees with account holders prevent liable-booked fees from matching the invoice total (raw lines 72–77). A category total is not bank-receipt or accounting sign-off proof. Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-reconciliation-use-cases-liable-account-summary]] → [[raw/adyen/docs/marketplaces/reconciliation-use-cases/liable-account-summary/2026-09-15]].
