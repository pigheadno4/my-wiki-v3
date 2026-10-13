---
title: "Make a POS diagnosis request | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/diagnostics/request-diagnosis"
raw_files:
  - "adyen/docs/point-of-sale/diagnostics/request-diagnosis/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, diagnosis, mobile-sdk, offline-payments]
---

## Overview

Adyen's Terminal API diagnosis guide covers health and connectivity checks for a payment terminal, and a separate diagnosis path for Android or iOS Mobile SDK Tap to Pay/card-reader solutions. It can surface offline transactions not yet forwarded to Adyen. The guide explicitly excludes the Mobile Payments app solution. A diagnostic `Response.Result: Success`, normal device status, or reachable host describes the diagnostic request and its reported conditions; it is not proof that a payment was authorized, captured, settled, or delivered.

## Key takeaways

- For a physical terminal, send `SaleToPOIRequest` with `MessageCategory: Diagnosis`, a target terminal `POIID`, unique `ServiceID`, and `DiagnosisRequest`. Start with `HostDiagnosisFlag: false` to check terminal condition. If `unconfirmedBatchCount > 0`, Adyen says there may be a network problem; send a further diagnosis with `HostDiagnosisFlag: true` to test reachability of the Adyen host and inspect `HostStatus.IsReachableFlag`. A zero count is a reported queue state, not proof of settlement for any transaction.
- Terminal `POIStatus` reports `GlobalStatus`, communication condition, and printer condition when applicable. `Response.AdditionalResponse` includes battery percentage only for battery-powered terminals; it can also report `unconfirmedBatchCount`, `firmwareVersion`, encoded network profile, assigned `merchantAccount`/`storeId`, and `terminalId`. The terminal ID is a model/serial `POIID`; firmware and optional P2PE component versions are software/version evidence, not terminal identity or payment outcome.
- A P2PE terminal's response additionally supplies manufacturer-provided protocol, SRED, vault and app-manager version data for annual PCI assessment. On UX300 and UX410 only, `tamperStatus: ARS_TRIGGERED` means anti-removal switches fired; the guide says to stop using the terminal immediately.
- For Mobile SDK solutions, `POIID` is the SDK installation ID, not a physical model/serial ID. With `HostDiagnosisFlag: true`, the SDK attempts an Adyen connection for a security scan, forwarding supported stored offline payments and, on iOS only, retrying prior failed captures; false does not connect. These are active diagnostic effects, not guaranteed successful forwarding or capture. `AdditionalResponse` can include `sdkExpiry`, pending count, decoded `storeAndForwardStatus` and `attestationStatus`, plus iOS-only `asyncCaptureStatus`. Mandatory SDK updates can block transactions; iOS capture retry inclusion has a three-minute wait after completion.
- A diagnosis request can fail with `Response.Result: Failure` and `Response.ErrorCondition: Busy` when the terminal or Mobile SDK is already processing another request. The example response's `TX_IN_PROGRESS` message is diagnostic failure information, not a payment-state result. The JSON and Java request examples, including `ProtocolVersion: 3.0`, are examples within the 2026-09-15 website snapshot, not authority for a particular SDK release.

## Detail locators

- `Requirements` — Terminal API terminal and Android/iOS Mobile SDK applicability; Mobile Payments app exclusion.
- `Diagnose a payment terminal` > `1. Verify the condition of a terminal` — request header and `DiagnosisRequest.HostDiagnosisFlag`, conditional `POIStatus`/`AdditionalResponse` fields, terminal and P2PE version labels, tamper warning and sample responses.
- `Diagnose a payment terminal` > `2. Verify that the Adyen host system is reachable` — `unconfirmedBatchCount` trigger, true host-diagnosis flag, and `HostStatus.IsReachableFlag`.
- `Diagnose a Mobile SDK solution` — installation-ID `POIID`, online side effects, offline-support condition, security and expiry fields, decoded status objects, iOS-only capture retry and timing.
- `Failed diagnosis request` — Busy failure while another request is being processed.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/diagnostics/request-diagnosis/2026-09-15|2026-09-15 Adyen diagnosis guide]]
