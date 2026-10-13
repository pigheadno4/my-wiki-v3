---
title: "Adyen Docs: Automate store management"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/automate-store-management"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/determine-account-structure/automate-store-management/2026-09-15.md"
tags: [adyen, point-of-sale, management-api, stores, payment-methods]
---

## Overview

Adyen's 2026-09-15 point-of-sale documentation snapshot explains how a POS integrator uses the Management API to retrieve, create, and update stores and to add or update a store's payment methods. Stores can also be managed manually in Customer Area. This page concerns merchant/store administration, not Terminal API payment messages or proof that an account is currently enabled. [[adyen]] · [[adyen-pos-store-management]]

## Key takeaways

- The stated prerequisites are an Adyen POS integration and an API credential/API key with Management API Stores read and read/write plus Payment methods read and read/write roles. A cloud-communications Terminal API integration may reuse its existing API key. Live store-related Management API endpoints have rate limits.
- A store's human-readable reference is unique within its merchant account, while Adyen generates a platform-unique store ID. Older stores without an assigned ID cannot be updated by PATCH under this snapshot. Use the unique store ID for updates, not a reference shared across merchant accounts.
- GET can list stores accessible to the API key or scope to a merchant account; POST can create under the account-level or merchant-level store route. Know the merchant account ID first. The merchant-level POST route takes that ID in the path rather than requiring it in the body.
- A new store is active but has no payment methods. Add methods individually through merchant payment-method settings; the resulting method ID is specific to the method/store combination. A listed Management API method may be web-only and unsupported by terminals. Assigning and boarding terminals is also needed for an active store to transact.
- Inactivating an active store blocks new transactions but permits capture of outstanding transactions and sets store transaction and Store-and-Forward limits to zero. Closure requires inactive first, immediately moves its terminals to merchant inventory, and cannot be reversed; terminals need reassignment and boarding before further transactions.

## Detail locators

- **Requirements and identity:** raw headings “Requirements” and “Store identification” (lines 28–47), including credential roles, live rate limits, reference scope, and legacy stores without IDs.
- **Status transitions:** “Opening and closing stores” (lines 49–57). Treat close as an irreversible operational change, not a reversible pause.
- **Retrieve:** “Get a list of stores” and “Get the details of a specific store” (lines 66–341). GET `/stores` returns stores accessible to the API key; GET `/merchants/{merchantId}/stores` scopes to a merchant. Reference filtering on the account-level route can return matches from multiple merchants; response pagination and example SDK calls are in raw.
- **Create:** “Create a store” (lines 518–547), with account-level POST `/stores` and merchant-level POST `/merchants/{merchantId}/stores`. Consult its field table for address and shopper-statement constraints, Japan-only localized information, and the Adyen for Platforms-only split configuration. Example payloads and test URLs in the following tabs are illustrations, not eligibility or live-operation proof.
- **Payment methods:** “Manage payment methods” (lines 1027–1050) and “Update a payment method” (lines 1464–1480). GET, POST, and PATCH use merchant payment-method-settings routes; the POST example's store ID belongs in the request body, whereas GET filtering uses a store ID query parameter. Inspect the raw for the exact body fields, business-line scope, and supported-method caveat.
- **Store PATCH:** “Update a store” (lines 1696–1722). PATCH `/stores/{storeId}` or `/merchants/{merchantId}/stores/{storeId}` takes only intended changes, including nested address fields; an empty `line3` is the page's removal example. The store country cannot be updated. The raw also limits `externalReferenceId` to Zip in this PATCH table and `splitConfiguration` to Adyen for Platforms merchants.
- The page links API Explorer “latest” endpoints and shows `management-test.adyen.com/v3` curl examples plus SDK examples with differing library versions. Verify current endpoint version, roles, and eligibility before implementation.

## Related

- [[adyen-pos-store-management]] — POS store and payment-method administration concept
- [[adyen-terminal-api]] — terminal messaging boundary
- [[adyen-api-access]] — general API credential and role scope

## Related raw API references

The linked API Explorer endpoints and linked account-structure, terminal-assignment, payment-method-variant, and rate-limit pages were not read for this entry; use them as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/determine-account-structure/automate-store-management/2026-09-15|Adyen Automate store management, fetched 2026-09-15]]
