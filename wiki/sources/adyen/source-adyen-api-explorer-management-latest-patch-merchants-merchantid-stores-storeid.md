---
title: "PATCH /merchants/{merchantId}/stores/{storeId} — update a store | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(storeId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(storeId)/2026-11-03.md"
tags: [adyen, management-api, point-of-sale, stores, store-status]
---

## Overview

This 2026-11-03-captured [[adyen]] Management API store-update reference describes `PATCH /merchants/{merchantId}/stores/{storeId}` on the listed TEST `https://management-test.adyen.com/v3` server. The API credential needs the **Management API—Stores read and write** role, and both the merchant-account ID and the Adyen store ID are required path parameters. The operation updates only some store parameters. See [[adyen-pos-store-management]]. [Raw: lines 5–24]

## Key takeaways

- The request-body table marks `address`, `businessLineIds`, `description`, `externalReferenceId`, `phoneNumber`, `splitConfiguration`, `status` and `subMerchantData` optional. It does not mark the whole body as required. A store's country cannot be updated. Within an address, `stateOrProvince` is required for Australia, Brazil, Canada, India, Mexico, New Zealand and the United States. [Raw: lines 27–45]
- `externalReferenceId` is required for a Brazil CNPJ in the stated format, optional for France SIRET (up to 14 digits) and Australia Zip (up to 50 digits). The documented phone input is E.164 with country code, with conversion and validation if a different format is passed. `splitConfiguration` names separate balance-account and split-profile IDs; those settings describe booking rules, not a completed split or payment. [Raw: lines 37–43]
- `subMerchantData` is an optional parent for registered payment facilitators transacting on standalone terminals, but its `email`, scheme-facing `id`, four-digit `mcc` and `name` are marked required within it. Its `id` is created by the caller and is distinct from the path's Adyen store ID; the field table gives length/format limits and says `name` overwrites the shopper statement on the card statement. [Raw: lines 45–49]
- Status starts `active` on creation. This PATCH permits `active` → `inactive`, and `inactive` → `active` or `closed`. An inactive store blocks new transactions while captures of outstanding transactions remain possible. Closing is irreversible and reassigns its terminals to merchant inventory, where they cannot process payments. The page does not specify when every device reflects the change. [Raw: lines 44, 120]
- A `200` is a succeeded request with a store response whose fields include optional store/merchant IDs, address, business-line IDs, references, status, split configuration and sub-merchant data. The response table marks `address.country` required within an optional address and describes business-line fallback/conditional multiplicity; these response statements do not override the request table's optional top-level fields. A separate `204` says processing succeeded with no additional content. Neither response proves terminal boarding, payment authorization, capture settlement or bank receipt. [Raw: lines 88–129]
- The page lists `400`, `401`, `403`, `422` and `500` errors with structured problem fields, and links to live rate limits without stating a number. It gives no idempotency, retry or propagation guarantee. [Raw: lines 13, 132–229]

> [!warning] Contradiction
> The listed TEST server uses `/v3`, while all three `200` response examples put a `/v1/stores/` URL in `_links.self.href`. The snapshot does not reconcile those versions; an example link is not proof of the endpoint's v3 route or current live behavior. [Raw: lines 15–16, 235–320]

## Detail locators

- Credential role, environment and required path IDs: raw lines 5–24.
- Request fields, conditional children and status transition rules: raw lines 27–49.
- Three request examples: raw lines 51–85.
- `200` response fields, nested requiredness and separate `204`: raw lines 86–129.
- Error statuses and problem-body fields: raw lines 132–229.
- Three `200` examples and their `/v1/stores/` self links: raw lines 231–323.

## Related

- [[adyen-pos-store-management]] — primary store administration concept
- [[adyen-terminal-management]] — terminal assignment and boarding context

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(storeId)/2026-11-03|Management API store PATCH — captured 2026-11-03]]