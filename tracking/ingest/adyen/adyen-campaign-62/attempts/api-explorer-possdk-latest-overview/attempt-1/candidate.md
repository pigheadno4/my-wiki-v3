---
title: "Adyen POS Mobile API v68 overview — deprecated"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/possdk/latest/overview"
raw_files:
  - "adyen/api-explorer/possdk/latest/overview/2026-09-15.md"
tags: [adyen, mobile-pos, pos-mobile-sdk, api, deprecated]
---

## Overview

This 2026-09-15 API Explorer overview identifies **POS Mobile API v68**, used in a mutual-authentication flow between the Android or iOS POS Mobile SDK and Adyen's payments platform. The page explicitly says this API is **deprecated** and directs readers to the SoftPOS configuration API. The SDK context is merchant-device in-person payments such as Tap to Pay or a mobile device with a card reader; this overview is not a Terminal API payment-result contract. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- Each POS Mobile API request must be signed with an API key supplied as `X-API-Key`. The page also requires a client key as part of setup but says it is not later used in the integration, so allowed origins need not be specified and the key need not be stored in the integrator's system. It does not define the underlying signing mechanism or a full credential-exchange sequence.
- The API versions in the endpoint URL. The captured test server base is `https://checkout-test.adyen.com/checkout/possdk/v68`; the live example has a company-account-specific prefix before `checkout-live.adyenpayments.com/checkout/possdk/v68`. Live access requires **new live Customer Area API and client keys**, separate from test keys.
- The sole listed operation is `POST /sessions`, summarized as “Create a communication session.” This overview supplies no request/response schema, session identifier, expiry, callback, error/status contract, payment authorization, capture, settlement, or bank-receipt evidence. The linked replacement API is a navigation target here, not evidence of its own operation or migration equivalence.
- The page does not identify a device model, account eligibility, SDK version, or live payment outcome. Its deprecation statement applies to POS Mobile API v68 in this snapshot; it does not by itself state that all POS Mobile SDK versions or in-person payment routes are deprecated.

## Detail locators

- API identity, deprecation/replacement and Android/iOS SDK purpose: raw lines 5–10.
- Authentication, client-key setup and live credentials: raw lines 12–16 and 26–32.
- URL versioning, test/live examples, server base and sole operation listing: raw lines 18–42.

## Related

- [[adyen]] — provider context.
- [[adyen-mobile-pos]] — Android/iOS merchant-device in-person routes and separate SDK baselines.
- [[adyen-terminal-api]] — separate terminal message and payment-result context.

## Related raw API references

- The raw overview links to the SoftPOS configuration API, POS Mobile SDK guide, API-key generation and client-key guidance. Those destinations are navigation, not evidence of the replacement API's schema or eligibility.

## Raw Sources

- [[raw/adyen/api-explorer/possdk/latest/overview/2026-09-15|Adyen POS Mobile API v68 overview, captured 2026-09-15]]
