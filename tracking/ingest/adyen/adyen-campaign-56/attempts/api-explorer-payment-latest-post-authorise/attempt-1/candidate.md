---
title: "Adyen Classic Payment API v68: POST /authorise"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/authorise"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/authorise/2026-09-15.md"
tags: [adyen, classic-payment-api, authorisation, api-reference]
---

## Overview

This captured [[adyen]] **Classic Payment API**, not Checkout API, reference describes `POST /authorise`. It creates a payment with an Adyen `pspReference` and attempts an authorization hold. For cards, the amount can later be captured or cancelled; non-card methods typically auto-capture as part of authorization. The page labels the endpoint **inactive** and unsupported for new integrations: use Checkout `/payments` for a new integration and contact Adyen about migrating an existing one. The captured server is `https://pal-test.adyen.com/pal/servlet/Payment/v68`; the `latest` URL does not establish a currently live latest version or live endpoint.

## Key takeaways

- The request table marks `amount`, `merchantAccount` and merchant `reference` required; `amount.currency` and `amount.value` are required children, with value in minor units. `reference` identifies the payment in merchant communication and is distinct from Adyen's response `pspReference`.
- The table describes either `bankAccount` or `card` in a payment request, but the recurring ContAuth sample supplies stored-detail identifiers without either field. Do not treat that table sentence as a universal schema rule for the recurring sample. `shopperReference` and `recurringProcessingModel` have recurring/token use conditions. Raw card examples and their fields are historical Classic API examples, not Checkout `/payments` schema or a recommendation to pass raw card data.
- 3DS2 inputs depend on channel and flow. `billingAddress` is conditionally required for browser/mobile 3DS2, `browserInfo` for web 3DS, and the table gives mobile redirect fields and Visa/JCB email/phone/IP conditions. Within optional `threeDS2RequestData`, `deviceChannel` is marked required; authentication-only flags and several 3DS fields have separate conditions. Use the raw field descriptions and relevant guide for the selected flow.
- HTTP 200 says the **request** succeeded. Optional `resultCode` can report `Authorised`, other final outcomes, pending/received states, or further 3DS/shopper action; authentication-only outcomes are not payment authorization. The `pspReference` identifies the request/transaction, and refusal reasons may accompany declined or errored authorization. Request success or an authorization hold does not itself establish later card capture or settlement.
- The raw reference lists 400, 401, 403, 422 and 500 error categories. Its example error bodies illustrate responses, not a complete set of possible codes.

## Detail locators

- Purpose, inactive/migration warning and v68 TEST server: raw lines 5–18.
- Core request fields and conditions: raw lines 22–102, 201–294; 3DS2 nested schema: lines 294–369.
- Alternative request examples, including 3DS, card, recurring and split flows: raw lines 373–572.
- 200 response fields and result states: raw lines 573–596; error response shapes and examples: lines 599–705.

## Related

- [[adyen-online-payments]] — provider-level online payments and migration route.
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration]] — Classic integration guide and historical prerequisites.
- [[source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api]] — migration guidance.
- [[adyen-3d-secure]] — broader 3DS context; this raw retains the Classic v68 fields.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/authorise/2026-09-15|Classic Payment v68 POST /authorise capture]]
