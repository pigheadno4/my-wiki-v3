# Fixed queries — docs-reporting-dynamic-sales-day

## Q1 — purpose, scope, and what not to infer

**Question:** What does a dynamic sales-day close change, and what does it not prove?

**Expected answer:** For a merchant account with an eligible Sales day payout setting, a successful one-night close request sets the cutoff at request time. Captured payments before it belong to that sales day's Settlement details report; captures after it belong to the next sales day's payable pending batch/report. This addresses report and batch grouping when a business application's closing time varies; it does not prove payment settlement, payout execution, or bank receipt. Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-dynamic-sales-day]] → [[raw/adyen/docs/reporting/dynamic-sales-day/2026-09-15]]. Raw locators: `Solution to reconciliation problems` lines 31–39; `Set the closing time for this night` lines 74–111; `Booking of payments` lines 135–140.

## Q2 — central capability, prerequisites, and warnings

**Question:** What eligibility, roles, time window, fallback, and failure conditions govern a nightly close?

**Expected answer:** The snapshot requires Sales day payout T+1 or T+2 and one merchant account per business application. It says the feature is unavailable in Africa, Brazil and Turkey and cannot solve different cutoffs from multiple applications consolidated into one merchant account. Configure the static time after midnight (06:00 is recommended), with Change payout schedule or Merchant admin in Customer Area. Nightly POST to `/merchants/{merchantId}/closeSalesDay` needs Management API—Sales Day Payout read and write; send after midnight and before 06:00 local time or an earlier static cutoff. The optional `closeNow` value does not change immediate-close behavior. Missing/late requests fall back to static; the next night resets to static unless another request is sent. A 422 `36_001` example can mean already closed or outside the allowed window. Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-dynamic-sales-day]] → [[raw/adyen/docs/reporting/dynamic-sales-day/2026-09-15]]. Raw locators: `Requirements` lines 21–29; `When dynamic closing times do not help` lines 41–55; `Preparation` lines 57–72; `Set the closing time for this night` lines 74–111; `Troubleshooting` lines 113–133.
