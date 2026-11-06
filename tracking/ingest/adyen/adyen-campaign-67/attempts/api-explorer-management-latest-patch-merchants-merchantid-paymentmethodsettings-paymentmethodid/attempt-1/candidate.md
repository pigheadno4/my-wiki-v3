---
title: "Update merchant payment-method settings | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/2026-11-05.md"
tags: [adyen, management-api, payment-methods, merchant-configuration]
---

## Overview

This 2026-11-05-captured Management API reference describes `PATCH /merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}`: it updates settings for the payment method identified by `paymentMethodId` under the merchant account identified by `merchantId`. Both are required path IDs. The listed server is TEST `https://management-test.adyen.com/v3`, and the caller's API credential needs **Management API—Payment methods read and write**. The endpoint configures a merchant payment method; it is not a Checkout payment request. See [[adyen]] and [[adyen-payment-method-variants]].

## Key takeaways

- The request table marks all its listed top-level fields optional, including `countries`, `currencies`, `enabled`, `storeId`/`storeIds` and the method-specific objects. The introduction says an additional object may be required depending on the method type; table-level optionality must therefore be read with type-specific prose. For example, `ebt.fnaNumber` is marked required within optional `ebt`, and the `jcb` description says Japan merchants need `midNumber`, `reuseMidNumber` and `serviceLevel`. The table does not independently declare whole-body requiredness. The sample with `EUR` and `NL` is illustrative, not an availability promise.
- Omitted `countries` and `currencies` default to all values the particular payment method supports. For transaction descriptions, the method-specific text says they cannot be configured in TEST; it recommends at most 22 characters because banks may truncate longer strings, which is guidance rather than a universal hard validation limit. `affirm.pricePlan` defaults to `core` when no selection is made. The full method-specific property catalog and conditions are in the raw request table.
- A `200` reports request success and can return `id` (marked required), `type`, `enabled`, scope, countries/currencies and method-specific details. Optional `associatedPaymentMethods` identifies other methods updated in an associated transition. Optional `allowed` is set true by Adyen after merchant screening, and optional `verificationStatus` has `valid`, `pending`, `invalid` and `rejected` values. Neither field is an input to this PATCH, and an `enabled` value does not by itself establish screening approval or a successful payment. `204` reports successful processing with no additional content.
- `400`, `401`, `403`, `422`, `429` and `500` error responses are listed. The page states no idempotency, later propagation, payment authorization, capture, settlement or bank-receipt guarantee. A returned configuration or optional status must be read at this snapshot's TEST scope.

> [!warning] Contradiction
> The introduction refers to the payment method `type` in the request and a type-dependent additional object, but the PATCH request-body table contains no top-level `type` property; `type` appears in the response table. The capture does not resolve whether a request type is accepted or needed. The required path `paymentMethodId` remains the documented target identifier.

## Detail locators

- Raw lines 5–23: update purpose, conditional type statement, caller role, TEST server and path IDs.
- Raw lines 26–129: request property table, method-specific conditions, defaults and transaction-description qualifications; lines 131–143: `EUR`/`NL` request example.
- Raw lines 146–346: `200` response schema, especially `allowed` (164), associated updates (173–176), `enabled` (222), `id` (235) and verification status (333); lines 349–350: `204`.
- Raw lines 353–469: error schemas; lines 471–495: illustrative `200` response.

## Related

- [[adyen-payment-method-variants]] — method-variant identity and account setup boundaries.
- [[adyen-online-payments]] — separate payment integration context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)/2026-11-05|2026-11-05 merchant payment-method settings PATCH reference]]