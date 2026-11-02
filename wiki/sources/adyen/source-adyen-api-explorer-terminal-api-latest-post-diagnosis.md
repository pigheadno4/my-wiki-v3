---
title: "Adyen Terminal API: POST /diagnosis diagnosis request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/diagnosis"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/diagnosis/2026-09-15.md"
tags: [adyen, terminal-api, diagnosis, point-of-interaction, api]
---

## Overview

This 2026-09-15 API Explorer capture describes Terminal API `POST /diagnosis` as a Sale-to-POI diagnosis request for a target point of interaction (POI). It lists test cloud device sync and async URLs under `/v1/merchants/{merchantAccount}/devices/{deviceId}/` and a local terminal IP server. The `latest` page path and cloud `v1` transport URLs do not identify a numbered Terminal API protocol version. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- The request-body table marks `POIID`, `HostDiagnosisFlag`, and `AcquirerID` all **No**. `POIID` identifies a POI system or terminal for the Sale-to-POI protocol and refers to `MessageHeader.POIID`; `HostDiagnosisFlag` asks for host diagnosis; the integer `AcquirerID` array is present when requesting only those hosts. The page does not state a default for the flag, a body-level mandatory selector, or caller authentication requirements.
- Under `200 Success`, the response body requires a `Response` object with required `Result` (`Success`, `Failure`, or `Partial`). Its description says `ErrorCondition` is absent or unused for Success and must be present otherwise. Optional `AdditionalResponse` provides processing information for logging, without real-time involvement. HTTP 200 alone therefore does not establish `Response.Result: Success`.
- Optional `POIStatus` reports terminal-component availability; if present, its `GlobalStatus` is required and may be `OK`, `Busy`, `Maintenance`, or `Unreachable`. Its security, PED, card-reader and communication flags, printer status, and fraud-suspicion flag are conditional or optional as described in the raw table. The optional `HostStatus` array describes hosts; each host object requires `AcquirerID`, while `IsReachableFlag` is optional.
- This diagnosis contract reports request processing and observed terminal/host condition. It does not describe a payment authorization, capture, reversal, reconciliation, settlement, bank receipt, resource creation, asynchronous result correlation, retry window, or endpoint rate limit. The separate [[source-adyen-docs-point-of-sale-diagnostics-request-diagnosis|diagnosis guide]] adds operational examples and Mobile SDK behavior; those are separate website evidence, not fields supplied by this API Explorer page.

## Detail locators

- Purpose and listed cloud sync/async test and local servers: raw lines 5–19.
- Request-body field types, requiredness and host-selector condition: lines 21–28.
- HTTP 200 response envelope, Result and ErrorCondition semantics: lines 30–42.
- POI and host status fields, condition text and enums: lines 43–53.

## Related

- [[adyen]] — provider route.
- [[adyen-terminal-api]] — Terminal API concept.
- [[source-adyen-docs-point-of-sale-diagnostics-request-diagnosis]] — separate POS diagnosis guide with operational examples and Mobile SDK qualifications.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/diagnosis/2026-09-15|POST /diagnosis API Explorer capture]]
