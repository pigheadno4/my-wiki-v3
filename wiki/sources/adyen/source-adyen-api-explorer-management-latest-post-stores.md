---
title: "Adyen Management API POST /stores — create store"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/stores"
raw_files:
  - "adyen/api-explorer/Management/latest/post/stores/2026-09-15.md"
tags: [adyen, management-api, stores, point-of-sale]
---

## Overview

This 2026-09-15 Management API Explorer capture documents `POST /stores` on the `/v3` test server. It creates a store under the request's `merchantId`, with the `Management API—Stores read and write` credential role. The page flags live-environment rate limits without giving their values. The store resource is distinct from its merchant account and any assigned terminal.

## Key takeaways

- The request property table requires `address`, `description`, `merchantId`, `phoneNumber` and `shopperStatement`. Within `address`, `country` is required and `stateOrProvince` is additionally required for Australia, Brazil, Canada, India, Mexico, New Zealand and the US. `businessLineIds` becomes required if the merchant has multiple business lines; otherwise the merchant account's business line is used. `externalReferenceId` is required for Brazil CNPJ and optional for the stated France/Australia uses.
- Optional `reference` is the store code with a restricted character set; if omitted, it is populated with Adyen's generated `id`. This endpoint page does not state a uniqueness scope for that reference. `shopperStatement` has a 22-character maximum and cannot be all digits. Japan local shopper statements require both listed scripts when localized information applies. Optional split configuration and registered payment-facilitator sub-merchant data have their own field conditions; consult `## Parameters`.
- A 200 response schema includes optional generated `id`, merchant ID, address, reference and `status`. The status description says new stores are assigned `active` automatically; `inactive` blocks terminals from new transactions while outstanding capture remains possible, and irreversible `closed` reassigns terminals to merchant inventory. Creating an active store alone does not establish terminal assignment, boarding, payment methods or successful payment processing.
- The success example's self link uses `/v1/stores` despite the `/v3` server. Its example values are illustrative and do not prove live store existence. Listed errors are 400, 401, 403, 422 and 500; this capture gives no detailed live rate limit, propagation timing or current `latest` version.

## Detail locators

- `## Parameters` → request requiredness, conditional country/business-line/external-reference fields, store code, localized statement, split and sub-merchant fields.
- `## Request examples` → illustrative US store request.
- `## Responses` → 200 store fields/status effects and generic error schemas.
- `## Response examples` → illustrative 200 payload and `/v1` self-link mismatch.

## Related

- [[adyen]] — provider.
- [[adyen-pos-store-management]] — store lifecycle and terminal readiness context.
- [[adyen-account-structure]] — merchant/store hierarchy.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/stores/2026-09-15|2026-09-15 captured API Explorer reference]]
