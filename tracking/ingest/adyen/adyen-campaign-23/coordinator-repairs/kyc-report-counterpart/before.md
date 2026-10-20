---
title: "Adyen Classic Platforms: Create account holders and accounts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/account-holders-and-accounts"
raw_files:
  - "adyen/docs/classic-platforms/account-holders-and-accounts/2026-09-15.md"
tags: [adyen, classic-platforms, account-holders, accounts, onboarding]
---

## Overview

This 2021-modified, 2026-09-15-captured guide is for **Classic Adyen for Platforms**. It describes creating a sub-merchant **account holder** with the Classic Account API, receiving an automatically created **account**, and optionally creating additional accounts for that holder. It directs new implementations to a separate new-integration guide. Keep its `accountHolderCode` and `accountCode` model distinct from the newer balance-platform resources.

## Key takeaways

- Choose the sub-merchant's legal-entity type, collect this 2021-modified guide's creation-stage minimum data for that type, and call `/createAccountHolder`. The listed types are Individual, Business, Nonprofit, Partnership and Public company; example request values use `NonProfit` and `PublicCompany`. The request supplies a unique `accountHolderCode`. See raw lines 25–93 and the entity-specific examples at lines 95–394.
- When the account holder is created, an **account is created automatically** and identified by `accountCode`, which the guide says to save for transactions. The examples use Classic Account API **v6 on a test host**. Optional extra accounts are created with `/createAccount` and the existing `accountHolderCode`; the guide gives separate business lines as an example. See raw lines 95–98 and 396–429.
- Creation is **asynchronous**. HTTP 200 can return an `accountCode`, while HTTP 202 acknowledges a queued request; for the final creation result, wait for `ACCOUNT_HOLDER_CREATED` and `ACCOUNT_CREATED` notifications. Likewise, an extra `/createAccount` call requires `ACCOUNT_CREATED`. Do not treat the request response or illustrative `Active` response object as completed creation. See raw lines 396–403 and 424–429.
- The guide says a newly created account holder with `accountHolderStatus.status: Active` may process payments on their behalf. **Paying out funds is a separate gate**: the sub-merchant must provide more information, including bank details, and pass verification checks. The status also determines whether processing and payouts are allowed. See raw lines 21–23 and 403–405.

## Dated verification qualification

The entity-specific fields here are the **2021-modified creation guide's minimum inputs**, not an exhaustive later verification checklist. A separate Classic [[raw/adyen/docs/classic-platforms/verification-process/requirements-update/2026-09-15|requirements-update raw]] says its additional rules apply to all new sub-merchants from **1 August 2022** (related raw lines 21–27). It distinguishes EEA owner-or-controller versus non-EEA controller information (related raw lines 43–45) and requires at least one identified signatory with further details (related raw lines 144–146). These two snapshots do not establish that the older minimum payload alone passes later verification checks.

## Detail locators

- Legal-entity choices and minimum collected fields, including 25% owner/signatory and nonprofit control-officer cases: [[raw/adyen/docs/classic-platforms/account-holders-and-accounts/2026-09-15|raw lines 25–79]].
- Classic Account API v6 test examples for each entity type: [[raw/adyen/docs/classic-platforms/account-holders-and-accounts/2026-09-15|raw lines 81–394]].
- Asynchronous creation, IDs, Active status, optional accounts and their notification gate: [[raw/adyen/docs/classic-platforms/account-holders-and-accounts/2026-09-15|raw lines 396–429]].

## Source wording note

In the optional `/createAccount` step, the HTTP 202 paragraph says `ACCOUNT_CREATED` confirms if the **account holder** was successfully created (raw line 429). The step is creating an additional **account** for an existing holder (raw lines 407–411); do not use that sentence to infer a second holder-creation flow.

## Related

- [[adyen-classic-platforms]] — Classic platform resource and money-flow context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/account-holders-and-accounts/2026-09-15|Account holders and accounts (captured 2026-09-15)]]
