---
title: "Adyen SFTP payout request parent-line fields"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payout-request-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payout-request-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, payout, request-file]
---

## Overview

This [[adyen]] SFTP batch reference defines the parent `L` line for a `Payout` request. The line holds metadata that applies to corresponding `SL` sub-lines; it is not itself a destination, amount, payout result, or proof that funds were sent. The pinned page ends after the `## Payout sub-lines` heading without listing those records, so use the linked child route for destination and payment-detail fields. See [[adyen-batch-processing]] for the batch file and validation lifecycle.

## Key takeaways

- The parent line's required positions are `L` record identifier (field 1), line number within the block (field 2, starting at 1 and increasing sequentially), fixed account type `MerchantAccount` (field 3), merchant account name (field 4), `Payout` processing type (field 5), and merchant reference (field 6). This is merchant-account context, not a user role or authorization to make payouts.
- Field 6 is described as a merchant reference identifying a transaction. The text then says, using modification-request terminology, that it can retain the original payment authorisation reference or use a new reference for the modification request. Preserve that wording as a page-level qualification rather than assuming an original-payment PSP reference, a payout PSP reference, or a universally safe reuse rule.
- Optional field 7 `EchoData` is returned unchanged in the result file when provided, is not used by Adyen's payment platform, and has an 80-character maximum. Echo data and the line counter are correlation metadata, not payment status.
- The table says that if the processing-type column shows `ValidationError`, the file has the linked validation-error **result-file** structure instead. This is not a successful payout request result. The page supplies no `SL` destination sub-line schema, amount/currency fields, approval workflow, or outcome webhook; no such behavior should be inferred from its empty heading.

## Detail locators

- **Parent `L` record purpose:** raw lines 14–18, under `# Payout request file` and `## Payout lines`.
- **Fields 1–5, block counter, merchant-account identity and processing-type/result-file caveat:** raw lines 20–26.
- **Merchant reference and optional `EchoData` semantics:** raw lines 27–29.
- **Undetailed payout sub-line heading:** raw lines 31–33, under `## Payout sub-lines`.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[adyen-payouts]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]]

## Related raw API references

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payout-request-file/payout-request/2026-09-15|Payout request sub-line detail — navigation only; raw not read for this entry]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/payout-request-file/2026-09-15|Adyen SFTP payout request parent-line reference — collected 2026-09-15]]
