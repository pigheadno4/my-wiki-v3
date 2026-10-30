---
title: "Adyen Management API v3: create a merchant account"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/2026-09-15.md"
tags: [adyen, management-api, merchant-accounts, account-structure]
---

## Overview

Captured Management API reference for `POST /merchants` on the listed test `/v3` server. The endpoint creates a merchant account under the company account identified by `companyId`; it is presented for integrations that require it, such as Adyen for Platforms Manage. Adyen contact setup and the **Management API—Accounts read and write** credential role are stated prerequisites. Creating this account is separate from live processing activation, payment-method configuration, or a successful payment. See [[adyen]], [[adyen-account-structure]], [[adyen-platforms]], and [[adyen-api-access]].

## Key takeaways

- The request-property table marks `companyId` required. For an Adyen for Platforms Manage integration, it additionally describes `businessLineId`, `legalEntityId`, and `pricingPlan` as required even though their general table rows say `No`; Adyen provides usable pricing-plan values (raw lines 20–29). The page does not separately state request-body requiredness.
- `reference` is generally optional. If Adyen configures a company-account reference template, `reference` becomes required and unique within that company; the template's format is 6–255 upper/lower-case letters, underscores and numbers. In that case the returned merchant `id` equals the submitted reference; otherwise Adyen generates the ID (lines 28, 54). The example has a reference and matching ID, but does not prove a template for every company (lines 31–42, 163–177).
- `200` says the request succeeded and describes the returned merchant-account fields; `204` says processing succeeded with no additional content (lines 43–61). The page does not describe a later activation or verification status. Error cases are `400`, `401`, `403`, `422`, and `500` (lines 64–161). The listed server is test `/v3`, and `latest` in the URL does not establish a live endpoint or current access.

## Detail locators

- Request fields and conditional requirements: raw lines 20–29. Request example: lines 31–42. Success schemas: lines 43–61. Error schemas: lines 64–161. Response example: lines 163–177.

## Related

- [[adyen-account-structure]] — company and merchant account hierarchy.
- [[adyen-platforms]] — conditional Platforms Manage context.
- [[adyen-api-access]] — credential and role boundaries.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/2026-09-15|POST /merchants API reference, captured 2026-09-15]]
