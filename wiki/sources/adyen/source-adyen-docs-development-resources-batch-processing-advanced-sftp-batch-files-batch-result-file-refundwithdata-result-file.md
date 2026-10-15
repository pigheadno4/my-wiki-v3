---
title: "Adyen RefundWithData batch result file"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/refundwithdata-result-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/refundwithdata-result-file/2026-09-15.md"
tags: [adyen, batch-processing, refund-with-data, result-file, psp-reference]
---

## Overview

This 2019-last-modified Adyen SFTP reference defines the `L` and `SL` records of a **RefundWithData result file**. It separates ordinary result rows from the separately linked parsing/validation-error result-file structure. The pinned page was captured 2026-09-15. It describes file fields, not final funds return to a shopper; see [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- The `L` line carries merchant-account metadata, fixed processing type `RefundWithData`, a merchant reference, and one of the literal status values `Success`, `Authorised`, `Refused`, `Cancelled`, `Received`, or `Error`. Optional `EchoData` returns as supplied and is not used by Adyen's payments platform. The page does not define a complete lifecycle transition or financial-finality meaning for those statuses.
- The `SL` result type is `RefundWithDataResult`. Its field 4 is the **original payment PSP reference**, not a PSP reference created for a refund. Field 5 is an authorisation code only when the payment is successfully authorised, otherwise empty; field 6 is a result code **if available**. Field 7 holds Adyen's mapped refusal reason or error description when the payment is not authorised, is refused, or an error occurs. The page lists possible error messages in the raw field table.
- The raw `TEST` example has one `L` row with `Received`, followed by an `SL` row whose result code is also `Received`, with a blank authorisation-code position. That example is not evidence of an `Authorised` status, an issued refund, or a final refund result.
- These `L`/`SL` tables do **not** specify amount or currency fields. The separate RefundWithData **request** guide has amount/exponent/currency fields; do not read a requested amount into this result row or infer a transferred/refunded amount from it. File parsing/validation errors use another linked result-file format. The example and status table do not establish whether an individual refund is safe to retry.

## Detail locators

- Lines 14–16: result-file identity and separate parsing/validation-error format.
- `## RefundWithData line`, lines 18–36: `L` merchant/account/reference/status/EchoData fields.
- `## RefundWithData sub-line`, lines 38–48: `SL` type, original-payment PSP reference, conditional authorisation code, optional result code and reason list.
- `## Example`, lines 50–59: `TEST` file with `Received` line and sub-line; illustrative only.

## Related

- [[adyen-batch-processing]] — batch-file route and reciprocal source link.
- [[adyen-refunds]] — separate refund-lifecycle boundary.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-refundwithdata-request-file-refundwithdata-request]] — separate request fields, including amount and exponent.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]] — common outer file/block records.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/refundwithdata-result-file/2026-09-15|RefundWithData result-file schema, captured 2026-09-15]]
