---
title: "PayoutConfirm request | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutconfirm-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutconfirm-request/2026-09-15.md"
tags: [adyen, batch-processing, sftp, payout-modification, payout-confirm]
---

## Overview

This 2026-09-15 [[adyen]] SFTP batch reference defines the mandatory `PayoutConfirm` `SL` sub-line for a `PayoutModification` request. The sub-line points to the **original payout PSP reference**; the enclosing `L` row and FH/BH/BT/FT wrapper are illustrated but governed by their own request-file references. A requested confirmation is not the result of the modification or proof of payout settlement. [[adyen-batch-processing]]

## Key takeaways

- The four sub-line fields are all marked required: fixed `SL`, a sub-line number starting at 1 and increasing sequentially within its parent `L`, fixed `PayoutConfirm`, and the original payout PSP reference. The PSP reference in `SL` field 4 is distinct from the `L` row's merchant reference shown in the example. See raw lines 16–25 and 27–36.
- The page says this `PayoutConfirm` requires a user role with permission to **review/decline a payout**. It does not name a particular role or establish that any merchant user has it. See raw line 38.
- The example uses a `PayoutModification` file header and a `PayoutConfirm` `L`/`SL` pair. These are request records; acceptance, a confirmation-result status, and original-payout or bank-settlement outcome require separate result and payout evidence.

## Detail locators

- **Mandatory positional `SL` schema and original payout PSP reference:** raw lines 16–25.
- **Illustrative file and parent `L` context:** raw lines 27–36.
- **User-permission qualification:** raw line 38.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-payoutmodification-request-file]] — parent `L` action and merchant-reference fields
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-payoutmodification-result-file]] — separate result status and modification PSP reference

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/payoutconfirm-request/2026-09-15|Adyen PayoutConfirm request — collected 2026-09-15]]
