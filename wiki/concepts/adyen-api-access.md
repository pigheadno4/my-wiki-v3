---
title: "Adyen API Access"
type: concept
category: technology
tags: [adyen, api-credentials, authentication, access-control]
---

## Definition

Adyen web service API credentials identify an integration for API requests. A credential combines a username, authentication secret, enabled roles, and an account scope; together these determine which account context and permitted operations the credential can reach. This is a provider-wide access route, separate from endpoint-specific authorization, idempotency, and payment lifecycle behavior.

## Access boundaries

Roles define credential permissions. Account scope defaults to company-wide access, including linked merchant accounts, when the credential is created on a company account, while a credential created on a merchant account is limited to that merchant account; company-level configuration can instead select particular account groups and merchant accounts. More credentials can narrow permissions across channels or systems but increase key-management overhead.

## Credential lifecycle

A newly generated API key is active immediately while its predecessor remains active for 24 hours by default. Basic-authentication password replacement instead deactivates the previous password immediately, so overlapping migration requires a separate credential. Live credentials must come from the live environment. IP allowlisting can restrict request origins, and a credential can be deactivated immediately and later reactivated but cannot be deleted.

These snapshot statements do not prove current merchant or user eligibility, successful authentication, endpoint access, correct secret storage, API availability, idempotent processing, or payment execution. Future authentication, role-catalog, idempotency, and API-security sources should extend this route without transferring their claims before review.

## Sources

- [[source-adyen-docs-development-resources-api-authentication]] — unversioned documentation snapshot for API-key and Basic request-header authentication, including library-managed versus direct-call responsibility

- [[source-adyen-docs-development-resources-security-api-security]] — unversioned guidance snapshot for API authentication, rate limiting and throttling, HTTPS/TLS, and security testing; guidance only, not a complete security standard or provider-runtime proof

- [[source-adyen-docs-development-resources-live-endpoints]] — unversioned live-endpoints documentation snapshot for test/live endpoint structure, company-specific URL prefixes, regional configuration matching, and network connection guidance

- [[source-adyen-docs-development-resources-api-credentials-roles]] — unversioned documentation snapshot for role-based API credential permissions, company credential delegation, frequently used payment and Management API role locators, and PCI/Support qualifications

- [[source-adyen-docs-development-resources-api-credentials]] — unversioned documentation snapshot for web service credential identity, permission and account scope, environment separation, rotation, IP restriction, and deactivation
