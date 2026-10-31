---
title: "Adyen Classic Fund API v6: set up a beneficiary account"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/post/setupBeneficiary"
raw_files:
  - "adyen/api-explorer/Fund/latest/post/setupBeneficiary/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, beneficiaries]
---

## Overview

Captured 2026-09-15 Classic Fund API v6 test-server reference for `POST /setupBeneficiary`. The operation defines a benefactor/beneficiary relationship between two accounts: the source is the benefactor and the destination is the beneficiary. The page says setup transfers the benefactor account's current funds to the beneficiary account and automatically sends later payments to the benefactor account onward to the beneficiary account. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The request body requires `sourceAccountCode` and `destinationAccountCode`; `merchantReference` is optional. A benefactor/beneficiary series may have no more than four beneficiaries and no cycle. The page does not specify a same-account-holder or same-platform restriction for this operation.
- This is relationship setup with described current-balance transfer and future-payment routing, not an ordinary one-time `/transferFunds` instruction. The response schema lists `invalidFields`, request `pspReference` and `resultCode`; it does not provide a posted-transfer amount or destination balance. A 200 says the request succeeded, whereas a 202 only says accepted for processing, with processing incomplete. A response receipt alone does not establish that the described funds movement has completed.
- The page lists 400, 401, 403, 422 and 500 errors; 403 means insufficient permissions. This captured v6 test endpoint does not establish current live availability, account eligibility or an actual completed transfer.

## Detail locators

- Operation description, limits, server and request schema/example: [[raw/adyen/api-explorer/Fund/latest/post/setupBeneficiary/2026-09-15|raw lines 5–30]].
- 200/202 responses, error schemas and permission boundary: raw lines 31–129.

## Related

- [[adyen-classic-platforms]] — Classic account and funds model.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/post/setupBeneficiary/2026-09-15|Fund API v6 setupBeneficiary captured raw]]
