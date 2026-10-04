---
title: "Braintree Forward API Cryptography"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/cryptography"
raw_files:
  - "braintree/docs/guides/extend/forward-api/cryptography-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, cryptography, encryption, mutual-tls]
---

## Overview

This collected unversioned Braintree guide describes the Forward API cryptographic toolkit for encrypting or signing parts of an outgoing forwarded request when a destination API requires security beyond the TLS protection that the page says already covers card data emitted by the Forward API. Production use of the Forward API is subject to eligibility. This is configuration and forwarding guidance, not evidence that a payment was executed or accepted.

## Key takeaways

- The page says all card data emitted by the Forward API is already protected by industry-standard TLS; the documented cryptographic functions are additional transformations for destination requirements, not a replacement for that transport protection.
- The guide documents AES-GCM transformations, RSA public-key encryption and certificate-based mutual TLS. The exact function names, key-array structure, nonce placement and request examples remain in the raw locators and linked references rather than being treated as a complete algorithm inventory.
- AES keys are sensitive and should be transmitted securely. The page directs merchants to encrypt them with the Forward API PGP public key before submitting them for use in configs.
- Mutual-TLS private keys are also sensitive and receive the same secure-transmission and PGP-encryption warning. The snapshot distinguishes sandbox, where a PEM-encoded client certificate and key may be supplied per request, from production, where a certificate and key are loaded with the config if necessary.
- The RSA example notes that encryption output is non-deterministic. The displayed AES, RSA and mutual-TLS payloads are examples, not proof of successful forwarding, destination acceptance or payment execution.
- Production Forward API use is eligibility-gated in this snapshot; the page directs readers to an Account Manager or Business Development rather than establishing eligibility for any merchant.

## Evidence boundary

> [!warning] Sensitive key material and forwarding scope
> Treat AES keys and mutual-TLS private keys as sensitive. This page instructs readers to use the Forward API PGP public key before submitting that material for configs, but the linked PGP page was not read as evidence for its operational procedure. The collected guide does not establish current merchant eligibility, destination behavior, successful request delivery, payment authorization, capture, settlement or any other payment outcome.

## Detail locators

- Production eligibility notice and inquiry routes: `# Cryptography > AVAILABILITY`, lines 14-17.
- Toolkit purpose, baseline TLS protection and destination-driven need for additional features: `## Overview`, lines 20-22.
- AES key-handling warning, required toolkit routes and three-step nonce/encryption outline: `## AES`, lines 25-39.
- AES partial config example: `## AES > ### Example partial config`, lines 41-64.
- RSA public-key encryption requirements, example request and non-deterministic result note: `## RSA`, lines 67-114.
- Mutual-TLS key-handling warning and sandbox-versus-production certificate/key handling: `## TLS mutual authentication`, lines 117-122.
- Mutual-TLS example request: `## TLS mutual authentication > ### Example`, lines 125-201.
- Additional signing and encryption navigation: `## Additional Features`, lines 204-206.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - unread navigation-only destination for the eligibility link; not used as behavioral evidence here
- [[raw/braintree/docs/guides/extend/forward-api/pgp-key-2026-09-16|Braintree Forward API PGP Public Key guide]] - unread navigation-only destination for encrypting sensitive key material; not used as procedural evidence here
- [[raw/braintree/docs/reference/forward-api/functions-2026-09-16|Braintree Forward API functions reference]] - unread navigation-only destination for cryptographic and signing function details; not used as behavioral evidence here
- [[raw/braintree/docs/reference/forward-api/config-2026-09-16|Braintree Forward API config reference]] - unread navigation-only destination for config key structure; not used as behavioral evidence here
- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Braintree Forward API forward reference]] - unread navigation-only destination for per-request sandbox certificate and key fields; not used as behavioral evidence here

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/cryptography-2026-09-16|Braintree Forward API Cryptography]] - complete collected guide covering toolkit purpose, production eligibility, AES and RSA transformations, mutual-TLS handling, sensitive-key warnings, environment qualifications and example boundaries
