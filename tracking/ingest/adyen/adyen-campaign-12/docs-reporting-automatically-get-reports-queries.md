# Fixed queries — docs-reporting-automatically-get-reports

## Q1 — purpose, scope, and what not to infer

**Question:** What does automatic report retrieval do, and does REPORT_AVAILABLE deliver a report or prove payment settlement?

**Expected answer:** A merchant enables automatic Customer Area report generation. When a report is generated, REPORT_AVAILABLE supplies `pspReference` as the file name and `reason` as the download URL. A separate authenticated HTTP GET retrieves the file. The notification does not contain the report and is not evidence of settlement, payout receipt, or even successful retrieval. Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-automatically-get-reports]] → [[raw/adyen/docs/reporting/automatically-get-reports/2026-09-15]]. Raw locators: opening lines 15–19; Step 2 lines 62–69; Step 5 lines 174–178.

## Q2 — central capability, prerequisites, and warnings

**Question:** Which schedules, roles, credentials, retrieval, and security conditions govern automatic reports?

**Expected answer:** The Customer Area user needs Merchant Report or Generate key financial reports to enable automatic generation; some reports require a chosen daily, weekly, monthly, or quarterly schedule, and account time-zone settings affect generation. The daily description gives 02:00–10:00 CET and previous 24 hours, without making that a universal report guarantee. Webhook setup is needed for REPORT_AVAILABLE. HTTP GET download needs a Report service user credential with Merchant Report Download role and account access; Merchant admin or Manage API credentials is needed to create it. Authentication can use API key or Basic auth; securely store credentials. Optional Reports-purpose PGP key encrypts future files. A migration may require ingestion changes for Received payment details, Interactive payment accounting, and Settlement details reports. Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-automatically-get-reports]] → [[raw/adyen/docs/reporting/automatically-get-reports/2026-09-15]]. Raw locators: Important changes lines 21–25; Step 1 lines 27–60; Step 2 lines 62–69; Step 3 lines 129–163; Step 4 lines 165–172; Step 5 lines 174–210.
