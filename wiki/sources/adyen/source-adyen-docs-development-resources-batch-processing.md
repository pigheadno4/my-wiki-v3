---
title: "Adyen batch processing"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing"
raw_files:
  - "adyen/docs/development-resources/batch-processing/2026-09-15.md"
tags: [adyen, batch-processing, bulk-requests, customer-area, sftp]
---

> [!warning] Contradiction
> The batch overview says one transaction type for one merchant account per SFTP file. The SFTP guide says one request type per merchant account and mentions Support-enabled modifications for multiple merchant accounts, without defining whether the one-merchant-account-per-file layout changes. These dated statements remain unresolved; confirm the approved file composition with Adyen for that case. [[source-adyen-docs-development-resources-batch-processing]] [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]]

## Overview

This 2026-09-15 snapshot of an Adyen development-resources landing page introduces uploading an input file to submit payment or modification requests in bulk. It gives refunds and failed-capture retries as examples, while advising API use for regular payments or modifications because preparing input files often takes manual effort. The page metadata says last modified in 2019. It compares upload routes; it does not document a particular file's acknowledgment, per-record result, or financial outcome.

## Key takeaways

- **Customer Area:** Modification requests only, using a simple CSV. The table says one file may contain modifications for different merchant accounts and that Customer Area helps add missing fields and fix errors. See `Batch processing options` and the `Submit modifications` navigation link.
- **SFTP:** The listed request types are Authorisation, Modification, RefundWithData, Payout, PayoutModification, AccountUpdater, and StoreToken. The input is a complex CSV with headers, footers, counters and multiline records. The table limits a file to one transaction type for one merchant account and calls for SFTP setup and PGP encryption. See `Batch processing options` and `Submit through SFTP`.
- Uploading or transporting a file must not be read as proof that every row was accepted or that an authorization, capture retry, refund or payout succeeded. This overview does not specify acknowledgment/result-file semantics; the linked route-specific guides must be read for those details. The failed-capture retry phrase is a use-case example, not a blanket instruction to replay an unresolved operation.

## Detail locators

- `Batch processing options`, lines 23–30: exact request-type matrix, channel, file shape, per-file merchant-account/type boundary, and SFTP/PGP prerequisites.
- `Choose an option`, lines 32–40: navigation to Customer Area modification submission and advanced SFTP batch files. The linked procedures have not been imported into this landing-page summary.

## Related

- [[adyen]]
- [[adyen-batch-processing]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/2026-09-15|Adyen batch-processing overview, 2026-09-15 snapshot]]
