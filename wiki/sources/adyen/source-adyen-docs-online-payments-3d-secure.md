---
title: "Adyen 3D Secure 2 authentication"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure"
raw_files:
  - "adyen/docs/online-payments/3d-secure/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, authentication, online-payments]
---

## Overview

This unversioned [[adyen]] website-guide snapshot introduces 3D Secure 2 for merchant online-payment integrations and routes readers among native and redirect implementations, Sessions and Advanced server-side flows, authentication-flow explanations, and additional 3DS routes. It is the high-level source for [[adyen-3d-secure]], not version-qualified implementation evidence for the separately retained native SDKs.

## Key takeaways

- Adyen describes 3D Secure 2 as an extra verification layer for card-not-present transactions and recommends it for strong-customer-authentication regulations and liability-shift rules. The recommendation is not proof that a particular transaction complies, authenticates successfully, or receives liability shift.
- The guide presents **Native** authentication within a merchant website or mobile app and **Redirect** authentication on the issuer's site. It warns that redirect can reduce conversion because of technical errors or shopper abandonment.
- The documented routing depends on the merchant's server-side payments flow: Sessions has built-in 3D Secure 2 support without additional configuration, while Advanced routes readers by platform and Drop-in, Components, or API-only integration type. Native integrations using Checkout API v46 or earlier are sent to a separate earlier-version guide.
- A qualifying native 3D Secure transaction can be frictionless or require an issuer challenge. The page also links authorization-only, data-only, and standalone-authentication variants; its data-only description is limited to Visa and Mastercard.

> [!warning] Evidence boundary
> This collected page is high-level integration guidance. It does not establish current merchant, card, issuer, region, or account eligibility; prove production configuration, authentication, authorization, capture, settlement, or liability shift; or define the versioned native SDK runtime. Use [[adyen-3ds2-ios-sdk]] and [[adyen-3ds2-android-sdk]] only for their separately retained package-qualified native implementation evidence.

## Detail locators

- **Definition, regulatory rationale, and Authentication Engine:** raw lines 19-23.
- **Native versus redirect implementations, Sessions versus Advanced routing, and the Checkout API v46-or-earlier route:** raw lines 25-46.
- **Frictionless and challenge flow descriptions:** raw lines 48-62.
- **Authorization-only, data-only, and standalone-authentication navigation:** raw lines 64-78.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[adyen-3ds2-ios-sdk]] — version-qualified native iOS SDK evidence, distinct from this merchant website guide
- [[adyen-3ds2-android-sdk]] — version-qualified native Android SDK evidence, distinct from this merchant website guide

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/2026-09-15|Adyen 3D Secure 2 authentication — collected 2026-09-15]]
