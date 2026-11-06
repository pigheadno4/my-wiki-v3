---
title: "Management API: Get merchant payment method details"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/2026-11-05.md"
tags: [adyen, management-api, payment-methods, merchant-account]
---

## Overview

The captured Management API `GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}` returns details for the merchant account and payment method identified by the two required path IDs. It lists the Test `https://management-test.adyen.com/v3` server and requires the caller's API credential to have **Management API—Payment methods read**. This is a configuration read, not a payment or method-activation request. [[adyen]] [[adyen-account-structure]]

## Key takeaways

- A `200` means the read request succeeded. Its response schema requires `id`, the resource identifier. `type` is an optional payment-method variant; `reference`, merchant category code, MID, countries, currencies, store IDs, and method-specific objects are optional. The raw response table is the locator for those fields and their conditional or method-specific descriptions.
- `allowed` is optional and indicates whether receiving payments is allowed; the page says Adyen sets it true after screening the merchant account. `enabled` separately indicates enabled or disabled configuration. `verificationStatus` is optional with `valid`, `pending`, `invalid`, or `rejected` values. These fields should not be collapsed into one readiness state. The optional `associatedPaymentMethods` parent lists methods updated as part of an associated transition; each item marks `enabled`, `id`, and `type` required within that item.
- The response's `businessLineId` description says it is required if the caller is a platform model, though the response table marks the field optional. This is a response-field condition, not an additional GET input. Some method-specific fields carry their own defaults or limits: for example, optional PayPal `directCapture` defaults true, and the PayPal `payerId` description specifies 13 single-byte alphanumeric characters. Transaction-description text recommends 22 characters and warns banks may truncate longer strings; that recommendation is not a universal request limit here.
- The page also documents `204` as successful processing with no additional content, so that status supplies no resource readback. It lists 400, 401, 403, 422, 429, and 500 error responses. The captured GET has no body, idempotency setting, mutation, deletion, propagation or approval transition, Live endpoint, or payment-outcome guarantee. A returned configuration does not itself prove current Live eligibility, successful authorization, capture, settlement, or bank receipt.

## Detail locators

- Purpose, credential role, Test server, and two required path IDs: raw lines 5–22.
- `200` response identity, `allowed`, associated transitions, `businessLineId`, countries/currencies, and `enabled`: raw lines 26–102. Method-specific detail continues through lines 103–226; `id` is line 115, PayPal fields are lines 168–171, `verificationStatus` is line 213.
- `204` no-content response and error statuses/body schemas: raw lines 229–349. This captured page has no request or response JSON example.

## Related

- [[adyen-account-structure]] — merchant-account placement of payment-method configuration.
- [[adyen-payment-method-variants]] — variant terminology; a variant name is not an activation or payment result.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/2026-11-05|Pinned Management API payment-method detail GET reference]]