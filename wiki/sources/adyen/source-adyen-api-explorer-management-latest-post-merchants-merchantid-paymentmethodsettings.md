---
title: "Adyen Management API v3: request a merchant payment method"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/2026-11-05.md"
tags: [adyen, management-api, payment-methods, merchant-account]
---

## Overview

This 2026-11-05-captured Management API v3 TEST reference defines `POST /merchants/{merchantId}/paymentMethodSettings` to request adding a payment method to the merchant account in the required `merchantId` path. The API credential needs `Management API—Payment methods read and write`. The request's required `type` is a payment method variant; see [[adyen-payment-method-variants]] and [[adyen-api-access]].

## Key takeaways

- The request body requires `type`. Its many method-specific parent objects are marked optional in the table, while nested fields can be required when the relevant object is supplied, and some prose imposes type, contract, or region conditions. For example, `businessLineId` is required for a platform model; `shopperInteraction` is required if the merchant has no sales channel or `type` is `alipay`. Read the exact method row before constructing a request.
- Optional `countries` and `currencies` default to all supported by the chosen method. Optional `storeIds` scopes configuration to stores. Method-specific defaults and limits vary: Apple Pay `domains` has a 99-domain request maximum; PayPal `directCapture` defaults to true and, when true, overrides merchant capture settings. Transaction-description settings cannot be configured in TEST.
- A 200 response requires resource `id` and may include `allowed`, `enabled`, `verificationStatus`, and `associatedPaymentMethods`. Adyen sets `allowed=true` after screening; `enabled` separately reports enablement; `verificationStatus` can be `valid`, `pending`, `invalid`, or `rejected`. The endpoint also documents 204 with no content. A successful request or returned ID does not itself establish screening approval, enablement, verification, transaction authorization, capture, or settlement.
- Documented failures are 400, 401, 403, 422, 429 and 500. The snapshot specifies no idempotency, propagation timing, deletion/reversal, or live-server behavior. The Visa and partner-model examples illustrate request and response shapes, not general eligibility.

## Detail locators

- Purpose, role, TEST v3 server and merchant path: raw lines 5–22.
- Request fields and method-specific/conditional requirements: raw lines 25–214; illustrative requests: lines 216–246.
- 200 response states, associated transitions and ID: raw lines 247–449; 204 and errors: lines 452–572.
- Illustrative 200 responses: raw lines 574–608.

## Related

- [[adyen-payment-method-variants]] — variant identity and configuration scope.
- [[adyen-api-access]] — credential permissions.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/2026-11-05|POST merchant paymentMethodSettings, captured 2026-11-05]]