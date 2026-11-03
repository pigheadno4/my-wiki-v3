---
title: "Adyen Management API v3: get a store"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/stores/(storeId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/stores/(storeId)/2026-11-03.md"
tags: [adyen, management-api, pos, stores]
---

## Overview

This 2026-11-03-captured Management API reference documents `GET /stores/{storeId}`, a role-gated read of the store identified by the required path `storeId`. The listed TEST server is `https://management-test.adyen.com/v3`; the API credential needs **Management API—Stores read** or **Management API—Stores read and write**. It notes live rate limits without stating values. See [[adyen]] and [[adyen-pos-store-management]].

## Key takeaways

- A `200` response can return the Adyen-generated store `id`, owning merchant-account `merchantId`, human-readable `reference` (store code), `address`, `businessLineIds`, `externalReferenceId`, localized/shopper statements, `splitConfiguration`, `subMerchantData`, and `_links`. The response table marks top-level fields optional; nested fields marked required apply within their objects. Conditions in the response descriptions, such as multiple merchant business lines, country/state requirements, Brazil CNPJ and Japan scripts, do not add request parameters to this GET.
- `splitConfiguration.balanceAccountId` identifies a balance account to which a split amount must be booked depending on separate split logic; `splitConfigurationId` identifies the profile. These are configuration references, not evidence that a payment was split or booked. `subMerchantData` is scoped to registered payment facilitators transacting on standalone terminals.
- Optional `status` can be `active`, `inactive` or `closed`. The page says active is assigned on store creation; inactive blocks terminals under the store from new transactions while outstanding captures remain possible; closed is irreversible and reassigns those terminals to merchant inventory. A readback does not change status or establish terminal assignment, boarding, payment-method availability, payment execution or financial finality.
- The reference lists `400`, `401` authentication, `403` permissions, `422` validation and `500` server errors with problem-body fields. It does not state idempotency, mutation/propagation or asynchronous approval semantics for this read.

> [!warning] Contradiction
> The listed TEST server is `/v3`, but the `200` example's `_links.self.href` points to `/v1/stores/...`. The example does not establish the v3 route's returned link shape; use the listed server and endpoint contract, and treat that link as illustrative.

## Detail locators

- Raw lines 5–25: purpose, credential roles, live-limit note, v3 TEST server and required store ID.
- Raw lines 27–66: response identity, merchant/business-line associations, conditional descriptions, split/sub-merchant fields and status effects.
- Raw lines 69–166: errors and problem response schema; lines 168–195: illustrative `200` example and `/v1` self-link conflict.

## Related

- [[adyen-pos-store-management]] — store administration and lifecycle context.
- [[source-adyen-api-explorer-management-latest-get-stores]] — paged store list reference.
- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-automate-store-management]] — broader automation guide.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/stores/(storeId)/2026-11-03|2026-11-03 GET store reference]]