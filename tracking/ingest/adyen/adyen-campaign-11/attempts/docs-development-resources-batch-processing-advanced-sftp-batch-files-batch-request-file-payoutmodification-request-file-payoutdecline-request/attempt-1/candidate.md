---
title: "Adyen SFTP PayoutDecline request sub-line"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutdecline-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutdecline-request/2026-09-15.md"
tags: [adyen, batch-processing, sftp, payout-modification]
---

## Overview

This Adyen webpage snapshot defines the mandatory `SL` sub-line for a PayoutDecline request within the SFTP PayoutModification request format. It is an input record for requesting a decline of an original payout, not a result or proof that a payout was declined. See [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- The sub-line table marks all four fields required: fixed `SL` record type; numeric `SL` number within its parent line, starting at 1 and incrementing by one; fixed `PayoutDecline` transaction type; and the **original payout PSP reference** as a numeric field.
- The original payout PSP reference in field 4 identifies the payout to modify. It is distinct from the merchant reference shown in the example parent `L` line, and this request page does not state a resulting modification PSP reference or final payout state.
- Adyen says the PayoutDecline action requires a user role with permission to review/decline a payout.
- The example shows `PayoutModification` in its `FH` file header and `PayoutDecline` in both the `L` and `SL` records. Treat example values and counters as an illustration, not an execution receipt.

## Detail locators

- `Mandatory sub-lines`, raw lines 16–25: four positional fields, requiredness, record numbering, action and original-payout reference.
- `Example`, raw lines 27–36: illustrated `FH`, `BH`, `L`, `SL`, `BT` and `FT` records.
- Permission condition, raw line 38.

## Related

- [[adyen-batch-processing]] — SFTP request and result boundaries.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file]] — parent PayoutModification request-line schema.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-payoutmodification-result-file]] — separate result format and status reference.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutdecline-request/2026-09-15|PayoutDecline request, fetched 2026-09-15]]
