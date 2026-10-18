---
title: "Adyen Business Accounts balance-platform transfer limits"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/use-transfer-limits/balance-platform"
raw_files:
  - "adyen/docs/business-accounts/use-transfer-limits/balance-platform/2026-09-15.md"
tags: [adyen, business-accounts, balance-platform, transfer-limits, configuration-api]
---

## Overview

This 2026-09-15 [[adyen]] Business Accounts guide describes creating, viewing and deleting balance-platform-level limits for outgoing external transfers. An active platform limit regulates covered transfers from all balance accounts on that platform, subject to a more specific balance-account limit. This is Configuration API setup and readback, not evidence that any specific limit was installed, enforced on a live transfer, or produced a bank receipt. See [[adyen-business-accounts]].

## Key takeaways

- The stated prerequisites are an Adyen for Platforms integration with Business Accounts, Configuration API access with **Balance platform base role**, and subscriptions to Transfer and Transaction webhooks. The guide excludes internal transfers and incoming external transfers from transfer-limit support.
- `POST /balancePlatforms/{id}/transferLimits` creates a limit with an amount in minor units and currency. `scope` is `perTransaction` (maximum per covered transfer) or `perDay` (maximum aggregate over a day); `transferType` is `instant` or `all`. The request table requires `scaInformation.exemption: setByPlatform`. These values describe configuration conditions, not blanket approval of a transfer.
- The guide describes `scheduled` before the start date, `active` from the start date, and `inactive` after the end date. An omitted/null `startsAt` defaults to request time; a future start schedules the limit, with no more than one future limit according to this page. Without `endsAt`, the limit stays active until overridden. Its step-by-step text says creation is scheduled, while the field table and response text allow immediate active creation; use actual returned status and dates.
- `GET /balancePlatforms/{id}/transferLimits` lists limits with optional scope/type/status filters, and `GET /balancePlatforms/{id}/transferLimits/{transferLimitId}` retrieves one. The delete route accepts only pending or scheduled limits; an active platform limit must instead be overridden by a new limit. The documented successful delete response is HTTP 204.
- The parent transfer-limits guide describes a platform limit as the default where no balance-account limit is configured; the balance-account guide says its matching `scope`/`transferType` limit overrides the platform limit. The platform-level page itself does not supply an effective-limit readback or actual transfer outcome. Its create curl body has missing JSON punctuation and its sample response is active despite the earlier blanket scheduled step; treat samples as illustrations rather than executable or outcome proof.

## Detail locators

- Scope, prerequisites and unsupported transfer directions: pinned raw lines 15–32.
- POST lifecycle and field table, including minor units, condition types, dates and exemption: raw lines 34–61.
- Malformed TEST create request and illustrative response: raw lines 63–113. The example is not valid JSON as printed; use the field table and API reference for implementation.
- List/filter GET and specific-limit GET, with sample readbacks: raw lines 115–244. The list example uses `-d` with GET and a `transfer` wrapper; verify the actual API response shape before consuming it.
- Delete eligibility, override instruction and HTTP 204 example: raw lines 246–268.

## Related

- [[adyen-business-accounts]] — product and account context.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — user balance-account limits, SCA and matching-scope override.

## Raw Sources

- [[raw/adyen/docs/business-accounts/use-transfer-limits/balance-platform/2026-09-15|Adyen Docs: Balance-platform transfer limits (2026-09-15 snapshot)]]
