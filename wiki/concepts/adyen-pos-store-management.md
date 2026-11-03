---
title: "Adyen POS Store Management"
type: concept
category: technology
tags: [adyen, point-of-sale, management-api, stores]
---

## Definition

Adyen POS store administration is distinct from Terminal API payment messaging. Merchants can create stores in the Customer Area, or automate store retrieval, creation, updates, status changes and payment-method settings through Management API. The two setup routes have their own credential and configuration requirements; see the respective source guides.

## Operational boundary

The POS Customer Area guide has the merchant account request additional payment methods, while adding a method to a store is asynchronous and can be reported by a Management `paymentMethod.created` webhook. After addition, the terminal picks up the method on its next configuration maintenance call or a manual update. A submitted request, a store webhook, and terminal readiness are distinct stages; the source gives no universal scheme or region availability. [[source-adyen-docs-point-of-sale-what-we-support-payment-methods-add-payment-methods]]


The 2026-09-15 Adyen guide uses a platform-unique store ID for store updates; a human-readable reference is unique only within its merchant account. In the Management API automation guide, new stores start active without payment methods, and terminals still need assignment and boarding to transact. Inactive stores block new transactions while outstanding captures remain possible. Closing requires an inactive store, moves its terminals to merchant inventory immediately, and cannot be undone; terminals must be reassigned and boarded to process again. See the source for credential roles, endpoint scope, regional fields, payment-method caveats, live rate limits, and versioned examples.

## Sources

- [[source-adyen-api-explorer-management-latest-patch-stores-storeid]] — 2026-11-03-captured Management API v3 TEST store-update reference for selected fields and irreversible closure; example self links use /v1, and a returned store does not establish terminal or payment readiness.

> [!warning] Contradiction
> This Management API reference lists a `/v3` TEST server while both 200 example store `self.href` links use `/v1/stores/`. The examples do not establish a v3 self-link route or the correct Live route.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-stores]] — 2026-11-03-captured Management API v3 TEST merchant-scoped store-creation contract, conditional fields and status effects; its 200 example uses a /v1 self-link despite the /v3 server, and an active store is not transaction proof.

> [!warning] Contradiction
> The pinned POST /merchants/{merchantId}/stores reference lists a TEST /v3 server, while its 200 response example self-link uses /v1/stores/. The example does not resolve which versioned route applies to a subsequent call. [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-stores]]


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-stores-storeid]] — 2026-11-03-captured Management API v3 TEST store PATCH by merchant/store IDs, with country fixed, role-gated updates and active/inactive/irreversibly closed transitions; a `200` store or bodyless `204` is not terminal or payment readiness.
> [!warning] Contradiction
> This operation lists a `/v3` TEST server but its `200` examples link to `/v1/stores/`; the captured page does not reconcile the version difference. [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-stores-storeid]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-stores]] — 2026-11-03-captured Management API v3 TEST, role-gated merchant-account store list with optional reference/page filters, counts and store status readback; listing does not establish terminal or payment readiness.

> [!warning] Contradiction
> This source lists a TEST v3 server but its example links use v1; its example's page count also conflicts with its last/next page links. Treat the example as illustrative, not a reliable v3 pagination contract.


- [[source-adyen-api-explorer-management-latest-get-stores-storeid]] — 2026-11-03-captured Management API v3 TEST store lookup by store ID, with merchant/business-line, split and status readback; status is not terminal or payment readiness, and the example self-link uses `/v1` despite the listed `/v3` server.

> [!warning] Contradiction
> The captured `GET /stores/{storeId}` reference lists the TEST `/v3` server, but its response example links to `/v1/stores/...`; the example does not resolve the route-version mismatch. [[source-adyen-api-explorer-management-latest-get-stores-storeid]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-stores-storeid]] — 2026-11-03-captured Management API v3 TEST merchant-scoped store GET with role gate, store status and optional configuration details; the v1 self link and spaced reference in its example conflict with the v3 server and reference character rule. Readback does not prove terminal or payment readiness.


- [[source-adyen-api-explorer-management-latest-post-stores]] — 2026-09-15-captured Management API v3 TEST store-creation contract for merchant-linked request, conditional address/business-line fields, automatic active status and irreversible closure effects; `/v1` example link does not prove v3 route behavior or terminal readiness.


- [[source-adyen-api-explorer-management-latest-get-stores]] — 2026-09-15-captured Management API v3 TEST store-list reference for role-gated merchant/reference filters, page counts and status descriptions; its example has v1/v3 path and page-count inconsistencies, and a read does not establish terminal or payment readiness.


- [[source-adyen-docs-point-of-sale-payment-facilitators]] — POS payment-facilitator guide (2026-09-15 snapshot) for sub-merchant store `subMerchantData`, Management API role and standalone store-only route; full commercial/data model belongs to [[adyen-pos-payment-facilitators]].


- [[source-adyen-docs-point-of-sale-what-we-support-payment-methods-add-payment-methods]] — Adyen 2026-09-15 POS Customer Area request guide, asynchronous store method addition, Management webhook, and terminal configuration timing.


- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure]] — Adyen Docs guide to company/merchant/store hierarchy, settlement and reporting trade-offs, terminal assignment, and Customer Area store creation (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-automate-store-management]] — 2026-09-15 Adyen POS Management API guide for store retrieval, creation, updates, status changes, and payment-method settings, identity, and status changes.
