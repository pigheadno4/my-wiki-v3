---
title: "Adyen Terminal API structure and transport"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/terminal-api/2026-09-15.md"
tags: [adyen, terminal-api, point-of-sale, in-person-payments, local-communications, cloud-communications]
---

## Overview

This Adyen Docs page introduces the nexo Retailer Protocol-based Terminal API for a POS system interacting with an Adyen-supplied payment terminal. It covers payment, refund, shopper-information and other terminal interactions, the JSON request/response envelope, local and cloud transport, and selected response identifiers. See [[adyen]] and [[adyen-terminal-api]]. This dated website snapshot explains the interface; it does not establish current merchant or terminal eligibility, a completed transaction, or the version history of GitHub SDKs and Postman examples.

## Key takeaways

- Before using Terminal API in the test environment, enable it under **Devices > Device settings > Integrations** in the test Customer Area and save; when switching to live, the page directs the same steps in the live Customer Area. This is environment-specific configuration, not proof of readiness or payment acceptance.
- Terminal API exchanges JSON with a `MessageHeader` and transaction-specific body. Each request is a `SaleToPOIRequest` containing a header and a matching request body, such as `PaymentRequest` or `InputRequest`. The request header identifies protocol version, message class/category/type, `ServiceID`, `SaleID`, and terminal `POIID`; `ServiceID` must be unique for that terminal within the preceding 48 hours. Consult the pinned header table for exact fields and constraints.
- Transport and authentication depend on the chosen architecture. Local communication sends the POS request directly to the terminal IP over a local network and receives the payment result synchronously. Cloud communication sends it to an Adyen platform endpoint for forwarding to the terminal; the result can be synchronous or asynchronous. This page does not specify the authentication procedure for either route.
- A synchronous response is a `SaleToPOIResponse` with a header echoing the request except for `MessageType: Response`, plus a transaction-specific response body. For asynchronous cloud results, the immediate Terminal API reply is only `ok`; the header and response body arrive in an event notification. Do not interpret the immediate `ok` as a payment result.
- Money-flow requests such as payments and refunds return a `POITransactionID.TransactionID`. The page describes a tender reference and PSP reference separated by a dot; it advises storing identifiers for later refund, acquired-card payment, and lookup. For a locally communicated Offline EMV or store-and-forward approved payment during a network issue, only the tender reference is initially generated; the platform generates a PSP reference after the terminal reconnects and processes the payment.

## Detail locators

- Interface purpose and nexo basis: `# Terminal API`, raw lines 19–24.
- Test and live enablement: `## Enable Terminal API`, raw lines 26–35.
- JSON envelope and request shape: `## API structure` through `## Requests`, raw lines 37–51. Request header fields and example: `### Request MessageHeader`, raw lines 53–86; transaction-specific body guidance: lines 88–90.
- Local and cloud transport: `## Sending Terminal API requests`, raw lines 92–102. The linked architecture pages are navigation, not evidence read for this entry.
- Response envelope and asynchronous cloud notification: `## Responses`, raw lines 104–116; response header example and body guidance: lines 118–143.
- Transaction identifier, offline exception, and receipt data: `#### Transaction identifier` through `#### Receipt data`, raw lines 145–177.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API concept and its separate exact-commit Postman/SDK evidence.
- [Terminal API reference](https://docs.adyen.com/api-explorer/terminal-api/latest/overview) — linked schema navigation; not read as evidence here.

## Related raw API references

- The raw page links to local/cloud architecture, event notifications, transaction-specific flows, receipt guidance, and a Terminal API reference. Follow and read those targets before asserting their detailed behavior; see raw lines 19–20, 90–112, 175–195.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/terminal-api/2026-09-15|Adyen Docs: Terminal API (2026-09-15 snapshot)]]
