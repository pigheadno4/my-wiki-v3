---
title: "Adyen Business Accounts: Use transfer limits"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/use-transfer-limits"
raw_files:
  - "adyen/docs/business-accounts/use-transfer-limits/2026-09-15.md"
tags: [adyen, business-accounts, transfer-limits, balance-accounts]
---

## Overview

This 2026-09-15-captured Adyen Business Accounts guide describes configured amount limits on outgoing external-bank transfers from users' balance accounts. A limit may be configured at balance-platform level as a default or at an individual balance-account level when that balance account is linked to an Adyen business account. A configured limit, its status, and an API response do not prove account opening, transfer execution or beneficiary bank receipt. The guide attributes an EU requirement to offer users a choice to configure limits on outgoing instant transfers; this dated statement is not a current legal determination.

## Key takeaways

- The balance-platform limit is described as the default for all balance accounts. A balance-account limit is specific to one account, requires linkage to an Adyen business account and user SCA when configured for that user. The overview says it overrides **any** platform default; the detailed account guide narrows precedence to the same `scope` and `transferType`, leaving other applicable platform limits. Consult that guide and effective-limit readback before assuming all defaults disappear.
- `scope` selects per-transfer versus daily total; `transferType` selects instant-priority only versus all transfers. After creation, the limit becomes `active` at its start, is checked on an outgoing request to an external bank account, and causes failure if the amount exceeds it. It becomes `inactive` after its end. With no start date it defaults to request time; with no end date it remains valid until overridden.
- Limit statuses are `pendingSCA`, `scheduled`, `active` and `inactive`. The page allows only one scheduled or pendingSCA limit for a given scope/type combination at a time; once the old limit is active, a newly scheduled one can override it when it becomes active. The example mistakenly compares TRLI_1 with itself where it evidently contrasts TRLI_1 and TRLI_2; use the stated rule, not the typo.
- For declines, the page routes to Transfer webhooks or Customer Area. It names `transactionRulesResult`, `reason: declinedByTransactionRule`, the limit reference and a description containing `transferLimitId`. Its calculation section instead speaks of balance-account **authorizations**, capture and release when an authorization expires or is canceled. That wording is not reconciled with the outgoing-transfer amount check; do not infer a complete transfer counter or bank settlement model from it.

## Detail locators

- Raw lines 15–26: purpose, validity/scope/type framing and dated EU statement. `## How it works` (28–40): platform/account hierarchy, Business Account linkage, SCA and active-period failure check.
- `## Transfer limit validity`, `## Transfer limit status`, and `## Transfer limit conditions` (42–89): date defaults, four statuses, scope/type combinations, one pending/scheduled rule, later override and example typo.
- `## Transfer limit calculation` (91–97): authorized amounts, uncaptured authorizations and release wording. `## Get updates when a limit is triggered` (99–110): webhook fields and Customer Area decline path. `## Next steps` (112–126): child configuration and effective-limit guides.

## Related

- [[adyen-business-accounts]] — product and resource context.
- [[adyen]] — provider context.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — detailed account-level precedence, SCA and effective-limit readback.
- [[source-adyen-docs-business-accounts-view-available-limits]] — available-limit lookup.

## Raw Sources

- [[raw/adyen/docs/business-accounts/use-transfer-limits/2026-09-15|Use transfer limits (captured 2026-09-15)]]
