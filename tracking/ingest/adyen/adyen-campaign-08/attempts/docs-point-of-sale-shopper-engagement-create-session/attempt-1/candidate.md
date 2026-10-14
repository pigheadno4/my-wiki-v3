---
title: "Create a flow | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/create-session"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/create-session/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, sessions]
---

## Overview

Adyen's **Create a flow** guide (last modified 2022-12-27; captured 2026-09-15) describes a Terminal API shopper-interaction session spanning input, display and payment requests. A POS sends one **Admin** request with `Session.Type=Begin`, then the selected operations, then a separate Admin request with the same `Session.Id` and `Type=End`. The session makes the terminal show a waiting screen between requests so the shopper sees that the POS is still working. Beginning or ending this UI flow is a nonfinancial Admin operation; its success does not authorize a payment inside the flow. See [[adyen]], [[adyen-pos-shopper-engagement]], and [[adyen-terminal-api]].

## Key takeaways

- The begin request puts Base64-encoded JSON in `AdminRequest.ServiceIdentification`. Its `Session.Id` is a unique session reference, distinct from the Terminal API message-header `ServiceID`, `SaleID` and terminal `POIID`. `Operation` selects `InputRequest`, `DisplayRequest`, and/or `Payment` types and currently uses the `WaitingScreen` variant with `UserInterfaceData.WaitingScreenTimeoutMs` per operation. The shown timeout governs **how long the waiting animation appears**, not a documented session expiry or payment timeout.
- After a configured input request completes or display/payment data is shown, the waiting screen appears for its configured milliseconds; another request interrupts that screen. End with a second Admin request carrying the **same `Session.Id`** and `Type=End`. An end request sent while the waiting screen is visible does **not** interrupt that screen; after the session ends, later input/display/payment requests do not trigger this session's waiting screen.
- The guide asks the POS to check `AdminResponse.Response.Result=Success` for both begin and end. It does not define Login/Logout messages, an exclusive resource claim/release, concurrent-session behavior, cancellation/notification flows, local-versus-cloud differences, supported terminal-model list, or a payment result. Check the operation-specific guides and current Terminal API contract before implementing those behaviors.
- The request table says `ServiceID` is 1–10 alphanumeric characters and unique within 48 hours per `POIID`, but the sample begin/end request places the longer `POSSystemID12345` string in `ServiceID` and `S00101` in `SaleID`; the sample response reverses those two values. Treat this as an internal example inconsistency. The table also labels the session field `ID` once while the JSON and end step use `Id`; verify exact current schema casing rather than copying annotations or sample identities blindly.

## Detail locators

- Purpose and three-step request order: [[raw/adyen/docs/point-of-sale/shopper-engagement/create-session/2026-09-15#How it works|How it works]] (raw lines 19–36).
- Begin JSON, `Operation` types/variant/timeout, Base64 encoding, Admin message header and response: [[raw/adyen/docs/point-of-sale/shopper-engagement/create-session/2026-09-15#Step 1: Start the session|Step 1: Start the session]] (raw lines 38–149). The encoded examples are illustrative.
- Waiting-screen behavior between requests: [[raw/adyen/docs/point-of-sale/shopper-engagement/create-session/2026-09-15#Step 2: Send requests|Step 2: Send requests]] (raw lines 151–155).
- Matched ID, End request/response, and visible waiting-screen exception: [[raw/adyen/docs/point-of-sale/shopper-engagement/create-session/2026-09-15#Step 3: End the session|Step 3: End the session]] (raw lines 157–214).

## Related

- [[adyen-pos-shopper-engagement]] — primary Input, Display, Print and flow hub.
- [[adyen-terminal-api]] — message-header and operation result context; financial payment outcome is separate.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/create-session/2026-09-15|Adyen Create a flow guide, captured 2026-09-15]]
