# C24 query checks — docs-classic-platforms-reports-and-fees-marketpay-balance-report

## Q1 — Purpose and report structure
Q: What does the Classic Marketpay Balance Report contain and how are entries identified?
A: It is a CET-based account-balance report across platform account holders/accounts; the filename pattern is MarketPay_balance_YYYY_MM_DD.csv, Default subscription, Daily/Weekly/Monthly frequency. After four summary lines and a line-5 header, each row is an entry with marketplace, accountHolderCode, accountCode and ISO currency. See raw/adyen/docs/classic-platforms/reports-and-fees/marketpay-balance-report/2026-09-15.md:19-29, :37-64.
Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-reports-and-fees-marketpay-balance-report]] → [[raw/adyen/docs/classic-platforms/reports-and-fees/marketpay-balance-report/2026-09-15]].

## Q2 — Balance grain and frequency boundary
Q: Are Balance/Pending Credit/Pending Debit major-unit transaction or payout rows, and is this report daily-only?
A: No. They are fixed-point minor-unit balances for the listed virtual account and currency, not individual movement or payout/bank-receipt proof. This child reference explicitly gives Daily, Weekly, or Monthly frequency, although the existing Classic reports-hub source summarizes it as daily account balances. Use the child line for this report's frequency and the separate transactional-ledger guide for reconciliation. See raw/adyen/docs/classic-platforms/reports-and-fees/marketpay-balance-report/2026-09-15.md:23-29, :48-64.
Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-reports-and-fees-marketpay-balance-report]] → [[raw/adyen/docs/classic-platforms/reports-and-fees/marketpay-balance-report/2026-09-15]].
