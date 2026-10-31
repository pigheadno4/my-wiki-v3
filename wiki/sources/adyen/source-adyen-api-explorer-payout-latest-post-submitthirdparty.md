---
title: "Adyen legacy Payout API v68: submit a stored-detail payout"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payout/latest/post/submitThirdParty"
raw_files:
  - "adyen/api-explorer/Payout/latest/post/submitThirdParty/2026-09-15.md"
tags: [adyen, payouts, legacy-payout-api, staged-payouts]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `POST /submitThirdParty` on the TEST Payout API v68 server (`https://pal-test.adyen.com/pal/servlet/Payout/v68`). It submits a payout using payment details previously stored through `/storeDetail`. The endpoint is deprecated and does not support new integrations: the page directs new integrations to Transfers API `POST /transfers` and existing Payout API users to their Adyen contact for migration.

## Key takeaways

- Submission is a stage, not the final payout. The submitted payout must later be confirmed or declined by a reviewer or via `/confirmThirdParty` or `/declineThirdParty`. This page does not state the reviewer role, deadline, or final settlement evidence.
- Required request properties are `amount` (with required `currency` and minor-unit `value`), `merchantAccount`, `recurring`, merchant `reference`, `selectedRecurringDetailReference`, `shopperEmail`, and `shopperReference`. Although nested `recurring.contract` is marked “No” in the table, the `recurring` description explicitly says it must be `PAYOUT`. `selectedRecurringDetailReference` identifies stored details and can be `LATEST`; it is not the submission response's PSP reference.
- Optional fields have conditional descriptions: `dateOfBirth` is mandatory for natural persons and required to update the existing recurring-contract value; `entityType`, `nationality`, and `shopperName` are required when updating their existing recurring-contract values. For a company, `shopperName.lastName` must contain the company name. The nested first and last name fields are marked required within `shopperName`.
- The 200 schema's required `pspReference` is a **new reference identifying this submission request**, while `resultCode` is `payout-submit-received` on success. Neither establishes confirmation, transfer execution, or beneficiary receipt. The merchant `reference` is used in status communication; uniqueness is recommended but explicitly not required.
- The page lists 400, 401, 403, 422 and 500 errors; it gives no successful payout example, idempotency contract, or LIVE execution evidence.

## Detail locators

- Deprecation, migration direction, stored-detail prerequisite and confirmation/decline stage: raw lines 5–28.
- Request schema and conditional fields: raw lines 32–58.
- Submission response reference and result code: raw lines 60–71.
- Error schemas and generic 400 example: raw lines 74–155.

## Related

- [[adyen]] — provider.
- [[adyen-payouts]] — legacy Payout API versus newer Transfers API context. Do not apply this endpoint's staged contract to the newer Payout Service by analogy.

## Raw Sources

- [[raw/adyen/api-explorer/Payout/latest/post/submitThirdParty/2026-09-15|Payout API v68 POST /submitThirdParty (captured 2026-09-15)]]
