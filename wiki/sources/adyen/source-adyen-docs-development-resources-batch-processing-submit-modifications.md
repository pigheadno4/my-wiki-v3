---
title: "Adyen Customer Area batch modifications"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/submit-modifications"
raw_files:
  - "adyen/docs/development-resources/batch-processing/submit-modifications/2026-09-15.md"
tags: [adyen, batch-processing, customer-area, payment-modifications, webhooks]
---

## Overview

This 2026-09-15 Adyen guide covers **uploading a CSV of payment modification requests through Customer Area**. Its opening list names capture, cancel, refund and cancel-or-refund. The field table also lists `authoriseReferral`, an unresolved difference to check before treating it as supported through this route. This is a batch-submission and validation workflow: neither file upload, `COMPLETED` batch status nor a green row proves that a financial modification finally succeeded. The page metadata says last modified in 2023.

## Requirements and file shape

- The user needs **Merchant submit batch modifications** and **Merchant manage payments role**. To process modifications for multiple merchant accounts, the guide says to contact Adyen Support for enablement. Set up webhooks to receive modification outcome updates. See `Requirements`.
- Prepare UTF-8 CSV following RFC 4180 with the page's exceptions: no header, one modification per line, identical fields across rows, no empty/null fields, and at most 6,000 records. The payment's PSP reference is marked required. The table describes merchant account, modification type, amount in minor units, currency and merchant reference. If merchant account is omitted, Customer Area uses the account uploading the file; missing modification, amount or currency can be added in Customer Area, but the supplied value applies to **all** rows. See `Create an input file`.
- The rule against empty fields appears hard to reconcile with example rows that end in a comma, suggesting an empty final reference. Treat the examples as illustrative and resolve the CSV format against the route's current validation before upload. See rules at lines 43–48 and examples at lines 64–75.
- The amount behavior depends on the modification: the table says `cancelOrRefund` **always refunds the full amount**, regardless of the amount value supplied. Do not use its sample `0` as evidence of a zero-value refund or a partial cancel/refund. See `Create an input file`, Amount row and example.

## Upload and outcome boundary

Customer Area **Payments > Batch modifications** has an initial file submission and `Review Batch` validation, where errors can be corrected in the CSV or some missing fields supplied as one fixed value for every row. Selecting the later **Upload** queues then processes the batch. After batch status becomes `COMPLETED`, the downloadable result file gives individual messages. A green `successful` row means the modification **passed validation**; Adyen then attempts processing, which can still fail. Such a later failure is reported asynchronously through a webhook. Check that outcome before treating a capture, cancellation or refund as completed. See `Upload modifications` and `Check the result`.

## Detail locators

- `Create an input file`, lines 37–75: exact CSV rules, columns and field descriptions, optional account/default behavior, operation-list difference, amount semantics and examples.
- `Upload modifications`, lines 77–110: Customer Area path, Review Batch error categories, fixed-value repair applied to all rows, and QUEUED/PROCESSED statuses.
- `Check the result`, lines 112–122: COMPLETED batch status, green/red row messages, validation checks, and later webhook failure boundary.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/submit-modifications/2026-09-15|Adyen Customer Area batch-modification guide, 2026-09-15 snapshot]]
