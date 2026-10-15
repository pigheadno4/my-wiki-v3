---
title: "Adyen batch file naming and structure"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-file-naming-and-structure"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-file-naming-and-structure/2026-09-15.md"
tags: [adyen, batch-processing, sftp, file-naming, validation]
---

## Overview

This [[adyen]] reference defines the request, result and acknowledgement filename patterns and common file structure for advanced SFTP batch processing. It is a file-level format and validation route through [[adyen-batch-processing]]; a correctly named file or validation ACK does not establish a transaction's financial outcome.

## Key takeaways

- Each request filename must be unique and use `[Submission Platform]_[File Sequence Number]_[FileType].csv`. The platform identifies the submitting server; the sequence is scoped to that platform and increments **exactly one** after each successful file submission. Reused or skipped sequence numbers cause rejection. The filename's file type must be one of the listed Authorisation, Payout, StoreToken, RefundWithData, Modification, PayoutModification or AccountUpdater types. See **Naming → Batch request file**, raw lines 18–45.
- Result filenames append `_result` or, for an encrypted result file, `_result_enc` to the original `.csv` filename. ACK filenames append `_ack`. These suffixes identify file routes; this page does not itself set up PGP, prove that a particular transfer was encrypted, or define successful individual payment or payout results. See raw lines 47–70.
- The CSV format follows RFC 4180 with no multiline fields and a variable number of fields per line. A header and trailer are needed for parsing. The `FH` sequence must match the filename, one file cannot mix transaction/file types, UTF-8 is specified, and optional fields may still require placeholder delimiters to preserve the fixed column count for that transaction type. See **Structure**, raw lines 72–99.
- The naming page says an ACK is posted to the `ack` folder if validation has an error, while the separately captured **batch acknowledgement file** guide explicitly documents both successful and failed validation ACKs. Treat the naming-page wording as incomplete on ACK generation. A successful ACK concerns file validation, not individual financial outcomes; after validation errors the ACK's `NextFileSubmissionNumber` can be a guess, and when the header cannot be parsed it is always incorrect. See this raw at lines 60–70 and [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]]; its raw lines 18–25 and 66–94.

## Detail locators

- Request uniqueness, platform-scoped sequence, duplicate/gap rejection and allowed types: **Naming → Batch request file**, raw lines 18–45.
- Result and ACK suffixes and folder descriptions: **Naming → Batch result file / Batch acknowledgment file**, raw lines 47–70.
- CSV exceptions, header/trailer and structural constraints: **Structure**, raw lines 72–99.

## Related

- Company: [[adyen]]
- Concept: [[adyen-batch-processing]]
- ACK validation meaning: [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]]
- Common request records: [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]]
- Common result records: [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-file-naming-and-structure/2026-09-15|Adyen batch file naming and structure]] — full pinned 2026-09-15 snapshot; page metadata says last modified 2020-04-09
