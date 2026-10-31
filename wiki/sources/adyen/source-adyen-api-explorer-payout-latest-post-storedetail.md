---
title: "Adyen Payout API v68: Store payout details"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payout/latest/post/storeDetail"
raw_files:
  - "adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15.md"
tags: [adyen, payouts, payout-api, recurring-details, deprecated]
---

## Overview

This 2026-09-15-captured `POST /storeDetail` reference is for the **deprecated Payout API v68 test endpoint** (`https://pal-test.adyen.com/pal/servlet/Payout/v68`). It stores bank or card payment details under a `PAYOUT` recurring contract for a **later, separate** `/submitThirdParty` payout request. The page says new integrations must use the Transfers API and existing Payout API users should contact Adyen about migration. This endpoint does not submit a payout. [[adyen-payouts]] [[adyen]]

## Key takeaways

- The request table marks `merchantAccount`, `entityType`, `nationality`, `shopperEmail`, `shopperReference`, `recurring`, and `dateOfBirth` required, while the `dateOfBirth` description says it is mandatory for **natural persons**. `recurring.contract` is not marked required as a nested row but the `recurring` description explicitly requires it to be `PAYOUT`. Treat those narrative conditions as part of this endpoint, without converting all other recurring enum values into valid contracts here. See [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|raw lines 60–76]].
- `bank` and `card` are each marked optional in the table, but each description makes it mandatory when the other is absent. The page does not state whether both can be sent together. Bank fields include account/IBAN/BIC, country and owner identity. For `ownerName`, the page describes transliteration of some non-Latin characters and a post-replacement minimum of three alphanumeric characters including a Latin letter; bad format returns error 203. Card rows include number/expiry/CVC details; the CVC row says it is not stored and warns against posting card details to the server when using Client-Side Encryption. See [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|raw lines 33–43 and 51–59]].
- `billingAddress` is conditional for cross-border payouts to and from Canada; its listed city, country, house number, postal code and street are required **inside the object**, while state/province is conditionally required for US/Canada. Optional `shopperName` has nested required first/last names, with company name in `lastName` when `entityType` is `Company`. The source also has a Paysafecard-specific `selectedBrand` value and date-of-birth note. See [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|raw lines 44–50, 60, 71–76]].
- HTTP 200 returns required `pspReference` (this storage request's reference), `recurringDetailReference` (token for later payout submission), and `resultCode`; `Success` means the details were **stored**, not that a payout was submitted, approved or paid. The example contains those three fields. See [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|raw lines 80–91 and 163–174]].
- Errors list 400 unreadable request, 401 authentication, 403 insufficient permissions, 422 validation and 500 server failure, with a generic 400 example. The page names no specific role, live endpoint, current integration eligibility or successful card/bank payout. See [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|raw lines 94–186]].

## Detail locators

- Deprecation, migration direction, separate later payout and v68 test server: [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|raw lines 5–26]].
- Full request schema and conditional bank/card, address, identity and recurring-contract fields: [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|raw lines 30–78]].
- Success/error schemas and examples: [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|raw lines 80–186]].

## Related

- [[adyen-payouts]] — legacy Payout API context and separate Transfers API model.
- [[adyen-card-payouts]] — card-specific legacy payout context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15|Store payout details API reference (captured 2026-09-15)]]
