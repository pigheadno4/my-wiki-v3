---
title: "Adyen Classic Platforms error codes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/error-codes"
raw_files:
  - "adyen/docs/classic-platforms/error-codes/2026-09-15.md"
tags: [adyen, classic-platforms, error-codes, account-holders]
---

## Overview

This 2019-modified page captured 2026-09-15 is a code-description lookup for **classic** Adyen for Platforms integrations. It says `errorCode` appears in Classic Platforms API responses and notifications and directs new implementations to a different integration guide. The catalog does not define the current modern Platforms API error contract. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The page has two distinct lookup sections: general `10_...` error codes for communication with Classic Platforms API and numeric account-holder codes that may be returned by `/createAccountHolder` and `/updateAccountHolder`. Keep the namespaces and request context when interpreting a number.
- The general list covers account/holder state, authentication, notification configuration, documents, bank accounts, transfers and payouts. For example, it lists insufficient balance (`10_066`), account-status/payout-state gates (`10_061`–`10_063`), failed fund transfer (`10_078`), and account or account-holder closure with a remaining nonzero balance (`10_115`–`10_116`). These are error descriptions, not proof that any live request failed or a payout moved.
- Account-holder codes include missing/invalid fields, documents, bank and payout details, account status, transfer limits, legal-entity information and stores. The table prints `125` twice, once for a missing virtual account and once for a non-parent account; code 125 alone is ambiguous in this snapshot. Consult returned context rather than assuming either description is definitive.

## Detail locators

- Classic-only warning, modern-guide redirect, and response/notification `errorCode` placement: raw lines 19–21. General table: raw lines 23–164; account, status, amount and funds examples: lines 31–99 and 129–135.
- Account-holder `/createAccountHolder`/`/updateAccountHolder` table: raw lines 166–299. Validation, funding and payout examples: lines 172–223. Duplicate `125` with two descriptions: lines 274–275.
- Classic verification, payment, payout and API-reference navigation: raw lines 301–306. The page supplies descriptions rather than a retry taxonomy or a universal remediation procedure.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — Classic integration context.
- [[adyen-platforms]] — separate modern Platforms context.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/error-codes/2026-09-15|Classic Platforms error codes — 2026-09-15 snapshot]]
