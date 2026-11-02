---
title: "Adyen Terminal API POST /abort — Abort Request body"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/abort"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/abort/2026-09-15.md"
tags: [adyen, terminal-api, point-of-sale, abort]
---

## Overview

This 2026-09-15 API Explorer `latest` POST /abort page describes the body of a Sale-to-POI Abort Request for identifying the message request carrying a transaction to abort. It lists test cloud sync and async Device API URLs and a local-terminal-IP placeholder. The page does not state a numbered Terminal API message version; `/v1` appears in the listed cloud transport URLs. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- `MessageReference` and `AbortReason` are required request-body fields. `MessageReference` identifies a previous POI transaction/message header; its listed child fields (`MessageCategory`, `ServiceID`, `DeviceID`, `SaleID`, and `POIID`) are each marked optional in this body table. `SaleID` and `POIID` have defaults from `MessageHeader`; the full header/envelope is not specified here.
- `DisplayOutput` is optional. If supplied, its table marks `Device`, `InfoQualify`, and `OutputContent` required, with `OutputContent.OutputFormat` required. The content fields depend on that format: `OutputText` for Text, `OutputXHTML` for XHTML, and `OutputBarcode` for Barcode. For the named Input Devices, Diagnosis, and `EnableService` cases, the page says `ResponseRequiredFlag` and `MinimumDisplayTime` must be absent. See the raw table for the exact nested conditions and values.
- A successful `AbortRequest` is documented as HTTP 200 OK with no body. This page supplies no original-payment response, terminal transaction result, authorization or reversal result, or later status confirmation. It does not establish that an HTTP 200 alone proves the transaction was aborted.
- The pinned page gives no authentication/header contract, error-response schema, live cloud URL, retry window, or deprecation notice. The listed async transport URL alone does not define callback delivery or a final asynchronous outcome.

## Detail locators

- Request purpose and captured test cloud sync/async and local-hosting server entries: raw lines 5–19.
- Required body fields, reference child optionality/defaults, optional display structure and conditional content: raw lines 21–51.
- Bodyless HTTP 200 response: raw lines 53–56.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API message and POS cancellation context.
- [[source-adyen-docs-point-of-sale-basic-tapi-integration-cancel-a-transaction]] — separate POS cancellation guide for the wider transaction flow.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/abort/2026-09-15|Adyen Terminal API latest POST /abort, captured 2026-09-15]]
