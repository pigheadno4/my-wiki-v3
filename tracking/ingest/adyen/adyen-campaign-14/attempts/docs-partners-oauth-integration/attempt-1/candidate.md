---
title: "Partner OAuth integration | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/partners/oauth/integration"
raw_files:
  - "adyen/docs/partners/oauth/integration/2026-09-15.md"
tags: [adyen, partners, oauth, delegated-access, pkce, tokens]
---

## Overview

This 2026-09-15 capture of a 2023-modified [[adyen]] guide describes a **partner OAuth client** requesting delegated access to selected customer account resources. After the customer authenticates and authorizes the request, the partner receives tokens for API calls on that customer's behalf, bounded by returned scopes and merchant accounts. This is distinct from an ordinary merchant API credential and does not itself establish seller identity, merchant of record, a payment result or live partner eligibility. [[adyen-partner-oauth]] [[adyen-partners]]

## Key takeaways

- Registration requires an account with the **OAuth apps manage** user role. The page says test merchant accounts created since November 2023 have it by default, directs older test accounts to Support, and limits the live role to partner accounts. Test integration first is **advice**, especially for online-payments scope. In Partner Portal, register an app with name/URL/description, Redirect URL and requested scopes, then securely retain the client secret because it cannot be retrieved later. Scopes cannot be extended after app creation; customers can authorize only the entire requested scope set. See raw lines 29–54.
- The partner sends the customer to an Adyen authorization page in the chosen test/live environment. The grant URL uses client ID, `response_type=code`, exact registered redirect URI, a random `state` for CSRF protection, and scopes matching the registered app. The guide requires PKCE `S256`: each request uses a unique verifier (43–128 allowed characters) and its base64url SHA-256 challenge. On success the redirect carries short-lived code and the returned state; on failure it carries an OAuth error. The parameter table at line 70 misleadingly calls `code_challenge` a “unique code verifier”; the dedicated PKCE instructions define the verifier and derived challenge separately. See raw lines 56–144.
- Exchange the code at the environment-specific OAuth `/v1/token` endpoint using Basic authentication built from client ID and secret, `authorization_code` grant, associated `code_verifier` and matching redirect URI. The response supplies bearer access token, one-time refresh token, scope and merchant-account `accounts`; the default access-token expiry is 86,400 seconds (24 hours). Use the access token as a Bearer header for resource API calls. These are documented request/response contracts, not evidence that a real customer granted access. See raw lines 186–247.
- On refresh, submit the refresh token with the `refresh_token` grant. The previous access token expires immediately; the previous refresh token expires shortly, with a brief retry grace for network errors. Refreshed access keeps the original scope and merchant-account set. The page does not document a revocation endpoint or imply that refresh extends the customer's consent scope. See raw lines 249–297.
- Live setup is separate: register a client in the **live Partner Portal**, replace the client ID, secret and client URI, and change all test endpoints to live. No live OAuth request or account change is evidenced by this snapshot. See raw lines 299–305.

## Detail locators

- **Role, environment, client registration, secret and immutable scopes:** raw lines 29–54.
- **Consent grant URL, PKCE/state, redirect success/failure:** raw lines 56–144.
- **Code exchange, token fields, account scope and Bearer use:** raw lines 186–247.
- **Refresh lifecycle and unchanged authorization scope:** raw lines 249–297.
- **Live client and endpoint cutover:** raw lines 299–305.

## Related

- [[adyen]]
- [[adyen-partners]]
- [[adyen-partner-oauth]]
- [[adyen-api-access]] — separate ordinary API credential model

## Raw Sources

- [[raw/adyen/docs/partners/oauth/integration/2026-09-15|Adyen partner OAuth integration — collected 2026-09-15]]
