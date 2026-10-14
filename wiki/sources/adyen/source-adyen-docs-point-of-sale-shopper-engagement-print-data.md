---
title: "Adyen Terminal API print data outside payments"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/print-data"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/print-data/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, printing]
---

## Overview

Adyen's print-data guide, last modified 2024-12-12 and captured 2026-09-15, describes a merchant POS app sending Terminal API print requests for text, QR codes or PNG images on a payment terminal **outside a payment flow**. Examples include a bill before a pay-at-table payment, an entry ticket and an order pickup slip. This is a [[adyen-pos-shopper-engagement]] Device/Print operation, not a payment, refund or proof that a transaction succeeded.

## Key takeaways

- **Printer hardware is required.** The guide says the Terminal API path works only on payment terminals with a built-in printer. Its example model list includes V240m Plus in Brazil, V400c Plus, V400m, S1F2, S1F2L and S1F4Pro; the list is a dated snapshot, not current model/region/account availability. EAN-8, EAN-13, UPC-A, Code 25, Code 128 and PDF417 are expressly unsupported barcode formats.
- **Use a Device-class Print request.** The standard `SaleToPOIRequest.MessageHeader` uses protocol 3.0, `MessageClass: Device`, `MessageCategory: Print`, `MessageType: Request`, SaleID, POIID and terminal-scoped ServiceID unique within the preceding 48 hours. The page's text example uses `PrintOutput.DocumentQualifier: Document`, `ResponseMode: PrintEnd`, `OutputFormat: Text` and one or more `OutputText` items. Formatting options include style, alignment and line-continuation; the exact field table is in the raw. A unique ServiceID is not a stated retry or idempotency guarantee.
- **Text and QR are separate requests.** A combined text-and-QR slip needs two consecutive print requests; unlike shopper receipt printing, this guide says there is no tear-off prompt after a print request. For its QR path, `DocumentQualifier` is `CustomerReceipt`, `OutputFormat` is `BarCode`, and `BarcodeType` is `QRCode`. A URL may be plain text; more complex content is URL encoded. The `CustomerReceipt` qualifier in this print example does not show that a payment receipt or payment outcome exists.
- **PNG printing has a specific encoding pipeline.** Base64-encode the PNG, place it in the given XML `<img>` sample with the specified space after `base64,`, then Base64-encode the entire XML for `OutputXHTML` with `OutputFormat: XHTML`. The page states a 256000-byte image limit and recommends 1-bit grayscale up to 384 pixels wide. Those dimensions are guidance, not a claim that every image prints successfully.
- **Check the print result.** The guide's successful examples show `PrintResponse.Response.Result: Success` with the matching `DocumentQualifier`. Printer-related failure uses `Result: Failure`, `ErrorCondition: DeviceOut` and `AdditionalResponse` explaining conditions such as low/no paper, a jam or no printer. A print success is not a payment authorization, and the page does not establish delivery, persistence, logging or security handling for sensitive content printed on paper.

## Detail locators

- Raw opening and `## Requirements` (lines 15–38): out-of-payment examples, two-request text/QR flow, built-in printer models and unsupported barcode formats.
- Raw `## Print text` (lines 40–313): Device/Print header, text `PrintOutput` fields, formatting flags, document/receipt-style examples and response check.
- Raw `## Print a QR code` (lines 315–456): URL encoding rule, `CustomerReceipt`/`BarCode`/`QRCode` fields, request examples and `PrintResponse`.
- Raw `## Print an image` (lines 458–557): 256000-byte limit, recommended 1-bit/384-pixel image, double Base64 XML process, `XHTML` output and response.
- Raw `## Handle print errors` (lines 559–605): `DeviceOut`, `AdditionalResponse` conditions and failed-print example.

## Related

- [[adyen-pos-shopper-engagement]] — POS shopper-interaction hub.
- [[adyen-terminal-api]] — Terminal API message and financial-operation boundary.
- [[adyen-payment-terminals]] — physical printer-capable hardware route.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/print-data/2026-09-15|Print data on the terminal, fetched 2026-09-15]]
