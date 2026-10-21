# Retrieval checks — docs-marketplaces-reports-and-fees-balance-report

Q1. What does the Marketplace Balance Platform Balance Report show, and which account-currency rows appear?

A1. It gives opening and closing daily balances by account holder, balance account and currency, generated on a schedule or manually for a selected day (raw lines 15–23). A row appears for nonzero opening balance or any movement in the window, including offsetting movements that close at zero; zero opening/closing with no movement is omitted (raw lines 19, 25–29). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-reports-and-fees-balance-report]] → [[raw/adyen/docs/marketplaces/reports-and-fees/balance-report/2026-09-15]].

Q2. Can absent rows or sample timestamps establish no activity, exact field mapping, or bank receipt?

A2. No. A zero-to-zero row can still appear if movement occurred, while an omitted zero-to-zero row merely meets the report's no-movement selection rule (raw lines 25–29). The window is 00:00 to next-day 00:00 in platform-configured timezone or CET; sample rows show CEST and sample `Opening Time`/`Closing Time` headers where the field table says `Opening TimeZone`/`Closing TimeZone` (raw lines 31–46, 55–60). Generated files may add columns (raw lines 33–34). Listed fields are snapshots, not individual transfer outcomes or bank receipt (raw lines 48–70). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-reports-and-fees-balance-report]] → [[raw/adyen/docs/marketplaces/reports-and-fees/balance-report/2026-09-15]].
