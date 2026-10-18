---
title: "SCA for transaction history | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/sca-for-transaction-history"
raw_files:
  - "adyen/docs/business-accounts/sca-for-transaction-history/2026-09-15.md"
tags: [adyen, business-accounts, transaction-history, sca, transfers-api]
---

## Overview

This Adyen guide, last modified 2022-11-30 and captured 2026-09-15, describes Authentication SDK SCA when a user retrieves balance-account transaction history with the Transfers API. It says EEA users must authenticate each time they check history, while listing both Adyen for Platforms and Classic integration support. Treat the legal wording as dated documentation, not a current legal determination for a specific user. [[adyen-business-accounts]]

## Key takeaways

- Prerequisites are an API key (recommended) or basic authentication, the **TransferService Webservice Retrieve** credential role assigned through an Adyen contact, an installed Authentication SDK and a registered user device. The page gives Android, iOS and web eligibility/authentication examples; a web `checkAvailability()` call can throw `SCA_UNAVAILABLE`. See raw lines 23-32 and 43-143.
- The server initiates `GET /transactions` for a `balanceAccountId` and time range using the device-eligibility `sdkOutput` in a `WWW-Authenticate` header with SCA realm `Transaction`. The guide's table marks `balanceAccountId`, `createdSince`, and `createdUntil` required. The first response is documented as HTTP 401 with an `auth-param1` challenge, which the client passes to the SDK as `sdkInput`. See raw lines 145-161 and 335-352.
- After user authentication, the SDK returns a new `sdkOutput` to the server. The guide gives 10 minutes from initiating the request to complete authentication and send the second `GET /transactions`; its returned `data` array is used to present history. SDK success alone does not establish that the history request succeeded or that any listed transfer reached its recipient. See raw lines 354-422 and 424-667.
- The examples are dated and illustrative: curl uses an unquoted URL with `&` query separators, Java snippets contain malformed syntax, and SDK samples name particular library versions. Verify runnable calls and current API/SDK behavior against the relevant versioned references. See raw lines 165-333 and 436-604.

## Detail locators

- Android Kotlin, iOS Swift and web JavaScript eligibility examples: raw lines 43-143. Authentication examples and cancellation/error paths: raw lines 354-422.
- `GET /transactions` SCA header, balance-account/time-window query and initial 401 challenge: raw lines 145-352. Final request and example `data` response: raw lines 424-667.
- The sample response shows booked transaction rows, transfer references and a pagination `next` link; these are response illustrations, not evidence of a live account or bank receipt. See raw lines 606-667.

## Related

- [[adyen]] — provider context.
- [[adyen-business-accounts]] — Business Accounts product scope and source map.
- [[source-adyen-docs-business-accounts-sca-for-funds-transfers]] — separate SCA flow for making funds transfers.

## Raw Sources

- [[raw/adyen/docs/business-accounts/sca-for-transaction-history/2026-09-15|2026-09-15 captured transaction-history SCA guide]]
