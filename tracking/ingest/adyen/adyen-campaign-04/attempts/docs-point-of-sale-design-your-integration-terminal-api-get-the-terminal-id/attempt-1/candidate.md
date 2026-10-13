---
title: "Get the Terminal API terminal ID | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/get-the-terminal-id"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/terminal-api/get-the-terminal-id/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, poiid, terminal-id]
---

## Overview

This Adyen guide explains how a point-of-sale integration obtains the unique payment-terminal identifier to place in Terminal API `MessageHeader.POIID`. The identifier selects the intended physical terminal for a request. Its model-plus-serial format identifies a device; the model label is not a terminal software version, SDK version, merchant account, or payment result. The page is a 2026-09-15 website snapshot.

## Key takeaways

- A Terminal API request names its target terminal with `POIID`, formatted as device model, a dash, and serial number, with any dashes removed from the serial-number portion. The page's `P400‑123456789` is an example format, not an assigned device ID.
- For a physical terminal, the serial number is on the back of the device or under **Settings > Device info**. Customer Area **Devices > Device list > Terminals** also shows a serial-number column. These routes provide the serial number; the model must still be combined with it to construct `POIID`.
- A cloud-communications integration can POST to `/connectedTerminals` specifying a merchant account and optionally one of its stores, then read `uniqueTerminalIds`. The array covers terminals with a live cloud connection belonging to that requested merchant-account or store scope; it is not a full terminal inventory or proof that an unlisted device does not exist.
- A local-communications integration can send a diagnosis request with placeholder `MessageHeader.POIID`. That request fails as described, but `DiagnosisResponse.MessageHeader.POIID` gives the actual ID of the terminal that received it. For an Android payment terminal with the merchant app installed on that terminal, the guide also gives a `Settings.Global.DEVICE_NAME` lookup.
- The guide states no Customer Area role requirements, terminal firmware/version mapping, proof of merchant enablement, or current connectivity guarantee beyond the live-connection filter of its cloud lookup. Follow the linked diagnostics or response guidance only as navigation unless separately read.

## Detail locators

- `# Get the terminal ID` — purpose and `MessageHeader.POIID` model/serial format.
- `Get the serial number from the terminal` — physical/screen serial lookup and dash normalization.
- `Get the serial number from your Customer Area` — device-list path to the serial column.
- `Make an API call` — cloud `/connectedTerminals` request, merchant account and optional belonging store, and live-connected `uniqueTerminalIds` results.
- `Use a diagnosis request` — local placeholder failure and actual ID in the response header.
- `Use an Android function` — on-terminal Android app condition and `Settings.Global.DEVICE_NAME`.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/terminal-api/get-the-terminal-id/2026-09-15|2026-09-15 Adyen terminal-ID guide]]
