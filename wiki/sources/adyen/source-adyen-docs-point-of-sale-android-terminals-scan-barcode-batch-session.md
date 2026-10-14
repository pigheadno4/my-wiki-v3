---
title: "Adyen Docs: Batch barcode scanning with Terminal API"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/scan-barcode/batch-session"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/scan-barcode/batch-session/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, terminal-api, barcode-scanning]
---

## Overview

This Adyen guide, last modified 2025-08-19 and captured 2026-09-15, describes using a Terminal API **Admin** request to start and end a batch barcode-scanning session on specified Android payment terminals. The operator holds the scan button during the active window; the POS application receives scan results through event notifications and must implement its own handling of the scanned content. This is a scanner-control and data-delivery flow, not a payment request or payment approval. See [[adyen-android-terminals]], [[adyen-terminal-api]], and [[adyen]].

## Key takeaways

- The guide names Android terminal models **S1E Barcode, S1E2L, S1F2L, and S1U2** with barcode scanners, in a Terminal API integration. Set up event notifications and POS-app logic to process the content first. This method does not require configuring the scanning button in Customer Area. The model list is a dated documentation scope, not current availability or account eligibility.
- To begin, Base64-encode a JSON `Session` with a unique `Id` and `Type: Begin`; the guide shows an `Operation` array with `Type: ScanBarcode` and `TimeoutMs` in the range **0–300000 ms**, defaulting to **300000 ms** if omitted. Put that string in `AdminRequest.ServiceIdentification`, with a standard Terminal API header using protocol 3.0, `MessageClass: Service`, `MessageCategory: Admin`, and `MessageType: Request`. The stated `ServiceID` rule is 1–10 alphanumeric characters, unique for 48 hours per terminal `POIID`.
- The `AdminResponse` reports `Response.Result` Success or Failure and an `AdditionalResponse` message; the latter's encoding may be Base64 or URL encoding. A successful session start enables the operator to scan; it is not itself barcode data.
- Each scan yields a `ScanBarcodeResult` event notification: success carries scanned `data` and `symbology`, while failure carries a `reason`. At the specified timeout the guide shows a failure event with `reason=Timeout`. To end early, send another Admin request with the same session reference and `Session.Type: End`; a successful cancel response acknowledges the stop.
- The guide's sample values are not a production contract: its begin-request `ServiceID` exceeds the stated 1–10 character rule, a failure-response JSON sample is malformed and has conflicting message text, and a cancel-response example uses `V400m` although the stated eligible scanner models are the four Android models above. Use the prose and parameter tables, then verify current Terminal API and device eligibility before implementation.

## Detail locators

- Supported device list, button condition and requirements: [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/batch-session/2026-09-15#Requirements|Requirements]] and the introduction immediately before it.
- Begin session object, timeout and Admin request header: [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/batch-session/2026-09-15#Start a batch barcode scanning session|Start a batch barcode scanning session]]. Sample request/response inconsistencies occur within this section.
- Per-scan data versus failures and timeout event: [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/batch-session/2026-09-15#Start a batch barcode scanning session|Start a batch barcode scanning session]], under the event-notification examples.
- Early stop with `Session.Type: End` and cancel response: [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/batch-session/2026-09-15#Cancel a batch barcode scanning session|Cancel a batch barcode scanning session]].

## Related

- [[adyen-android-terminals]] — Android terminal family and device-scope route.
- [[adyen-terminal-api]] — the Admin and event-message interface; payment messages use separate categories.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/batch-session/2026-09-15|Adyen batch barcode-scanning guide, 2026-09-15 snapshot]]
