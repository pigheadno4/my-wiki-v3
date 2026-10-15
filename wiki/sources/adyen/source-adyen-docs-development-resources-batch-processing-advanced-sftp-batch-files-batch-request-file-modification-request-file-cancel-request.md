---
title: "Adyen SFTP Cancel request sub-line"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/cancel-request"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/cancel-request/2026-09-15.md"
tags: [adyen, batch-processing, cancel, modification, request-schema]
---

## Overview

This 2019-last-modified Adyen SFTP batch reference defines the mandatory `Cancel` **request sub-line** used when submitting a payment cancellation modification. It gives four marked-required positions and says partial cancellation modifications cannot be submitted. The raw page was captured 2026-09-15. A shaped request is distinct from batch validation, a cancellation result, and any financial outcome; see [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- The `Cancel` `SL` is mandatory for a payment cancellation request. Fields 1–4 are all marked required: `SL` record type, sequential sub-line number within the parent `L` line, fixed `Cancel` type, and the **original payment PSP reference**. The table gives no amount or currency position.
- The page explicitly says **partial cancellation modifications cannot be submitted**. This request-shape limit should not be expanded into a claim about partial capture, refund, or a particular payment's current cancellation eligibility.
- The illustrative `TEST` `Modification` file has a parent `L` with a merchant reference and one `SL,1,Cancel,<original PSP reference>`. The merchant-reference text in `L` and original-payment PSP reference in `SL` are different field identities. Example values do not prove a real file was sent, accepted, or acted on.
- This page does not define ACK validation, result-file statuses, webhook behavior, whether the original payment remains cancellable, or a completed cancellation. Retrieve the separate batch result and payment-lifecycle routes for those questions.

## Detail locators

- `## Mandatory sub-lines`, lines 16–18: required `Cancel` sub-line.
- `### Cancel`, lines 20–30: modification context, no partial cancellation, all four required fields and original-payment PSP reference.
- Lines 32–39: illustrative `TEST` `Modification` file with `L` and `Cancel` `SL`.

## Related

- [[adyen-batch-processing]] — batch request, ACK and result boundaries.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-result-file-modification-result-file]] — separate result-file schema.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]] — common outer request-file records.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/modification-request-file/cancel-request/2026-09-15|Cancel request sub-line schema, captured 2026-09-15]]
