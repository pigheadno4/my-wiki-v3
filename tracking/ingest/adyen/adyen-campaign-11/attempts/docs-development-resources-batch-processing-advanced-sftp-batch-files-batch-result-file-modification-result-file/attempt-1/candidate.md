---
title: "Adyen SFTP modification result file"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/modification-result-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/modification-result-file/2026-09-15.md"
tags: [adyen, batch-processing, modification, result-file, psp-reference]
---

## Overview

This 2019-last-modified Adyen reference defines the transaction-type `L` and `SL` records in an SFTP **Modification result file**. It links a separate structure for parsing or validation errors. Although its opening says “in case of a successful modification,” the table and example also contain `Error` and `Pending` modification statuses; that opening should not be applied to every row. The page was captured 2026-09-15. See [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- An `L` record identifies the merchant account, a processing type (`Cancel`, `Refund`, `Capture`, `CaptureOrRefund`, or `AuthoriseReferral`), optional merchant reference echoed from the corresponding request, and `Success`, `Error`, or `Pending` status. `Pending` says the modification request must be postponed for processing. Optional `EchoData` returns exactly as provided but is not used by Adyen's payments platform. A `ValidationError` processing type uses the separately linked validation-error file shape.
- The `ModificationResult` `SL` has **two different PSP references**: field 4 uniquely identifies **this modification**, while field 5 identifies the **original payment authorisation**. Neither is the `L` field-6 optional merchant reference. A row in the sample happens to repeat its `L` field-6 value in `SL` field 4; that example does not redefine the fields.
- `SL` field 6 carries a mapped refusal reason or error description when the payment is not authorised, is refused, or an error occurs. The raw list includes expired transactions, insufficient balance, full-only capture/refund limits, currency mismatch, unavailable/disallowed/failed operation and other cases. These are possible messages, not proof that a retry is safe.
- The sample `TEST` file shows a `Capture` `Success` row, a `Capture` `Error` row with `Transaction not found`, and a `Refund` `Error` row with `Insufficient balance on payment`. It demonstrates schema placement, not a live modification, ultimate capture/refund completion, or payment authorisation. This page does not define `Received` or `Authorised` as result-file statuses; do not import those from another lifecycle.

## Detail locators

- Lines 14–16: stated result-file scope and separate parsing/validation-error route.
- `## Modification line`, lines 18–37: `L` record metadata, action types, optional merchant reference, statuses and EchoData.
- `## Modification sub-line`, lines 39–74: `SL` result type, distinct modification/original-authorisation PSP references and error-message list.
- `## Example`, lines 76–89: `TEST` capture/refund rows with one success and two errors.

## Related

- [[adyen-batch-processing]] — batch workflow and reciprocal source route.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]] — common outer result-file records, separate from `L`/`SL` modification fields.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]] — validation ACK, not the modification result.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/modification-result-file/2026-09-15|Modification result-file reference, captured 2026-09-15]]
