---
title: "Adyen SFTP batch CancelOrRefund request"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/cancelorrefund-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/cancelorrefund-request/2026-09-15.md"
tags: [adyen, batch-processing, sftp, modification, cancel-or-refund]
---

## Overview

This Adyen Docs snapshot (2019-04-30 last-modified metadata; captured 2026-09-15) defines the mandatory `CancelOrRefund` sub-line of an advanced-SFTP **Modification** batch request. Despite the operation name, its introductory sentence calls it a cancellation request; the page does not define how Adyen chooses cancellation versus refund for a particular original payment. It is a request format, not evidence that either financial action completed. See [[adyen-batch-processing]] and [[adyen]].

## Key takeaways

- The mandatory `CancelOrRefund` `SL` positions are fixed `SL`, sequential sub-line counter, fixed `CancelOrRefund`, and the **original payment PSP reference** at position 4. No amount or currency position appears in this page's table or sample. [Raw lines 16–30, 32–39]
- The page explicitly says partial **cancellation** modifications cannot be submitted. It does not thereby define partial-refund support, a partial amount, original payment state, or a rule for when the combined operation resolves to cancellation versus refund. [Raw lines 20–23]
- The TEST sample places `CancelOrRefund` on the `L` line and `SL,1` within a `Modification` file. It is illustrative request content; file ACK, per-modification result, and downstream financial outcome must be checked separately. [Raw lines 32–39]

## Detail locators

- Operation wording and partial-cancellation prohibition: raw lines 14–23. Complete required `SL` table: raw lines 25–30. TEST file example: raw lines 32–39.
- This source does not report an action status, cancellation completion, refund success, or a refund credit. Route result questions to the batch Modification result source and the original payment's actual state.

## Related

- [[adyen-batch-processing]]
- [[adyen]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/cancelorrefund-request/2026-09-15|Adyen CancelOrRefund request, 2026-09-15 snapshot]]
