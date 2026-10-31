---
title: "Adyen Classic Account API v6: create account holder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/createAccountHolder"
raw_files:
  - "adyen/api-explorer/Account/latest/post/createAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holders]
---

## Overview

Captured 2026-09-15 API Explorer reference for `POST /createAccountHolder` on the Classic Platforms Account API v6 test server (`https://cal-test.adyen.com/cal/services/Account/v6`). It creates a sub-merchant account holder in a platform; `accountHolderCode` identifies that holder, while an `accountCode` can identify a newly created account. This is a Classic account-holder/account contract, distinct from newer Platforms legal-entity and balance-account resources. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The request table marks `accountHolderCode`, `accountHolderDetails`, its `address`, and `legalEntity` required; the address has a required country. The code must be unique, 3–50 characters, using letters, digits or hyphens. `legalEntity` is Business, Individual or NonProfit. Business/NonProfit requires `businessDetails` with at least one shareholder; Individual requires `individualDetails`. A `phoneNumber` is required if `fullPhoneNumber` is absent. Conditional address and other nested requirements remain in the raw table.
- `createDefaultAccount` defaults to true, creating an account with default options unless changed. POS onboarding requires `storeDetails`. For a bank account supplied during creation, providing `bankAccountUUID` makes that bank-account creation fail while account-holder creation continues. Including `legalArrangementCode` in creation fails the request. These conditions make a successful holder response insufficient proof that every associated resource was created.
- The 200 response can contain `accountHolderCode`, new `accountCode`, `accountHolderStatus`, `invalidFields`, `resultCode`, `pspReference`, and verification data. Payout permission is separately represented by `payoutState.allowPayout`, which aggregates conditions including KYC and disablement; an illustrative `Active`/`allowPayout: true` response does not establish approval or payout eligibility for another holder. The page documents 400, 401, 403, 422 and 500 responses; 403 means insufficient permissions. This snapshot and test server do not establish current live availability, actual verification approval or completed money movement.

## Detail locators

- Request identity, server, required and conditional fields: [[raw/adyen/api-explorer/Account/latest/post/createAccountHolder/2026-09-15|raw lines 5–122]]. Bank UUID behavior: lines 26–31; legal-arrangement code: lines 71–80; POS and default account: lines 100–119.
- Business and individual request examples: raw lines 124–177. Response schema, statuses, error bodies and examples: raw lines 178–552. Examples illustrate payloads, not universal outcomes.

## Related

- [[adyen-classic-platforms]] — Classic account-holder model and source routes.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/createAccountHolder/2026-09-15|Account API v6 createAccountHolder captured raw]]
