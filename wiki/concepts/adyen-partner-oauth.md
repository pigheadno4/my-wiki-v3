---
title: "Adyen Partner OAuth"
type: concept
category: technology
tags: [adyen, partners, oauth, delegated-access, merchant-consent]
---

## Definition

Adyen partner OAuth lets a partner-registered application request customer authorization for selected account resources and then use a bearer access token for API calls on that customer's behalf. The token's returned `scope` and `accounts` delimit access; this delegation is distinct from an ordinary merchant API credential. [[source-adyen-docs-partners-oauth-integration]]

## Authorization boundary

The captured integration guide requires an OAuth-app management role, registered redirect URI and all-or-nothing scopes, plus an authorization-code flow with PKCE `S256` and CSRF `state`. Its live role is described as partner-account-only. Access tokens expire after a default 24 hours; one-time refresh tokens rotate access, immediately invalidating the previous access token while preserving scope and merchant accounts. The page documents no revocation endpoint. Use the source for environment-specific URLs, secret handling, retry grace and the guide's `code_challenge` terminology conflict. A documented flow is not proof of customer consent, granted scopes, live authorization or payment execution.

## Sources

- [[source-adyen-docs-partners-oauth-installed-oauth-apps]] — 2023-modified, 2026-09-15-captured Customer Area route for merchant-account-specific app consent, Merchant-admin view/uninstall and immediate access invalidation; no actual grant or revoke proof.


- [[source-adyen-docs-partners-oauth]] — 2026-09-15 partner-only OAuth overview of customer resource-owner consent, requested scope, authorization-code exchange, access-token use and refresh; navigation hub, not proof of an installed app, granted scope, or payment.


- [[source-adyen-docs-partners-oauth-scopes]] — 2026-09-15 partner OAuth scope-to-API-action guide for webhooks, online payments, tokenization, raw card, payment links, account settings and Cloud device requests; token scope and merchant grant bound access.


- [[source-adyen-docs-partners-oauth-integration]] — 2026-09-15 snapshot of 2023-modified Adyen partner OAuth registration, consent, PKCE, token exchange, refresh and live cutover.

## Related

- [[adyen]]
- [[adyen-partners]]
- [[adyen-api-access]]
