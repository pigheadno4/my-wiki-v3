# docs-issuing-report-types-balance-report retrieval checks

Q1. What does the Balance Platform Balance Report show, and which account-currency rows appear?

Answer: It shows opening and closing balances by account holder, balance account and currency for a selected day (raw lines 19, 36-50). A row appears when opening balance is nonzero or any movement occurs in the window. A zero-opening/zero-closing balance with offsetting movements appears; zero opening with no movement is excluded (raw lines 23-29). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-issuing-report-types-balance-report]] → [[raw/adyen/docs/issuing/report-types/balance-report/2026-09-15]].

Q2. How is the day boundary selected, and what does the report not establish?

Answer: A selected day runs from 00:00 to 00:00 the next day, in the configured balance-platform time zone or CET; generation may be scheduled or manual (raw lines 21, 36-38). The report is a balance snapshot and cannot by itself prove an individual transfer, external bank receipt or current live balance. The linked sample CSV is absent from this pinned raw, and generated reports can add columns based on platform settings (raw lines 31-34). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-issuing-report-types-balance-report]] → [[raw/adyen/docs/issuing/report-types/balance-report/2026-09-15]].
