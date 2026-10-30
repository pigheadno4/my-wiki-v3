---
title: "Adyen Management API v3 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/overview"
raw_files:
  - "adyen/api-explorer/Management/latest/overview/2026-09-15.md"
tags: [adyen, management-api, api-access, merchant-accounts, stores, terminals]
---

## Overview

This 2026-09-15 API Explorer snapshot introduces Management API v3 for configuring and managing Adyen company and merchant accounts, stores and payment terminals. It gives API-key authentication, test/live base URLs, URL-based versioning and a broad endpoint catalog. This is the **Management API**, distinct from the Balance Platform Configuration API and its account-holder/balance-account objects. See [[adyen]], [[adyen-api-access]], [[adyen-account-structure]] and [[adyen-terminal-management]].

## Key takeaways

- Each Management API request must use an API key in the `X-API-Key` header. The overview says live access needs a new key generated in the live Customer Area. Its test base is `https://management-test.adyen.com/v3` and its stated live base is `https://management-live.adyen.com/v3`; the version is part of the endpoint URL.
- The `## Endpoints > ### General` table catalogs routes for company and merchant accounts, credentials and allowed origins, users, webhooks, merchant payment-method and payout settings, split configurations, stores, terminal orders/settings/actions, donation campaigns and nonprofits. Some entries describe a **request** to activate a merchant or add a payment method; listing the route does not establish approval or activation.
- This overview has no operation-specific request/response schema, required property list, role matrix, error contract or examples. Its method/path/summary rows are navigation, not evidence of each operation's prerequisites, destructive effects, timing, rate limits, or successful execution. For those, inspect the relevant operation reference or guide. The snapshot is not proof of current availability, credential permissions, merchant eligibility, terminal state, payment or payout outcome.

## Detail locators

- Purpose, API-key authentication, live-key separation, URL versioning and base hosts: pinned raw lines 5–32.
- Full endpoint catalog: `## Endpoints > ### General`, lines 34–178. Company paths and `/me`: lines 39–90; merchant paths: lines 91–157; stores, terminal and campaign paths: lines 158–178.

## Related

- [[adyen-api-access]] — credential and authentication context.
- [[adyen-terminal-management]] — terminal operation guides.
- [[adyen-account-structure]] — company and merchant account distinction.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/overview/2026-09-15|Management API v3 overview snapshot]]
