---
title: "Adyen Classic Account API v6: unsuspend an account holder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/unSuspendAccountHolder"
raw_files:
  - "adyen/api-explorer/Account/latest/post/unSuspendAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holders]
---

## Overview

Captured 2026-09-15 API Explorer reference for `POST /unSuspendAccountHolder` on the Classic Platforms Account API v6 test server (`https://cal-test.adyen.com/cal/services/Account/v6`). It changes an account holder from **Suspended** to **Inactive**, subject to the verification-check condition below. The request identifies the holder by `accountHolderCode`; it does not create a new account or promise an **Active** state. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- An account holder can be Suspended through `/suspendAccountHolder` or after a verification deadline expires. Unsuspension is allowed only if the holder has no verification check with **FAILED** status. The request body's sole listed property, `accountHolderCode`, is required.
- The response schema can include `accountHolderStatus`, scheduled events, processing and payout states, validation errors, `pspReference` and `resultCode`. `payoutState.allowPayout` aggregates conditions such as KYC and disablement; unsuspending to Inactive does not itself establish that processing or payouts are enabled.
- HTTP 200 says the request succeeded. HTTP 202 says it was accepted for processing and processing has **not** completed. The page also lists 400, 401, 403, 422 and 500 responses; 403 denotes insufficient permissions. Neither a 202 receipt nor this test-server reference proves completed state propagation, current live eligibility, verification approval or any financial outcome.

## Detail locators

- Purpose, suspension sources, eligibility, server, request field and example: [[raw/adyen/api-explorer/Account/latest/post/unSuspendAccountHolder/2026-09-15|raw lines 5–29]].
- 200 and 202 response schemas, including status and payout/processing fields: raw lines 30–103. Error schemas and examples: raw lines 106–194.

## Related

- [[adyen-classic-platforms]] — Classic account-holder lifecycle and source routes.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/unSuspendAccountHolder/2026-09-15|Account API v6 unSuspendAccountHolder captured raw]]
