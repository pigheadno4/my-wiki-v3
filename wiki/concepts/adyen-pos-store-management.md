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

- [[source-adyen-docs-point-of-sale-what-we-support-payment-methods-add-payment-methods]] — Adyen 2026-09-15 POS Customer Area request guide, asynchronous store method addition, Management webhook, and terminal configuration timing.


- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure]] — Adyen Docs guide to company/merchant/store hierarchy, settlement and reporting trade-offs, terminal assignment, and Customer Area store creation (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-automate-store-management]] — 2026-09-15 Adyen POS Management API guide for store retrieval, creation, updates, status changes, and payment-method settings, identity, and status changes.
