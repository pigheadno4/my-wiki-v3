---
title: "Adyen Business Accounts: Manage balance accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/manage-balance-accounts"
raw_files:
  - "adyen/docs/business-accounts/manage-balance-accounts/2026-09-15.md"
tags: [adyen, business-accounts, balance-accounts, account-holders]
---

## Overview

This 2026-09-15-modified [[adyen]] Business Accounts guide describes Configuration API operations for a balance-account resource containing information about funds held by a user. A balance account is attached to an account holder and belongs to a wider verification and onboarding process. Resource creation or an example `status: active` does not establish that a particular Business Account is verified, usable or funded. [[adyen-business-accounts]]

## Key takeaways

- To create a balance account manually, `POST /balanceAccounts` with the account holder ID to which it should attach. Retain the returned balance account `id` for view, update and close operations (raw lines 23–27, 227–253). The TEST example includes `defaultCurrencyCode: EUR`, zero-valued EUR balances and `status: active`; these are response example values, not universal currency, default/primary-account rules or live balance evidence.
- For observation, Customer Area can show balance accounts and available balances for one selected balance platform at a time. The API lists an account holder's balance accounts through paginated `GET /accountHolders/{id}/balanceAccounts`, details and balances through `GET /balanceAccounts/{id}`, and associated payment instruments through `GET /balanceAccounts/{id}/paymentInstruments` (raw lines 256–278). The latter is labeled “cards” in this page; do not broaden that parenthetical into a complete inventory rule for every product.
- `PATCH /balanceAccounts/{id}` updates a balance account; the worked example changes `description` (raw lines 280–295). The page does not state a special Customer Area role or a procedure for choosing a primary account; consult product-specific authorization and account-holder guidance rather than inferring those from the sample description “Primary Balance Account.”
- Closure is permanent in the guide. Check for zero balance; if funds remain, transfer them through the separately linked internal-transfer flow before setting each balance account's `status` to `Closed` through update. Discontinuing the platform relationship can involve separate permanent account-holder deactivation (raw lines 473–482). This guide does not prove a transfer occurred or that closure completed.

## Detail locators

- Resource definition, onboarding and verification context: raw lines 17–21.
- TEST create requests, SDK versions and illustrative response fields: raw lines 23–254.
- Customer Area and API view routes: raw lines 256–278.
- Description-only PATCH examples: raw lines 280–471.
- Zero-balance and permanent closure sequence: raw lines 473–482.

## Related

- [[adyen-business-accounts]]
- [[source-adyen-docs-business-accounts-manage-account-holders]] — account-holder resource and capability status.
- [[source-adyen-docs-business-accounts-account-structure-resources]] — resource relationships.
- [[source-adyen-docs-business-accounts-create-business-accounts]] — separate bankAccount payment instrument and business account number.

## Raw Sources

- [[raw/adyen/docs/business-accounts/manage-balance-accounts/2026-09-15|Captured Manage balance accounts guide]]
