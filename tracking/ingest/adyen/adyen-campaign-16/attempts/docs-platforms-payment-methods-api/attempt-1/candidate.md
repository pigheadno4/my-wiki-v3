---
title: "Adyen for Platforms: Manage payment methods with API"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/payment-methods/api"
raw_files:
  - "adyen/docs/platforms/payment-methods/api/2026-09-15.md"
tags: [adyen, platforms, payment-methods, management-api, account-holders]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes Management API requests to add, list, inspect and update payment-method settings for a user's store under a merchant account. It distinguishes a configured or enabled method from one the user's account holder can actually use. [[adyen]] [[adyen-platforms]]

## Key takeaways

- A platform first needs an Adyen online or in-person payments integration, a configured user store and business line, and a Management API credential with the Payment methods read and write role. The page calls for a payment-method webhook subscription and limits configuration to methods supported for the currency and integration. External factors can delay availability; the page says methods typically appear within a day and recommends requesting at least a day before opening, not a guaranteed activation time.
- POST `/merchants/{merchantId}/paymentMethodSettings` requests a method for a user's store, using the merchant account ID in the path and method `type`, `storeIds`, and `businessLineId` in the body. Optional countries and currencies can restrict supported coverage. Some methods need additional configuration. After Adyen enables a method, its variants are accepted by default; the Visa variant list is illustrative and is not proof of card-method eligibility on an account.
- Addition is asynchronous. The request response includes a payment-method ID; a `paymentMethod.created` Management webhook follows addition. If the account holder's `receivePayments` capability is not allowed, the user cannot use the method even when the method shows `enabled`. The page requires `receivePayments` to be enabled, allowed and verification-valid for availability, with `balancePlatform.accountHolder.updated` or GET `/accountHolders/{id}` as status routes. If the capability does not reach the stated states within 60 days, the activation request is automatically removed.
- GET list and GET detail routes inspect configured methods at merchant/store scope. PATCH can change countries, currencies or `enabled`. Disabled methods are automatically deleted after 90 days; closing a store automatically disables its linked methods and deletes them after 90 days. Updating a verified user's legal-entity or account-holder information may disable methods pending renewed verification.
- The examples use the test Management endpoint and version-specific server API libraries. They demonstrate request and response shapes, not a live method grant, a completed configuration change, an authorized payment, a split booking or payout. The guide does not assign merchant-of-record or legal-fund ownership.

## Detail locators

- Raw `Requirements` (lines 29–40): integration, credential role, webhook, supported-method and store/business-line prerequisites.
- Raw `Request payment methods` (lines 42–288): merchant/store/business-line request fields, countries/currencies, test endpoint and language-specific library examples.
- Raw `Payment method added`, `Payment method pending`, `Webhooks`, and `Troubleshooting` (lines 289–475): `allowed` versus `enabled`, verification status, 60-day request removal, asynchronous webhook and re-verification effect.
- Raw `Get a list of all payment methods` and `Get the details of a specific payment method` (lines 476–795): merchant/store-scoped read routes.
- Raw `Update a payment method` (lines 796–1039): PATCH parameters, 90-day deletion and update example.

## Related

- [[adyen-platforms]] — platform and user account context.
- [[source-adyen-docs-platforms-manage-stores]] — store configuration context.
- [[source-adyen-docs-platforms-verification-overview-capabilities]] — capability and verification-status context.
- [[source-adyen-docs-platforms-online-payments]] — separate split-booking and liable-account route.

## Raw Sources

- [[raw/adyen/docs/platforms/payment-methods/api/2026-09-15|Adyen Manage payment methods with API webpage snapshot (2026-09-15)]]
