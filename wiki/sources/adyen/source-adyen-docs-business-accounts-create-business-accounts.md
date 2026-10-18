---
title: "Adyen Business Accounts: Create business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/create-business-accounts"
raw_files:
  - "adyen/docs/business-accounts/create-business-accounts/2026-09-15.md"
tags: [adyen, business-accounts, balance-platform, payment-instruments]
---

## Overview

Adyen's 2024-modified Business Accounts guide describes generating a business account number linked to a user's balance account so third parties can send business-related payments or fund transfers. The API operation creates a `bankAccount` payment instrument; the balance account remains the resource where financial transactions are processed. This captured guide describes a setup flow, not evidence that a particular user's live account was opened, usable, or funded. [[adyen-business-accounts]]

## Key takeaways

- Before creation, the platform must meet Business Accounts requirements and have legal entities for the user and associated entities (such as UBOs), two business lines (one for receiving payments and one for Business Accounts), an account holder and balance account, completed Business Accounts verification checks, and the account holder's `issueBankAccount` capability both allowed and enabled. See raw lines 21–34 for the prerequisite sequence.
- After that capability state, `POST /paymentInstruments` with `type=bankAccount`, `balanceAccountId`, and `issuingCountryCode` generates the business account number. `description` and `reference` are optional mappings; see raw lines 32–44. The guide's captured country list is NL and US, with the issuing country's currency required to match the balance account currency (raw line 41). Treat that list as dated documentation, not current eligibility.
- A balance account can have only one business account number; the API returns an error if one already exists (raw line 46). The NL example returns a payment instrument `id` and IBAN (raw lines 268–282); the US example returns a payment instrument `id` and account/routing details (raw lines 505–521). Example `status: Active` and TEST requests do not establish any real account's approval or ability to receive funds.
- To find an existing number associated with a balance account, the page points to `GET /balanceAccounts/{id}/paymentInstruments` with the balance account ID in the path (raw lines 524–526).

## Detail locators

- Required request fields and optional reference fields: raw lines 36–46.
- NL and US TEST code examples, including client library versions: raw lines 48–282 and 285–503.
- Example response resource identities and bank details: raw lines 268–282 and 505–521.

## Related

- [[adyen-business-accounts]]
- [[source-adyen-docs-business-accounts-account-structure-resources]] — resource relationship.
- [[source-adyen-docs-business-accounts-manage-account-holders]] — account holder and capabilities.
- [[source-adyen-docs-business-accounts-manage-legal-entities]] — legal entity prerequisite.
- [[source-adyen-docs-business-accounts-onboard-users-terms-of-service]] — separate consent flow.

## Raw Sources

- [[raw/adyen/docs/business-accounts/create-business-accounts/2026-09-15|Captured Create business accounts guide]]
