# Fixed queries — docs-platforms-prepare-reports

## Q1 — purpose, scope, and non-inference

**Query:** What does this Platforms report-preparation guide set up, and does a configured report prove reconciliation or payout?

**Answer:** It guides selecting reports/fees after understanding balance-platform structure and funds flow, configuring time zones and columns, downloading Adyen-account and balance-platform reports, and matching references across them (raw lines 15–27, 29–40, 75–107). It recommends testing with complete reports before live reconciliation (lines 109–116). Report configuration, sample/test files or a successful join are not proof of a complete month close, settled payment, live payout or beneficiary-bank credit. Canonical route: [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-prepare-reports]] → [[raw/adyen/docs/platforms/prepare-reports/2026-09-15|pinned raw]].

## Q2 — central capability, prerequisites, and warnings

**Query:** Which columns, roles, reference mappings and time checks matter before combining the reports?

**Answer:** The page recommends Payment accounting `Store` when stores are used, `Split payment data` for comparing instructions to accounting postings, `AMS Booking Date` for invoice-period alignment, and Settlement details `Funds Destination` only for a Classic-upgrade parallel reconciliation (raw lines 42–52). Customer Area column configuration requires one of four listed merchant report/admin/financial/POS roles; adding or reordering columns can affect automated consumers and file size (lines 36–40, 54–73). The mapping distinguishes payment PSP, merchant, modification and split references between Adyen-account and balance-platform Accounting reports, with unique values recommended even when API fields are optional (lines 84–100). Combine only reports from the same reporting period and time zone; mismatches commonly cause reconciliation failures (lines 102–107). Detailed retrieval permission and individual report field semantics belong to the linked guides. Canonical route: [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-prepare-reports]] → [[raw/adyen/docs/platforms/prepare-reports/2026-09-15|pinned raw]].
