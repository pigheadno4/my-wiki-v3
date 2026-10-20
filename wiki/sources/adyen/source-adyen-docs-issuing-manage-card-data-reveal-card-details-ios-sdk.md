---
title: "Adyen Issuing: reveal card details with the iOS SDK"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-card-data/reveal-card-details-ios-sdk"
raw_files:
  - "adyen/docs/issuing/manage-card-data/reveal-card-details-ios-sdk/2026-09-15.md"
tags: [adyen, issuing, card-data, ios]
---

## Overview

This 2026-09-15 Issuing guide describes revealing an Adyen-issued card's PAN, CVC and expiration date to its cardholder inside an iOS app. Its flow obtains an Adyen public key through the Configuration API, uses the Card Reveal iOS SDK to generate an encrypted symmetric session key, requests encrypted details for a `paymentInstrumentId`, then decrypts and displays those details on the client. This is sensitive card-data access, not card activation, a payment authorization, or a claim about a particular integration's PCI scope. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Prerequisites stated here are Configuration API credentials with the **Bank Issuing PaymentInstrument Reveal Webservice** role, iOS **13.0 or later**, and Adyen's Card Reveal iOS SDK. The snapshot does not pin a Card Reveal SDK release; its server-language snippets carry historical library versions and TEST endpoints.
- The server obtains `GET /publicKey` with `purpose=panReveal` and `format=jwk`; the response contains a public key and expiry date. The guide calls the key “base64-encoded RSA” in its prose while requesting JWK format and passing the result to `generateEncryptedKey(withJwk: publicKey)`. Preserve this representation ambiguity instead of assuming the raw response is directly interchangeable with any base64 RSA encoding.
- The app initializes `CardRevealService` and generates an `encryptedKey`; the server then calls `POST /paymentInstruments/reveal` with that key and the target `paymentInstrumentId`. Adyen returns `encryptedData`, which is passed to the client; `cardDetails(from: encryptedData)` decrypts it, and the app reveals the result to the cardholder. The guide does not document user-authentication, entitlement or display-retention controls for this flow.
- The sample keys, IDs, API calls and responses are illustrative TEST examples. They do not establish that a real card was retrieved or that a live sensitive-data flow met security or compliance requirements.

## Detail locators

- Raw lines 15–47 define purpose, ordered flow and prerequisites.
- Raw lines 49–58 specify public-key retrieval and query values; lines 60–232 contain TEST/server-library snippets and sample response with public-key expiry.
- Raw lines 234–254 show iOS `CardRevealService` and `generateEncryptedKey(withJwk:)`.
- Raw lines 256–266 define the reveal request fields; lines 267–476 contain TEST/server-language examples, encrypted response and client handoff.
- Raw lines 478–492 show SDK decryption and app display.

## Related

- [[adyen-issuing]] — Issuing program context.
- [[adyen]] — provider context.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-card-data/reveal-card-details-ios-sdk/2026-09-15|Adyen Issuing iOS card-details reveal, captured 2026-09-15]]
