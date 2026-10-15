---
title: "Retrieve stored details | Adyen Classic API"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/retrieve-stored-details"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/retrieve-stored-details/2026-09-15.md"
tags: [adyen, classic-api, tokenization, recurring-payments, stored-payment-methods]
---

## Overview

This Adyen Classic API guide describes using Recurring API `/listRecurringDetails` to retrieve stored payment-detail records and their `recurringDetailReference` after details were stored with an `/authorise` call. The reference identifies a stored detail for later requests. The page marks the endpoint inactive and unsupported for new integrations; it directs new builds to Checkout API and existing integrations to contact Adyen about migration.

## Key takeaways

- The request supplies the merchant account and the `shopperReference` for a shopper whose details were previously stored. The page's test cURL example authenticates with an API key; the shopper reference selects the shopper record, while `recurringDetailReference` is the stored-detail identifier returned for later use.
- When stored details exist for that shopper reference, the response contains one or more `RecurringDetail` objects, with fields that may be missing or nil depending on payment method. A nonexistent shopper reference returns an empty object; for an existing shopper reference with a specified contract type but no matching recurring detail, the response omits the `details` array.
- The JSON and SOAP responses are examples, including card-display and shopper-related fields; they do not establish that every response has those fields or that the example's identifier, contract types, and payment method apply to other shoppers.
- This retrieval guide does not itself describe the consent or initial storage flow. The separate Classic storage guide and modern Checkout tokenization guidance have their own conditions; this page should not be used to infer that consent is unnecessary or that Classic references have the same scope as Checkout tokens.

## Detail locators

- Raw lines 16–23 — inactive Classic lifecycle, migration guidance, and reason for retrieving a `recurringDetailReference`.
- `Request` — `/listRecurringDetails` inputs; JSON, SOAP, cURL and version-labeled library examples. The cURL example uses test Recurring API v25 and an API-key header.
- `Response` — presence and absence cases, optional fields, Recurring API response-schema link, and illustrative JSON/SOAP payloads.
- `Next steps` — Classic recurring authorization, update, and disable routes.

## Related

- Company: [[adyen]]
- Concept: [[adyen-tokenization]]
- Related source: [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-store-payment-details]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/retrieve-stored-details/2026-09-15|2026-09-15 snapshot — Classic retrieve stored details]]
