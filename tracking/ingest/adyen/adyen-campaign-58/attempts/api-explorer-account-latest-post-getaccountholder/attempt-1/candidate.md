---
title: "Adyen Account API: POST /getAccountHolder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/getAccountHolder"
raw_files:
  - "adyen/api-explorer/Account/latest/post/getAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holder, verification]
---

## Overview

This 2026-09-15 Account API Explorer capture documents `POST /getAccountHolder` on the listed TEST Account v6 server. It retrieves a Classic Platforms account holder by account code or account-holder code; it does not perform an account-holder update. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The request body lists `accountCode` and `accountHolderCode` as individually optional, but each is required if the other is absent. Optional `showDetails` is described as true when account-holder details should be returned. The two request examples use one code each; they do not establish a rule for providing both.
- The 200 and 202 response schemas list top-level `accountHolderCode`, `accountHolderDetails`, `accountHolderStatus`, `accounts`, `legalEntity`, `migrationData`, `systemUpToDateTime`, and `verification` as optional, among other fields. Nested `Yes` fields are conditional on their optional enclosing objects; creation/update guidance embedded in the response schema must not be mistaken for extra requirements on this retrieval request.
- `accountHolderStatus` has holder-level status, scheduled events, payout state and processing state. `payoutState.allowPayout` is described as the aggregate payout gate for all of the holder's accounts; platform `disabled=false` alone does not establish that payouts are allowed. Processing state is separate. Each entry in `accounts` has its own optional account status and payout configuration. These returned states or schedules do not prove an actual payout, payment processing event, or bank receipt.
- Optional `verification` groups KYC check results by holder, legal arrangements and their entities, payout methods, shareholders, signatories and ultimate parent company. Optional `migrationData` describes Classic-to-balance-platform identifiers and mappings when present; the schema does not prove that this holder has migrated or make the two API resource models interchangeable. `systemUpToDateTime` is the response's stated information-freshness time, not proof of current status beyond the response.
- HTTP 200 says the request succeeded; 202 says accepted for processing but incomplete. The listed errors are 400 request reading/understanding, 401 authentication, 403 permissions, 422 validation, and 500 server processing. No successful response example or actual holder record is supplied in this capture.

## Detail locators

- Endpoint, TEST v6 server, request alternatives and examples: raw lines 5–35.
- 200 response: top-level and nested holder details, bank accounts, stores, payout methods and schedules, status, verification and migration mappings: raw lines 36–230. See especially lines 144–176 for holder versus account state; 186–205 for migration and freshness; 206–230 for KYC.
- Repeated 202 response schema and pending-processing meaning: raw lines 233–425.
- Error classes, generic schemas and 400/403 examples: raw lines 428–516.

## Related

- [[adyen-classic-platforms]] — older platform holder/account model.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/getAccountHolder/2026-09-15|Account API Explorer POST /getAccountHolder capture]]
