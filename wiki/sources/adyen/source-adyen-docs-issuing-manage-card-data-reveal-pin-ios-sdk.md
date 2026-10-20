---
title: "Adyen Issuing: Reveal PIN with the Card Reveal iOS SDK"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-card-data/reveal-pin-ios-sdk"
raw_files:
  - "adyen/docs/issuing/manage-card-data/reveal-pin-ios-sdk/2026-09-15.md"
tags: [adyen, issuing, pin, ios, card-reveal, encryption]
---

## Overview

This 2026-09-15-captured Adyen Issuing guide shows how a platform can let a cardholder reveal the PIN of an Adyen-issued card in its iOS app through Adyen's Card Reveal iOS SDK. The flow obtains a public key from Adyen, generates an encrypted symmetric session key on the client, requests an encrypted PIN block for a specific card, and decrypts it for display in the app. It concerns access to sensitive card data under [[adyen-issuing]], not PIN change, card activation, or payment authorization. See [[adyen]].

## Key takeaways

- Prerequisites are Configuration API credentials with the **Bank Issuing PIN Reveal Webservice role**, an app running **iOS 13.0 or higher**, and the installed Card Reveal iOS SDK (raw lines 36–46). This page does not identify a Card Reveal SDK release version. Its many server API-library snippets have their own named versions and use TEST environment examples; those versions are not the SDK's version (raw lines 63–214, 270–463).
- Retrieve a base64-encoded RSA public key through Configuration API `GET /publicKey` with `purpose=pinReveal` and `format=pem`; the response includes the key and its expiry date. Pass the returned public key to the client, where `PinRevealService.generateEncryptedKey(withPem:)` creates the encrypted session key (raw lines 48–57, 217–253). Some multi-language sample calls use literal `string` placeholders rather than the specified query values; follow the prose and endpoint parameters.
- Request `POST /pins/reveal` with the card's `paymentInstrumentId` and the `encryptedKey`. Adyen's response supplies an ISO Format 4 `encryptedPinBlock` and a `token`; pass both to the client. The SDK's `pin(from:token:)` method decrypts the block, after which the app displays the decrypted PIN to the cardholder (raw lines 255–264, 465–495). The PIN is sensitive data: this guide describes a secure-transfer flow, while the app is the place where the decrypted PIN is handled and displayed.
- The test endpoint and example IDs/ciphertext demonstrate request shape only. A public-key response, generated key, or PIN-block response does not by itself establish that a particular cardholder is authenticated, a live PIN was shown, or any payment succeeded.

## Detail locators

- Purpose and four-step flow: raw lines 15–34.
- Role, iOS and SDK prerequisites: raw lines 36–46.
- Public-key API and response including expiry: raw lines 48–231; Swift session-key generation at 233–253.
- PIN-block request and test/API-library examples: raw lines 255–463.
- Encrypted block, token and client-side reveal: raw lines 465–495.

## Related

- [[adyen]] — provider context.
- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-manage-card-data]] — card-data management hub.
- [[source-adyen-docs-issuing-manage-card-data-reveal-pin]] — separate standard-encryption PIN-reveal path.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-card-data/reveal-pin-ios-sdk/2026-09-15|Adyen Issuing reveal PIN with iOS SDK, captured 2026-09-15]]
