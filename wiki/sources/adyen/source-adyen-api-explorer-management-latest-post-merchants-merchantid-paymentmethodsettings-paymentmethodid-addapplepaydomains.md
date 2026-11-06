---
title: "Add Apple Pay domains | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/addApplePayDomains"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/addApplePayDomains/2026-11-05.md"
tags: [adyen, management-api, apple-pay, payment-method-settings]
---

## Overview

`POST /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}/addApplePayDomains` adds domains to the Apple Pay domain list registered for the named merchant account and payment method. The captured Management API server is `https://management-test.adyen.com/v3`. This is a merchant payment-method configuration operation, separate from Apple Pay merchant validation or a payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The caller's API credential requires **Management API—Payment methods read and write**. Both `merchantId` (merchant account) and `paymentMethodId` (payment method) are required path identifiers.
- The body requires `domains`, an array of merchant-domain strings, with a maximum of **99 domains per request**. The example supplies `https://example.com`; the example is not a validation rule for every allowed string. The pinned page states no other body field or default.
- The documented success is HTTP **204**, with no response resource fields; the page tells readers to inspect the actual status code. It does not specify a returned domain list, asynchronous approval state, verification result, or activation timing.
- Authentication, permission, request validation, rate-limit and server-error routes appear as 401, 403, 422, 429 and 500; 400 covers request-reading problems. The 429 section provides a generic error schema without retry timing.

> [!warning] Outcome boundary
> A successful add-domain request records a configuration operation in this reference. The pinned page alone does not establish that the domain was independently verified, Apple Pay is live or eligible for this merchant, a wallet session was created, or any payment was authorized or settled. Its sole captured server is test.

## Detail locators

- Raw lines 5–28: operation purpose, credential role, test v3 server, required path identities and `domains` body limit.
- Raw lines 30–43: illustrative body and 204 success instruction.
- Raw lines 46–162: 400, 401, 403, 422, 429 and 500 response descriptions and generic error fields.

## Related

- [[adyen-online-payments]] — online payment architecture and Apple Pay source routes.
- [[source-adyen-docs-payment-methods-apple-pay-web]] — separate Apple Pay web guidance; not evidence for this endpoint's response.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/addApplePayDomains/2026-11-05|Add Apple Pay domains, captured 2026-11-05]]