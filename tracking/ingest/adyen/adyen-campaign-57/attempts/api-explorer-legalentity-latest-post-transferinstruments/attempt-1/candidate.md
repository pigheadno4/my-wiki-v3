---
title: "Adyen Legal Entity Management API v4: create a transfer instrument"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/transferInstruments/2026-09-15.md"
tags: [adyen, legal-entity-management, transfer-instruments, verification, api-reference]
---

## Overview

Captured Legal Entity Management API reference for `POST /transferInstruments` on the listed test `lem/v4` server. A transfer instrument is a bank account owned by a legal entity. Creating its resource is distinct from Adyen's verification checks: only after the instrument passes those checks does the page say funds can be sent from the balance platform to it. Verification results are communicated by webhooks or API responses. See [[adyen]], [[adyen-platforms]], and [[adyen-payouts]].

## Key takeaways

- The request-property table marks `bankAccount`, `legalEntityId`, and `type` required; the only listed `type` is `bankAccount`. `legalEntityId` names the owner, not a merchant account or source balance account (raw lines 32–41). The table marks nested `accountIdentification`, `accountType`, `bankName`, and `countryCode` optional, and does not separately state request-body requiredness.
- Three examples show IBAN, UK local account-number/sort-code, and US local account-number/routing-number identification (lines 43–87). The page does not provide a complete country/type-required-fields matrix for bank identification; example values should not be promoted into universal requirements. The US response example adds `accountType: checking` even though its request example omits it (lines 74–86, 246–269).
- The `200` response says the request succeeded and includes instrument `id`, owning `legalEntityId`, bank account and type. Optional `capabilities` and `problems` report verification state/errors; `verificationStatus` can be `pending`, `invalid`, `valid`, or `rejected` (lines 88–133). The EUR and US examples show `sendToTransferInstrument` requested but not allowed while verification is pending; the UK example omits capabilities (lines 200–270). A created ID or `200` is not verification approval or payout eligibility.
- Rate limits are listed as 700 requests per five seconds live, 200 per five seconds test, plus five failed requests per ten seconds (lines 13–19). The optional `x-requested-verification-code` header is test-only and takes one suberror code at a time (lines 24–29). Documented errors are `400`, `401`, `403`, `422`, and `500` (lines 136–198); the page does not name a specific permission role or guarantee live access.

## Detail locators

- Request schema and examples: raw lines 32–87. Response schema and verification fields: lines 88–133. Error schema: lines 136–198. Response examples: lines 200–270.

## Related

- [[adyen-platforms]] — platform legal-entity and verification context.
- [[adyen-payouts]] — payout lifecycle is separate from instrument creation.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/transferInstruments/2026-09-15|POST /transferInstruments API reference, captured 2026-09-15]]
