---
title: "Adyen Issuing: get one dispute attachment"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/(attachmentId)"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07.md"
tags: [adyen, issuing, disputes, attachments, api-explorer]
---

## Overview

This 2026-11-07-captured `GET /disputes/{disputeId}/attachments/{attachmentId}` reference retrieves one attachment associated with a raised dispute. It appears under a `transfers-api` URL with Balance Platform v4 Test and Live servers; the retrieved attachment is evidence data, not a dispute decision or funds-movement result. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Both path IDs are required: `disputeId` identifies the raised dispute and `attachmentId` identifies its attachment. No query parameters or body are specified on this page.
- `200 Success` describes a successful request. The response table requires `attachmentType` (`receipt`, `correspondence`, or `other`), Base64 `content`, and `fileName` with a supported `jpeg`, `pdf`, or `tiff` extension; `id` is optional in that table.
- The page lists `401` authentication required, `403` insufficient permissions, and `422` request validation error. Error-object fields are optional at the parent level, while `invalidFields` child entries have required fields if that optional array is present. No attachment upload, submission, dispute outcome, settlement or bank receipt is established by this read.

> [!warning] Contradiction
> The `content` description says Base64 strings must have no line breaks, then says not to use Java's `Base64.NO_WRAP` or an equivalent. The capture does not resolve this conflicting encoding guidance; do not infer a working encoder choice from it.

## Detail locators

- Endpoint purpose, Test/Live v4 servers and required path IDs: [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07#L5|raw lines 5–23]].
- `200` response fields, allowed types/extensions and conflicting Base64 text: [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07#L25|raw lines 25–36]].
- Authentication, permission and validation errors with optional error-object fields: [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07#L39|raw lines 39–93]].

## Related

- [[adyen-issuing]] — Issuing dispute context.
- [[source-adyen-api-explorer-transfers-api-latest-overview]] — separate Raise disputes API v4 catalog.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07|Adyen dispute-attachment GET reference capture, 2026-11-07]]
