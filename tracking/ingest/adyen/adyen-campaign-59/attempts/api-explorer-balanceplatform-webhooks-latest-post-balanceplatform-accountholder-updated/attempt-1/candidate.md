---
title: "Adyen Balance Platform webhook: accountHolder.updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.accountHolder.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.accountHolder.updated/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, account-holders]
---

## Overview

This 2026-09-15 capture documents the incoming Balance Platform `balancePlatform.accountHolder.updated` webhook that Adyen sends after a successful account-holder update. It is an event contract, not a merchant POST operation. The `latest` route is a documentation label; the captured page does not state an independently verified current API version. See [[adyen]], [[adyen-platforms]] and [[adyen-webhooks]].

## Key takeaways

- The request-body table requires top-level `data`, `environment` (`test` or `live`) and `type`; `timestamp` is optional and denotes when the event was queued. `data.balancePlatform` and `data.accountHolder` are optional in that table. Within the optional `accountHolder` object, `id` and `legalEntityId` are marked required. Keep the holder ID distinct from the associated legal-entity ID and the balance-platform ID.
- The optional holder `status` describes `active`, `suspended` (temporarily disabled with payouts blocked) and `closed` (permanently disabled, final). The optional `capabilities` object carries per-capability settings; the examples show `requested`, `enabled`, `allowed`, verification errors and `verificationStatus` values that differ despite holder `status: active`. An update event or active status alone does not establish capability approval or payout eligibility.
- The table describes omitted existing metadata key-value pairs as deleted during a metadata update. That is a qualification of the update behavior, not evidence that every webhook event changes metadata.
- The examples are illustrative test and live payloads, including verification problems and pending/invalid capability states. The page does not establish financial movement, event ordering, duplicate handling, retries or signature verification. Its response section says a `2xx` HTTP response accepts the webhook, not that the underlying holder capability is verified.

## Detail locators

- Trigger and event purpose: pinned raw introduction, lines 5–7.
- Request-body requirements, identities, status and metadata descriptions: `## Parameters > ### Request body`, lines 11–32.
- Test and live event examples, including capability and verification problems: `## Request examples`, lines 34–235.
- Webhook acknowledgement: `## Responses > ### 200 Success`, lines 236–244.

## Related

- [[source-adyen-api-explorer-balanceplatform-latest-post-accountholders]] — separate account-holder creation API reference.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.accountHolder.updated/2026-09-15|Account holder updated webhook snapshot]]
