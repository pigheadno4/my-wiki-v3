---
title: "Adyen Terminal API v1 overview"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/overview"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/overview/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, point-of-sale]
---

## Overview

Captured API Explorer overview for **Adyen Terminal API v1**, a nexo Sale to POI based JSON message interface for payments, refunds, shopper information and other interactions through Adyen-supplied payment terminals; the page also says Terminal API is used for Adyen Mobile solution transactions. It describes POS-to-terminal communication and cloud routing, not a complete operation schema. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- A request has a `SaleToPOIRequest` with `MessageHeader` and an operation-specific body. The header identifies transaction type, terminal or Mobile SDK instance and unique transaction identifiers. The `SaletoPOIResponse` header echoes request values except `MessageType=Response`, with an operation-specific response body. The overview does not state field-level requiredness, identifier formats or cardinality; follow the linked operation references for those.
- Local communication sends from the POS to the terminal IP over a local network and receives a synchronous result. Cloud communication sends from POS to an Adyen endpoint for forwarding to a terminal; the POS can wait for a synchronous response or close the connection and receive an asynchronous event notification. A cloud `/sync` or `/async` routing choice therefore does not itself establish a transaction's authorization, capture or settlement result.
- Cloud device API uses POST paths identifying a merchant and `deviceId`: test examples use `{merchantAccount}`; the listed regional live examples use `{merchantId}` and require selection of the geographically closest data center in live Customer Area. Each cloud request requires an API key with **Cloud Device API role** in `X-API-Key`; generate a new key in the live Customer Area for go-live. The page points to separate local communication protection guidance without giving its security procedure.
- Legacy `terminal-api` cloud endpoints remain supported but receive no future development; the overview strongly recommends migrating to Cloud device API for logs, versioning, routing and future features. This is migration guidance, not a statement that old endpoints are already unavailable.

## Detail locators

- Purpose, nexo basis and JSON envelope: raw lines 5–23.
- Local versus cloud delivery, `/sync` and `/async` choice: raw lines 25–43.
- Test and regional live cloud URLs, with different merchant placeholders and live data-center selection: raw lines 45–77.
- Legacy endpoints and migration rationale: raw lines 79–109.
- Cloud API-key role/header and live key: raw lines 111–115.
- Operation directory: raw lines 117–152 lists POST Login, Logout, EnableService, Admin, Payment, CardAcquisition, StoredValue, Reversal, Reconciliation, GetTotals, BalanceInquiry, TransactionStatus, Abort, Diagnosis, Display, Input, Print and CardReaderAPDU. These are navigation entries; this overview supplies no operation request/response field schemas, limits, failure/reversal rules or timing guarantees.

## Related

- [[adyen-terminal-api]] — principal concept route for Terminal API message and integration boundaries.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/overview/2026-09-15|Adyen Terminal API v1 overview, captured 2026-09-15]]
