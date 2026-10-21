---
title: "Adyen Marketplaces manage balance accounts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-balance-accounts"
raw_files:
  - "adyen/docs/marketplaces/manage-balance-accounts/2026-09-15.md"
tags: [adyen, marketplaces, platforms, balance-accounts, configuration-api]
---

## Overview

This 2026-09-15 Adyen Marketplaces guide covers creation, lookup, update and permanent closure of a **user balance account** with the Balance Platform Configuration API and Customer Area. The balance account is an API resource containing information about funds held by a user and is attached to an account holder. These operations sit within the broader onboarding and verification process; creating the resource is not proof that verification, payments or payouts are enabled. [[adyen]] [[adyen-platforms]]

## Key takeaways

- To create a user balance account manually, POST `/balanceAccounts` with the account holder ID to attach it to. Retain the returned balance-account `id` for subsequent view, update or close operations. The TEST example response shows an `active` status and zero balances, but is illustrative rather than proof of a live account or its funds (raw lines 23–27, 227–254).
- To view accounts and available balances, Customer Area can show one balance platform at a time or search by balance-account ID. The API provides a paginated GET `/accountHolders/{id}/balanceAccounts`, GET `/balanceAccounts/{id}` with balances, and GET `/balanceAccounts/{id}/paymentInstruments` for associated cards. These are distinct resource lookups; a balance account is not itself the account holder or card (raw lines 256–278).
- PATCH `/balanceAccounts/{id}` updates an account. The worked request changes only its description; do not infer other mutable fields from that example (raw lines 280–471).
- Closing is **permanent** and requires an empty/zero balance account. If funds remain, the guide directs the platform to pay out or transfer the remaining balance first; then PATCH the account status to `Closed`. Permanent account-holder deactivation is a separate route when the contractual relationship ends. The page does not show a closure request or confirmation response, and a payout/transfer instruction is not proof funds have moved (raw lines 473–482).

## Detail locators

- Resource purpose and verification/onboarding context: raw lines 15–21. Creation endpoint, TEST SDK examples, returned ID and illustrative balances/status: lines 23–254.
- Customer Area navigation and paginated/detail/payment-instrument GETs: lines 256–278. PATCH description example across SDKs: lines 280–471.
- Permanent close prerequisite, transfer/payout route, `Closed` status, and separate account-holder deactivation: lines 473–482.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern Platforms model and Marketplace route.
- [[source-adyen-docs-marketplaces]] — marketplace integration overview.
- [[source-adyen-docs-platforms-manage-balance-accounts]] — separate Platforms-path guide; do not silently merge its details into this source.
- [[adyen-classic-platforms]] — separate legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-balance-accounts/2026-09-15|Marketplace balance-account management — 2026-09-15 snapshot]]
