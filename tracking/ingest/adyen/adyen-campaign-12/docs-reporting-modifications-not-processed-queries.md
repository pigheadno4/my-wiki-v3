# docs-reporting-modifications-not-processed fixed queries

## Q1 — Purpose, scope, and what not to infer

**Question:** Which events appear in this report, and what does a row establish?

**Answer:** The 2026-09-15 page says the report includes modification attempts on an original authorised payment that could not be processed, such as capture, cancel or refund (raw lines 15–27). Each post-header row is a separate entry (lines 33–41), with event values `RefundNotProcessed`, `CaptureNotProcessed` and `CancelNotProcessed` plus a reason in `Eventdescription` (lines 57–58). The original payment's Customer Area status stays unchanged for an unprocessed modification; the example failed refund for insufficient balance leaves it `Settled` (line 25). A failure webhook is sent (line 27), but the row or webhook is not evidence that a later attempt succeeded or permission to retry blindly. Canonical route: [[source-adyen-docs-reporting-modifications-not-processed]] → [[adyen-reporting]]; evidence: [[raw/adyen/docs/reporting/modifications-not-processed/2026-09-15]] lines 15–27, 33–58.

## Q2 — Central fields, qualifications, and warnings

**Question:** How can a reader distinguish the original payment from the failed modification, and what timing, currency, role and retry limits apply?

**Answer:** The original payment fields include `Psp Reference`, merchant reference, transaction `Currency` and original `Amount`; the separate modification fields include `Modification Reference` (its PSP reference), optional modification merchant reference, `Modification Currency`, `Modification Amount`, `Modification Date`, event code and reason (raw lines 43–58). The account time-zone setting affects the report (line 21). `Modification Date` is receipt time at Adyen; `Creation Date` is literally described as capture receipt time, even though report population also includes cancels/refunds, so do not assume that wording fits all event types (lines 51–56). Both timestamps use `YYYY-MM-DD HH:MM:SS`. The page does not give report-access roles, a specific time zone, conversion between transaction and modification currencies, or a retry procedure. Inspect the failure reason and operation identity before any fresh action; do not retry a possibly pending operation from this report alone. Canonical route: [[source-adyen-docs-reporting-modifications-not-processed]] → [[adyen-reporting]]; evidence: [[raw/adyen/docs/reporting/modifications-not-processed/2026-09-15]] lines 19–58.
