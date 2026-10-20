---
title: "Adyen Issuing: Change PIN using standard encryption methods"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-card-data/change-pin"
raw_files:
  - "adyen/docs/issuing/manage-card-data/change-pin/2026-09-15.md"
tags: [adyen, issuing, cards, pin, encryption]
---

## Overview

This Adyen Issuing guide (last modified and captured 2026-09-15) describes a platform feature for a cardholder to change an issued card PIN through an app or website. It gives the Configuration API public-key and `/pins/change` route, encryption sequence, and request-status values. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The guide requires Configuration API credentials with the **Bank Issuing PIN Change Webservice** role. Its illustrated steps obtain an Adyen public key, generate a 256-bit AES key, RSA-encrypt that AES key as a session key, generate a token and encrypted PIN block, then send a POST `/pins/change` request for a `paymentInstrumentId`. See raw lines 19–43, 227–248, 281–290.
- For the key request, GET `/publicKey` uses `purpose=pinChange`; the response includes the public key and its expiry date, and the guide says to pass the public key to the front end. The RSA encryption step cites PKCS 1. The token must be a 16-digit random number without zeros. The PIN block uses ISO format 4; the full formatting and AES/ECB sequence is in the raw, not repeated here. See raw lines 45–51, 211–279.
- The POST request table lists `paymentInstrumentId`, `encryptedKey`, `token`, and `encryptedPinBlock`. The `encryptedKey` row calls the field “The symmetric session AES key,” while the preceding text instructs encrypting the AES key with Adyen's public key to produce an encrypted session key. Keep that distinction when implementing; do not infer that a plaintext AES key should be sent. See raw lines 229–238 and 281–290.
- The response gives request status values **completed**, **pending**, or **unavailable**. A submitted sample or `pending` response is not proof that the PIN changed. The curl and library snippets use a test host/environment and mixed library versions; the prose specifies `purpose=pinChange` even though several generated library snippets show generic `string` placeholder arguments. Read version-specific SDK details in raw lines 55–209 and request samples at lines 294–509. The page gives no evidence of a live card or payment outcome.

## Detail locators

- Role and workflow prerequisites: raw lines 19–43.
- Public-key request, response, expiry and test/SDK snippets: raw lines 45–225.
- AES/RSA, token and ISO-4 PIN-block sequence: raw lines 227–279.
- PIN-change request fields and examples: raw lines 281–509.
- Response status values: raw line 511.

## Related

- [[adyen-issuing]] — main concept.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-card-data/change-pin/2026-09-15|Change PIN using standard encryption methods, captured 2026-09-15]]
