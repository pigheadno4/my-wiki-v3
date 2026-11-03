---
title: "Adyen Management API v3: get a merchant account"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/2026-11-03.md"
tags: [adyen, management-api, merchant-accounts, api-access]
---

## Overview

This 2026-11-03 [[adyen]] Management API reference describes `GET /merchants/{merchantId}` for the merchant account identified by the required path string `merchantId`. The calling API credential must have access to that merchant account and the `Management API—Account read` role. The captured server is `https://management-test.adyen.com/v3`; the page does not give a live server URL. Merchant-account readback does not create or activate the account or prove a payment, payout or bank receipt. [[adyen-account-structure]]

## Key takeaways

- The path ID identifies the merchant account, distinct from optional response `companyId` (its parent company account), `id` (returned merchant ID), `reference`, and the legal-entity name/city fields. No query parameter or request body is documented.
- A `200` says the lookup succeeded. The response table makes `_links` optional but marks `_links.self` required within it; `apiCredentials`, `users` and `webhooks` links are optional. Other optional fields include `captureDelay`, `defaultShopperInteraction`, `description`, data centers and live prefixes, company and merchant IDs, legal-entity name/city, pricing plan (partner-managed accounts only), primary settlement currency, reference, shop URL and `status`. The `description` maximum is 300 characters; the described capture-delay choices are Immediate, Manual or 1–29 days. For test requests, `livePrefix` is empty and `default` is the data-center name. These are returned settings, not evidence that a payment was captured or settled.
- The status definitions distinguish `PreActive` (created, no Customer Area access or payment processing), `Active` (Customer Area access; processing and payouts enabled only if the company account is also Active), `InactiveWithModifications` (no new payments, but modifications such as refunds and payouts remain possible), `Inactive` (processing and payouts disabled), and irreversible `Closed` (no login, processing or payouts). A returned status does not report a particular transaction or actual bank receipt.
- The page also lists `204` success with no additional content, and `400`, `401`, `403`, `422` and `500` error forms. This GET has no documented update, activation action, idempotency contract, propagation timing, review decision or reversal for a state transition.

> [!warning] Contradiction
> The captured server is `/v3`, but the `200` example's `self`, API-credential, user and webhook `href` values use `/v1`. The response table capitalizes `Manual` for `captureDelay`, while the example uses `manual`. Treat those example values as illustrative; the snapshot does not reconcile their version or case.

## Detail locators

- **Purpose, credential scope/role and test server:** raw lines 5–14.
- **Required path ID:** raw lines 16–21.
- **Response fields, nested requiredness, limits and status conditions:** raw lines 23–54.
- **204 and error forms:** raw lines 57–158.
- **Illustrative merchant and conflicting v1 links/capture-delay case:** raw lines 160–190.

## Related

- [[adyen-account-structure]] — company and merchant account hierarchy.
- [[adyen-api-access]] — credential roles and account scope.
- [[source-adyen-api-explorer-management-latest-get-merchants]] — credential-scoped merchant list.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/2026-11-03|Management API v3 merchant-account GET — collected 2026-11-03]]