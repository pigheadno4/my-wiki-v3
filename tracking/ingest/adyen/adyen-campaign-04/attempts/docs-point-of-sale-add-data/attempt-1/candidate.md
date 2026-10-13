---
title: "Adyen POS payment SaleToAcquirerData"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/add-data"
raw_files:
  - "adyen/docs/point-of-sale/add-data/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, sale-to-acquirer-data, additional-response, payment-data]
---

## Overview

This Adyen Docs page explains how a Terminal API in-person payment request can carry extra data in `PaymentRequest.SaleData.SaleToAcquirerData`, and how selected processing and request data can return in `PaymentResponse.Response.AdditionalResponse`. Its stated integration scope is Terminal API with payment terminals or a Mobile solution. See [[adyen]] and [[adyen-terminal-api]]. The page is a dated website guide with examples, not a fixed Checkout API schema/version or proof that a particular account, tender option, tokenization flow, split, or statement is enabled and accepted.

## Key takeaways

- `SaleToAcquirerData` can carry application information, merchant-defined metadata, shopper-recognition/tokenization inputs, dynamic shopper statement, platform split details, tender options, and other additional data. These categories serve different purposes; the page routes their exact fields and behavior to more specific guides and a sample collection.
- Before relying on additional response fields, select the desired data types under **Developers > Additional data** in Customer Area. The response can include some submitted fields and data produced by payment processing. The page says merchant metadata can include up to 20 fields, with names at most 20 characters and values at most 80; receiving metadata in settlement reports requires contacting Support.
- The request field supports two encodings: a JSON object converted to a Base64 string, or form-encoded key-value pairs separated by `&`. Under the described default behavior, `AdditionalResponse` matches that request encoding; with no `SaleToAcquirerData`, it uses key-value pairs. Contact Support to always receive one response format regardless of the request encoding. Preserve the format when decoding; the illustrated JSON and Java payloads are examples, not a comprehensive field contract.
- Shopper identifiers used for recognition or later token payments are created by including such fields as `shopperEmail`, `shopperReference`, and `recurringProcessingModel` in the initial request, then retrieving and storing returned identifiers. A transaction-specific `shopperStatement` reaches a bank statement only if the account is configured for dynamic transaction descriptions; the page recommends a short restricted-character value because banks can truncate or lack Unicode support.
- The Base64 and key-value examples each show a payment request with metadata, shopper statement, shopper identifiers, and `ReceiptHandler,AskGratuity` tender options, followed by a corresponding `AdditionalResponse`. Their `MessageHeader.ProtocolVersion` is `3.0`; that is the Terminal API/nexo protocol value in the examples, not a pinned Checkout API version. The separate API Explorer link for additional data uses `latest` and is navigation only here.

## Detail locators

- Purpose, stated terminal/Mobile scope, and response setup prerequisite: `# Add information to a payment` and `## Requirements`, raw lines 15–28.
- Data categories and their downstream routes: `## Data elements`, raw lines 30–42; metadata limits/reporting: lines 50–54; shopper recognition inputs: lines 56–60; statement advice and configuration gate: lines 62–68; split/tender/additional-data pointers: lines 70–82.
- Two supported encodings and response-format rule: `## Adding data elements to your request`, raw lines 84–93; Customer Area selection and no-request-data default: `## Receiving the additional response`, lines 95–105.
- Base64 JSON construction, Terminal API request and matching response illustration: `## Option 1`, raw lines 107–327, especially lines 111–145, 149–178, 222–265.
- Key-value construction, request and matching response illustration: `## Option 2`, raw lines 329–468, especially lines 333–360 and 428–462. The example strings do not establish an exhaustive encoding or validation specification.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — in-person Terminal API message architecture and provenance boundary from versioned GitHub examples.

## Related raw API references

- The raw page links to the SaleToAcquirerData sample collection, application information, shopper recognition, tender options, in-person platform payments, and API Explorer additional data. Those linked pages have not been read for this entry; use them for navigation, not additional behavioral claims. See raw lines 42–82 and 470–475.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/add-data/2026-09-15|Adyen Docs: Add information to a payment (2026-09-15 snapshot)]]
