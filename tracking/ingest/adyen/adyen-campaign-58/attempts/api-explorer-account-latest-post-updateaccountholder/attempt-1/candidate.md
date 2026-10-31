---
title: "Adyen Account API v6: update an account holder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder"
raw_files:
  - "adyen/api-explorer/Account/latest/post/updateAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holders]
---

## Overview

Captured Classic Platforms Account API v6 TEST reference for `POST /updateAccountHolder`. It updates an account holder's details or processing tier and can add bank accounts and shareholders. This is a Classic account-holder operation identified by `accountHolderCode`; its response does not itself establish completed KYC, payout eligibility, or a payment. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- `accountHolderCode` is required. `accountHolderDetails` is required if `processingTier` is absent, and `processingTier` is required if details are absent; the tier cannot be lowered through this request. Other request properties include optional `description`, `legalEntity`, `primaryCurrency`, and `verificationProfile`. The table's nested “Yes” entries and conditional descriptions are not all top-level body requirements. See raw lines 32–44 and 135–139.
- Omitted `accountHolderDetails` parameters stay unchanged, except that sending `metadata` replaces the entire metadata object and deletes omitted existing key-value pairs. Metadata values over 80 characters are truncated. Changing any field in `address`, `fullPhoneNumber`, `bankAccountDetails.BankAccountDetail`, or `businessDetails.shareholders.ShareholderContact` requires all fields needed to validate that object; the page gives an address example. See raw lines 7–25 and 99–100.
- New bank accounts and shareholders are supplied without `bankAccountUUID` or `shareholderCode`. For bank accounts, a missing UUID with other details creates a new account; on update, an uncorrelated UUID fails the account-holder update, while a correlated UUID updates the existing bank account. The request table points to separate required-information guidance for country-specific bank fields; it does not enumerate a universal bank-field set here. See raw lines 25, 44–70.
- The request table also describes conditional details: `legalEntity` Business/NonProfit calls for business details with at least one shareholder, while Individual calls for individual details; a supplied store split configuration requires `virtualAccount`; existing payout-method and store updates require their respective generated codes. Several business/individual detail descriptions explicitly say “when creating,” so do not generalize every nested creation rule to every partial update. See raw lines 72–98, 101–132, 135–138.
- 200 says the request succeeded; 202 explicitly means accepted for processing but incomplete. Response fields can include `invalidFields`, `accountHolderStatus`, `verification`, and a request-identifying `pspReference`. `payoutState.allowPayout` is an aggregate of conditions, whereas `payoutState.disabled` is the platform-controlled disable flag; `disabled: false` alone does not imply `allowPayout: true`. Sample Active/payout values are examples, not a status guarantee. See raw lines 269–433, 436–598 and 665–902.
- The reference lists 400 malformed/readability, 401 authentication, 403 permission, 422 validation, and 500 server responses, plus generic 400 and 403 examples. It does not state a propagation deadline or idempotency behavior. See raw lines 601–663 and 904–926.

## Detail locators

- Purpose, partial-update and validation rules: raw lines 5–25.
- TEST server and request schema, including country-dependent bank details, legal arrangements, payout methods and store fields: raw lines 27–139.
- Four request examples (shareholder, bank, business, general): raw lines 141–268.
- 200 and 202 response schemas, payout/processing state and verification checks: raw lines 269–598.
- HTTP error schemas and response examples: raw lines 601–926.

## Related

- [[adyen-classic-platforms]] — Classic Platforms context.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/updateAccountHolder/2026-09-15|Account API v6 updateAccountHolder captured 2026-09-15]]
