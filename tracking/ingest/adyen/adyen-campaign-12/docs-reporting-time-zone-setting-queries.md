# Fixed queries — Adyen report time-zone setting

## Q1 — purpose, scope, and what must not be inferred

**Query:** What does the account/report time zone affect, and does it alter transaction timestamps or prove a financial event?

**Answer:** It affects report-data start/end boundaries. Scheduled intervals depend on interval length and the report's time zone, which may be fixed for the type or inherited from the account. Company and merchant accounts can have different settings and thus different reporting periods. The page does not say a setting changes underlying transaction date fields, captures, settlements, payouts or bank receipt. Raw: `raw/adyen/docs/reporting/time-zone-setting/2026-09-15.md:17-23,34-42`. Canonical route: `[[source-adyen-docs-reporting-time-zone-setting]]` → `[[adyen-reporting]]`.

## Q2 — central capability, prerequisites, and warnings

**Query:** How should a time-zone change be handled, and which report-generation schedules are exceptions to a generic account-zone assumption?

**Answer:** Existing reports remain unchanged and the change may introduce a gap or overlap; save old reports, ask Adyen Support to change the account setting, regenerate/download, merge corresponding reports and remove duplicates. Settlement details can be triggered by payable-batch close and, if configured, is expected within three hours; view the batch-closing setting from the company account. The table also lists scheduled Settlement details and several transaction reports before 06:00 in the account time zone, Daily/Monthly finance before 10:00 CET, and distinct Balance Platform schedules. These are generation times, not payout or bank-settlement times. Raw: `raw/adyen/docs/reporting/time-zone-setting/2026-09-15.md:25-32,38-74`. Canonical route: `[[source-adyen-docs-reporting-time-zone-setting]]` → `[[adyen-reporting]]`.
