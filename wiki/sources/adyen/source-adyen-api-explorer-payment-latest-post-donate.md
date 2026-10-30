---
title: "Adyen Payment API v68 POST /donate"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/donate"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/donate/2026-09-15.md"
tags: [adyen, payment-api, donations, giving]
---

## Overview

This 2026-09-15 capture describes the **Payment API v68** `POST /donate` endpoint: it schedules a new donation payment and authorisation request using payment details from an original payment. This is an [[adyen]] [[adyen-giving]] donation request, distinct from the original payment. The listed server is `https://pal-test.adyen.com/pal/servlet/Payment/v68`; the `latest` URL does not prove a later version or live availability.

## Key takeaways

- The endpoint is marked **inactive** and unsupported for new integrations. The page directs new integrations to Checkout API `/donations`; existing users are told to contact Adyen and migrate to Checkout API (raw lines 7–18). This Payment API reference does not define the Checkout endpoint contract.
- The request table marks `donationAccount`, `merchantAccount`, and `modificationAmount` with nested `currency` and `value` as required properties. The donation currency must match the original authorisation currency and its value must be no greater than the authorised amount (lines 20–29). The table does not separately state whole-body requiredness.
- `originalReference` is labeled optional even though its description identifies the original payment's PSP reference and the example supplies it (lines 30, 37–51). Do not promote the example to unconditional requiredness. `reference` is an optional merchant modification reference. Platform chargeback options are conditional; `targetAccount` is required if `behavior` is `deductFromOneBalanceAccount` (lines 31–35).
- The `200 Success` response contains a request-associated `pspReference` and `response` indicating whether the modification request was **received for processing** (lines 52–62). That acknowledgement is not donation authorisation, capture, settlement, or nonprofit receipt. The page lists 400, 401, 403, 422, and 500 errors (lines 65–132) and illustrative error bodies (lines 134–171).

## Detail locators

- Endpoint identity, inactive/migration notice, test server: raw lines 5–18.
- Request properties, conditions, JSON example: raw lines 20–51.
- Success/error schemas and error examples: raw lines 52–171.

## Related

- [[adyen-giving]] — Giving concept and route-specific outcome context.
- [[adyen-online-payments]] — online integration context.

## Related raw API references

- Checkout API `POST /donations` — linked from this page (raw line 11); its separate reference must be read for Checkout-specific schema and behavior.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/donate/2026-09-15|Payment API POST /donate reference, captured 2026-09-15]]
