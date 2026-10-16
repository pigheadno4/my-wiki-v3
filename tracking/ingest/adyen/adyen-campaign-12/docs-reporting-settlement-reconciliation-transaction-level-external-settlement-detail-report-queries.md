# Fixed queries — docs-reporting-settlement-reconciliation-transaction-level-external-settlement-detail-report

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This Adyen External settlement detail report covers transactions for which Adyen is not the acquirer; the page gives direct American Express and PayPal funding arrangements as examples. It is available for company and merchant accounts, with a selected Customer Area date and the account's time-zone setting. Each row is a separate entry. The page explicitly says a transaction in the report does not confirm that the external acquirer paid the merchant. It is therefore not proof of bank arrival, complete reconciliation, or accounting finality.

**Raw locators:** lines 15–27 (identity, external-acquirer scope, retrieval, time zone, date and account availability); lines 35–43 (row grain, non-payment warning and column configuration).

**Canonical route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-external-settlement-detail-report]] → [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** Standard entry fields carry company/merchant account, references, creation date and time zone, journal Type, transaction Gross Currency and Gross Debit/Credit, settlement Net Currency and Net Debit/Credit, exchange rate, acquirer fees and identifiers. Net field descriptions subtract acquirer fees. Commission versus Markup/Scheme Fees/Interchange depends on whether the acquirer supplies interchange-level information. Journal types have stated Debit, Credit, or Debit/Credit occurrences, including external settlement, refunds, chargebacks, payouts and unmatched activity. The acquirer auth code is not unique for reconciliation. Account settings can add columns; configuring them can affect automated consumers. The four listed roles apply to column configuration. The source does not state an all-purpose generation role or guarantee payout from any row.

**Raw locators:** lines 47–78 (standard columns and conditional fee treatment); 80–92 (optional columns and non-unique acquirer auth code); 94–113 (configuration, roles and automation warning); 115–134 (journal occurrence and meanings).

**Canonical route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-external-settlement-detail-report]]; full field and journal meanings at [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report/2026-09-15]].
