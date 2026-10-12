---
title: "Adyen Docs: Mutual authentication"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/mtls"
raw_files:
  - "adyen/docs/development-resources/mtls/2026-09-15.md"
tags: [adyen, mtls, api-authentication, client-certificates, api-credentials]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide describes mutual TLS authentication for supported API calls. A client certificate adds client identity verification to the server certificate and API key. Adyen can sign a merchant-generated certificate signing request (CSR); the private key stays on the merchant's system. The signed certificate's subject DN is linked to a company-level API credential, and requests to supported APIs then present the certificate and full chain at an mTLS endpoint. See [[adyen-api-access]].

## Key takeaways

- The documented enrollment path needs Management API client-certificate read and read/write roles as applicable, an API key, a CSR tool, and a company-level `ws_*@Company.*` credential. Merchant-level and balance-platform credentials are excluded. The page limits a company account to 10 valid client certificates and states 397-day validity. Test-issued certificates work only with test mTLS endpoints.
- Adyen constructs the signed certificate's `subjectDN` from the company account and API credential, not from the CSR subject supplied in the example. The enrollment response contains a Base64 DER leaf, a CA chain, and `subjectDN`. Present the PEM bundle with the leaf first and all returned chain entries after it, together with the private key; a leaf-only presentation causes an `unknown_ca` TLS alert before any HTTP response.
- Linking `subjectDN` to the API credential is an operational cutover: the guide says subsequent requests using that credential to supported APIs must include the client certificate or fail. It directs merchants to test enrollment, linking, and a certificate-authenticated request in the test environment before linking a live credential.
- The supported mTLS APIs listed are Checkout, classic Payment, Recurring, Payout, and BinLookup. Management, Balance Platform, Transfers, Legal Entity Management, and Terminal Management are listed as unsupported and continue to use API-key authentication at standard endpoints. Checkout mTLS endpoints differ by test/live region; the Payment/Recurring/Payout/BinLookup group uses separate `palcert` endpoints. The live Checkout mTLS route is not the ordinary prefixed API-key endpoint.
- Adyen recommends its own CA enrollment but permits a certificate signed by another CA that Adyen trusts when its subject DN matches the credential's stored subject DN. The guide's `prime256v1` EC private-key/CSR example concerns mTLS client authentication. A separate JWE card-encryption guide contains an EC-certificate sample paired with `RSA-OAEP-256` code; this mTLS example does not reconcile or validate that different encryption recipe.

## Detail locators

- **Purpose and certificate authority options** — opening text, raw lines 15-23; client certificate supplements server certificate and API key, with Adyen CA recommended and external CA separately allowed.
- **Roles, account scope, count, and validity** — `## Requirements`, raw lines 25-39.
- **Enrollment and certificate bundle** — `## Generate a client certificate`, raw lines 53-134; EC CSR example, DN construction, Management API request, test/live separation, leaf/chain assembly, and `unknown_ca` effect.
- **Credential linking and cutover** — `## Link the certificate to your API credential`, raw lines 136-168; Customer Area and Management API routes, username-versus-ID distinction, and no-certificate failure after linking.
- **Test procedure and supported API boundary** — `## Test your setup` and `## Supported APIs`, raw lines 170-215.
- **mTLS endpoint mapping and request examples** — `## Endpoints for mutual authentication` through `## Make a request with your client certificate`, raw lines 217-312; regional Checkout and `palcert` hostnames, curl and Java examples.
- **External CA conditions** — raw lines 314-321.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-api-access]]
- Separate certificate purpose: [[adyen-card-encryption]]

## Raw Sources

- [[raw/adyen/docs/development-resources/mtls/2026-09-15|Adyen Docs — Mutual authentication (2026-09-15)]]
