---
title: "Adyen Session authentication API v1 overview (API Explorer snapshot)"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/sessionauthentication/latest/overview"
raw_files:
  - "adyen/api-explorer/sessionauthentication/latest/overview/2026-09-15.md"
tags: [adyen, api-explorer, session-authentication, jwt, platform-components]
---

## Overview

Captured API Explorer overview for **Session authentication API v1**, which Adyen describes as creating and managing JSON Web Tokens (JWT) needed to integrate components. It lists test `https://test.adyen.com/authe/api/v1` and live `https://authe-live.adyen.com/authe/api/v1` base URLs, and identifies `POST /sessions` as the create-session-token route. This is an overview and route catalog, not that operation's request or response schema. See [[adyen]], [[adyen-platform-components]], and [[adyen-api-access]] for separately sourced component and credential context.

## Key takeaways

- **Caller credential and environment.** Adyen recommends an API key and shows `X-API-Key` as the request header for connecting. For platform or marketplace setups, generate the key in Customer Area; for an Issuing integration, the page directs generation in Balance Platform Customer Area. Its going-live instruction calls for a **live** Customer Area API key before using the live endpoint. The captured example has placeholder `YOUR_API_KEY`, not a usable credential. See raw lines 9–18 and 24–34.
- **Component permissions are conditional.** Token-creation requirements vary by component type. The overview links Onboarding and Platform Experience component guidance for those requirements, without defining particular roles, policy resources, allow-origin values, legal-entity/account identities, or token claims on this page. See raw lines 20–22.
- **Outcome boundary.** The single endpoint row names `POST /sessions` and its purpose, but supplies no request body, response body, HTTP status, token/session ID, lifetime, refresh/revocation process, error behavior, rate limit, asynchronous outcome or deprecation rule. Listing a token-creation operation and the live URL does not prove that a particular user was authenticated or authorized, a component session was issued, or an account/payment/transfer/payout state changed. See raw lines 5–7 and 28–41.

## Detail locators

- Raw opening and Authentication (lines 5–18): API v1 purpose, recommended API key and example `X-API-Key` header.
- Raw Roles and permissions / Going live (lines 20–26): component-dependent token requirements and live-key instruction.
- Raw `## Servers` and `## Endpoints` (lines 28–41): test/live base URLs and `POST /sessions` route catalog.

## Related

- [[adyen-platform-components]] — component session and UI context.
- [[adyen-api-access]] — provider credential context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/sessionauthentication/latest/overview/2026-09-15|Session authentication API v1 overview, fetched 2026-09-15]]
