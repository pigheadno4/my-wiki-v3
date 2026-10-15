---
title: "Adyen SFTP Capture request sub-line"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/capture-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/capture-request/2026-09-15.md"
tags: [adyen, batch-processing, capture, modification, request-schema]
---

## Overview

This 2019-last-modified Adyen SFTP batch page defines the mandatory `Capture` **request sub-line** for a payment capture modification. It identifies the original payment PSP reference and the requested amount, exponent, and currency. An optional airline-data branch is linked but not specified here. The raw was captured 2026-09-15; see [[adyen]], [[adyen-batch-processing]], and the separate [[adyen-payment-capture]] lifecycle route.

## Key takeaways

- A `Capture` `SL` is mandatory when submitting a payment capture request. Its table marks fields 1–7 required: `SL` record type, sequential sub-line number, `Capture` type, **original payment PSP reference**, numeric amount, numeric currency exponent, and three-character ISO currency code. The page gives no additional amount conversion rule beyond those field descriptions.
- The optional airline-data route is linked in the introduction. Use its separate guide before adding or interpreting airline fields; this page does not define their conditional schema.
- The sample is a `TEST` `Modification` file containing one `Capture` line and an `SL,1,Capture,...,100,2,EUR` request. It illustrates field placement. It is not evidence that the file was submitted, passed validation, that the payment method supports capture, or that this or any other capture completed.
- This page does not define capture-result or webhook states, partial/multiple-capture eligibility, retry safety, or settlement. The original-payment reference in a **request** must not be confused with any later modification PSP reference in a result file.

## Detail locators

- Line 16: optional airline-data child route.
- `## Mandatory sub-lines`, lines 18–24: mandatory `Capture` request `SL` and its purpose.
- `### Capture` field table, lines 26–34: all seven marked-required fields, especially original PSP reference and amount/exponent/currency.
- Lines 36–43: illustrative `TEST` `Modification` batch file and Capture sub-line.

## Related

- [[adyen-batch-processing]] — SFTP batch flow and reciprocal source route.
- [[adyen-payment-capture]] — separate capture lifecycle, method support and asynchronous outcome boundary.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-modification-request-file-capture-request-capture-with-airline-data]] — separate optional airline-data capture guide.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file]] — distinct Modification result-file fields.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/capture-request/2026-09-15|Capture request sub-line schema, captured 2026-09-15]]
