---
title: "Adyen Business Accounts: Manage third-party consent"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/consent"
raw_files:
  - "adyen/docs/business-accounts/consent/2026-09-15.md"
tags: [adyen, business-accounts, open-banking, consent, tpp]
---

## Overview

This [[adyen]] Business Accounts Open Banking page tells a third-party provider (TPP) how to inspect or revoke a previously granted account-holder consent through `/consents`. The account holder grants or withdraws permission; the TPP checks status, authorization progress, permitted scope and validity, and can call DELETE to revoke on the holder's behalf. The 2026-09-15 capture is marked modified that day. The examples use TEST endpoints and old sample dates; they do not demonstrate current consent, account access, payment initiation, or funds movement.

## Key takeaways

- This is a TPP guide, not a platform-integration setup guide. It presumes Adyen onboarding and the separate account-holder consent flow. The GET and DELETE examples use a consent ID, `X-Request-ID` UUID and bearer access token; the raw page gives the exact TEST paths and prerequisites.
- GET `/consents/{consent_id}/status` returns `consentStatus`: `received` requires another check before use, `valid` means accepted/valid, and the table also lists `rejected` (final), `revokedByPsu`, `expired`, and `terminatedByTpp`. A valid status alone does not describe every allowed action.
- GET `/consents/{consentId}/authorisations/{authorization-id-consent}` returns separate `scaStatus` for the holder's authentication/authorization flow (`scaMethodSelected`, `started`, `finalised`, `failed`); the last two are final authorization-resource states. GET `/consents/{consent_id}` returns consent status, `validUntil`, permitted `access` (the example lists account, balance and transaction IBAN scopes), frequency/recurrence fields and resource links. Inspect current status, expiry and scope together before treating a consent as usable. The example's `validUntil: 2023-10-12` is sample data, not a current authorization.
- DELETE `/consents/{consent_id}` is described as withdrawing authorization to access information or initiate payments, depending on the consented action. The page says a successful deactivation returns HTTP 200 and future status checks show `revokedByPsu`, even though it describes a TPP making the call and separately lists `terminatedByTpp` for TPP termination. Preserve that status-name tension; this page does not establish which code applies in every revocation scenario.

## Detail locators

- Opening and `Requirements` (raw lines 15–32): account-holder/TPP roles and prerequisites.
- `Check if the account holder granted consent` (raw lines 34–67): status endpoint, headers and `consentStatus` values.
- `Check the authorization status` (raw lines 69–100): separate SCA authorization resource and `scaStatus`.
- `Check consent details` (raw lines 102–150): allowed access, `validUntil`, frequency and links, illustrated by a TEST example.
- `Delete a consent` (raw lines 152–166): revocation request, HTTP 200 and future-status wording; `Next steps` (168–180) routes to AISP/PISP/PIISP.

## Related

- [[adyen-business-accounts]] — Business Accounts and Open Banking context.
- [[source-adyen-docs-business-accounts-oauth-flow]] — earlier account-holder consent grant and token flow.

## Raw Sources

- [[raw/adyen/docs/business-accounts/consent/2026-09-15|Adyen manage consent, captured 2026-09-15]]
