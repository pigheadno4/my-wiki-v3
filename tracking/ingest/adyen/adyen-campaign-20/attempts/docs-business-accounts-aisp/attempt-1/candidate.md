---
title: "Adyen Business Accounts AISP account information"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/aisp"
raw_files:
  - "adyen/docs/business-accounts/aisp/2026-09-15.md"
tags: [adyen, business-accounts, open-banking, aisp, account-information]
---

## Overview

This 2026-09-15 Adyen Open Banking/AISP page addresses a **third-party Account Information Service Provider**, not the platform creating a Business Account. It shows consented read access to an account holder's Adyen business-account list, details, balances and transactions through dedicated `/accounts` endpoints. Onboarding, an access token and that holder's consent ID are prerequisites. The examples show account information retrieval, not account opening, consent creation, payment initiation, available funds for a particular live user or bank receipt. See [[adyen]], [[adyen-business-accounts]] and [[source-adyen-docs-business-accounts-oauth-flow]].

## Key takeaways

- The requirements call for Adyen onboarding, an access token for the Adyen business account and the ID of the holder's consent. Requests add a `Consent_Id` header, a Bearer access token and `X-Request-ID` in the test examples. Having credentials or a listed account is not proof of authorization to move funds.
- GET `/accounts` lists accounts associated with the consented holder; returned `resourceId` identifies an account for GET `/accounts/{resourceId}`, `/balances` and `/transactions`. The account-list prose calls the response “an array of accounts,” while its JSON example wraps the array in an `accounts` object; do not derive a parser contract from the prose alone. Example `ownerName` values also differ between list and detail responses, so they are illustrative identities.
- Balances have distinct `balanceType` labels such as `authorised`, `expected`, `interimAvailable` and `interimBooked`; the example includes amounts but does not demonstrate a particular real account's available balance. Transaction lookup uses `bookingStatus`, `dateFrom` and `dateTo` filters, with optional `pageSize` (1–50; default 1); the response may include balances only if consent includes balances, and pagination links point to more records.
- The transaction section and response links use `/obeu/aisp/v1/accounts/...`, while the transaction curl example uses `/obeu/v1/accounts/...` without `aisp`. Treat this as an unresolved documentation-path mismatch, not two confirmed routes. The sample `booked` transaction and balance records describe account-information state, not independent confirmation that a third-party beneficiary bank received a payment.
- This AISP account-information flow is separate from the Business Accounts page on open-banking verification of an **unregistered external individual's** bank-account ownership. The two have different actors and objectives; neither establishes a live financial operation.

## Detail locators

- AISP actor, purpose and prerequisites: raw lines 15–35.
- Account list and sample response shape: lines 38–86; account-detail request and sample owner mismatch: lines 88–122.
- Balance types and example: lines 124–176.
- Transaction filters, pagination, conditional balances and response: lines 178–268. Compare the transaction example URL at line 197 with the `aisp` endpoints and response links at lines 47, 97, 133 and 261–264.
- Links to payment initiation and funds confirmation are navigational only (lines 270–273), not evidence of a payment-instruction capability in this AISP guide.

## Related

- [[adyen-business-accounts]] — Business Accounts product context.
- [[source-adyen-docs-business-accounts-oauth-flow]] — linked third-party provider token and holder-consent setup.
- [[source-adyen-docs-business-accounts-verify-account-holder]] — distinct external-individual bank-account verification use case.

## Raw Sources

- [[raw/adyen/docs/business-accounts/aisp/2026-09-15|Adyen Docs: Get account holder information (2026-09-15 snapshot)]]
