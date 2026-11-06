---
title: "Get Apple Pay domains | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/getApplePayDomains"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/getApplePayDomains/2026-11-05.md"
tags: [adyen, management-api, apple-pay, payment-methods, domains]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, describes `GET /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/getApplePayDomains`. It returns Apple Pay domains registered with the merchant account and payment method identified in the path. The listed server is TEST `https://management-test.adyen.com/v3`; the calling API credential needs `Management API—Payment methods read`. See [[adyen-online-payments]] for the Apple Pay integration context and [[adyen-api-access]] for credential scope.

## Key takeaways

- Both path inputs are required strings: `merchantId` identifies the merchant account and `paymentMethodId` the payment method. The reference specifies no query parameters, request body, defaults or limits. [Raw: lines 16–22]
- The documented `200` response marks the request successful and has an optional `domains` array of strings described as the list of merchant domains. The separate `204` success response has no additional content; it supplies no domain list or other state readback. [Raw: lines 24–36]
- This GET reads registration information for the identified merchant/payment-method pair. A returned domain list does not demonstrate domain verification, wallet/browser availability, certificate validity, Live enablement, a completed Apple Pay session, payment authorization or settlement. The raw points to separate Apple Pay guides for registration and going live; those linked guides are navigation, not evidence of their detailed requirements here. [Raw: lines 5–7, 29–36]
- The reference lists `400` request interpretation, `401` authentication, `403` insufficient permission, `422` validation and `500` server failures. Their error tables define problem-detail fields; see raw for exact requiredness. [Raw: lines 39–136]
- This read-only capture specifies no idempotency rule, domain-registration mutation or deletion, propagation timing, review/approval/activation workflow, or Live endpoint. Its `latest` label and capture date do not prove current eligibility or availability.

## Detail locators

- Purpose, caller role, TEST v3 server and path identities: pinned raw lines 5–22.
- `200` optional domain list and `204` no-content result: pinned raw lines 24–36.
- Failure categories and exact error-field schemas: pinned raw lines 39–136.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/getApplePayDomains/2026-11-05|Management API Apple Pay domains GET — captured 2026-11-05]]