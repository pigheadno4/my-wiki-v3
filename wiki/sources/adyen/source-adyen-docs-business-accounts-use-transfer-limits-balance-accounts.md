---
title: "Create and manage transfer limits for balance accounts | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/use-transfer-limits/balance-accounts"
raw_files:
  - "adyen/docs/business-accounts/use-transfer-limits/balance-accounts/2026-09-15.md"
tags: [adyen, business-accounts, transfer-limits, balance-accounts, sca]
---

## Overview

This 2026-09-15-captured Adyen for Platforms Business Accounts guide describes Configuration API transfer limits on outgoing external transfers from a user's balance account. The balance account must be linked to a `bankAccount` payment instrument (an Adyen business account). It is a limit-configuration guide, not evidence that a particular account was opened, a live transfer was approved, or funds reached a bank. [[adyen-business-accounts]]

## Key takeaways

- The guide requires a Business Accounts integration, the Balance platform base API role, transfer and transaction webhook subscriptions, an Adyen business account linked to the balance account, and an installed Authentication SDK with registered SCA devices. The limits do not cover internal transfers or incoming external transfers. See raw lines 21-36.
- A limit's amount is in minor units. `scope` is `perTransaction` or `perDay`; `transferType` is `instant` or `all`. `startsAt` and `endsAt` control validity; the guide says only one future limit can be scheduled and an omitted end date remains active until override. See raw lines 126-139. This page's unqualified one-future-limit wording conflicts with the parent [[source-adyen-docs-business-accounts-use-transfer-limits]], which permits multiple limits with different `scope`/`transferType` combinations and limits concurrent scheduled or `pendingSCA` limits only for the same combination (parent raw lines 65-69); do not infer a global one-future-limit cap.
- The user can authenticate each creation on initiation or authenticate one or more `pendingSCA` limits on approval. The initiation and approval walkthroughs use a 401 SCA challenge, Authentication SDK exchange and a second POST with matching body within 10 minutes; documented exemptions are `lowerLimit`, `notRegulated`, `setByPlatform`, `initialLimit`, and `alreadyPerformed`. The guide says platform-set limits need no user SCA; exemption type must be specified. See raw lines 38-66, 72-98, 116-220, 267-461. These are documented flows, not a determination of legal exemption for a user.
- A successful limit is described as `scheduled` before its start, `active` while regulating covered transfers, then `inactive` after its end. Pending SCA approval precedes that sequence. Only pending or scheduled limits can be deleted; an active limit must be overridden with a new limit. See raw lines 72-98 and 723-745.
- The guide says a balance-account limit overrides a balance-platform limit for the same `scope` and `transferType`; otherwise an applicable platform limit remains. Its next sentence mistakenly says that when no platform limit is set, the platform limit applies. Treat that sentence as internally contradictory, and verify effective limits with the documented `/balanceAccounts/{id}/transferLimits/current` route rather than inferring an absent limit. See raw lines 616-627.

## Detail locators

- `POST /balanceAccounts/{id}/transferLimits` and `POST /balanceAccounts/{id}/transferLimits/approve`: creation, SCA headers, pending approval, exemptions, parameters and sample responses, raw lines 100-529.
- `GET /balanceAccounts/{id}/transferLimits`, `/current`, and `/{transferLimitId}`: configured, effective and specific readback, raw lines 530-721. The `/current` prose names the `/current` route, while its sample curl uses the non-current route; use the prose route as a locator and verify implementation against the API reference.
- `DELETE /balanceAccounts/{id}/transferLimits/{transferLimitId}`: pending/scheduled deletion and HTTP 204 example, raw lines 723-745. Several request examples have malformed JSON; the approval and current-limit example URLs conflict with their prose endpoint paths. Treat examples as illustrations, not executable requests.

## Related

- [[adyen]] — provider context.
- [[adyen-business-accounts]] — Business Accounts product scope and source map.

## Raw Sources

- [[raw/adyen/docs/business-accounts/use-transfer-limits/balance-accounts/2026-09-15|2026-09-15 captured transfer-limit guide]]
