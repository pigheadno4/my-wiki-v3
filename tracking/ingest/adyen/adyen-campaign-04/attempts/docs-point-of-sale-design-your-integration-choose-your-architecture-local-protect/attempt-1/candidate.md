---
title: "Protect with your own code | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/local/protect"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/protect/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, local-communications, security]
---

## Overview

Adyen's "Protect with your own code" guide explains how a POS app protects **local** communications with an Adyen payment terminal. It covers terminal certificate validation and encrypted, authenticated Terminal API messages for a merchant-written implementation. The pinned documentation was fetched 2026-09-15 and carries a 2021-06-17 `last_modified` field; this snapshot does not establish current protocol or production security validation. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The guide says local integrations need protection against interception, eavesdropping, and tampering. Its stated prerequisites are an installed Adyen root certificate and a configured shared key. The POS app must verify the terminal certificate chain against that root on **every connection** and validate the Common Name using the documented test or live formats. The guide says a DNS Common Name mismatch during chain verification is normal; that observation does not replace the separate Common Name validation step.
- For message protection, the POS app derives secret key material from the shared passphrase, encrypts the complete Terminal API message before sending, and decrypts and validates received messages before processing. The guide's protocol walkthrough derives 80 bytes using PBKDF2-HMAC-SHA1, splits HMAC/cipher/IV material, uses a nonce with the derived IV for AES-256-CBC, and computes an HMAC-SHA256 over the original plaintext. The outbound wrapper retains the message type and `MessageHeader`, carries the encrypted `NexoBlob`, and includes a `SecurityTrailer` with `Hmac`, `Nonce`, `KeyIdentifier`, `KeyVersion`, and `AdyenCryptoVersion` 1.
- On receipt, the walkthrough selects the shared key by identifier and version, checks the crypto version, decrypts, checks the HMAC, and compares the outer plaintext `MessageHeader` with the decrypted header. Derived key material remains secret and requires secure storage if cached. A crypto error can indicate that the key values in POS code do not match Customer Area; an SSL connection error can indicate an incorrectly installed root certificate.
- The language examples are illustrative code, **not proof of a production-secure implementation**. In particular, the full PHP receiver explicitly says almost all validation is missing and its key lookup returns a fixed test passphrase for demonstration. Review the normative steps and actual implementation rather than treating copied samples as complete security validation.

## Detail locators

- Prerequisites and certificate/Common Name checks: pinned raw, `## Requirements` and `## Validate the terminal certificate` (lines 26–63).
- Encryption sequence, key derivation parameters, nonce/IV, HMAC, wrapper and trailer: pinned raw, `## Encrypt communications` through `#### Compose the new message` (lines 65–243).
- Decryption, key identifier/version lookup, HMAC and header checks: pinned raw, `### Decrypt Terminal API messages` through `#### Validate the message` (lines 245–358).
- Java, PHP, C# and NodeJS examples and their code-specific limits: pinned raw, `## Full encryption code samples` (lines 360–1272); PHP receiver warning at line 764.
- Shared-key and root-certificate troubleshooting: pinned raw, `## Troubleshooting` (lines 1273–1317).

## Related

- [[adyen-terminal-api]] — Terminal API message architecture and transport boundaries.
- [[adyen]] — provider hub.

## Related raw API references

The raw page points to the local-integration setup and library-protection guides for navigation; those linked pages are outside this pinned source's evidence boundary.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/protect/2026-09-15|Protect with your own code — 2026-09-15 snapshot]]
