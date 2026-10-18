# Liable account summary retrieval checks

Q1. Who can access the Liable account summary, and what account, period and balance does it summarize?
Expected forward route: [[adyen-index]] → [[adyen-reporting]] → ## Sources → [[source-adyen-docs-platforms-reconciliation-use-cases-liable-account-summary]] → [[raw/adyen/docs/platforms/reconciliation-use-cases/liable-account-summary/2026-09-15]]. Inspect raw lines 30–56 for role, merchant-account view, liable-account/currency/date filters, sales-day availability, timezone and starting-plus-categories ending balance.

Q2. Can the dashboard reconcile individual references or be expected to equal the monthly invoice and prove bank receipt?
Expected forward route: [[adyen-index]] → [[adyen-reporting]] → ## Sources → [[source-adyen-docs-platforms-reconciliation-use-cases-liable-account-summary]] → [[raw/adyen/docs/platforms/reconciliation-use-cases/liable-account-summary/2026-09-15]]. Inspect raw lines 60–77 for report combinations, missing transaction-level data, liable-account-only fees, CET invoice difference and fee-split mismatch; lines 79–142 locate category-to-accounting-report mappings. Dashboard categories alone do not establish bank arrival or approved books.
