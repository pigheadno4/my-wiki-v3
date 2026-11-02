---
title: "Adyen Terminal API POST /enableservice — EnableService Request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/enableservice"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/enableservice/2026-09-15.md"
tags: [adyen, terminal-api, pos, enable-service]
---

## Overview

This captured **Terminal API latest** API Explorer page describes `POST /enableservice`: an EnableService request conveying services to enable on a POI terminal before a Sale System service request, optionally inviting the customer to start. It lists cloud test device endpoints (synchronous and asynchronous) and a local terminal IP server; it does not supply a numeric Terminal API protocol version. The cloud path identifies `merchantAccount` and `deviceId`; the page does not define a message header, `POIID`, sale/session identifier, or authentication scheme. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- `TransactionAction` is required and is `StartTransaction` or `AbortTransaction`. The page describes starting a swipe-ahead transaction with enabled services, or aborting a swipe-ahead or CardAcquisition-started transaction that has not been followed by a Sale System service request to complete it. `ServicesEnabled` is mandatory for `StartTransaction`, absent otherwise, and can list `CardAcquisition`, `Loyalty`, or `Payment`. See raw lines 23–27.
- Optional `DisplayOutput` has required nested `Device`, `InfoQualify`, and `OutputContent` when present; `OutputContent.OutputFormat` is required. The page gives format-specific content rules and excludes `ResponseRequiredFlag` and `MinimumDisplayTime` for EnableService. See raw lines 28–46.
- The documented `200 Success` response conveys **Enable Service processing**, with required `Response.Result` values `Success`, `Failure`, or `Partial`. For a non-success result, `ErrorCondition` must be present; `AdditionalResponse`, if present, is logged by the POI. This does not establish payment authorization, capture, settlement, or bank receipt. See raw lines 48–60.

## Detail locators

- Captured request purpose and test/local server forms: raw lines 5–19.
- Full request-body field and enum table, including display and menu branches: raw lines 23–46.
- Response structure, result/error values, and logging description: raw lines 48–60.

## Related

- [[adyen-terminal-api]] — Terminal API concept and related POS guidance.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/enableservice/2026-09-15|Captured EnableService API Explorer page]]
