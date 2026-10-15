---
title: "Adyen Classic API browser-based native 3D Secure 2 integration"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/2026-09-15.md"
tags: [adyen, classic-api, online-payments, 3d-secure, 3ds2, browser]
---

## Overview

Adyen's browser-based **full payment** guide describes native 3D Secure 2 authentication for an existing Classic Payment API `/authorise` integration on a merchant website. An eligible payment can take a frictionless or issuer challenge path before authorization. The merchant builds both browser and server portions; this page's authentication-only route is separate because it postpones payment authorization. Adyen says it no longer accepts new Classic API integrations and recommends migrating to Native 3DS2 on Checkout API, which also requires migration to Checkout API. [[adyen-3d-secure]] [[adyen]]

## Key takeaways

- Begin with server-side `/authorise`, including `threeDS2RequestData` with `deviceChannel: browser` and a challenge notification URL plus shopper `browserInfo`. Use the returned `resultCode` to select the next step. An `IdentifyShopper` response starts browser device fingerprinting; `ChallengeShopper` can arrive directly or after fingerprint submission. An `Authorised` result means the payment authorization completed in the stated flow, not merely that authentication occurred.
- For `IdentifyShopper`, the browser sends base64url `threeDSMethodData` to the issuer in a hidden iframe. The issuer posts the result to the merchant's method notification URL. After a response or the stated 10-second wait, the merchant server calls `/authorise3ds2` with the token and `threeDSCompInd` set to `Y` for a timely callback or `N` otherwise.
- For `ChallengeShopper`, the browser posts a base64url `CReq` to the issuer ACS in an iframe. The issuer sends `CRes` to the challenge notification URL. The merchant submits the decoded `transStatus` and token through server-side `/authorise3ds2`; if no callback arrives within 10 minutes, this guide instructs submission of `transStatus: U`, indicating authentication or account verification could not be performed. Do not treat the iframe challenge or callback alone as payment authorization.
- The guide says Adyen's Authentication Engine can route to 3D Secure 1 based on issuer performance; contact Adyen Support if automatic fallback is unwanted. Optional prefetch of fingerprint keys requires Support enablement and regularly updated per-BIN cache to avoid refusals.

## Detail locators

- `Before you begin` — test account, API key, API library, and two absolute issuer callback URLs.
- `Step 1: Submit a payment request` — initial request objects, additional-parameter qualification, result codes, and language examples.
- `Step 2: Get the 3D Secure 2 device fingerprint` — method-data encoding, hidden iframe, 10-second callback condition, and `/authorise3ds2` completion indicator.
- `Step 3: Present a challenge` — challenge data and iframe, 10-minute callback condition, `transStatus: U`, and payment result.
- `Optional: Prefetch device fingerprinting keys` — Support gate, BIN-key retrieval, transaction ID, cache freshness, and altered initial `/authorise` sequence.
- `Testing 3D Secure 2` — test-only cards, credentials, direct-challenge and frictionless scenarios.

## Related

- [[adyen-3d-secure]] — provider 3D Secure concept and integration routing.
- [[adyen]] — provider overview.

## Related raw API references

The linked `/authorise`, `/authorise3ds2`, `get3dsAvailability`, helper-function, and authentication-only documents are navigation from this page; their contents are not evidence read for this entry.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/browser-based-integration/2026-09-15|Adyen browser-based integration, fetched 2026-09-15]]
