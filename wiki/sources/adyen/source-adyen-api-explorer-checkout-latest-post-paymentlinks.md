---
title: "Adyen Checkout API POST /paymentLinks (captured v72)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentLinks"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/paymentLinks/2026-09-15.md"
tags: [adyen, checkout, pay-by-link, payment-links, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Checkout API `POST /paymentLinks` on the displayed test `https://checkout-test.adyen.com/v72` server. It creates a payment-link object and URL for an Adyen-hosted Pay by Link page, with presented methods dependent on request currency and country. It does not itself execute or confirm a shopper payment. See [[adyen]] and [[adyen-unified-commerce]].

## Key takeaways

- The request property table marks `amount` (with currency and minor-unit value), `merchantAccount`, and `reference` required. `countryCode` is optional in the table even though the introduction says method presentation depends on currency and country. The optional `Idempotency-Key` header has a 64-character maximum. Nested `Yes` marks apply within optional parent objects; the page does not separately declare the entire request body required.
- `expiresAt` defaults to 24 hours after creation and can be no later than 70 days after creation. `reusable` defaults to false, which permits one successful payment only; true requests a reusable link. `returnUrl` is marked optional and, when supplied, shows a Continue button for shopper-selected redirection. A 422 example says “Return URL is missing,” an unresolved conflict with that optional mark; do not generalize the example into a universal requirement.
- Conditional request fields include `lineItems` for listed buy-now-pay-later methods, `shopperName` for certain methods or PayPal Seller Protection, `recurringProcessingModel` when `storePaymentMethodMode` is `askForConsent` or `enabled`, and specified phone data for Visa/JCB 3DS authentication without shopper email. `requiredShopperFields` can request named fields on the hosted page. The metadata table gives 20-pair/20-character-key limits and reserved `checkout.linkId` behavior.
- The `201` response identifies the link with `id`, gives its shopper-facing `url`, and includes a link `status` such as `active`, `expired`, `completed` or `paymentPending`. `paymentPending` denotes an unfinished asynchronous shopper flow. This response is link creation, not payment authorization, manual capture or settlement; even a link status should not be collapsed into those financial events. The page lists 400, 401, 403, 422 and 500 error schemas/examples, which are request/error outcomes rather than payment results.
- The captured `latest` URL displays a test v72 server. It does not establish current latest version, live merchant eligibility or any actual link/payment execution. Related GET/PATCH routes have separate contracts; this page alone supplies no detail for their behavior.

## Detail locators

- Purpose and displayed server: raw lines 5–12. Header: 16–19.
- Request schema: 22–222; core fields 26–28, 173, 181; expiry/reuse/return 71, 183–184; conditional fields 145, 175, 180, 182, 192, 209–220. Request example: 224–256.
- Response 201 schema: 257–466; link identity 380, statuses 449, URL 466. Error schemas: 469–536. Response and error examples: 538–640, including 422 return-URL tension at 616–627.

## Related

- [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-api]] — broader API integration guide with webhook, reuse and forced-expiry routes.
- [[adyen-unified-commerce]] — provider concept and reciprocal source route.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/paymentLinks/2026-09-15|Checkout API POST /paymentLinks snapshot (2026-09-15)]]
