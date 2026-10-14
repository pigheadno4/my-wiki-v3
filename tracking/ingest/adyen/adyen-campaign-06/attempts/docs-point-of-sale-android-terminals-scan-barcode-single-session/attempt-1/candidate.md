---
title: "Adyen Docs: Activate one barcode scan with Terminal API"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/scan-barcode/single-session"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/scan-barcode/single-session/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, terminal-api, barcode-scanning]
---

## Overview

This Adyen guide, last modified 2025-04-24 and captured 2026-09-15, describes a Terminal API Admin session that activates an Android payment terminal's scanner for one barcode, returns the scan content to the merchant POS app, and can be canceled before timeout. It names S1E Barcode, S1E2L, S1F2L, and S1U2 terminals with barcode scanners. This is a POS-controlled scanner interaction, not a payment authorization or an Android app-deployment route. [[adyen]] · [[adyen-android-terminals]] · [[adyen-terminal-api]]

## Key takeaways

- The prerequisite is a Terminal API integration on one of the named scanner-equipped Android terminals. The POS app must implement both a scan-trigger button and logic to process the returned barcode. This Terminal API method does not require setting up the terminal's scanning button in Customer Area. A separate batch-scan guide covers multiple barcodes.
- To activate one scan, Base64-encode a JSON `ServiceIdentification` object with a unique `Session.Id`, `Session.Type: Once`, and an `Operation` of `Type: ScanBarcode` with `TimeoutMs` from 0 to 30000. Send it in a Terminal API `AdminRequest` with a Service/Admin/Request message header using protocol version 3.0 and the terminal `POIID`. The header table specifies a per-terminal `ServiceID` of 1–10 alphanumeric characters, unique for the previous 48 hours.
- A successful single scan deactivates the scan button. The guide's success path returns barcode content through `AdminResponse.AdditionalResponse`; after decoding, `Barcode.Data` is the content and `Barcode.Symbology` its format, with `UNKNOWN` for an unrecognized symbology. Failure can report `Cancel`, `Aborted`, `UnavailableService`, or `NotFound`, with a failure reason in `AdditionalResponse`. The guide warns that `AdditionalResponse` may use Base64 or URL encoding and directs merchants to Support to consistently receive one format.
- To stop an active scan before timeout, send a separate Admin request whose encoded `ServiceIdentification` contains the session ID and `Session.Type: End`. A successful cancel response reports `Response.Result: Success` with a cancellation message; it is a scanner-session outcome, not a payment result.
- **Example conflict:** The activation parameter table and standalone JSON show `Session.Type: Once`, but the Base64 embedded in the illustrated full activation request decodes to `Begin`. The same request example uses `ServiceID: POSSystemID12345` despite the table's 1–10-character rule; response examples swap sale/service identifiers, and the cancel response uses a V400m `POIID` outside the page's named scanner models. Treat these examples as illustrative and check the documented fields and current Terminal API contract before implementing.

## Detail locators

- **Scope and prerequisites:** raw introduction (lines 19–29), “Requirements” (31–40), and “How it works” (42–47) for named models, POS implementation, Customer Area button exception, and single-scan lifecycle.
- **Activate request:** raw “Activate the barcode scanner for a single scan” (49–126) for `Once`, `ScanBarcode`, timeout range, Base64 `ServiceIdentification`, and the Service/Admin header. The standalone JSON is at 62–76; the full request sample is at 105–125. The full request's encoded payload decodes to `Begin`, in conflict with `Once` in the table and standalone JSON.
- **Response and decoding:** same section (128–209) for success/failure fields, encoding caveat, decoded `Barcode.Data`/`Symbology`, and POS-side processing. The example response headers are inconsistent with the request header; use field definitions rather than their sample values.
- **Cancel:** raw “Cancel scanning session” (213–309) for `End` and the cancel response. The illustrated cancel success response at 289–309 uses a V400m `POIID` despite the four scanner models in this guide.

## Related

- [[adyen-android-terminals]] — on-terminal Android capabilities
- [[adyen-terminal-api]] — POS message architecture and Admin request context

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/scan-barcode/single-session/2026-09-15|Adyen single barcode scan guide, fetched 2026-09-15]]
