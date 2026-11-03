---
title: "PATCH /transferInstruments/{id} — Update a transfer instrument | Adyen Legal Entity Management API"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/patch/transferInstruments/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/patch/transferInstruments/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management-api, transfer-instrument, bank-account, api-reference]
---

## Overview

This 2026-11-03-captured Legal Entity Management API `/lem/v4` reference updates a transfer instrument identified by path `id`. It lists the TEST server `https://kyc-test.adyen.com/lem/v4`, and separately states live and test request-rate limits; the capture does not give a live server URL or establish account-specific access. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The required path `id` is the transfer-instrument ID. The request table marks `bankAccount`, `legalEntityId` (the owning legal entity), and `type=bankAccount` required. Within `bankAccount`, `accountIdentification`, `accountType`, `bankName`, and `countryCode` are optional in this table. The example supplies IBAN identification, but does not make IBAN mandatory or establish accepted identification variants. No query parameter or endpoint-specific idempotency key is listed.
- The optional `x-requested-verification-code` header can use `0_0001` to resolve suberrors associated with the transfer instrument, and requested verification codes are TEST-only. The page states 700 requests per 5 seconds in live, 200 per 5 seconds in test, and 5 failed requests per 10 seconds.
- A `200` means the update request succeeded and returns required `bankAccount`, `id`, `legalEntityId`, and `type`. Optional response material includes `bankAccount.trustedSource`, `capabilities`, `documentDetails`, and `problems`. Capability fields are for supporting entities: `allowed`, `requested`, and `verificationStatus` are distinct, and the response defines `pending`, `invalid`, `valid`, and `rejected` verification states. The schema says an allowed supporting entity may be usable even if the parent legal entity is not allowed because other supporting entities failed verification; that does not imply every capability or instrument is approved.
- The listed error classes are `400`, `401`, `403`, `422`, and `500`, with optional fields in their error bodies. A successful update or returned bank-account data is not independent proof of verification approval, capability enablement, transfer execution, payout, settlement, or bank receipt. The reference gives no update propagation timing or version/conflict rule.

## Detail locators

- Purpose, rate limits and TEST server: raw lines 5–18.
- Path, optional TEST-only header, required body and IBAN example: raw lines 20–59.
- `200` response, bank-account metadata, supporting-entity capabilities, documents and problems: raw lines 60–105.
- Error classes/bodies and response example: raw lines 108–189.

## Related

- [[adyen-platforms]] — platform resource and verification context.
- [[source-adyen-docs-platforms-manage-transfer-instruments]] — separate management guide for transfer-instrument lifecycle.
- [[source-adyen-docs-platforms-verification-overview-capabilities]] — separate capability and verification context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/patch/transferInstruments/(id)/2026-11-03|PATCH transfer instrument captured 2026-11-03]]
