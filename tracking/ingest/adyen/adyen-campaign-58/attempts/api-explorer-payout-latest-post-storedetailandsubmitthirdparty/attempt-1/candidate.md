---
title: "Adyen Payout API v68: store detail and submit third-party payout"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payout/latest/post/storeDetailAndSubmitThirdParty"
raw_files:
  - "adyen/api-explorer/Payout/latest/post/storeDetailAndSubmitThirdParty/2026-09-15.md"
tags: [adyen, payout-api, third-party-payouts, deprecated]
---

## Overview

Captured 2026-09-15 reference for `POST /storeDetailAndSubmitThirdParty` on the Payout API v68 test server (`https://pal-test.adyen.com/pal/servlet/Payout/v68`). It both submits a third-party payout and stores the supplied details for later payouts. The endpoint is deprecated and does not support new integrations; the page directs new integrations to Transfers API `POST /transfers` and existing Payout API integrators to contact Adyen about migration. See [[adyen]] and [[adyen-payouts]].

## Key takeaways

- The submitted payout still requires confirmation or decline by a reviewer or `/confirmThirdParty` or `/declineThirdParty` calls. Submission and detail storage are not payout approval or completion. The 200 response's success `resultCode` is `payout-submit-received`, a submission receipt rather than a final money-movement result.
- The request table requires `amount` with currency and minor-unit value, `merchantAccount`, `entityType`, `nationality`, `recurring`, `reference`, `shopperEmail`, and `shopperReference`. `recurring.contract` must be `PAYOUT`. One of `bank` or `card` is required. `dateOfBirth` is marked Yes in the table and described as mandatory for natural persons; preserve that conditional wording rather than infer a universal company requirement. `billingAddress` is required for cross-border payouts to and from Canada, with its listed subfields and US/Canada state condition. `shopperName.lastName` must contain the company name when entityType is Company.
- `reference` is the merchant's payout-status communication reference; uniqueness is advised but not required. `shopperReference` identifies the shopper for this transaction. `pspReference` in the response uniquely identifies the request. A 403 means insufficient permissions. This test-server snapshot does not establish current eligibility, live availability, reviewer approval, final payout outcome or bank receipt.

## Detail locators

- Deprecation, operation, confirmation boundary, test server and request body: [[raw/adyen/api-explorer/Payout/latest/post/storeDetailAndSubmitThirdParty/2026-09-15|raw lines 5–85]]. Nested bank/card rules, billing address, identity fields and recurring contract are in lines 35–83.
- Response success and error schemas plus response example: raw lines 87–182.

## Related

- [[adyen-payouts]] — broader payout routes and legacy Payout API boundary.

## Raw Sources

- [[raw/adyen/api-explorer/Payout/latest/post/storeDetailAndSubmitThirdParty/2026-09-15|Payout API v68 storeDetailAndSubmitThirdParty captured raw]]
