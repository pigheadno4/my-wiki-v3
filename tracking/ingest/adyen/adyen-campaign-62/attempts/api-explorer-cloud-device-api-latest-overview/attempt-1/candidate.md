---
title: "Adyen Cloud device API v1 overview"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/cloud-device-api/latest/overview"
raw_files:
  - "adyen/api-explorer/cloud-device-api/latest/overview/2026-09-15.md"
tags: [adyen, cloud-device-api, terminal-api, point-of-sale, api-explorer]
---

## Overview

This 2026-09-15 API Explorer page describes **Cloud device API v1** as a cloud transport for sending Terminal API requests to payment devices when direct local-network communication is unsuitable, plus connection checks for payment terminals or Mobile-solution devices. A POS system sends a Terminal API request to Adyen, which forwards it to the payment device. This API's cloud transport and connection status are separate from Terminal API message semantics and payment outcomes. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- Every request needs an API key with the **Cloud Device API** role in `X-API-Key`. Test and live keys come from their respective Customer Areas. For live use, the page requires choosing the geographically closest data center and live endpoint; it lists Australia, East Asia, Europe and United States base URLs.
- The v1 path uses `{merchantAccount}` and `{deviceId}` to target a merchant and payment device. Test `POST .../sync` keeps the connection open waiting for a response; test `POST .../async` closes it for a new request and delivers the Terminal API response later through an event-notification webhook to a configured endpoint.
- The overview also lists `GET .../connectedDevices` and `GET .../devices/{deviceId}/status` as connection lookup routes. A connected status or transport response does not prove a Terminal API transaction succeeded, was authorized/captured, or reached reconciliation, settlement or bank receipt.
- The page supplies operation names and routing, but no request/response body schema, HTTP acceptance contract, timeout duration, retry rule, correlation field, error condition, payment reversal rule, or device-session lifecycle. Read each operation reference for its own contract.

## Detail locators

- Purpose, authentication, POS-to-Adyen-to-device flow: [[raw/adyen/api-explorer/cloud-device-api/latest/overview/2026-09-15#L5|raw lines 5–24]].
- Sync/async behavior, test URLs and event notification: [[raw/adyen/api-explorer/cloud-device-api/latest/overview/2026-09-15#L26|raw lines 26–35]].
- Live key, data center and regional servers: [[raw/adyen/api-explorer/cloud-device-api/latest/overview/2026-09-15#L37|raw lines 37–80]].
- Listed methods: [[raw/adyen/api-explorer/cloud-device-api/latest/overview/2026-09-15#L82|raw lines 82–90]].

## Related

- [[adyen-terminal-api]] — message architecture and cloud transport distinction.
- [[adyen]] — provider overview.

## Related raw API references

- The four operation paths listed in this overview are navigation only; their separate request/response references were not read for this source.

## Raw Sources

- [[raw/adyen/api-explorer/cloud-device-api/latest/overview/2026-09-15|Adyen Cloud device API v1 overview capture, 2026-09-15]]
