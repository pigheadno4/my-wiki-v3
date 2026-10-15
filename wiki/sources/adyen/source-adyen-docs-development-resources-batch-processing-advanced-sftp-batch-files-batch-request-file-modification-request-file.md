---
title: "Modification request file | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, modification, request-file]
---

## Overview

This 2026-09-15 [[adyen]] SFTP batch **Modification request-file** reference defines the common per-request `L` record and directs readers to operation-specific `SL` formats. It identifies the merchant account, selected modification processing type, and optional merchant reference; it does not define a complete capture/refund sub-line or report a modification outcome. [[adyen-batch-processing]]

## Key takeaways

- `L` fields 1–5 are marked required: fixed `L`, a line number increasing by one within its block, fixed `MerchantAccount`, merchant account name, and processing type. The allowed type labels in this table are `AuthoriseReferral`, `Cancel`, `Capture`, `Refund`, and `CancelOrRefund`. This list names request actions; it does not assert that any action succeeded. See raw lines 16–30.
- Field 6 is an optional merchant reference for the transaction. For a modification it may retain the original payment authorisation merchant-reference value or use a new value for this modification. That choice is about a **merchant reference**, not a statement that it is the original payment PSP reference or the modification PSP reference. Field 7 `EchoData` is also optional and returned unchanged when populated; Adyen says it does not use it for processing. See raw lines 31–33.
- The number and type of `SL` records vary by modification request. This page does not specify their individual field schemas, a `Received` status, or a final capture/refund result. If a result processing-type column shows `ValidationError`, the table points to the separate ValidationError **result-file** structure. See raw lines 30 and 35–37.

> [!warning] Contradiction
> The request-file field-5 list includes `CancelOrRefund` (raw request line 30), but the linked [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file|Modification result-file]] field-5 list uses `CaptureOrRefund` (result raw line 31). The sources do not establish whether these labels map to each other or which label a `CancelOrRefund` request returns. Check the result source and confirm the applicable mapping with Adyen before interpreting a result row.

## Detail locators

- **`L` identity, sequence, merchant account and five processing types:** raw lines 16–30.
- **Optional merchant reference and echo behavior:** raw lines 31–33.
- **Variable operation-specific sub-lines:** raw lines 35–37.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]] — common FH/BH/BT/FT file structure
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file]] — modification result status and PSP-reference schema
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file-validationerror]] — validation-error result rows

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/2026-09-15|Adyen Modification request file — collected 2026-09-15]]
