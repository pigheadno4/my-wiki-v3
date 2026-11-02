---
title: "Adyen Terminal API POST /login — Login Request and Response"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/login"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/login/2026-09-15.md"
tags: [adyen, terminal-api, point-of-sale, login, session]
---

## Overview

This 2026-09-15 API Explorer `latest` POST /login page describes a Sale-to-POI `LoginRequest` and `LoginResponse` for a session defined here as the period between Login and the following Logout. It lists test cloud sync and async Device API URLs and a local-terminal-IP placeholder. The page does not state a numbered Terminal API message version; `/v1` appears in the cloud transport URLs. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- The Sale System supplies required `DateTime`, `SaleSoftware` (with required manufacturer, application, software-version and certification identifiers), and `OperatorLanguage` in the request body. Optional `OperatorID` and `ShiftNumber` identify the cashier/operator and shift; the page lists conditions for sending `OperatorID`. Optional `SaleTerminalData` is sent if a Sale Terminal is involved, and its optional `TotalsGroupID` can group POI transactions for reconciliation or another Sale System purpose. The body table does not give a complete message-header contract or length/format constraints for these fields.
- Optional `TrainingModeFlag` tells the POI that the entire session is for system test or operator training rather than real transactions. Optional `TokenRequestedType` asks for a transaction or customer token; optional `CustomerOrderReq` selects open/closed order information; `POISerialNumber` has a stated condition. See the raw table for exact field conditions and values.
- The HTTP 200 section includes a required `Response` object with required `Result` values `Success`, `Failure`, or `Partial`. For results other than Success, the page says `ErrorCondition` must be present, even though its table marks it optional in general. A 200 transport status therefore does not itself mean Login succeeded.
- `POISystemData` is table-optional and described as returned when `Result` is Success. If present, it contains required POI `DateTime` and `POISoftware`; optional `POIStatus` describes component availability, with required `GlobalStatus` inside that object. Login success and terminal readiness are distinct signals. Optional `TokenRequestStatus` reports token-request status if the POI manages tokens.
- This page gives no operator credential or authentication exchange, access grant, payment authorization/capture, transaction totals, reconciliation result, settlement, bank receipt, callback contract, live cloud URL, or deprecation notice. The separate POS login/logout guide explicitly says Login does not authenticate an operator; its operational lifecycle and message-header details are separately sourced.

## Detail locators

- Session purpose and captured test cloud sync/async and local-hosting server entries: raw lines 5–19.
- Complete request-body schema, including Sale/POI identity, operator/group/shift attribution, training mode and token/order options: raw lines 21–40.
- HTTP 200 Login Response schema, `Result` and conditional `ErrorCondition`, POI software/status and token-status fields: raw lines 42–70.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API message and POS session context.
- [[source-adyen-docs-point-of-sale-reconciling-totals-log-in-and-log-out]] — separate POS guide for operational login/logout use, header example and explicit non-authentication boundary.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/login/2026-09-15|Adyen Terminal API latest POST /login, captured 2026-09-15]]
