---
title: "Adyen Raise disputes API v4: add an attachment to an Issuing dispute"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/post/disputes/(disputeId)/attachments"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/post/disputes/(disputeId)/attachments/2026-11-07.md"
tags: [adyen, issuing, disputes, attachments, transfers-api]
---

## Overview

This 2026-11-07-captured `transfers-api` `latest` `/btl/api/v4` reference adds supporting information to an already raised dispute, such as receipts or correspondence. Its Test and Live server bases are listed. This is the Issuing raised-dispute attachment route, not a funds transfer or an acquiring dispute-defense submission. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The path requires `disputeId`, the unique identifier of the raised dispute. The request-body table marks `attachmentType` (`receipt`, `correspondence`, or `other`), `content`, and `fileName` required. `content` is Base64-encoded image data, and the filename must include one of the supported extensions: `jpeg`, `pdf`, or `tiff`. The page says line breaks, wrapping, and even a trailing newline in the encoded string cause malformed input.
- A `200` response says the request succeeded, but its response table marks `attachmentId` optional. Neither status nor an attachment ID establishes dispute submission, review, approval, chargeback, fee reversal, or a won outcome.
- The listed failures are 401 authentication required, 403 insufficient permissions, and 422 request validation error. Their problem fields are table-optional; within an optional `invalidFields` array, `message`, `name`, and `value` are required per item. No file-size limit, idempotency contract, or subsequent dispute status is stated here.

> [!warning] Contradiction
> The `content` description instructs callers to generate Base64 without line breaks or wrapping, then says not to use Java `Base64.NO_WRAP` or its equivalent. The capture does not reconcile those encoding instructions; it separately says trailing newlines cause malformed input.

## Detail locators

- Pinned raw, lines 5–15: purpose and Test/Live v4 server bases.
- Pinned raw, lines 19–30: dispute ID and complete request-body fields, types, extensions, and Base64 instructions.
- Pinned raw, lines 32–97: `200` with optional attachment ID and 401/403/422 problem-body schemas. The pinned page has no request or response example.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/post/disputes/(disputeId)/attachments/2026-11-07|Raised-dispute attachment API reference, captured 2026-11-07]]
