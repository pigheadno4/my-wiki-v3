---
title: "Adyen Card Encryption"
type: concept
category: technology
tags: [adyen, cards, jwe, encryption, api-only]
---

## Definition

Adyen's JWE card-encryption route supports a custom Web API-only integration in which the merchant's own frontend can access unencrypted card details. The frontend uses a third-party JWT library and a public key derived from a merchant-account-specific X.509 certificate to encrypt the card details on the shopper device. The merchant passes the compact JWE to its server, which supplies it as `paymentMethod.encryptedCard` in a `/payments` request; Adyen says it does not share the decryption keys, so only Adyen can decrypt the payload for payment processing. [[source-adyen-docs-online-payments-card-encryption-with-jwe]]

## Access and compliance boundaries

The retained guide requires a Web API-only integration, the Checkout webservice API-credential role, the Customer Area **Manage API credentials** role, a backend able to make a payment, and the downloaded client-side-encryption certificate. These access prerequisites connect to [[adyen-api-access]], but the encryption lifecycle is a separate concept. Because the custom frontend can access unencrypted card details and the guide tells implementers to check PCI DSS requirements, encryption does not by itself establish PCI compliance or reduced scope. The snapshot also does not prove current eligibility, certificate validity, successful decryption, payment authorization, capture, settlement, or fulfillment safety.

## Sources

- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-client-side-encryption-hosting-the-cse-library]] — legacy Classic Web CSE self-hosting and form-encryption guide, phased out for new Web integrations; this is distinct from the JWE route above (2026-09-15 snapshot).


> [!warning] Snapshot example conflict
> The retained guide's sample certificate has an EC P-256 key while its JOSE import/encryption example uses `RSA-OAEP-256`. Do not copy this inconsistent sample as a working integration; verify compatible certificate/key and algorithm. See [[source-adyen-docs-online-payments-card-encryption-with-jwe]].

- [[source-adyen-docs-online-payments-card-encryption-with-jwe]] — unversioned Adyen guide captured 2026-09-15 for custom Web JWE purpose, prerequisites, certificate-derived public-key flow, client/server handoff, `/payments` request shape, and PCI boundary
