---
title: "GET recurring top-ups for a balance account | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/recurringTopUps"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/recurringTopUps/2026-11-02.md"
tags: [adyen, balance-platform, issuing, recurring-top-ups, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /balanceAccounts/{balanceAccountId}/recurringTopUps` to list configured recurring top-ups for one balance account. It links to an Issuing management guide; see [[adyen-issuing]] for that product context. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` documentation URL alone does not establish live availability.

## Key takeaways

- Required path `balanceAccountId` selects the balance account. Optional `cursor` is required to request the next or previous page; optional `limit` must be 1–100. No default limit is stated. The 200 response requires `link` and `recurringTopUps`; optional first/last/next/previous/self link objects can contain `href`. [Raw: lines 14–26, 30–47]
- Each returned top-up has required `counterparty.transferInstrumentId`, description, top-up `id`, `topUpAmount`, and `trigger`. The funding transfer-instrument ID, top-up ID and queried balance-account ID are different identities. Description is cut to 140 characters if longer. The beneficiary reference is optional and described as sent in transfer-related webhooks. The amount is in minor units and can have optional fixed or target objects. [Raw: lines 47–56]
- `status` is optional; if omitted, the table says it defaults to `active`. `active` describes an enabled top-up that will pull funds; `inactive` cannot be triggered. The trigger can be a schedule or a minimum-balance threshold, but the schema table marks `schedule` optional and nested `threshold` required. Preserve this schema/prose tension instead of asserting that every configuration requires both trigger forms. A returned configuration or active status does not prove a top-up was initiated, transferred, booked or received. [Raw: lines 53–59]
- Errors listed are 401 authentication, 403 permission, 404 missing top-up and 500 server processing. The 404 example instead says a balance account was not found; it is illustrative, not a complete catalog of missing-resource cases. [Raw: lines 62–135, 207–219]

## Detail locators

- Purpose, TEST v2 server and pagination inputs: pinned raw lines 5–26.
- Success response, identities and trigger/status fields: lines 28–59.
- Error schemas: lines 62–135; success and error examples: lines 137–233.

## Related

- [[adyen-issuing]] — Issuing funds context.
- [[source-adyen-docs-issuing-add-manage-funds-top-ups]] — separate recurring top-up guide.
- [[source-adyen-docs-issuing-add-manage-funds-top-ups-top-up-webhooks]] — separate asynchronous event guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(balanceAccountId)/recurringTopUps/2026-11-02|Captured API Explorer page (2026-11-02)]]
