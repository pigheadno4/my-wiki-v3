---
title: "Modifications not processed | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/modifications-not-processed"
raw_files:
  - "adyen/docs/reporting/modifications-not-processed/2026-09-15.md"
tags: [adyen, reporting, payment-modifications, capture, cancel, refund]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot defines the **Modifications not processed** report for modification attempts on an original authorised payment that could not be processed. Its examples are captures, cancels and refunds. Each post-header row is a separate unprocessed-modification entry; the report is evidence of a failed modification attempt, not proof that a capture, cancellation or refund succeeded. [[adyen-reporting]]

## Key takeaways

- The original payment's Customer Area transaction status does **not** change for an unprocessed modification. The page's insufficient-balance refund example leaves the original transaction at `Settled`. A failed modification attempt also triggers a webhook carrying failure information; the page does not define webhook payload or a retry procedure. Reconcile the original and modification references and failure reason before deciding what action is safe. See raw lines 21–27.
- Rows distinguish original-payment `Psp Reference`, merchant reference, transaction currency and original amount from `Modification Reference` (a separate PSP reference), optional modification merchant reference, modification currency and modification amount. `Modificationevent` can be `RefundNotProcessed`, `CaptureNotProcessed` or `CancelNotProcessed`; `Eventdescription` gives the reason. These fields identify the attempt and explain non-processing, rather than the result of a new attempt. See raw lines 33–58.
- The account's time-zone setting affects report data. `Modification Date` is when Adyen received the modification. The raw column definition calls `Creation Date` the time Adyen received a **capture**, although the report also covers cancel and refund attempts; do not generalize that field wording to every modification type without checking the relevant event. Both timestamps are documented in `YYYY-MM-DD HH:MM:SS` format. See raw lines 19–21, 49–58.
- This page does not specify access or generation roles, report schedule, a particular time zone, or a currency-conversion rule between original and modification amounts. The sample is a navigation route, not proof of a merchant's live report content. See raw lines 19–58.

## Detail locators

- **Population, original status, webhook and time-zone qualification:** raw lines 19–27.
- **Entry grain and sample:** raw lines 29–41.
- **Original versus modification identifiers, amounts, currencies, timestamps and event reason:** raw lines 43–58.

## Related

- [[adyen]]
- [[adyen-reporting]]
- [[adyen-payment-capture]]
- [[adyen-refunds]]

## Raw Sources

- [[raw/adyen/docs/reporting/modifications-not-processed/2026-09-15|Adyen Modifications not processed — collected 2026-09-15]]
