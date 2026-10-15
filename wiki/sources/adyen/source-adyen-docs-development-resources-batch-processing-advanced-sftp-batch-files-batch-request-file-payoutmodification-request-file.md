---
title: "PayoutModification request file | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, payout-modification, request-file]
---

## Overview

This 2026-09-15 [[adyen]] SFTP **PayoutModification request-file** reference defines the common per-request `L` row for `PayoutConfirm` or `PayoutDecline` and says operation-specific `SL` requirements vary by that choice. These are requested actions against a payout, not a result for the original payout, a confirmed transfer, or a bank-settlement record. [[adyen-batch-processing]]

## Key takeaways

- The table marks `L` fields 1–6 required: fixed `L`, a block-local sequential line number, fixed `MerchantAccount`, merchant account name, one processing type (`PayoutConfirm` or `PayoutDecline`), and a merchant reference that uniquely identifies a transaction. It does not define an original payout PSP-reference field in this `L` schema. See raw lines 16–28.
- Field 7 `EchoData` is optional, at most 80 characters, and returned unchanged when supplied; Adyen says it does not use this data for processing. The number and type of sub-lines vary with the selected payout modification. This page does not provide those operation-specific field tables. See raw lines 29–33.
- If a result processing-type column shows `ValidationError`, the field-5 description points to the separate ValidationError result-file structure. A prepared `PayoutConfirm` or `PayoutDecline` request does not establish acceptance, a modification result, the status of the original payout, or final receipt of funds; retrieve the relevant result file and later payout evidence separately.

## Detail locators

- **`L` record sequence, account, action choice and merchant reference:** raw lines 16–28.
- **Optional echo, variable sub-lines and ValidationError result route:** raw lines 27–33.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]] — common file and block wrapper
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-payoutmodification-result-file]] — result status and PSP-reference schema
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file-validationerror]] — validation-error result rows

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payoutmodification-request-file/2026-09-15|Adyen PayoutModification request file — collected 2026-09-15]]
