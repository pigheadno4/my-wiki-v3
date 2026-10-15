---
title: "Adyen TLS version, cipher, and certificate guidance"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/security/sensitive-data/tls"
raw_files:
  - "adyen/docs/development-resources/security/sensitive-data/tls/2026-09-15.md"
tags: [adyen, integration-security, tls, certificates, api-connectivity]
---

## Overview

This [[adyen]] security guide describes TLS configuration for connections between an integration and Adyen's platform. It applies across Adyen integration types and states that unsupported versions or ciphers can prevent Adyen from receiving API requests. This transport requirement is distinct from [[adyen-api-access|API credentials and access permissions]] and from the optional client-certificate route for mTLS. The version, cipher, and certificate statements below are from the pinned 2026-09-15 webpage snapshot, not live negotiation or current security proof.

## Key takeaways

- The snapshot supports TLS 1.2 only for existing merchants using the listed strong ciphers. New integrations must use TLS 1.3 with `TLS_AES_256_GCM_SHA384` or `TLS_CHACHA20_POLY1305_SHA256`; existing TLS 1.2 users are encouraged to upgrade. TLS connections must use SNI. The full TLS 1.2 cipher list is at the raw table.
- Adyen says cipher strength and support can change and that it monitors versions and ciphers, notifying affected users through Customer Area notifications. A configured TLS version or cipher alone does not prove a particular request negotiated successfully.
- Adyen strongly recommends against certificate pinning because a replacement server certificate can break a client connection even when the new certificate chains to a trusted CA. The page says Adyen does not support pinning of any kind.
- If an organization must pin by policy, the guide gives a risk-reduction exception: pin all listed root certificates, not a leaf or whole chain, and track updates. Adyen says ordinary root-CA changes are announced by system message 30 days in advance, while emergency notice can be shorter. The integration owner remains responsible for handling certificate changes. The five root names and current validity must be checked against the raw locator and present trust information before implementation.

## Detail locators

- **Purpose, applicability and connection failure warning:** raw lines 15–34, under `# Transport Layer Security (TLS)` and `## Requirements`.
- **Existing TLS 1.2 versus new TLS 1.3, exact ciphers, SNI and upgrade guidance:** raw lines 36–54, under `## Supported TLS versions and ciphers`.
- **Pinning prohibition/recommendation and certificate-rotation failure mode:** raw lines 56–65, under `## Certificate pinning`.
- **Conditional root-only pinning list, notices and owner responsibility:** raw lines 67–86, under `### Certificate changes`.

## Related

- [[adyen]]
- [[adyen-api-access]]
- [[source-adyen-docs-development-resources-mtls]]
- [[source-adyen-docs-development-resources-security-api-security]]

## Raw Sources

- [[raw/adyen/docs/development-resources/security/sensitive-data/tls/2026-09-15|Adyen TLS configuration guide — collected 2026-09-15]]
