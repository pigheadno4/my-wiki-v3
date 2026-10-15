---
title: "Authorisation result file | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/authorisation-result-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/authorisation-result-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, authorisation, result-file]
---

## Overview

This Adyen SFTP **Authorisation result-file** reference (last modified 2019-10-25; collected 2026-09-15) defines the transaction-level `L` metadata row and its `PaymentResult` `SL` row after processing an authorisation batch. Parsing or validation errors instead use a separately linked `ValidationError` result-file structure. The page identifies authorization-result fields; it does not report capture, settlement, or consent. [[adyen-batch-processing]]

## Key takeaways

- The `L` row distinguishes the merchant account, `Authorisation` processing type, merchant reference for the transaction, and a transaction-status field. The listed status values are `Success`, `Authorised`, `Refused`, `Cancelled`, `Received`, and `Error`; the page does not define `Received` as authorized or treat all values as final payment outcomes. `EchoData` is a returnable echo field that Adyen does not use for processing. See raw lines 18–36.
- The `PaymentResult` `SL` row has a separate **original payment PSP reference** field. It can carry an authorization code when the payment is successfully authorized; that field is empty when it is not authorized. Result code is supplied if available, and refusal/error reason appears for a payment that is not authorized. Merchant reference (`L` field 6) and PSP reference (`SL` field 4) are distinct schema identities even though the example happens to show equal-looking numeric values. See raw lines 38–75 and 77–87.
- The example shows one `Authorised` result with code and one `Refused` result without authorization code. It is illustrative and does not establish that a merchant's particular authorisation was captured or settled. The detailed reason list includes modification and recurring-related strings, but this source specifies only a `PaymentResult` sub-line; no `Recurring` sub-line or credential-consent semantics are defined here.

## Detail locators

- **Validation-error alternate result-file route:** raw line 16 and `L` field 5 at line 28.
- **`L` row sequence, account, merchant reference, statuses and echo:** raw lines 18–36.
- **`PaymentResult` PSP reference, authorization code, result/reason fields:** raw lines 38–75.
- **Two-record illustrative result file:** raw lines 77–88.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]] — common result-file wrapper and successful ACK prerequisite
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]] — file-validation acknowledgment, distinct from per-record authorization results

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/authorisation-result-file/2026-09-15|Adyen Authorisation result file — collected 2026-09-15]]
