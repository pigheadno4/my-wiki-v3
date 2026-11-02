---
title: "Terminal API Print request and response | Adyen API Explorer"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/print"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/print/2026-09-15.md"
tags: [adyen, terminal-api, print, api-explorer, point-of-sale]
---

## Overview

This 2026-09-15 API Explorer snapshot describes `POST /print` as a Print Request carrying the data to print and instructions for processing it, plus a Print Response. It lists test cloud Device API `/v1/merchants/{merchantAccount}/devices/{deviceId}/sync` and `/async` server addresses and a local terminal-IP placeholder. Those paths identify a merchant account and device for cloud transport; this page does not provide a Terminal API protocol version, message header, terminal `POIID`, sale/session identity, authentication scheme, or production endpoint. The `latest` documentation label is not a pinned protocol version.

## Key takeaways

- The request-body table requires `PrintOutput` with `DocumentQualifier`, `ResponseMode`, and `OutputContent.OutputFormat`. Qualifiers include sale, cashier and customer receipts, document, voucher, and journal; response modes are `NotRequired`, `Immediate`, `PrintEnd`, and `SoundEnd`. Output formats are `MessageRef`, `Text`, `XHTML`, and `BarCode`. The table makes `OutputText` mandatory only for Text, `OutputXHTML` only for XHTML, and `OutputBarcode` only for barcode output, disallowing each outside its format. See the raw for the exact names and types.
- Optional `IntegratedPrintFlag` allows print integration with another print or separate printing. When integrated, the response is always immediate even if `ResponseMode` is `PrintEnd`; an immediate response therefore must not be read as proof that printing has ended. Optional `RequiredSignatureFlag` indicates a physical customer signature requirement for a cardholder payment receipt.
- The 200 response description says a print response can be absent when a response is not required. When present, its body table requires `DocumentQualifier` and `Response.Result`, with `Success`, `Failure`, or `Partial` results. The `Response` description says `ErrorCondition` is absent or unused on Success and must be present otherwise; `AdditionalResponse` is optional logging detail. A successful Print response concerns print processing, not payment authorization, capture, settlement, or bank receipt.
- The page supplies no payload-wide content-size or image/barcode limits, device-printer compatibility guarantee, retry/idempotency, timeout, reversal, deprecation, asynchronous callback, or payment lifecycle rule. Separate POS print guidance carries any such detail.

## Detail locators

- Operation purpose and captured test cloud/local server addresses: raw lines 5–19.
- Request required and conditional output fields, response modes, and integrated-print timing exception: raw lines 21–36.
- Print response absence, required fields, results, errors, and logging field: raw lines 38–51.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API concept and integration boundaries.
- [[source-adyen-docs-point-of-sale-shopper-engagement-print-data]] — separate POS guide for print examples, hardware and payload qualifications; those details are not asserted by this API Explorer page.
- [[source-adyen-docs-point-of-sale-basic-tapi-integration-generate-receipts]] — separate receipt guide.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/print/2026-09-15|Adyen API Explorer Print request/response (2026-09-15 snapshot)]]
