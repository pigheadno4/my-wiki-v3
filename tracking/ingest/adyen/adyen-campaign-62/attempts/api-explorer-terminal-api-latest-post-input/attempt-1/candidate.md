---
title: "Adyen Terminal API v1 POST /input"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/input"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/input/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, shopper-input]
---

## Overview

Captured Terminal API **POST /input** schema for `InputRequest`: a POS-side request to present content on an input device and collect or process cashier/customer input through a terminal or local-hosted device route. The schema describes an input command and optional display operation. See [[adyen]], [[adyen-terminal-api]] and [[adyen-pos-shopper-engagement]].

## Key takeaways

- The request body table marks `InputData` required. Within it, `Device`, `InfoQualify` and `InputCommand` are required; `InputCommand` permits GetAnyKey, GetConfirmation, SiteManager, TextString, DigitString, DecimalString, GetFunctionKey, GetMenuEntry and Password. Optional controls include `MaxInputTime` in seconds, length bounds, masking/default/layout/correction/cancel flags and `ImmediateResponseFlag`, which requests a response before command completion. The page provides no numeric defaults or permitted ranges for these controls.
- `DisplayOutput` is optional; when provided, its `Device`, `InfoQualify` and `OutputContent` are marked required, and `OutputContent.OutputFormat` is required. `OutputText` is mandatory only for Text format, `OutputXHTML` only for XHTML, and `OutputBarcode` only for the barcode format; the other format variants disallow those fields as specified in the table. `MenuEntry` is an optional input-command menu, and the page says `ResponseRequiredFlag` and `MinimumDisplayTime` must be absent for Input Devices, Diagnosis and EnableService.
- The 200 response table marks `InputResult` required, with `Device`, `InfoQualify` and `Response` required inside it; `Response.Result` is Success, Failure or Partial. `ErrorCondition` is absent or unused on Success and must be present otherwise. `InputResult.Input` is optional and carries command-dependent fields such as confirmation, function key, text, digits, password or menu selection. `OutputResult` is optional if an output result was required. Thus the HTTP 200 section and any immediate response do not alone prove a completed user entry.
- The page lists test cloud `/sync` and `/async` device endpoints using `merchantAccount` and `deviceId`, plus a local terminal IP. It does not supply authentication headers, full nexo message envelope/correlation fields, asynchronous event structure or financial authorization/capture/settlement behavior. A user input result is separate from any payment or consent decision.

## Detail locators

- InputRequest purpose and three server routes: raw lines 5–18.
- `DisplayOutput`, output format and conditional content fields: raw lines 20–43.
- Required `InputData`, commands, optional timeout/length/flag and menu controls: raw lines 44–65.
- HTTP 200 result, optional `OutputResult`, required `InputResult`, Success/Failure/Partial and `ErrorCondition`: raw lines 67–89.
- Optional command-specific `InputResult.Input` and selected menu indexes (1 to n, -1 parent, 0 root): raw lines 90–97.

## Related

- [[adyen-pos-shopper-engagement]] — terminal shopper and cashier interaction route.
- [[adyen-terminal-api]] — Terminal API messaging and transport boundaries.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/input/2026-09-15|Terminal API v1 POST /input, captured 2026-09-15]]
