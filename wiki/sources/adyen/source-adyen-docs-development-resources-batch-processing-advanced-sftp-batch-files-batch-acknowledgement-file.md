---
title: "Adyen batch acknowledgement file"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-acknowledgement-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-acknowledgement-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, acknowledgement, validation]
---

## Overview

This Adyen Docs page describes the batch acknowledgement (ACK) file generated after validation of a submitted batch request file. A successful validation yields an overview of processed data; a failed validation identifies request-file lines that failed checks. The ACK describes file validation and does not itself establish each transaction's financial outcome.

## Key takeaways

- A successful ACK example contains file header `FH`, processed block and line counts in `R`, and the next file submission number in `N`. Its header identifies the environment (`TEST` or `LIVE`), company account, submission platform, file sequence, linked API credential username, and file type. Consult the raw field table for exact positions and allowed file types.
- A failed-validation ACK includes an `E` line per failed request-file line. The error record identifies whether the problem belongs to the file header (`FH`), line (`L`), sub-line (`SL`), or incomplete/unreadable file (`F`), along with file line number, code, and description.
- `N,NextFileSubmissionNumber` appears regardless of validation outcome. After an erroneous file, Adyen may only guess the next number, so it may be wrong; if the header cannot be read or parsed, the number is always incorrect. Do not use that value alone as proof that a rejected file advanced the submission sequence.

## Detail locators

- Raw heading **ACK - Validation successful**, lines 23–64: sample `FH`/`R`/`N` records and the successful ACK field tables.
- Raw heading **Next File Submission Number [N]**, lines 66–94: submission-platform sequence and invalid-number warnings.
- Raw heading **ACK - Validation failed**, lines 96–122: failed-line sample and `E` field table.
- Raw heading **Next File Submission Number [N]**, lines 124–152: repeated `N` behavior for failed validation.

## Related

- [[adyen]] — provider context
- [[adyen-batch-processing]] — batch-file flow and related source routes

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-acknowledgement-file/2026-09-15|Batch acknowledgement file (2026-09-15 snapshot)]]
