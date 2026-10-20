---
title: "Adyen Issuing: Change PIN using the iOS SDK"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-card-data/change-pin-ios-sdk"
raw_files:
  - "adyen/docs/issuing/manage-card-data/change-pin-ios-sdk/2026-09-15.md"
tags: [adyen, issuing, ios, cards, pin]
---

## Overview

This Adyen Issuing guide (last modified and captured 2026-09-15) describes changing an issued card's PIN within an iOS app using Adyen's Card Reveal iOS SDK to form the encrypted PIN block, then the Balance Platform Configuration API to request the change. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Requirements are Configuration API credentials with the **Bank Issuing PIN Change Webservice** role, an app on **iOS 13.0 or higher**, and the installed Card Reveal iOS SDK. The page's flow gets a public key, generates an encrypted PIN block in the client, and sends POST `/pins/change`. See raw lines 19–45.
- GET `/publicKey` specifies `purpose=pinChange` and `format=pem`. The returned public key has an expiry date and is passed to the client. The public-key examples use a test host; several generated language snippets show generic `string` placeholders, while the prose specifies the actual query values. See raw lines 47–68 and 216–230; versioned SDK examples are at raw lines 70–214.
- The iOS example constructs `PinChangeService` and calls `encryptedPinBlock(withPem: publicKey, pin: pin)`. The resulting object contains `encryptedPinBlock`, `encryptedKey`, and `token` to submit with the card's `paymentInstrumentId`. The new PIN is supplied to the SDK's client method; the described API request carries the encrypted block and related outputs, not a plaintext PIN field. See raw lines 232–267.
- The request table describes `encryptedKey` as “The symmetric session AES key,” while the SDK-output prose calls it the symmetric session `encryptedKey` used to securely send the block. Keep the encrypted-output identity when reading the terse table; the page does not specify sending a plaintext AES key. See raw lines 252–267. The companion [[source-adyen-docs-issuing-manage-card-data-change-pin]] describes the separate standard-encryption route.
- The POST response reports request status **completed**, **pending**, or **unavailable**. A sample request or `pending` response does not establish a completed PIN change. The API snippets are test-environment examples with differing library versions, not evidence of a live card or payment. See raw lines 269–488.

## Detail locators

- Scope, role, iOS and SDK prerequisites: raw lines 19–45.
- Public-key parameters, example response and expiry: raw lines 47–230.
- iOS PIN-block method and outputs: raw lines 232–256.
- POST fields, test snippets and status values: raw lines 258–488.

## Related

- [[adyen-issuing]] — main concept.
- [[source-adyen-docs-issuing-manage-card-data-change-pin]] — standard-encryption PIN-change route.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-card-data/change-pin-ios-sdk/2026-09-15|Change PIN using Adyen's iOS SDK, captured 2026-09-15]]
