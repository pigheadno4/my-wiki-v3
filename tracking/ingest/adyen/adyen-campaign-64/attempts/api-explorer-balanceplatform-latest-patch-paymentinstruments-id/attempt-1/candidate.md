---
title: "Adyen Balance Platform API v2: Update a payment instrument"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/paymentInstruments/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/paymentInstruments/(id)/2026-11-02.md"
tags: [adyen, platforms, balance-platform, issuing, payment-instruments, api-reference]
---

## Overview

Captured Balance Platform API v2 TEST `PATCH /paymentInstruments/{id}` reference for updating an identified payment instrument. Its principal rule is status-only updates once an instrument is active; cards created inactive may also change their associated balance account. This [[adyen]] [[adyen-platforms]] resource operation does not itself authorize a payment or move funds.

## Key takeaways

- The path requires payment-instrument `id`; the listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. Request `balanceAccountId`, `card`, `status`, `statusReason`, and `statusComment` are table-optional, subject to the operation's lifecycle constraints. `balanceAccountId` can change only while the instrument is inactive. Once active, only status can be updated.
- The optional `card` parent includes fields marked required within the card object, including `brand`, `brandVariant`, `cardholderName`, and `formFactor`; optional nested `configuration` has required `configurationProfileId`, and optional `deliveryContact` has required address/name. These nested markers do not make the parent `card` required for every PATCH, nor override the active-status restriction. Card authentication is described as required for specified EEA/UK online or wallet-capable cards; the raw gives OTP phone and password constraints at the detailed locators.
- `status` may be active, inactive, suspended, or permanently closed; closure cannot be undone. The status description's default active, with physical-US-card exception, applies when *creating* a payment instrument, not to an omitted PATCH status. If `statusReason` is `other`, send `statusComment`. Request and response status-reason enumerations differ: response additionally lists `transactionRule`; use the request enum for this PATCH input.
- A 200 says the update request succeeded and returns instrument `id`, associated `balanceAccountId`, `issuingCountryCode`, and `type` as required fields. Optional bank-account/card objects and statuses describe resource state. The card response schema notes that CVC is returned only in the POST response for single-use virtual cards; PAN is masked by default and returned only for single-use virtual cards. The masked PAN in this PATCH example does not establish access to full PAN/CVC here.

> [!warning] Contradiction
> The operation prose and `balanceAccountId` field limit balance-account reassignment to **inactive** instruments (raw lines 7, 23), but the generic 422 example says it can change when status is `Inactive or Requested` (lines 344–355). `Requested` is not among this PATCH request's status values (line 59). Treat the example as conflicting generic error evidence, not an additional permitted state.

## Detail locators

- Operation, TEST server, path/body and lifecycle rules: pinned raw lines 5–61. Card nesting, authentication, physical-card and status constraints: lines 24–61. Request examples: lines 63–77.
- Success response fields, optional card/bank-account details and POST-only CVC note: lines 78–149. Success examples: lines 251–303. Error schemas and generic examples: lines 152–249 and 305–369.

## Related

- [[adyen-platforms]] — platform instrument and balance-account context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/paymentInstruments/(id)/2026-11-02|Pinned 2026-11-02 API reference]]
