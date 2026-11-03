---
title: "POST /merchants/{merchantId}/stores — Create a store | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/stores"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/stores/2026-11-03.md"
tags: [adyen, management-api, stores, point-of-sale]
---

## Overview

This 2026-11-03 Management API reference describes `POST /merchants/{merchantId}/stores` on the listed `https://management-test.adyen.com/v3` server. It creates a store for the merchant account identified by required path `merchantId`. The API credential needs the `Management API—Stores read and write` role. The page flags live rate limits without stating values. The store, merchant account, optional business lines, balance account and split profile have distinct identifiers. See [[adyen]], [[adyen-pos-store-management]] and [[adyen-platforms]].

## Key takeaways

- The request-body table marks `address`, `description`, `phoneNumber` and `shopperStatement` required. Inside `address`, `country` is required; `stateOrProvince` is additionally required for Australia, Brazil, Canada, India, Mexico, New Zealand and the US. The page does not separately state whole-body requiredness.
- `businessLineIds` is optional when the merchant account has one business line, which is then used by default; it becomes required when the merchant has multiple business lines. `externalReferenceId` is required for Brazil CNPJ, with the stated format, and optional for France SIRET and Australia Zip. Optional `reference` is the store code; if omitted, Adyen populates it from the generated store `id`. `shopperStatement` is limited to 22 characters and cannot consist only of numbers.
- Optional `localizedInformation`, `splitConfiguration` and `subMerchantData` have nested conditions. Japan requires `ja-Hani` and `ja-Kana` local shopper statements when using the localized field. The split configuration can name a balance account and split profile; these settings are not evidence that any amount was split or booked. Registered payment facilitators using standalone terminals may supply sub-merchant data, whose listed children are required within that optional object.
- The page documents `200` with an optional store `id`, `merchantId`, `reference`, `status`, address and other store fields, and also lists `204` with no additional content. It says `active` is assigned automatically upon creation; `inactive` blocks terminals under the store from new transactions while outstanding captures remain possible, and `closed` is irreversible and reassigns those terminals to merchant inventory. A creation response does not itself show terminal assignment, payment-method activation, authorization, capture or settlement.
- Listed errors are `400`, `401` authentication required, `403` insufficient permissions, `422` validation and `500`. The reference does not state an idempotency contract, propagation timing, or an asynchronous approval step for store creation.

> [!warning] Contradiction
> The listed API server is `/v3`, but the `200` example's `_links.self.href` uses `/v1/stores/`. The example does not resolve the version mismatch or establish the route to use for subsequent calls.

## Detail locators

- Purpose, required credential role, live-limit notice and TEST v3 server: raw lines 5–16.
- Path merchant identity and request body, including conditional address, business line, tax-reference, local statement, split and sub-merchant fields: raw lines 18–54.
- Illustrative request: raw lines 56–75.
- `200` response fields and store status meanings: raw lines 76–115; bodyless `204`: lines 118–119.
- `400`, `401`, `403`, `422`, `500` schemas: raw lines 122–219. Illustrative `200` response and v1 self-link: lines 221–249.

## Related

- [[source-adyen-api-explorer-management-latest-post-stores]] — Separate company-scoped store creation reference with body `merchantId`.
- [[source-adyen-docs-platforms-manage-stores]] — Platform store-management guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/stores/2026-11-03|Pinned Adyen merchant-scoped store creation reference (2026-11-03)]]
