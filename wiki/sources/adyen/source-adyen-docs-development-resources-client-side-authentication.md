---
title: "Adyen client-side authentication"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/client-side-authentication"
raw_files:
  - "adyen/docs/development-resources/client-side-authentication/2026-09-15.md"
tags: [adyen, client-key, authentication, allowed-origins, api-credentials]
---

## Overview

This 2026-09-15 Adyen Docs snapshot explains the **client key** used by eligible client-side payment integrations. It is a public key tied to an API credential and a test or live environment, with allowed origins on that credential. It is distinct from the **API key** needed for Adyen API requests. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The guide says Web Drop-in and Components use the client key for secure input/encryption, card-type detection, and some server-side barcode or QR rendering. A client key identifies the API credential; allowed origins and CORS constrain expected client-side request origins. This description does not establish successful authentication, merchant eligibility, payment-method availability, or payment execution.
- Compatibility is version-specific: Web Drop-in/Components support client key from 3.10.1, with older versions using origin keys; iOS and Android Drop-in/Components support it from 3.7.0, with older versions using client encryption public keys. Starting at 4.0.0, the page says client key is the only client-side authentication route for those listed products. It also lists POS Mobile SDK Tap to Pay on iPhone and Android card-reader solutions, without giving SDK versions.
- A credential has one client key for its allowed origins in an environment. The key has a `test_` or `live_` prefix; switching to live requires a new key from the live Customer Area. Test allowed origins may use HTTPS, or HTTP only in secure contexts such as localhost; live allowed origins must use HTTPS. Wildcard origins are shown as permitted.
- Allowed origins can be added or removed without regenerating the client key. The guide says a newly generated client key leaves the old one valid for 24 hours, while newly saved origins take a few seconds to become available. These are client-key and origin-management statements, distinct from server API-key rotation or API credential IP allowlisting.
- The Customer Area path is Developers > API credentials > the integration credential, then Client settings > Authentication > Client key. The page directs the user to generate a key, add origins, and save changes; it does not specify the Customer Area user role for those actions.

## Detail locators

- Client-key purposes and API-key boundary: lines 17–25.
- One-key/environment model and compatibility table: lines 27–46.
- Public key, credential identity, CORS, key structure and live prefix: `How it works`, lines 48–57.
- Wildcards, test secure-context HTTP exception, live HTTPS, and origin linkage: `Allowed origins`, lines 59–69.
- Customer Area generation path, old-key 24-hour expiry, and separate live generation: `Get your client key`, lines 71–83.
- Origin changes without regeneration and propagation delay: `Manage allowed origins`, lines 85–92.

## Related

- [[adyen-api-access]] — credential scope, roles, API-key and client-key distinction.
- [[source-adyen-docs-development-resources-api-credentials]] — server credential administration and API-key rotation.

## Raw Sources

- [[raw/adyen/docs/development-resources/client-side-authentication/2026-09-15|Client-side authentication (2026-09-15)]]
