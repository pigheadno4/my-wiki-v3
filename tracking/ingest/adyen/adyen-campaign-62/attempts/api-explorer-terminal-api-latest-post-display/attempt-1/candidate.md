---
title: "Adyen Terminal API POST /display — Display Request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/display"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/display/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, display]
---

## Overview

Captured API Explorer contract for `POST /display`, the Terminal API Display Request. It conveys complete content to display and processing instructions, with at most one `DisplayOutput` for each `Device`/`InfoQualify` pair. The path says `latest`; the captured page does not give a numbered protocol or schema version. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The captured servers are two test cloud integration routes, `/sync` and `/async`, under `device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}`, plus a local terminal IP address. The page names no caller or session identifier; `{merchantAccount}` and `{deviceId}` identify cloud route parameters. See raw lines 10–19.
- The request table marks `DisplayOutput` required. Each item requires `Device`, `InfoQualify`, and `OutputContent`; `OutputContent` requires `OutputFormat`. `OutputText` is mandatory only for `Text` and disallowed otherwise; `OutputXHTML` and `OutputBarcode` have analogous format conditions. `ResponseRequiredFlag`, `MinimumDisplayTime` (seconds), `MenuEntry`, and `OutputSignature` are optional in the displayed table. See raw lines 23–44 for nested fields, enum values, and conditional wording.
- A `200 Success` response describes display processing results, except that the response can be absent when it is not required. When present, `OutputResult` is required, with one item per request `DisplayOutput` in the same order. Each result contains `Device`, `InfoQualify`, and `Response.Result` (`Success`, `Failure`, or `Partial`). For non-success results, `ErrorCondition` must be present; `AdditionalResponse` is logging information. See raw lines 46–61. An HTTP 200 heading alone does not establish a successful display result.

## Detail locators

- Cloud test and local server forms: raw lines 10–19.
- Request schema, device/qualifier and output-format enums, conditional content, and display minimum time: raw lines 23–44. The enum spells `BarCode`, while the conditional `OutputBarcode` description says `Barcode`; preserve the captured difference when implementing.
- Response schema and error-condition enum: raw lines 46–61.

## Related

- [[adyen-terminal-api]] — provider concept and integration context.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/display/2026-09-15|POST /display captured API Explorer page]]
