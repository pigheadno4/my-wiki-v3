---
title: "Adyen Classic API native 3D Secure 2 authentication"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/2026-09-15.md"
tags: [adyen, online-payments, classic-api, 3ds2, authentication]
---

## Overview

This 2026-09-15 snapshot is an Adyen guide to adding native 3D Secure 2 authentication to an **existing Classic Payment API `/authorise` integration** on a website or mobile app. Its metadata says last modified in 2020. Adyen says it no longer accepts new Classic API integrations and recommends migrating both the integration and native 3DS2 route to Checkout API. This page maps integration choices and result-code flows; it is not a current SDK-version or merchant-enablement guarantee.

## Key takeaways

- In native 3DS2, the issuer authenticates within the app or payment form. Issuer requirements decide between a passive frictionless path and a challenge requiring shopper interaction. A web challenge can follow the first payment request or device fingerprint; the app flow fingerprints before a challenge is deemed required. A 3DS1 fallback can redirect the shopper to the issuer, so a Classic implementation should support that route too. See `Authentication flows` and `Payments routed to 3D Secure 1`.
- The implementation-options table distinguishes Checkout API Components, older Quick Integration SDKs/plugins/HPP, and Classic API/CSE. For the Classic API/CSE path it routes web to helper functions and mobile to the Classic 3DS2 SDKs. The table includes historical version-specific guidance and redirect behavior for other integration types; consult the exact row rather than treating every route as native.
- The merchant server starts the 3DS flow with a payment request containing the required 3DS2 objects. `IdentifyShopper` calls for a device fingerprint; `ChallengeShopper` calls for shopper interaction; `RedirectShopper` routes to 3DS1; refusal/error requires handling the reason. An `Authorised` response means **payment authorization** succeeded, potentially because 3DS2 was exempt or out of scope when returned directly to the payment request, or following frictionless processing. It does not prove a shopper challenge occurred. See `3D Secure 2 payment flows`.
- The guide separates a **full integration** (Adyen 3DS2 authentication and payment authorization on web, iOS or Android), **authentication-only** (3DS2 with Adyen and payment authorization submitted later), and **authorization with third-party 3DS2 data**. Do not treat completion of authentication-only as payment authorization. See `Implementation options`.
- The page gives only a general challenge-flow liability-shift statement and points to separate rules; it does not establish a shift for a particular transaction. See the paragraph before `Native 3DS2 implementation options`.

## Detail locators

- `Native 3DS2 implementation options`: table of specific integration families, historical SDK/plugin minimums, native versus redirect support, and Classic web/mobile routes.
- `Authentication flows` and `3D Secure 2 payment flows`: frictionless/challenge device and shopper steps, result-code branches, and links to detailed result-code handling.
- `Implementation options` and `Next steps`: distinct browser, Android and iOS full guides; authentication-only and third-party data routes.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[adyen-3ds2-ios-sdk]]
- [[adyen-3ds2-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/2026-09-15|Adyen Classic native 3DS2 guide, 2026-09-15 snapshot]]
