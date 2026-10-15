---
title: "Adyen SFTP batch Refund modification request"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/refund-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/refund-request/2026-09-15.md"
tags: [adyen, batch-processing, sftp, refund, modification, request-file]
---

## Overview

This Adyen Docs snapshot (2019-04-30 last-modified metadata; captured 2026-09-15) gives the mandatory `Refund` sub-line for a **Modification** SFTP batch refund request. It defines request fields, not acceptance, refund execution, a final shopper credit, or retry safety. For the larger file and result routes see [[adyen-batch-processing]] and [[adyen]].

## Key takeaways

- A refund modification request requires the `Refund` `SL` sub-line. Its positions 1–3 are fixed `SL`, sequential sub-line counter, and fixed `Refund` transaction type. Position 4 is the **original payment PSP reference**, not a new refund reference. [Raw lines 16–29]
- Positions 5–7 are required numeric amount, numeric currency exponent, and three-character ISO currency code. The TEST sample `SL,1,Refund,9630124578963201,123,2,EUR` illustrates placement; the page does not spell out partial-refund eligibility, an amount ceiling, original-capture state, or a general minor-unit conversion rule. Seek those qualifications in the relevant refund guidance and result evidence before applying a live case. [Raw lines 30–41]
- The example places the `Refund` sub-line under an `L` line with `Refund` action in a `Modification` file. It is not a recorded successful refund. ACK validation and per-modification results belong to distinct batch sources. [Raw lines 34–41]

## Detail locators

- Entire `Refund` sub-line table and requiredness: raw lines 24–32. TEST file example: raw lines 34–41. The page links general online refund guidance at raw line 22, but that linked content is not included here.
- This page gives no successful/failed/pending refund status and no settlement timing. Check original transaction state and later result evidence separately; do not infer that a syntactically formed request can safely be retried.

## Related

- [[adyen-batch-processing]]
- [[adyen]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/refund-request/2026-09-15|Adyen Refund modification request, 2026-09-15 snapshot]]
