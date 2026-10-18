# C17 platform report-generation retrieval checks

## Q1 — Generation and proof boundary

Query: How can a platform obtain a balance-platform report, and does `balancePlatform.report.created` prove its contents or a payout outcome?

Expected route: `wiki/adyen-index.md` → `wiki/concepts/adyen-reporting.md` → `wiki/sources/adyen/source-adyen-docs-platforms-prepare-reports-generate-download-reports.md` → pinned `raw/adyen/docs/platforms/prepare-reports/generate-download-reports/2026-09-15.md`. Answer: configure automatic generation per report type or generate once in Customer Area, then use the report-created webhook's `downloadUrl` or the generated-reports table to download the file. The webhook signals availability, not file contents, reconciliation, booked settlement, or beneficiary-bank receipt. Raw locators: lines 15–19, 30–79, 81–113.

## Q2 — Roles, schedule effect, formats and authentication

Query: What access and operational limits apply when generating and downloading Adyen balance-platform reports?

Expected route: `wiki/adyen-index.md` → `wiki/concepts/adyen-reporting.md` → `wiki/sources/adyen/source-adyen-docs-platforms-prepare-reports-generate-download-reports.md` → pinned `raw/adyen/docs/platforms/prepare-reports/generate-download-reports/2026-09-15.md`. Answer: Customer Area generation/download roles and Report service user API key with BalancePlatform Report Download role for programmatic retrieval; obtain report credentials and authenticate HTTP GET. Turning off Automatic generation deletes the schedule. Schedules and manual bulk/date/account/time-zone options depend on report type/configuration. Reports are CSV, with Accounting also available as TSV. Downloaded files still need their own report-grain and period validation. Raw locators: lines 21–28, 32–75, 98–144.
