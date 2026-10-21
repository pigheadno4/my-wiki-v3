# C26 report-generation retrieval checks

## Q1 — Purpose and prerequisites

**Query:** How does a Marketplace operator generate and download balance-platform reports, and which access is needed?

**Answer:** The Customer Area Reports page supports scheduled automatic or one-time manual generation; a `balancePlatform.report.created` webhook carries the `downloadUrl` when a generated report is available (raw lines 19–20, 30–79). Customer Area generation/download roles are listed in raw lines 25–27; HTTP GET download requires report credentials, with the Report service user API key and BalancePlatform Report Download role stated for API-key use (raw lines 25, 115–125). The file can be downloaded in Customer Area or over authenticated HTTP GET (raw lines 98–144). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-prepare-reports-generate-download-reports]] → [[raw/adyen/docs/marketplaces/prepare-reports/generate-download-reports/2026-09-15]].

## Q2 — Schedule and evidence boundary

**Query:** What happens if automatic generation is switched off, and does a report-created webhook prove reconciliation or a payout?

**Answer:** Deselecting Automatic generation deletes that report's generation schedule; timing depends on report type and balance-platform configuration (raw lines 44–50). The report-created webhook announces availability and supplies a download URL, not report rows (raw lines 77–96). The downloaded format is CSV, with TSV also available for the Accounting report; report-specific contents and financial outcomes require separate checking (raw lines 98–102). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-marketplaces-prepare-reports-generate-download-reports]] → [[raw/adyen/docs/marketplaces/prepare-reports/generate-download-reports/2026-09-15]].
