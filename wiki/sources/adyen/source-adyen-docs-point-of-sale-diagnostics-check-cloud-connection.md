---
title: "Adyen POS cloud WebSocket connection checks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/diagnostics/check-cloud-connection"
raw_files:
  - "adyen/docs/point-of-sale/diagnostics/check-cloud-connection/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, cloud-device-api, websocket, terminal-diagnostics]
---

## Overview

This Adyen Docs page explains how to inspect whether a payment terminal has a live WebSocket connection for Terminal API cloud communications: in Customer Area, through Cloud device API, through an older Terminal API endpoint, or on the physical terminal. See [[adyen]] and [[adyen-terminal-api]]. A terminal's Wi-Fi/network connection alone does not establish WebSocket connectivity; a connection check at a particular time is also not a payment request/result, local POS-to-terminal connectivity test, or proof of authorization, capture, or settlement.

## Key takeaways

- For cloud Terminal API, enable WebSockets under **Devices > Device settings > Integrations** in Customer Area. In **Devices > Device list > Terminals**, the WebSocket column shows status but can lag actual state. An individual terminal's **Cloud connection > Check connection** performs a check; its icon does not refresh automatically, so run it again for current state. A missing Cloud connection field indicates WebSockets are not enabled for that terminal.
- Adyen recommends Cloud device API for API checks. Its individual `GET /merchants/{merchantAccount}/devices/{deviceId}/status` uses an API key with the **Cloud device API role** and returns `deviceId` plus `status` (`ONLINE` or `OFFLINE`) for cloud connection. Here `deviceId` is a device-model/serial identifier for a payment device, or an app installation ID in an IPP Mobile solution; do not substitute a merchant/store ID for it. The shown host is a test-environment example and linked API Explorer uses `latest`, not a fixed API version guarantee.
- `GET /merchants/{merchantAccount}/connectedDevices` returns IDs with active cloud connections under that merchant account, optionally filtered by store; offline devices are excluded. A device's absence from this list should be read in the context of merchant/store selection and the moment checked, rather than as a permanent hardware failure or payment result.
- The older `POST /connectedTerminals` path is still described but explicitly discouraged in favor of Cloud device API. It has separate test and live Terminal API hosts, uses the Terminal API request API key, and accepts `merchantAccount` with optional `store` or terminal `uniqueTerminalId` (`POIID`). Its `uniqueTerminalIds` list includes connected terminals; an empty list can mean no live cloud connection **or** WebSockets not enabled. Keep this legacy endpoint distinct from the newer Cloud device API's `deviceId`, `status`, and `uniqueDeviceIds` fields.
- On a physical terminal, the linked Terminal API connection test asks for a cloud icon and green checks for **API enabled**, **WebSocket enabled**, and **WebSocket connection**. If a check shows no cloud connection, the page directs checking WebSockets, whether the terminal was off when checked, and restarting a powered-on terminal. These are diagnostics/recovery steps for connectivity, not evidence that a payment reached the terminal or was completed.

## Detail locators

- Cloud WebSocket requirement versus ordinary network attachment: `# Check the cloud connection`, raw lines 15–28.
- Customer Area list lag, missing setting, individual check and manual refresh: `## Check in the Customer Area`, raw lines 30–54.
- Recommended Cloud device API, individual status route and credential/ID requirements: `## Check using an API request` through `### Check the cloud connection status of an individual device`, raw lines 56–96. Connected-device list and optional store filter: lines 98–137.
- Older Terminal API `/connectedTerminals` route, environment hosts, key, request properties and ambiguous empty response: `### Old API request to check cloud connection`, raw lines 141–214.
- Terminal-side test and restore checks: `## Check on the terminal` and `## Restore the cloud connection`, raw lines 216–234.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — cloud Terminal API architecture, separately from local communications and versioned GitHub examples.

## Related raw API references

- The raw page links to Cloud device API Explorer (`latest`), Terminal API connection tests, and a separate diagnosis request. Those targets are navigation until independently read; see raw lines 58–71 and 216–240.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/diagnostics/check-cloud-connection/2026-09-15|Adyen Docs: Check the cloud connection (2026-09-15 snapshot)]]
