---
title: "Adyen 3D Secure"
type: concept
category: technology
tags: [adyen, 3d-secure, 3ds2, authentication, online-payments]
---

## Adyen 3D Secure

Adyen's merchant-facing online-payments guide describes 3D Secure 2 as an additional verification layer for card-not-present transactions. It recommends 3DS2 in connection with strong-customer-authentication regulations and liability-shift rules, but the guide does not prove compliance, successful authentication, payment authorization, or liability shift for a particular transaction. [[source-adyen-docs-online-payments-3d-secure]]

## Merchant integration routes

The guide presents two implementation shapes: **Native**, where the issuer performs authentication within the merchant website or mobile app, and **Redirect**, where the shopper moves to the issuer's site. Adyen warns that redirect can lower conversion because of technical errors or shopper abandonment.

Server-side routing is separate from that shopper-facing distinction. Sessions has built-in 3D Secure 2 support without additional configuration. Advanced integrations are routed by Web, iOS, or Android and by Drop-in, Components, or API-only integration type. Native integrations using Checkout API v46 or earlier are routed to a separate earlier-version guide.

For a qualifying native transaction, issuer requirements determine whether the flow is frictionless or presents a challenge. The page also navigates to authorization-only, data-only, and standalone-authentication variants; the data-only description is limited to Visa and Mastercard.

## SDK evidence boundary

This concept covers the high-level merchant website guide across web and mobile integration choices. It does not replace [[adyen-3ds2-ios-sdk]] or [[adyen-3ds2-android-sdk]], which retain package-qualified native transaction, challenge, lifecycle, security, privacy, and UI evidence. Do not attribute those SDK-specific behaviors or versions to the unversioned website guide, and do not use SDK availability as proof of merchant enablement or payment outcome.

## Related

- [[source-adyen-docs-online-payments-3d-secure-authorize-mpidata]] — Checkout `/payments` v46+ guide for using third-party 3DS2 authentication data in a separate Adyen authorization request, including scheme-specific mapping and co-badged-card consistency warnings (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-web-drop-in]] — Web Drop-in redirect 3DS guide for the advanced `/payments` and `/payments/details` flow, including version-specific return handling and live-region consistency

- [[source-adyen-docs-online-payments-3d-secure-standalone-authentication]] — Advanced-flow guide for separating 3DS2 authentication from later authorization, including cross-PSP and expiry limits (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-3d-secure]] — unversioned website guide for purpose, routing, flow shapes, and material qualifications
- [[adyen-3ds2-ios-sdk]] — separately versioned native iOS runtime
- [[adyen-3ds2-android-sdk]] — separately versioned native Android runtime
- [[adyen]]


## Regulation and liability boundaries

Adyen's regulation-compliance overview is region-, actor-, scheme-, period-, transaction-, issuer-, and flow-dependent. It says many surveyed regulations apply to issuers rather than directly to merchants, although issuer evaluation of non-compliance can reduce authorization rates. The page states a general fraud-liability shift after a successfully completed 3DS2 challenge and says some regions may also grant it after a successful frictionless flow, but its scheme tables contain material exceptions; for example, a rare US domestic Visa CAVV-validation failure can prevent liability shift even when ECI 05 is returned. Treat the regional rules and dated changes as snapshot guidance rather than universal current legal requirements or a guarantee for a transaction. [[source-adyen-docs-online-payments-3d-secure-for-regulation-compliance]]


## Sources

- [[source-adyen-docs-online-payments-3d-secure-data-only]] — unversioned Adyen webpage snapshot for the Visa and Mastercard 3DS2 data-only flow (collected 2026-09-15)
