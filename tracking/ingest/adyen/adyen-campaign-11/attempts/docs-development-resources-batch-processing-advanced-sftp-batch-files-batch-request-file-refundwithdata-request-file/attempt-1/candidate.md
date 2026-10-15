---
title: "Adyen RefundWithData batch request-file parent"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/refundwithdata-request-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/refundwithdata-request-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, refund-with-data, request-file]
---

## Overview

This Adyen Docs snapshot (last-modified metadata 2026-09-15; captured 2026-09-15) defines the parent `L` record for an advanced-SFTP **RefundWithData request file**. The line carries metadata for associated `SL` records. It is a request layout, not a refund result, payment reversal, or bank-credit confirmation. See [[adyen-batch-processing]] and [[adyen]] for the larger batch flow.

## Key takeaways

- Required `L` fields 1–6 are record type `L`, sequential line number within the block, fixed `MerchantAccount` account type, merchant account name, fixed `RefundWithData` processing type, and merchant reference. Field 7 is optional `EchoData`: up to 80 characters passed back unchanged and not used by Adyen for processing. [Raw lines 18–29]
- The merchant-reference field may reuse the original payment-authorisation reference value or use a new reference for this modification request. That merchant reference is not described here as a PSP reference or as evidence of successful refund processing. [Raw lines 27–28]
- The page says `RefundWithData` has one processing type and one sub-line, but does **not** specify that sub-line's fields. Follow the separate child RefundWithData request source for its actual `SL` schema; its detail is not imported into this parent summary. [Raw lines 31–33]
- The `L` processing-type row also contains a `ValidationError` instruction pointing to a **result**-file structure, despite appearing on this **request**-file page. Preserve that context mismatch as source wording, not as evidence that a normal RefundWithData request is itself a validation result. [Raw line 26]

## Detail locators

- Complete parent `L` field table and requiredness: raw lines 20–29. Sub-line count statement: raw lines 31–33.
- This page has no amount, card/bank detail, validation acceptance, per-refund result, or final funds movement. Retrieve the child schema and the distinct batch ACK/result sources for those questions.

## Related

- [[adyen-batch-processing]]
- [[adyen]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-refundwithdata-request-file-refundwithdata-request]]

## Related raw API references

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/refundwithdata-request-file/refundwithdata-request/2026-09-15|RefundWithData child request sub-line schema, navigation only]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/refundwithdata-request-file/2026-09-15|Adyen RefundWithData request-file parent, 2026-09-15 snapshot]]
