# Fixed retrieval checks: Classic native 3DS2 overview

## Q1 — Purpose and scope

**Query:** What integration does this Adyen native 3DS2 page cover, and does it prescribe a new Classic API build?

**Expected answer:** The page describes native 3DS2 on top of an existing Classic Payment API `/authorise` site or app integration. Adyen says new Classic integrations are no longer accepted and recommends moving to native 3DS2 on Checkout API, which also requires migrating the payment integration. The table distinguishes Classic web helper functions and mobile Classic SDKs from Checkout Components and older SDK/plugin/HPP redirect routes. Do not infer current SDK availability, account enablement, or payment success from this 2026 capture of a page last modified in 2020.

**Raw locators:** `# Native 3D Secure 2 authentication`, lines 15–33; `## Native 3DS2 implementation options`, lines 35–50. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/2026-09-15|pinned raw]].

## Q2 — Flow and authentication/payment boundary

**Query:** Which 3DS2 paths and result codes are described, and when is payment authorization distinct from authentication?

**Expected answer:** Issuer requirements determine frictionless or challenge authentication within the site/app; a 3DS1 fallback can redirect to the issuer. The server starts with a payment request and 3DS2 objects. IdentifyShopper requests fingerprinting, ChallengeShopper requires shopper interaction, RedirectShopper uses the 3DS1 path, and Refused/Error needs reason handling. `Authorised` means the payment was authorized and can follow an exempt/out-of-scope initial request or a frictionless path; it does not prove a shopper challenge. Full integration combines Adyen authentication with payment authorization; authentication-only performs 3DS2 first and submits payment authorization later; the third-party data route differs again. Do not claim that authentication-only completion itself authorizes a payment or guarantees liability shift.

**Raw locators:** `## Authentication flows`, lines 52–68; `## 3D Secure 2 payment flows`, lines 70–92; `## Payments routed to 3D Secure 1`, lines 94–96; `## Implementation options`, lines 98–104. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/2026-09-15|pinned raw]].
