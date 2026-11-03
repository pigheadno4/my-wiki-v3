---
title: "Adyen Balance Platform API POST /balanceAccounts/{id}/transferLimits — create a transfer limit"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits/2026-11-03.md"
tags: [adyen, business-accounts, balance-platform-api, transfer-limits, sca]
---

## Overview

The 2026-11-03 Balance Platform API Explorer capture describes `POST /balanceAccounts/{id}/transferLimits` as creating a transfer limit for the balance account identified by the required path `id`. Its listed server is the test base `https://balanceplatform-api-test.adyen.com/bcl/v2`. The operation configures a limit in the [[adyen-business-accounts]] context; a returned limit or SCA state does not record a funds transfer.

## Key takeaways

- The request body requires `amount` (currency plus integer value in minor units), `scope` (`perTransaction` or `perDay`) and `transferType` (`instant` or `all`). Scope sets the maximum per transfer or daily total; transfer type selects instant-priority transfers or all priorities. Optional fields are caller `reference`, `startsAt`, `endsAt`, and `scaInformation`. The parameter table also lists an optional `WWW-Authenticate` header for SCA. The page names no API credential role or idempotency key.
- A future `startsAt` schedules the limit. With no `endsAt`, the page says the limit stays active until overridden by a new limit. The optional SCA information lists exemptions `lowerLimit`, `notRegulated`, `setByPlatform`, `initialLimit`, and `alreadyPerformed`; the listed labels do not themselves establish that a caller qualifies for an exemption. `scaOnApproval: true` defers initiation of SCA to approval for pending limits; `false` is the documented default and initiates SCA immediately after request submission.
- The 200 body requires the limit `id`, `amount`, `limitStatus`, `scope`, `startsAt`, and `transferType`. `limitStatus` can be `active`, `inactive`, `pendingSCA`, or `scheduled`. If optional response `scaInformation` is present, its `status` is required and can be `notPerformed` (failed authentication or an exemption), `pending`, or `performed`. A 200 response may therefore still report pending SCA or future activation; the illustrated response does exactly that.
- Error descriptions include 400 for invalid input or no registered SCA device, 401 requiring resolution of an SCA challenge, and 422 for request validation. This captured route does not describe the approval call, later activation, deletion rules, effective-limit precedence, reversal, transfer execution, settlement, or bank receipt. It lists a test server only; `latest` in the URL is not proof of the current live version.

## Detail locators

- `## Servers`; `## Parameters > ### Path parameters`, `### Header parameters`, and `### Request body` — test server, balance-account ID, SCA header, request constraints and timing.
- `## Request examples > ### Create a transfer limit request` — illustrative request.
- `## Responses > ### 200 Success` — returned ID, statuses and requiredness; `### 400 Client Error`, `### 401 Client Error`, `### 422 Client Error` — errors.
- `## Response examples > ### 200 Success` — illustrative `pendingSCA`/`pending` response.

## Related

- [[adyen]] — provider.
- [[adyen-business-accounts]] — financial-product and SCA context.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — separate balance-account transfer-limits guide; its lifecycle and setup claims are not imported into this endpoint contract.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits/2026-11-03|2026-11-03 captured API Explorer reference]]
