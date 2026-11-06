---
title: "Adyen Cloud Device API v1: send an asynchronous Terminal API request to a device"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/async"
raw_files:
  - "adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/async/2026-11-07.md"
tags: [adyen, cloud-device-api, terminal-api, point-of-sale, asynchronous]
---

## Overview

This captured Cloud Device API v1 reference describes `POST /merchants/{merchantAccount}/devices/{deviceId}/async`: it sends a JSON Terminal API request to a payment device and delivers the actual Terminal API response later as an event notification webhook. The caller's API credential needs the Cloud Device API role. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The required path values identify the merchant account and destination device. `deviceId` must match the Terminal API request's `MessageHeader.POIID`: use a model–serial terminal ID for a payment terminal or the SDK installation ID for a Mobile solution.
- HTTP `200 OK` means the device is online and Adyen's backend has sent the request. It is not the Terminal API result or proof of a successful payment; that result is delivered to the event notification endpoint.
- The captured server list includes test and separate live regional v1 endpoints for Australia, East Asia, Europe and the United States.

## Detail locators

- Request purpose, JSON body shape, role and asynchronous result route: raw lines 5–15. The body schema is delegated to Terminal API request types; this page does not enumerate body properties.
- Test/live server URLs: raw lines 17–32. Required path parameters and device identity: raw lines 34–40. `200 Success` response section: raw lines 42–45; it lists no response fields.

## Related

- [[adyen-terminal-api]] — Terminal API message structure and cloud transport context.

## Raw Sources

- [[raw/adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/async/2026-11-07|Cloud Device API asynchronous device request, captured 2026-11-07]]
