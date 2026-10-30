---
title: "Adyen Balance Platform API v2: reveal payment-instrument data"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments/reveal"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/reveal/2026-09-15.md"
tags: [adyen, balance-platform, issuing, payment-instruments, card-data, encryption, api]
---

## Overview

This 2026-09-15-captured Balance Platform API v2 reference documents `POST /paymentInstruments/reveal` on the test server. For a specified card payment instrument, it returns encrypted PAN, CVC and expiry data for later decryption and display in a user interface. The page does not itself establish who viewed the data, an active card, a payment or current live availability. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The page requires the API credential to have the **Bank Issuing PAN Reveal Webservice** role. Its separate [[source-adyen-docs-issuing-manage-card-data-reveal-card-details|Issuing card-details guide]] names **Bank Issuing PaymentInstrument Reveal Webservice** for this flow. The captured sources use different role labels; do not treat them as equivalent without separate confirmation.
- The request-body table marks both `encryptedKey` and `paymentInstrumentId` required. `encryptedKey` is the symmetric session key encrypted with an Adyen public key obtained separately; `paymentInstrumentId` identifies the card payment instrument. The endpoint returns required `encryptedData` encrypted using that key. The reference links a version-`2` `GET /publicKey` page for the key; this capture does not specify the key's purpose, expiry, format or a full cryptographic implementation.
- A `200` response confirms the reveal request succeeded and contains ciphertext. Decryption and UI display are separate client steps; the response is not proof of cardholder access, card activation, authorization, settlement or funds movement. Handle the encrypted card data as sensitive.
- The page lists `400` malformed/unreadable request, `401` authentication, `403` insufficient permission, `422` validation and `500` server-processing errors. Its generic `422` example discusses a balance-account ID status change, and its generic `500` example says creation of a payment instrument failed; neither establishes a reveal-specific lifecycle rule or creation effect.

## Detail locators

- Purpose, sensitive fields and credential role: raw lines 5–19.
- Test-server base URL: line 22; request-body fields and public-key link: lines 24–30.
- `200` encrypted response: lines 32–40.
- Error meanings and common problem-body schema: lines 43–140.
- Generic error examples, including unrelated `422`/`500` wording: lines 142–209.

## Related

- [[adyen-issuing]] — Issuing card-program context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-publickey]] — separate key-retrieval reference.
- [[source-adyen-docs-issuing-manage-card-data-reveal-card-details]] — broader cardholder-facing flow and conflicting credential-role label.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/reveal/2026-09-15|POST /paymentInstruments/reveal API Explorer capture]]
