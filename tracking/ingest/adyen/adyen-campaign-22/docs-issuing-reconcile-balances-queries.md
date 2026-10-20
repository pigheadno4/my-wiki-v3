# docs-issuing-reconcile-balances retrieval checks

Q1. What flow is reconciled, and which report pairs and dates does the guide use?

Answer: Adyen describes merchant-account settlement funds moving into the balance platform as internal transfers (raw line 19). Daily, match SDR MerchantPayout with BPSR InternalTransfer by batch, amount, description and BPSR Value Date versus SDR Creation Date or conditional Booking Date (AMS) (raw lines 144-164). Monthly, compare BPIAR booked InternalTransfer entries whose Value Date falls in the month against ASDR MerchantPayout totals for all relevant merchant accounts (raw lines 176-194). Align merchant-account and balance-platform time zones; one sales day can cross two CET dates (raw lines 142, 154-162). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-issuing-reconcile-balances]] → [[raw/adyen/docs/issuing/reconcile-balances/2026-09-15]].

Q2. When is the dashboard method allowed, and what source conflict or outcome boundary matters?

Answer: Use the Liable account summary dashboard method only with one account holder; for multiple holders use Adyen reports (raw lines 205-207). Its steps request ASDR, but the count/amount comparisons call the report SDR (raw lines 217-222), so the captured labels conflict. A transfer-created webhook example and report matching instructions do not prove live settlement or bank receipt (raw lines 62-68, 125-129, 226-241). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-issuing-reconcile-balances]] → [[raw/adyen/docs/issuing/reconcile-balances/2026-09-15]].
