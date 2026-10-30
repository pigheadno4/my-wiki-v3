---
title: "Adyen Issuing: Reveal card details with standard encryption"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-card-data/reveal-card-details"
raw_files:
  - "adyen/docs/issuing/manage-card-data/reveal-card-details/2026-09-15.md"
tags: [adyen, issuing, card-data, encryption, pan]
---

## Overview

This 2026-09-15 Issuing guide describes an app or website flow for revealing an Adyen-issued card's PAN, CVC and expiration date to its cardholder. It uses an Adyen RSA public key, a locally generated AES session key, and an encrypted Configuration API reveal response before rendering sensitive details in the interface. This is card-data display guidance, not a payment or card-activation result. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The guide requires Configuration API credentials with the **Bank Issuing PaymentInstrument Reveal Webservice** role. GET `/publicKey` uses `purpose=panReveal`; its response carries `publicKey` and `publicKeyExpiryDate`. The curl request uses the test Balance Platform API host.
- Generate a 256-bit AES key, then encrypt it with Adyen's public RSA key using the guide's PKCS 1 wording. POST `/paymentInstruments/reveal` supplies `paymentInstrumentId` and `encryptedKey`; its response contains `encryptedData`, which is passed to the client. Decrypt with that AES key in CBC mode with PKCS 5 padding, then render the extracted card details to the cardholder. This flow makes PAN/CVC plaintext available to the rendering client after decryption; a successful API request alone does not prove that the intended cardholder saw it.
- The SDK snippets for GET `/publicKey` use placeholder `purpose: string`/`format: string` while the prose and curl specify `panReveal`. Do not substitute the placeholder for the stated purpose. The GET and reveal sections also show different language-library version labels; treat these as dated examples rather than one pinned SDK integration.

> [!warning] Contradiction
> This guide names **Bank Issuing PaymentInstrument Reveal Webservice**. The separately captured Configuration API v2 [[source-adyen-api-explorer-balanceplatform-latest-post-paymentinstruments-reveal]] instead names **Bank Issuing PAN Reveal Webservice**. Preserve the two snapshot labels; neither establishes that the role names are interchangeable.

## Detail locators

- Cardholder-facing data and high-level sequence: raw lines 17–39. Credential role: raw lines 41–46.
- `purpose=panReveal` GET, test curl, language examples and public-key expiry response: raw lines 48–228. The SDK placeholder-purpose examples appear at lines 98, 124, 173 and 193.
- AES/RSA session-key steps: raw lines 230–241. POST reveal request fields, test-host and SDK examples: raw lines 243–452. Encrypted response, client handoff and AES-CBC/PKCS 5 decryption: raw lines 453–474. Example plaintext JSON and final display statement: raw lines 476–491.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing card-program context.
- [[source-adyen-docs-issuing-manage-card-data]] — card-data management navigation.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-card-data/reveal-card-details/2026-09-15|Reveal card details — 2026-09-15 snapshot]]
