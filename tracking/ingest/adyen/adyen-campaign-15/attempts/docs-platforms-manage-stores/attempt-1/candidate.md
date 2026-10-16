---
title: "Adyen Platforms manage stores"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-stores"
raw_files:
  - "adyen/docs/platforms/manage-stores/2026-09-15.md"
tags: [adyen, platforms, stores, payment-routing]
---

## Overview

This 2025-06-19-modified Adyen for Platforms guide, captured 2026-09-15, covers creating, viewing and updating a platform user's **store** through Customer Area or Management API. A store is linked to the user's **legal entity through business lines** and is associated with a merchant account; its own ID, merchant-account-scoped reference, status, shopper statement and optional split configuration have separate roles. A store resource or active status does not establish a verified account holder, enabled payment methods, live eligibility or successful transaction. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The guide says a payment processed through the user's store can be split across platform balance accounts, including the liable balance account, either per payment or through an optional store-linked split configuration profile. This describes routing/configuration choices, not proof that a split or payout occurred. The store ID is Adyen-wide unique, while an optional store reference is unique only within its merchant account; the ID is needed for updates, and the reference is used to route Checkout payment/payment-method requests to a store.
- Store status is **active** on creation under the guide's model. **Inactive** blocks new transactions but still permits capture of outstanding ones; reactivation reverses that restriction. **Closed** requires first changing to inactive and cannot be reopened. These are consequential store-state rules, distinct from account-holder capability or KYC verification status.
- Customer Area creation is available by default for platforms using **onboarding on invite**; others must contact an Adyen representative to activate that feature. It requires **Merchant POS terminal management admin**. A new store's country/region must already be associated with the account holder; otherwise the guide says create another account holder. Use a business line for the industry-code/sales-channel combination. eCommerce needs a contact phone; POS needs address and phone. The Customer Area presents country/region-based default payment methods for review and edit, not an assurance every method is enabled or usable.
- Management API creation needs credentials with **Management API-Stores read and write**, the merchant account ID and business-line context, plus store address/phone and shopper-statement details. Its POST table marks address, description, merchantId, phoneNumber and shopperStatement as required; businessLineIds becomes required when the merchant account has multiple business lines and only one is permitted. The merchant-scoped POST alternative omits merchantId from the body. These are the page's captured API-guide conditions, not proof of current schema or account authorization.
- Viewing in Customer Area requires **Balance platform base role**; the API route requires **Management API-Stores read**. Updates require the Customer Area admin role or API read/write role. The optional **Change payment methods** role is described for access to transaction descriptions. PATCH is partial; an empty address line can remove that line, but the **country cannot be changed**. The guide lists updateable business line, split configuration, contact/location and status fields; permanent closure remains irreversible.
- The examples use test endpoints and dated SDK versions. Linked payment-method and route-payment pages are next-step navigation; this page is no live operation, seller-of-record determination, region-eligibility decision or payment outcome evidence.

## Detail locators

- Store/legal-entity/business-line relationship, splits, identity and statuses: pinned raw lines 15–41.
- Customer Area creation enablement, roles, country/sales-channel conditions and default payment methods: pinned raw lines 43–90.
- Management API creation roles, merchant/business-line IDs and parameter table: pinned raw lines 92–130.
- View roles and Customer Area/API differences: pinned raw lines 132–157.
- Update roles, partial PATCH, country immutability and closure: pinned raw lines 159–254.
- Illustrative test SDK/address response and linked next steps: pinned raw lines 254–540.

## Related

- [[adyen-platforms]] — provider Platforms hub for distinct platform-user, legal-entity, account-holder and store resources.
- [[adyen-account-structure]] — company/merchant account hierarchy; this store is linked through a platform user's business line and merchant account.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-stores/2026-09-15|Adyen Manage stores, captured 2026-09-15]]
