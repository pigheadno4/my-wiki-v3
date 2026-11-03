---
title: "Adyen Balance Platform API v2: Reveal card PAN by payment instrument ID"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/reveal"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/reveal/2026-11-02.md"
tags: [adyen, balance-platform, issuing, card-data, api]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform API Explorer capture documents `GET /paymentInstruments/{id}/reveal` on the listed TEST `/bcl/v2` server. It returns sensitive card details for the payment instrument identified in the path. The page explicitly requires the API credential's `Balance Platform BCL PCI` role. This GET response schema lists card data directly; it is distinct from the separately captured [[source-adyen-api-explorer-balanceplatform-latest-post-paymentinstruments-reveal|POST /paymentInstruments/reveal]] encrypted-data route. Neither endpoint's response proves cardholder display, card activation or a transaction. The `latest` URL and TEST host do not establish current version, LIVE availability or credential entitlement.

## Key takeaways

- Required string path `id` is the payment instrument's unique identifier. This page lists no query parameters, request body, idempotency header, defaults or amount limits.
- The 200 schema marks `pan`, `cvc` (card CVC2) and `expiration` required at the top level. Within required `expiration`, `month` and `year` are individually optional. The one 200 example illustrates values but does not guarantee particular card details or display to a cardholder. The page does not describe encryption of this GET response or the client handling path.
- The page documents 400 request, 401 authentication, 403 permission, 422 validation and 500 server errors. Its generic 422 example concerns changing a balance-account ID on a payment instrument; its generic 500 example concerns creation of a payment instrument. Those example details do not define reveal-specific state transitions or failures.

> [!warning] Contradiction
> The generic 422 and 500 examples describe payment-instrument update/creation (raw lines 192–218), while this endpoint is a GET that reveals card data. They must not be interpreted as this GET changing or creating an instrument.

## Detail locators

- Raw lines 5–21: reveal purpose, required BCL PCI role, TEST v2 server and path ID.
- Raw lines 23–35: 200 card-data response schema and nested expiration requiredness.
- Raw lines 38–135: 400, 401, 403, 422 and 500 error schemas.
- Raw lines 137–218: one 200 example and generic error examples; unrelated update/creation text at lines 192–218.

## Related

- [[adyen]]
- [[adyen-issuing]]
- [[source-adyen-api-explorer-balanceplatform-latest-post-paymentinstruments-reveal]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/reveal/2026-11-02|Adyen Balance Platform API Explorer GET card reveal (captured 2026-11-02)]]
