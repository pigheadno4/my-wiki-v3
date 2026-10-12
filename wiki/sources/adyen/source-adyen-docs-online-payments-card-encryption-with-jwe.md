---
title: "Adyen Card Encryption with JWE"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/card-encryption-with-jwe"
raw_files:
  - "adyen/docs/online-payments/card-encryption-with-jwe/2026-09-15.md"
tags: [adyen, cards, jwe, encryption, api-only]
---

## Overview

This Adyen guide documents a JSON Web Encryption (JWE) route for a custom Web card integration in which the merchant implements its own UI. It uses a third-party JWT library and an Adyen-provided, merchant-account-specific X.509 certificate-derived public key to encrypt card details on the shopper device before the encrypted payload is sent through the merchant server in a `/payments` request.

## Key takeaways

- The route is for a Web API-only integration whose frontend has access to unencrypted card details, including the page's examples of a multiple-payment-service-provider setup or a merchant risk engine.
- The stated prerequisites include the Checkout webservice API-credential role, the Customer Area **Manage API credentials** role, a backend able to make a payment, and the downloaded client-side-encryption public key as an X.509 certificate.
- The merchant derives a JSON Web Key (JWK) from the merchant-account-specific certificate, encrypts the card details on the client, sends the compact JWE to its server, and submits it as `paymentMethod.encryptedCard` in `/payments`.
- Adyen says it does not share decryption keys, so only Adyen can decrypt the encrypted card details for payment processing. The guide advises using algorithms that meet Adyen's security standards; its JOSE example sets `alg` to `RSA-OAEP-256` and `enc` to `A256GCM`.

> [!warning] PCI and evidence boundary
> The page directs implementers to check their PCI DSS requirements and explicitly describes a frontend that can access unencrypted card details. JWE encryption is therefore not evidence that an integration is PCI-compliant or outside PCI scope. This unversioned documentation snapshot also does not prove current account or role eligibility, certificate validity, library security, successful decryption, payment authorization, capture, settlement, or fulfillment safety.

## Detail locators

> [!warning] Snapshot certificate/algorithm conflict
> The sample certificate (raw lines 77–86) contains an EC P-256 public key, but the import/encryption examples use `RSA-OAEP-256` (lines 89–95 and 119–127). These are inconsistent; do not treat the pasted sample as a working recipe. Verify a compatible merchant certificate and algorithm before implementation; this snapshot does not resolve the conflict.

- Purpose and shopper-device encryption model: opening paragraphs under `# Card encryption with JWE`.
- Integration type, roles, PCI guidance, backend preparation, and certificate prerequisite: `## Requirements`.
- Intended custom-integration cases, server handoff, decryption-key boundary, and algorithm guidance: `## JSON Web Encryption (JWE)`.
- Certificate-to-JWK-to-client-encryption-to-server-to-`/payments` sequence: `## How it works`.
- Customer Area certificate download path: `## Get your X.509 certificate`.
- Third-party JOSE example for importing the X.509 certificate, including the EC/RSA sample conflict: `## Compute your JWK`.
- Card-detail object fields, protected-header example, the same certificate/algorithm conflict, and `paymentMethod.encryptedCard` request shape: `## Encrypt card details`.

## Related

- Company: [[adyen]]
- Concept: [[adyen-card-encryption]]
- Adjacent access controls: [[adyen-api-access]]
- Online-payment architecture: [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/card-encryption-with-jwe/2026-09-15|Adyen card encryption with JWE]] — complete collected guide for the custom Web JWE purpose, prerequisites, certificate and key flow, client-side encryption, server handoff, `/payments` request shape, and PCI guidance
