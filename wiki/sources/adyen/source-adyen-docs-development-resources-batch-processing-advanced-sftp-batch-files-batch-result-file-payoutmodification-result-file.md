---
title: "Adyen PayoutModification batch result file"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/payoutmodification-result-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/payoutmodification-result-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, payout-modification, result-file]
---

## Overview

This Adyen Docs snapshot (2019-10-25 last-modified metadata; captured 2026-09-15) specifies the `L` and `SL` records in an SFTP batch **PayoutModification result file**. It concerns a `PayoutConfirm` or `PayoutDecline` modification and its result fields, rather than the original payout request or proof that funds have finally arrived. See [[adyen-batch-processing]] and [[adyen]] for the broader file flow.

## Key takeaways

- In the `L` record, fields 3–6 carry `MerchantAccount`, merchant-account name, `PayoutConfirm` or `PayoutDecline` processing type, and merchant reference. Field 7 reports `Success`, `Error`, or `Pending`; `Pending` says the modification request is postponed for processing. Field 8 is echoed merchant data, not a platform-used payment value. [Raw lines 18–34]
- The `ModificationResult` `SL` record separates field 4, **this modification's PSP reference**, from field 5, **the original payout PSP reference**. Field 6 supplies a mapped refusal reason or error description when applicable; the source lists possible messages, many worded generically around payments, captures, refunds, and fund transfers. Do not treat those generic message labels as extra payout actions. [Raw lines 36–45]
- Parsing or validation errors use the separately linked validation-error result-file structure. If the `L` processing-type column shows `ValidationError`, this page likewise routes to that structure; the ordinary `PayoutConfirm`/`PayoutDecline` layout should not be applied to such a file. [Raw lines 16, 28–29]
- The example shows a TEST `PayoutConfirm` with `Success` and distinct modification/original-payout references. It is an example row, not evidence of a live modification, final payout settlement, or a safe retry for a pending original payout. [Raw lines 47–56]

## Detail locators

- `L` positional schema, statuses and echo field: raw lines 20–34. `SL` positional schema, reference identities and error text: raw lines 38–45. Sample `FH`/`BH`/`L`/`SL`/`BT`/`FT` file: raw lines 47–56.
- For shared header/footer and block fields, use the batch-result-file source; for validation-error layouts, follow the raw link at lines 16 and 29. This page does not define ACK validation or later bank-side payout finality.

## Related

- [[adyen-batch-processing]]
- [[adyen]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/payoutmodification-result-file/2026-09-15|Adyen PayoutModification result file, 2026-09-15 snapshot]]
