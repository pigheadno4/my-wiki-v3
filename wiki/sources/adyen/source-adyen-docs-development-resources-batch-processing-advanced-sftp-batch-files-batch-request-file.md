---
title: "Batch request file | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/2026-09-15.md"
tags: [adyen, batch-processing, sftp, batch-request, file-format]
---

## Overview

This 2026-09-15 [[adyen]] Docs reference defines common records and fields in an SFTP batch request file across transaction types: File Header (`FH`), Block Header (`BH`), Block Trailer (`BT`), and File Trailer (`FT`). It specifies the file and block identifiers, type and environment fields, requiredness, counters, and upload handoff. Transaction-specific records remain in the linked request-file guides. [[adyen-batch-processing]]

> [!warning] Contradiction
> This common request-file table marks FH field 9 (`FileType`) required, while the separately reviewed naming guide calls FH field 9 optional and describes a delimiter placeholder. These snapshot statements conflict; the generic optional-field placeholder example does not establish that a blank FileType is accepted. Confirm the accepted schema for implementation. [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-file-naming-and-structure]]

## Key takeaways

- The `FH` table marks fields 1–9 required: `FH`, format version `1.0`, `TEST` or `LIVE`, `Company`, company account name, submission platform, file sequence number, company-linked API credential username, and one listed file type. Submission platform and file sequence number must match the filename. Field 10, `EchoData`, is optional, returned unchanged when populated, and not used by Adyen for payment processing. See raw lines 26-57 for exact positions, allowed types, and the 80-character `EchoData` limit.
- `BH` starts a grouping of transactions and has a required block number increasing by one per block; its `EchoData` is optional. `BT` carries the number of line records in its block; `FT` carries the number of blocks in the file. These are different counter units. See raw lines 59-86.
- Once prepared, the file can be uploaded to the SFTP `in` subfolder so Adyen can fetch and queue it. Upload or queueing is not a file acceptance, per-record result, or financial outcome; use the separate acknowledgment and result guides.

> [!warning] Account-scope wording
> The `FH` prose says it identifies the merchant account (raw line 30), but its field table instead requires a `Company` account type and company account name (raw lines 41-45). This page does not resolve that difference or the parent batch overview's one-merchant-account-per-file rule versus the SFTP guide's Support-enabled multi-merchant-account modifications. Preserve those qualifications and verify the applicable file composition before use.

## Detail locators

- **Example FH/BH/BT/FT layout:** raw lines 16-24; ellipsis stands for omitted records and is not an actual line-count illustration.
- **File Header identity, environment, filename matching, credential and type fields:** raw lines 26-57; type-specific links are navigation.
- **File Trailer block count:** raw lines 59-66.
- **Block Header number and optional echo:** raw lines 68-77.
- **Block Trailer line-record count and SFTP `in` handoff:** raw lines 79-88.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] — SFTP setup and multi-account qualification
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]] — file acknowledgment

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/2026-09-15|Adyen batch request file — collected 2026-09-15]]
