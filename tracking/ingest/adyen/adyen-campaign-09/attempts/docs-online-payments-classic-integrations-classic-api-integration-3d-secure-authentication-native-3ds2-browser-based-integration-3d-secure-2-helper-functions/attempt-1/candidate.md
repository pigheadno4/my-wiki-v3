---
title: "Classic API browser 3D Secure 2 helper functions | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15.md"
tags: [adyen, classic-api, 3ds2, browser, authentication]
---

## Overview

This 2026-09-15 snapshot documents JavaScript helper functions for browser-based 3D Secure 2 in the Classic Payment API `/authorise` integration. Adyen says it no longer develops or accepts new Classic API integrations and directs migration to the Checkout API helper-function route. This is historical Classic behavior, not the modern Checkout API contract. See [[adyen]], [[adyen-online-payments]], and [[adyen-3d-secure]].

## Key takeaways

- The helpers collect browser information, encode/decode base64url data, create fingerprint and challenge iframes and forms, and configure challenge-window size. The page says they replace the Web 3D Secure 2 SDK implementation for this Classic route.
- The page's setup requires a test account, API key, API library, separate issuer callback URLs for the 3DS method and challenge result, and the helper functions. Browser information is passed to the merchant server; the server sends Classic `/authorise` with `threeDS2RequestData` and `browserInfo`. Its payment examples use Payment API v68 test URLs and various dated library versions.
- `IdentifyShopper` leads to device fingerprinting. The issuer posts to the method notification URL; the server sends `/authorise3ds2` with the token and `threeDSCompInd=Y` if the response arrived within 10 seconds, otherwise `N`.
- `ChallengeShopper` leads to an issuer challenge in an iframe. After the challenge response, the server sends `/authorise3ds2` with the token and `transStatus`; if no response reaches the challenge notification URL within 10 minutes, the guide says to send `transStatus: U` to finalize the payment attempt. Authentication, the intermediate result code, and final payment authorization are distinct states.
- The optional front-end notification sample uses `postMessage` and checks the message origin. Its test cards and examples are scenario illustrations, not proof of a current API version, merchant eligibility, or successful authorization.

## Detail locators

- Classic lifecycle warning, Checkout API migration, helper functions, and SDK replacement: lines 19–33.
- Account, key, library, callback URL, and helper setup: `Before you begin`, lines 35–69.
- Browser information and initial Classic payment request: `Collect the shopper's browser information` and `Submit a payment request`, lines 71–101; language-specific examples run through line 559.
- Initial result-code distinction: lines 560–599.
- Fingerprint sequence, 10-second callback condition, and `threeDSCompInd`: `Get the 3D Secure 2 device fingerprint`, lines 601–659; examples through line 925.
- Challenge data and window sizes: `Present a challenge`, lines 927–950; 10-minute callback and `transStatus: U`: lines 996–1020; final conditional `Authorised` response: line 1258.
- Optional notification-to-front-end `postMessage` example and origin check: lines 1285–1345.
- Test cards and scenario routing: `Testing 3D Secure 2`, lines 1347–1409.

## Related

- [[adyen-3d-secure]] — provider 3DS2 concept.
- [[adyen-online-payments]] — online-payment integration and lifecycle routes.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/3d-secure-2-helper-functions/2026-09-15|Classic 3DS2 helper functions (2026-09-15)]]
