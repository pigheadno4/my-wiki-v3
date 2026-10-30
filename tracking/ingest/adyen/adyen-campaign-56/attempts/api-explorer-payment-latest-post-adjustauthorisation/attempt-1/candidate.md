---
title: "Adyen Classic Payment API POST /adjustAuthorisation (captured v68)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/adjustAuthorisation"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/adjustAuthorisation/2026-09-15.md"
tags: [adyen, classic-api, payment-api, authorization-adjustment, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Classic Payment API `POST /adjustAuthorisation` at the displayed test `https://pal-test.adyen.com/pal/servlet/Payment/v68` server. It requests an increase or decrease to an already authorised payment amount. The page marks this endpoint inactive and unsupported for new integrations, directs new builds to Checkout API `/payments/{paymentPspReference}/amountUpdates`, and tells existing users to contact Adyen about migration. This source is the Classic endpoint contract, not the Checkout amount-update contract. See [[adyen]] and [[adyen-authorization-adjustment]].

## Key takeaways

- The request property table marks `merchantAccount`, `modificationAmount.currency`, `modificationAmount.value`, and `originalReference` required. `modificationAmount` is the **new total** authorised amount in minor units, not the incremental difference. `originalReference` is the original payment PSP reference from the authorisation response or notification. Optional `reference` is the merchant's reference for this modification, distinct from the original PSP reference and response's modification/request PSP reference.
- The 200 response's `response` field indicates that the modification request was **received for processing**; the example is `[adjustAuthorisation-received]`. The returned `pspReference` identifies this request. Neither 200 nor that acknowledgement establishes final issuer acceptance, capture or settlement; the related Classic adjustment guide provides the later webhook and lifecycle detail.
- The raw lists 400 malformed-request, 401 authentication, 403 permission, 422 validation and 500 server failures with generic error objects. It gives 200, 400, 401 and 500 examples. The optional `originalMerchantReference` row says “original merchant reference to cancel,” wording inconsistent with this adjustment endpoint; do not read it as a cancellation action.
- This captured `latest` path displays Classic Payment API test v68 and does not prove today's latest version, live eligibility, a successful adjustment, or the schema of the linked Checkout replacement.

## Detail locators

- Purpose, inactive/new-build migration note and displayed test server: raw lines 5–18.
- Request table: lines 22–59; core required properties 26–29 and 44, optional modification reference 49, ambiguous originalMerchantReference 43, conditional platform split data 45–57. Example request: 61–74.
- 200 response fields and received-state meaning: lines 75–85, example 157–167. Error schemas/examples: 88–155 and 169–204.

## Related

- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-adjust-authorisation]] — wider Classic pre-authorization, webhook, capture and expiry guide.
- [[adyen-authorization-adjustment]] — provider concept and reciprocal source route.

## Related raw API references

- Checkout `/payments/{paymentPspReference}/amountUpdates` is linked by this raw at line 11; use its separately reviewed contract for Checkout request/response details.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/adjustAuthorisation/2026-09-15|Classic Payment API POST /adjustAuthorisation snapshot (2026-09-15)]]
