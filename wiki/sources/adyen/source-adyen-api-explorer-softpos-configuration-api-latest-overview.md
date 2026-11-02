---
title: "Adyen SoftPOS configuration API v3 overview"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/softpos-configuration-api/latest/overview"
raw_files:
  - "adyen/api-explorer/softpos-configuration-api/latest/overview/2026-09-15.md"
tags: [adyen, softpos, mobile-pos, api-explorer, communication-session]
---

## Overview

This 2026-09-15 API Explorer page explicitly identifies the **SoftPOS configuration API v3** as part of the mutual-authentication flow between an Adyen Android or iOS Mobile SDK and the Adyen payments platform. The SDK context is in-person payments on commercial off-the-shelf devices, including Tap to Pay or mobile-device-plus-card-reader transactions. The listed operation is `POST /auth/certificate`, summarized as “Create a communication session.” This configuration/session API overview does not define a Terminal API payment request, a payment result, or an SDK release version. [[adyen]] [[adyen-mobile-pos]]

## Key takeaways

- The authentication paragraph calls requests to the “POS Mobile API” API-key signed and instructs setting the Customer Area API key in `X-API-Key`. It also requires a client key for setup, says it is not used later in the integration, and says allowed origins and system storage are unnecessary for that setup key. The page does not identify a separate POS Mobile API surface or the precise caller role for this endpoint; retain the captured label alongside the SoftPOS configuration API v3 title. See raw lines 11–15.
- Live access requires a newly generated API key and client key in the live Customer Area and a geographically closest live endpoint. Versioning is in the endpoint URL. The page shows a TEST `/softposconfig/v3` server and v3 live servers for Australia, Asia Pacific South East, Europe, North East Asia, and the United States; its preceding example URLs use `v{version}` placeholders except the US example. These environment and region paths are configuration API endpoints, not evidence that a particular mobile device, SDK, merchant, or payment method is enabled. See raw lines 17–69.
- The endpoint table gives only the method, `/auth/certificate` path, and communication-session creation summary. It supplies no request or response schema, setup-token or session-data fields, session identity/lifetime, renewal, error/reversal, rate/size limit, asynchronous delivery, or transaction state. A listed operation or request acceptance would not prove that mutual authentication completed or any payment was authorized, captured, settled, or received by a bank. See raw lines 71–76.

## Detail locators

- API identity and Mobile SDK context: raw lines 5–9.
- API/client keys and live credential requirement: raw lines 11–15.
- URL versioning, regional live and TEST endpoints: raw lines 17–69.
- Operation list: raw lines 71–76.

## Related

- [[adyen-mobile-pos]] — provider concept and reciprocal source route.

## Raw Sources

- [[raw/adyen/api-explorer/softpos-configuration-api/latest/overview/2026-09-15|Adyen SoftPOS configuration API v3 overview raw snapshot]]
