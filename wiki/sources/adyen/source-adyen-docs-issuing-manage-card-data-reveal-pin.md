---
title: "Reveal PIN using standard encryption methods | Adyen Issuing"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-card-data/reveal-pin"
raw_files:
  - "adyen/docs/issuing/manage-card-data/reveal-pin/2026-09-15.md"
tags: [adyen, issuing, pin, card-data]
---

## Overview

This 2026-09-15 snapshot of an [[adyen]] [[adyen-issuing]] guide describes how a platform can retrieve an encrypted PIN block for an Adyen-issued card and reveal the decrypted PIN to its cardholder in its own app or website. It is a sensitive-data implementation guide, not evidence that any particular cardholder, credential, or deployment can reveal a PIN.

## Key takeaways

- The stated prerequisites are Configuration API credentials with the **Bank Issuing PIN Reveal Webservice role**. The guide has the platform obtain a base64-encoded RSA public key using `GET /publicKey?purpose=pinReveal`, generate a 256-bit AES key, and encrypt that key with the Adyen public key using RSA PKCS 1 to form `encryptedKey`. See raw **Requirements**, **Get a public key from Adyen**, **Generate an AES key**, and **Generate an encrypted session key** (lines 37–50, 226–237).
- The platform sends `paymentInstrumentId` and `encryptedKey` to `POST /pins/reveal`. The described response supplies an ISO Format 4 `encryptedPinBlock` and a `token`; the guide then says to pass both to the client for decryption and cardholder display. See raw **Request the PIN block from Adyen** and **Decrypt the PIN block and reveal the PIN** (lines 239–249, 449–490).
- **Cryptographic ambiguity requiring clarification:** the last decryption step says to use RSA in ECB mode with the previously generated key, which the earlier section identifies as a 256-bit AES key. The guide also calls the session-key step a request for a PIN *change* (line 232) although the page and endpoint concern PIN *reveal*. Do not treat that conflicting decryption wording as validated implementation instructions. See raw lines 228, 232–237, 465–490.

## Detail locators

- The test-host curl and language-library samples are in **Get a public key from Adyen** (lines 52–224) and **Request the PIN block from Adyen** (lines 250–447); their library version labels differ by endpoint and language. They are examples, not live-environment evidence.
- Token formatting, XOR, byte conversion, and example PIN extraction positions are in **Decrypt the PIN block and reveal the PIN** (lines 465–496). That section is affected by the cryptographic ambiguity above.

## Related

- [[adyen-issuing]] — Issuing concept and source route.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-card-data/reveal-pin/2026-09-15|Reveal PIN using standard encryption methods, captured 2026-09-15]]
