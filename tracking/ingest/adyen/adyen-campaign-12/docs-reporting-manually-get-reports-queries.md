# Fixed queries — docs-reporting-manually-get-reports

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This page explains one-time manual generation and download of Adyen reports in Customer Area. A report can be available at company-account, merchant-account, or both levels. It is a retrieval guide; a queued message, generated file, or downloaded report does not itself prove settlement, full reconciliation, or bank receipt. The captured page states a two-year retention rule beginning January 13, 2024, with invoices excluded; current account availability is not independently verified here.

**Raw locators:** lines 15–23 (purpose, account availability, report retention and invoice exception); lines 25–45 (manual flow and queue/download distinction).

**Canonical route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-manually-get-reports]] → [[raw/adyen/docs/reporting/manually-get-reports/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** The user needs either Merchant Report or Generate key financial reports role. Under Reports → Report overview, find the report, choose Manage report → Manual (generate once), select report-specific options such as date range or file type, then Generate report. The success message says the report is queued; generation may take several hours due to size or demand. Once generated, select the report name and item under Generated reports to download. This page does not provide one universal report date range, file format, or time zone; read the selected report's own specification before using its values.

**Raw locators:** line 27 (roles); lines 31–39 (navigation and settings); lines 41–45 (queue, delay and generated-report download).

**Canonical route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-manually-get-reports]]; exact steps at [[raw/adyen/docs/reporting/manually-get-reports/2026-09-15]].
