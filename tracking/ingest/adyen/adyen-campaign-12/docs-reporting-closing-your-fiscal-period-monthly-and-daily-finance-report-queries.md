# Fixed queries — docs-reporting-closing-your-fiscal-period-monthly-and-daily-finance-report

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This Adyen webpage describes Monthly and Daily finance reports for reviewing payment activity and account balances over a selected report date range. Company and merchant account levels are eligible; values are stated in primary settlement currency, and report time is CET. It is a report description and field guide, not proof of a particular bank receipt, a completed reconciliation, or accounting finality.

**Raw locators:** lines 15–27 (identity, purpose, formats, generation, CET, date range, availability); lines 74–79 (period totals and distinct balances); lines 198–203 (batch and payout dates).

**Canonical route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-closing-your-fiscal-period-monthly-and-daily-finance-report]] → [[raw/adyen/docs/reporting/closing-your-fiscal-period/monthly-and-daily-finance-report/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** The report combines a monthly/daily overview, a status-grouped payment balance sheet, and payout-batch detail. Customer Area generation lets the user select the included date range; manual and automatic retrieval are linked. Interpret gross captured, net payable, Deposit, and Refund Reserve separately. The overview's total paid out does not equal the four prior rows' sum. Opening and previous end balances can differ because of exchange rates, and the Check valuation difference is not currency-conversion gain or loss. Payout Date may be blank when a batch produced no payout. Net/Cost can represent credits or debits for specified mutations; retain the field and batch context.

**Raw locators:** lines 19–27 (scope/access); 33–46 (three sheets); 60–79 (overview and balances); 81–95 (status grain, period, currency/FX caveat); 184–225 (payout-batch grain, CET dates, payout-date exception and Net/Cost).

**Canonical route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-closing-your-fiscal-period-monthly-and-daily-finance-report]]; full field meanings at [[raw/adyen/docs/reporting/closing-your-fiscal-period/monthly-and-daily-finance-report/2026-09-15]].
