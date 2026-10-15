---
title: "Adyen SFTP batch result file common records"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, result-file, file-format]
---

## Overview

This [[adyen]] reference describes fields common to SFTP batch result files after a batch acknowledgement (ACK) file reports successful validation. It says the result file can be obtained two days after that ACK. Its scope is the outer file and block records—`FH`, `FT`, `BH`, and `BT`—not a transaction-type-specific line result or a final payment, refund, or payout outcome. Use [[adyen-batch-processing]] for the batch route and the relevant request-type result guide for individual records.

## Key takeaways

- `FH` carries request-file header identity: format version `1.0`, `TEST` or `LIVE`, `MerchantAccount` or `Company`, account name, submission platform, file sequence number, the SFTP upload API credential name, file type, and optional file-header `EchoData`. The account and submission values are inherited from the corresponding request file; they do not identify an individual payment.
- `FT` counts blocks in the result file. `BH` has a sequential block number and optional block-header `EchoData` from the request. `BT` counts line records in that block. These file/block counters and echo fields help correlate structure and requests; they are not transaction statuses.
- The `FH` file-type list routes to Authorisation, Payout, RefundWithData, Modification, PayoutModification, and AccountUpdater result guides. This common-record page gives no per-line result schema or PSP reference field. Do not substitute its file sequence, upload credential, block number, or `EchoData` for a transaction PSP reference.
- A successful ACK validation only precedes the possible result-file retrieval described here. It does not prove that each submitted operation succeeded, and this page does not settle whether a later webhook or lifecycle event is required for a particular operation. The displayed `TEST` file fragment is illustrative, not an execution record.

## Detail locators

- **Result-file timing after successfully validated ACK:** raw lines 14–18.
- **`FH` request-file identity, environment, account, file sequence, credential, type and echo fields:** raw lines 20–42, under `### File Header [FH]`.
- **`FT` block count:** raw lines 44–51, under `### File Trailer [FT]`.
- **`BH` block identity/echo and `BT` line-record count:** raw lines 53–70, under `### Block Header [BH]` and `### Block Trailer [BT]`.
- **Illustrative file fragment:** raw lines 72–78.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]]

## Related raw API references

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/authorisation-result-file/2026-09-15|Authorisation result-file detail — navigation only; raw not read for this entry]]
- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/modification-result-file/2026-09-15|Modification result-file detail — navigation only; raw not read for this entry]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-result-file/2026-09-15|Adyen batch result common-record reference — collected 2026-09-15]]
