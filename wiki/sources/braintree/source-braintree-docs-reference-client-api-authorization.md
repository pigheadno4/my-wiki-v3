---
title: "Braintree Client API Authorization Reference"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-api/authorization"
raw_files:
  - "braintree/docs/reference/client-api/authorization-2026-09-16.md"
tags: [braintree, client-api, authorization-fingerprint, client-token]
---

## Overview

This captured Braintree Client API reference explains the `authorizationFingerprint` request parameter and where that fingerprint appears inside a client token. It is a narrow client-request authorization reference, not Braintree Auth OAuth, server-side gateway authorization, account enablement, or proof that a payment was authorized or completed.

## Key takeaways

- The page says every Client API request must carry an `authorizationFingerprint` that authorizes the requested action. Its payment-method-list request is an example, not evidence that a request succeeded or that any merchant, account, payment method, or buyer is eligible.
- The fingerprint is described as a signed collection of the merchant's public ID and values supplied during client-token generation. The page places the fingerprint inside the client token; it does not make that fingerprint a server credential or document authorization for server-side gateway operations.
- Client tokens are described here as JSON-encoded data. For client-token versions 2 and later, the JSON string is base64-encoded, and the minimal version-3 example includes `authorizationFingerprint`, `version`, and `configUrl`. That example is not an exhaustive or stable schema guarantee across token versions.
- The captured prose collapses markup around the field name (`anauthorizationFingerprintparameter` and `anauthorizationFingerprintfield`); the curl and JSON examples spell the key as `authorizationFingerprint`.
- This 2026-09-16 webpage snapshot does not establish current endpoint availability, token lifetime, merchant or account eligibility, environment configuration, successful client or payment execution, or exact-version SDK/GitHub behavior and history.

## Detail locators

- Client API request requirement and payment-method-list example framing: `# Authorization`, lines 14-22.
- Signed merchant-public-ID and generation-values description: `# Authorization`, lines 23-24.
- Client-token containment, JSON encoding, version-2-and-later base64 encoding, and version variability: `## Get an Authorization Fingerprint`, lines 25-29.
- Minimal version-3 decoded-token example and exact field spelling: `### JSON`, lines 29-37.
- Captured page create/update metadata: frontmatter, lines 5-10.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- SDK context: [[braintree-web-sdk]]
- Related source: [[source-braintree-authorization-overview]]
- Related source: [[source-braintree-authorization-client-token]]
- Related source: [[source-braintree-client-token-generate-node]]

## Related raw API references

- [[raw/braintree/docs/reference/request/client-token/generate/node-2026-09-16|Braintree Node.js client-token generation reference]]

## Raw Sources

- [[raw/braintree/docs/reference/client-api/authorization-2026-09-16|Braintree Client API authorization reference]] - complete captured page covering the authorization-fingerprint request field and client-token representation
