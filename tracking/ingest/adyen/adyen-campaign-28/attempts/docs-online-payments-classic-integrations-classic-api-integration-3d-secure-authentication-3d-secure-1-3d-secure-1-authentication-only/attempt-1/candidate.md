---
title: "Adyen Classic API 3D Secure 1 authentication-only integration"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/3d-secure-1-authentication-only"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/3d-secure-1-authentication-only/2026-09-15.md"
tags: [adyen, classic-api, 3d-secure-1, authentication-only, legacy]
---

## Overview

This 2026-09-15-captured [[adyen]] Classic Payment API guide describes a historical 3D Secure 1 authentication-only flow. Adyen says it no longer develops Classic `/authorise` or accepts new Classic integrations, and directs migration to Checkout API standalone authentication. The legacy flow obtains authentication data for a later authorization by another PSP/acquirer, or optionally continues to a distinct authorization with Adyen. This page is not evidence of current 3DS1 issuer or merchant eligibility. See [[adyen-3d-secure]].

## Key takeaways

- **Prerequisites and fallback scope:** The guide presumes an Adyen test account, API key, and familiarity with the full Classic 3DS1 guide. It presents 3DS1 authentication-only as a fallback when an issuer does not support the legacy 3DS2 authentication-only integration. The migration instruction requires moving to Checkout API as well as its newer standalone-authentication route. See pinned raw lines 19–39.
- **Authentication request and shopper handoff:** Submit Classic Payment API `/authorise` with `authenticationData.authenticationOnly: true` and required 3DS1 parameters; the TEST v46 example returns `RedirectShopper`, `issuerUrl`, `md`, and `paRequest`. Redirect the shopper to the issuer; after authentication the issuer posts `MD` and `PaRes` to the merchant `TermUrl`. `RedirectShopper` begins the authentication handoff and is not payment authorization. See pinned raw lines 41–109.
- **Authentication result:** Submit `MD` as `md`, `PaRes` as `paResponse`, and `authenticationData.authenticationOnly: true` to `/authorise3d`. A finished flow returns `AuthenticationFinished`; `additionalData.threeDAuthenticatedResponse: Y` signals successful authentication in this guide, with other values directed to the separate status reference. Its sample response includes `cavv`, `xid`, and `eci`. Authentication completion or `Y` alone does not authorize a payment. See pinned raw lines 113–367.
- **Separate optional authorization:** If processing with Adyen, send a later server-side `/authorise3d` request with `authenticationData.authenticationOnly: false`; the guide's successful example returns `Authorised`. Processing with another PSP/acquirer instead requires its separate authorization using the authentication data, which this guide does not execute. See pinned raw lines 25–27 and 371–401.
- **Example caution:** The initial curl JSON omits a colon after `authenticationData` (line 60). Several language-specific `/authorise3d` snippets omit the `authenticationOnly: true` field despite the prose and curl requirement (lines 115–121 and 145–340). Treat those examples as historical illustrations, not copy-ready proof of an authentication-only request.

## Detail locators

- Classic deprecation, migration and prerequisites: pinned raw lines 19–39.
- `/authorise` TEST v46 request, response and issuer redirect: pinned raw lines 41–109.
- Authentication-only `/authorise3d`, SDK examples and result fields: pinned raw lines 113–369.
- Optional Adyen authorization branch: pinned raw lines 371–401.

## Related

- [[adyen-3d-secure]] — merchant authentication context and reciprocal route.
- [[source-adyen-docs-online-payments-3d-secure-standalone-authentication]] — separately documented Checkout API standalone authentication.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/3d-secure-1-authentication-only/2026-09-15|Classic 3DS1 authentication-only guide, captured 2026-09-15]]
