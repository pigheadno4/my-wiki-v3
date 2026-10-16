---
title: "Manage balance accounts | Adyen for Platforms"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-balance-accounts"
raw_files:
  - "adyen/docs/platforms/manage-balance-accounts/2026-09-15.md"
tags: [adyen, platforms, balance-accounts, account-holders, configuration-api]
---

## Overview

This 2026-09-15 [[adyen]] for Platforms guide describes Configuration API and Customer Area routes for creating, viewing, updating and permanently closing an account holder's balance account. A balance account is a resource concerning funds held for a platform user and belongs to a broader onboarding and verification process. It is distinct from the account holder, a legal entity, the platform's liable account, a payout-bank transfer instrument, or an actual transfer/payment event. [[adyen-platforms]]

## Operations and boundaries

- **Create:** POST `/balanceAccounts` with the `accountHolderId` to attach the new balance account to that account holder. Retain the returned balance-account `id` for later view, update or close operations. The shown test request and response are examples: the response's `defaultCurrencyCode: EUR`, zero balances, `timeZone` and `status: active` do not assert a default currency, funded balance, enabled capability or completed onboarding for other accounts.
- **View:** Customer Area **Balances → Balance accounts** shows one selected balance platform at a time and can open/search a balance-account ID. API routes list an account holder's balance accounts with pagination, retrieve one balance account and its balances, or list the **payment instruments (cards)** associated with the balance account. Those cards are not the user's bank-account **transfer instrument** used for payout. Viewing an available balance is not proof of settlement or bank receipt.
- **Update:** PATCH `/balanceAccounts/{id}` is shown for changing a description. This source does not demonstrate general changes to account-holder ownership, currency, legal entity, reserve/liable identity or underlying funds. Sample code uses test-environment credentials and versioned libraries; consult the raw for implementation details, not for current runtime proof.
- **Close:** The page calls this **permanent**. Only an empty balance account can be closed; check for zero balance, and if funds remain, separately pay them out or transfer them before setting `status` to `Closed` through an update. The guide points to a separate account-holder deactivation path when the contractual relationship ends. Closing the balance account is not the same as deactivating its account holder and is not proof that a payout or transfer cleared. This source gives no self-service reversal of closure.

## Detail locators

- **Balance-account identity, larger verification/onboarding context and create call:** raw lines 15–27.
- **Versioned test code and sample create response/ID/balance fields:** raw lines 29–254.
- **Customer Area and API view routes, pagination and associated cards:** raw lines 256–278.
- **Description PATCH example and versioned test code:** raw lines 280–471.
- **Empty-balance prerequisite and permanent close/deactivation distinction:** raw lines 473–482.

## Related

- [[adyen-platforms]]
- [[adyen-payouts]] — separate payout flow

## Raw Sources

- [[raw/adyen/docs/platforms/manage-balance-accounts/2026-09-15|Adyen Platforms balance-account management — collected 2026-09-15]]
