---
title: "Adyen Management API v3: update a store"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/stores/(storeId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/stores/(storeId)/2026-11-03.md"
tags: [adyen, management-api, point-of-sale, stores]
---

## Overview

This captured Management API v3 reference describes `PATCH /stores/{storeId}`: update supported parameters of the store identified by the required, unique path `storeId`. The listed server is `https://management-test.adyen.com/v3`. The API credential needs the **Management API—Stores read and write** role; the page flags Live rate limits without giving a numeric limit. See [[adyen-pos-store-management]] and [[adyen]].

## Key takeaways

- Request body fields are optional at the top level. Supported fields include address details (country cannot be changed), business-line IDs, description, external reference, phone number, split configuration, status, and standalone-terminal registered-payment-facilitator `subMerchantData`. If `subMerchantData` is provided, its email, ID, MCC and name are required within that object. The address's `stateOrProvince` is marked optional in the table but described as required for seven listed countries. The external reference has conditional country/payment-method uses and formats.
- `status` permits active → inactive and inactive → active or closed. Inactive blocks new transactions while outstanding captures can still occur. Closing reassigns terminals to merchant inventory and is irreversible; it is not a reversible pause. A 200 store response is not terminal boarding, payment-method readiness, a successful transaction, split booking, or payout.
- The 200 response schema includes store, merchant, address, business-line, status and optional split/sub-merchant fields. `businessLineIds` defaults to the merchant-account business line when unspecified and is required when multiple business lines exist under that account, according to the **response** description; the request field itself is marked optional. The response examples' `self.href` uses `/v1/stores/` while this reference lists a `/v3` server; do not use the example as v3 route evidence.

## Detail locators

- Purpose, role, Live limit notice, TEST server and path: raw lines 5–24.
- Request schema and conditional fields: raw lines 27–49; three illustrative requests: lines 51–85.
- 200 response schema and status effects: raw lines 86–125.
- Error contracts: raw lines 128–225 (400, 401, 403, 422, 500). The error schema's `requestId` analogy to `pspReference` does not make this a payment response.
- Illustrative 200 responses and older-version `self.href`: raw lines 227–289.

## Related

- [[source-adyen-api-explorer-management-latest-post-stores]] — store creation.
- [[adyen-pos-store-management]] — store administration and terminal-readiness context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/stores/(storeId)/2026-11-03|PATCH /stores/{storeId} captured 2026-11-03]]