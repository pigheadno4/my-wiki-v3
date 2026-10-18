# Fixed queries — docs-platforms-reports-and-fees-statement-report

## Q1 — purpose, scope, and non-inference

**Query:** What does the Balance Platform Statement Report show, and can an absent account or a row prove no activity or bank receipt?

**Answer:** This daily report describes starting and ending balance and balance-changing transactions for included accounts and available currencies, with scheduled/on-demand payout transaction tracking as a use case (raw lines 15–26). A balance account with both opening and ending balance zero is omitted, so absence cannot by itself prove there were no intraday changes (line 19). A report row or completed transaction ID is balance-platform reporting evidence, not independent beneficiary-bank receipt, final payout status or legal ownership proof. Canonical route: [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-reports-and-fees-statement-report]] → [[raw/adyen/docs/platforms/reports-and-fees/statement-report/2026-09-15|pinned raw]].

## Q2 — central capability, prerequisites, and warnings

**Query:** Which identifiers, amount/balance and date fields must be kept distinct when using this report?

**Answer:** The report separates Account Holder and Balance Account IDs, Category/Type/Status, pending-debit/credit Transfer Id, completed-debit/credit Transaction Id, and distinct PSP payment/modification references (raw lines 36–58). `Amount` is described as transfer/transaction amount and typed Alpha text; starting and ending balances each have their own currency. Booking Date denotes booking and Value Date denotes funds availability, each with a time-zone field (lines 59–68). The source does not define Amount signs or a report cutoff, and the linked sample is not exhaustive because generated columns may vary (lines 28–32). Customer Area supports schedule or manual day generation, while retrieval roles and downstream bank outcome require separate evidence (lines 21–26). Canonical route: [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-reports-and-fees-statement-report]] → [[raw/adyen/docs/platforms/reports-and-fees/statement-report/2026-09-15|pinned raw]].
