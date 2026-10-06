---
title: "Braintree In-Person Receipt Printing API"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/receipt-printing-api"
raw_files:
  - "braintree/in-person/guides/receipt-printing-api-2026-09-16.md"
tags: [braintree, in-person, receipt-printing, verifone-v400m, graphql, offline-mode]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide documents how an API caller requests customized text and PNG-image output from the built-in receipt printer on a V400m reader, then polls the returned print context to determine the print action's final status. It is a device-printing route, not evidence that a receipt was physically printed or delivered, that a payment succeeded, or that an account is currently eligible for the API.

## Key takeaways

- The documented API is available for the V400m only. The `requestPrintFromInStoreReader` GraphQL mutation targets a V400m `readerId` and accepts caller-defined receipt `contents`; the guide describes text lines and images rather than a fixed transaction-receipt schema.
- A request must contain 1–500 content entries and the combined contents cannot exceed 122,880 bytes. Text entries can carry value, alignment, line-ending and optional decoration, weight, style and size fields; the exact field discussion is retained at the locator below.
- Image entries must be PNG, base64-encoded in the `value` field and no larger than 76,800 bytes. The guide calls 300 pixels the ideal image width and also documents alignment and line-ending behavior.
- The online example's mutation result is `PENDING`, and the guide requires starting context-ID polling after the initial request to determine whether printing succeeded. It recommends polling every 1–2 seconds and states a default 30-second timeout for an unsuccessful print. A request response, sample `PENDING` state or sample polled `COMPLETE` state is not proof of a physical print for another request.
- The guide also supplies a distinct offline-mode mutation and directs the caller to the offline-processing polling logic. This documents receipt-print-request support in offline mode; it does not establish that an associated payment was authorized, captured, settled or funded.
- The downloadable sample receipt is presented as a generic development baseline. The page says it includes recommended EMV receipt data; that recommendation is not itself proof that a customized receipt is compliant.

## Material warnings

> [!warning] Request and outcome boundary
> Initiating `requestPrintFromInStoreReader` does not establish that paper output completed. Poll the returned print context and handle the documented receipt-printing error range. Even a recorded API status is not evidence of physical delivery to a customer or of any payment outcome.

> [!warning] Scope and environment boundary
> The guide is restricted to the V400m built-in printer. Its examples show an online reader and separately document offline-mode requests, but sample states do not establish current service availability, merchant-account eligibility, network reachability, production configuration or success in a caller's environment.

## Detail locators

- V400m-only scope: introductory statement, line 16.
- Built-in printer, `requestPrintFromInStoreReader`, customizable receipt content and 122,880-byte aggregate limit: `## Introduction`, lines 19-21.
- Required `readerId` and `contents`, 1–500 content entries, text-or-image input identity and aggregate request size: `## Initiating a printing request`, lines 24-26.
- Text value, alignment, `endOfLineFlag` and optional styling fields: `### Text Inputs`, lines 29-31.
- PNG-only image input, 76,800-byte image limit, base64 `value`, alignment, `endOfLineFlag` and ideal width: `### Image Inputs`, lines 34-36.
- Online mutation shape, sample `PENDING` response and required context-ID polling handoff: `### Example print request`, lines 39-41.
- Recommended 1–2-second polling cadence, unsuccessful-print timeout and sample node-query shape: `### Example context ID polling request`, lines 44-48.
- Offline request and offline node-query examples: `## Printing Receipts in Offline Mode`, lines 49-61.
- Generic sample template, recommended EMV receipt data and downloadable Postman collection: `## Sample Receipt Template`, lines 62-68.
- Receipt-printing error codes 96733–96737, PNG/base64 reminder, image-width guidance, timeout, spacing technique and offline support: `## Important tips for integrating with the Receipt Printing API`, lines 69-85.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/hardware/verifone-v400m-2026-09-16|Verifone V400m]] - unread hardware navigation linked by the guide
- [[raw/braintree/in-person/guides/making-a-transaction-2026-09-16|Making a transaction]] - unread online node-query polling and EMV-data navigation linked by the guide
- [[raw/braintree/in-person/guides/offline-transactions-2026-09-16|Offline transactions]] - unread offline-processing and polling navigation linked by the guide
- [[raw/braintree/in-person/reference/emv-receipt-reference-2026-09-16|EMV receipt reference]] - unread sample EMV receipt navigation linked by the guide
- [[raw/braintree/in-person/guides/graphql-error-handling-2026-09-16|GraphQL error handling]] - unread receipt-printing error-code navigation linked by the guide

## Raw Sources

- [[raw/braintree/in-person/guides/receipt-printing-api-2026-09-16|Braintree In-Person Receipt Printing API]] - complete collected guide for V400m print requests, content formats and limits, context polling, offline-mode examples and receipt template guidance
