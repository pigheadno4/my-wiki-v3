---
title: "Manage account holders for Business Accounts | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/manage-account-holders"
raw_files:
  - "adyen/docs/business-accounts/manage-account-holders/2026-09-15.md"
tags: [adyen, business-accounts, account-holders, capabilities, verification, kyc]
---

## Overview

This [[adyen]] Business Accounts guide, last modified 2023-03-28 and captured 2026-09-15, describes Configuration API and Customer Area operations for the **account holder** resource representing a balance-platform user. The resource links a legal entity and balance accounts and carries capability states. Account-holder creation and an `active` resource status do not themselves establish verification, allowed capabilities, an opened Business Account or a completed money movement. See [[adyen-business-accounts]].

## Key takeaways

- Create the legal entity first, then `POST /accountHolders` with its legal-entity ID; for a sole proprietorship, use the owner's individual legal-entity ID. Save the returned account-holder `id` for webhook matching, balance-account creation and later updates. The sample creation response has `status=active` while several capabilities show `requested=true`, `enabled=true`, `allowed=false` and `verificationStatus=pending`; do not equate resource status or a request with permitted use. Listen for `balancePlatform.accountHolder.updated` capability/verification changes. [Raw: lines 19–29, 238–290]
- Account holders **cannot be deleted**. The introduction mentions temporary suspension to disable payout capabilities, but this captured page has no matching `#suspend-account-holder` section or suspension procedure. For permanent closure, the guide requires zero-balance accounts, closure of non-primary balance accounts first, primary account only after the others, and then `status=Closed` on the account holder. Moving residual funds is a separate transfer step, not implied by closure. [Raw: lines 21–23, 750–760]
- View an account holder through Customer Area or `GET /accountHolders/{id}`; lists of holders and associated balance accounts are paginated. Customer Area detail includes status, balance accounts, linked legal entities, document identifiers and capabilities/deadlines. Searching an individual legal entity by name/email requires the `View account holders PII` role. `PATCH /accountHolders/{id}` can update properties such as `primaryBalanceAccount`. [Raw: lines 292–340, 485–545, 735–748]
- Capability observation separates `allowed` (Adyen allows), `enabled` (user can use), `verificationStatus` (`invalid`, `pending`, `rejected`, `valid`) and a nonempty `problems` array requiring attention. Some capabilities are requested automatically; additional capabilities, such as third-party send/receive, require a request. In Customer Area that request or an enabled-state edit requires the **Manage account holder capabilities** role. API request sets `requested=true`; the documented response can remain `allowed=false` and `pending`. A later `enabled=false` sample remains `allowed=true`/`valid`, so the flags are distinct. [Raw: lines 762–826, 1069–1091, 1093–1129, 1370–1392]
- The request-capability examples conflict: prose names `receivePayment`, most examples request `receivePayments`, Python/Ruby examples use `withdrawFromAtm`, and the response shows `sendToThirdParty`. Do not copy a capability key from this mixed example without the relevant current API schema and product-specific capability guide. The KYC section separately describes legal-entity statuses `Awaiting data`, `In review`, `Verified`, `Unsuccessful` (errors may be resolved) and `Rejected` (final in this guide). KYC document access is role-gated and privacy-sensitive. None of these sample screens or statuses proves a particular user's completed onboarding or opened account. [Raw: lines 824–826, 837–843, 1007–1042, 1077–1091, 1394–1448]

## Detail locators

- Account-holder identity, non-deletion and legal-entity-first creation: raw lines 19–29.
- TEST-environment create examples, response identity/default capability flags and webhook: raw lines 31–290.
- Customer Area/API view, PII search, paginated lists, and primary-account update: raw lines 292–748.
- Ordered permanent closure; capability flags, request and enable/disable paths: raw lines 750–1392.
- KYC legal-entity statuses and document-role/privacy rules: raw lines 1394–1448.

## Related

- [[adyen-business-accounts]] — Business Accounts product context
- [[adyen-platforms]] — platform resource context
- [Manage legal entities](https://docs.adyen.com/business-accounts/manage-legal-entities) — prerequisite legal-entity route
- [Manage balance accounts](https://docs.adyen.com/business-accounts/manage-balance-accounts) — linked balance-account and closure route
- [Business Accounts verification overview](https://docs.adyen.com/business-accounts/verification-overview) — capability and KYC context

## Raw Sources

- [[raw/adyen/docs/business-accounts/manage-account-holders/2026-09-15|Adyen Business Accounts manage account holders — collected 2026-09-15]]
