---
title: "Adyen Balance Platform API v2: Assign authorised card users"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02.md"
tags: [adyen, balance-platform, issuing, cards, api]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform API Explorer capture documents `POST /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers` on the listed TEST `/bcl/v2` server. It assigns authorised users, identified by legal-entity IDs, to a card payment instrument. The page says users must have the `authorisedPaymentInstrumentUser` capability to use the card. An assignment response is separate from capability approval, card activation, cardholder authentication or a card transaction. The `latest` path and TEST server do not prove current version or LIVE eligibility.

## Key takeaways

- `paymentInstrumentId` is a required string path parameter. The request-body table lists only `legalEntityIds`, an optional array of legal-entity ID strings linked to that payment instrument; it does not separately state whole-body requiredness, cardinality, empty-array behavior or a default. The request example contains two IDs, but that does not establish a two-user limit or requirement.
- A 204 response says “Successful operation” and provides no response-body schema, returned assignment resource or status. The page gives no propagation timing or card-use guarantee. Confirming the users' required capability and any subsequent card-use outcome needs separate evidence.
- Error tables document 400 bad request, 401 unauthorized, 403 forbidden and 422 validation. The 400 example describes an instrument already linked with legal entities and directs use of PATCH; the 422 example describes a payment instrument that is not multi-use. These illustrate possible errors but do not establish exhaustive lifecycle rules or a guaranteed result for every instrument. The 403 example says a card partner is not allowed yet, without defining an entitlement grant. No idempotency header, deletion/reversal operation or asynchronous outcome contract is specified on this page.

## Detail locators

- Raw lines 5–23: purpose, capability qualification, TEST v2 server, path ID and optional body field.
- Raw lines 25–39: two-ID request example and bodyless 204 success.
- Raw lines 42–115: 400, 401, 403 and 422 error schemas.
- Raw lines 117–171: example error payloads, including already-linked, card-partner and non-multi-use cases.

## Related

- [[adyen]]
- [[adyen-issuing]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02|Adyen Balance Platform API Explorer POST authorised card users (captured 2026-11-02)]]
