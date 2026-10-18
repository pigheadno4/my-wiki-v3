---
title: "Adyen Business Accounts: User capabilities"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/verification-overview/capabilities"
raw_files:
  - "adyen/docs/business-accounts/verification-overview/capabilities/2026-09-15.md"
tags: [adyen, business-accounts, capabilities, verification, kyc]
---

## Overview

This 2024-02-20-modified [[adyen]] Business Accounts guide explains the account-holder capability settings and verification states that govern actions on a balance platform. It identifies the Business Account capability set, how default and additional capabilities are requested, and how to observe changes. A requested capability, a favorable example flag or a verification-in-progress state does not prove a particular user passed KYC or obtained an open and usable Business Account. [[adyen-business-accounts]]

## Key takeaways

- In most cases Adyen configures default capabilities during business design; those are automatically requested when account holders are created. A non-default capability needs a separate request and may prompt additional KYC checks (raw lines 19–23). The Business Account table names `issueBankAccount` to allow an Adyen business bank account, and `receiveFromThirdParty`/`sendToThirdParty` for third-party bank-account fund flows. The latter two are described as enabled by default when the user has `issueBankAccount` (raw lines 25–33). Other balance-platform actions may need general capabilities, some automatic and some separately requested (raw lines 35–37).
- Capability verification status is observable through `balancePlatform.accountHolder.created`/`.updated` webhooks or `GET /accountHolders/{id}` (raw lines 39–45). First-time `pending` has `requested=true, allowed=false`; when previously allowed user data changes, `pending` can coexist with `allowed=true` while checks run. `valid` indicates passed capability checks and `allowed=true`, while `rejected` is final and `allowed=false` in this guide (raw lines 46–53).
- `invalid` normally flags failed or missing evidence, returns a `problems` object with verification/error/action detail and `allowed=false` until resolved. The same row states an important exception: after previously successful verification, changed or missing user data can revert status to `invalid` yet preserve `allowed=true` during a specified deadline while the user provides information (raw line 52). Thus status alone is insufficient to infer present permission.
- The API `capabilities` object separates `requested`, `allowed` and `enabled`. `requested` records whether the capability was requested, including automatic defaults; `allowed` is Adyen's permission state, with the pending/invalid deadline exceptions; `enabled` is a separately managed access setting that does not trigger KYC or prevent requesting. The capability can be used only when both `allowed` and `enabled` are true (raw lines 55–66). Even those flags describe capability availability, not completed account opening, funds movement or legal eligibility in a particular country.

## Detail locators

- Default/additional request and possible new KYC checks: raw lines 19–23.
- Business Account and general capability names: raw lines 25–37.
- Webhook/API observation and verification-state matrix, including changed-data exceptions: raw lines 39–53.
- Requested/allowed/enabled setting matrix and deadline nuance: raw lines 55–66.

## Related

- [[adyen-business-accounts]]
- [[source-adyen-docs-business-accounts-verification-overview]] — wider asynchronous KYC and deadline flow.
- [[source-adyen-docs-business-accounts-manage-account-holders]] — capability request and account-holder operations.
- [[source-adyen-docs-business-accounts-create-business-accounts]] — bankAccount instrument creation after prerequisite checks.

## Raw Sources

- [[raw/adyen/docs/business-accounts/verification-overview/capabilities/2026-09-15|Captured User capabilities guide]]
